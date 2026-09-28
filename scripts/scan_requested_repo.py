#!/usr/bin/env python3
import argparse, json, os, re, subprocess, sys, urllib.parse, urllib.request, urllib.error
from pathlib import Path

REPO_RE = re.compile(r'^https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)/?$')
AUTH_TEXT = 'I am authorized to submit this repository or workflow for analysis.'

def authenticated_gh_api(path):
    p = subprocess.run(['gh','api',path], text=True, capture_output=True)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout).strip() or f'gh api failed: {path}')
    return json.loads(p.stdout)

def api_json(path):
    if os.getenv('DETERMA_SCAN_TRANSPORT') == 'authenticated-gh':
        return authenticated_gh_api(path)
    return public_api(path)

def public_api(path):
    url = 'https://api.github.com/' + path
    req = urllib.request.Request(url, headers={
        'User-Agent': 'DETERMA-public-approval-scan-v1',
        'Accept': 'application/vnd.github+json'
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        raise RuntimeError(f'PUBLIC_GITHUB_API_{e.code}:{path}:{body[:240]}')

def extract_section(body, heading):
    marker = f'### {heading}'
    if marker not in body:
        return ''
    after = body.split(marker,1)[1]
    value = after.split('\n### ',1)[0].strip()
    return value

def parse_issue(event_path):
    event=json.loads(Path(event_path).read_text())
    issue=event.get('issue') or {}
    body=issue.get('body') or ''
    repo_url=extract_section(body,'Repository URL').splitlines()[0].strip()
    mode=extract_section(body,'Preferred mode').splitlines()[0].strip()
    authorized=(f'- [x] {AUTH_TEXT}' in body or f'- [X] {AUTH_TEXT}' in body)
    return {
      'issue_number':issue.get('number'),
      'repo_url':repo_url,
      'mode':mode,
      'authorized':authorized
    }

def scan(repo_full_name, limit=10):
    meta=api_json(f'repos/{repo_full_name}')
    if meta.get('private') is True:
        raise ValueError('PRIVATE_REPOSITORY_NOT_ALLOWED_IN_AUTOMATED_SCAN')
    if meta.get('archived'):
        archived=True
    else:
        archived=False

    q=f'repo:{repo_full_name} is:pr review:approved updated:>=2026-01-01'
    sr=api_json('search/issues?q='+urllib.parse.quote(q,safe='')+f'&sort=updated&order=desc&per_page={limit}')
    items=sr.get('items',[])[:limit]
    rows=[]
    skipped=[]
    for item in items:
        n=item['number']
        pr=api_json(f'repos/{repo_full_name}/pulls/{n}')
        rv=api_json(f'repos/{repo_full_name}/pulls/{n}/reviews?per_page=100')
        approvals=[x for x in rv if x.get('state')=='APPROVED' and x.get('commit_id') and x.get('submitted_at')]
        if not approvals:
            skipped.append({'pr':n,'reason':'NO_RETRIEVABLE_APPROVED_REVIEW'})
            continue
        approvals.sort(key=lambda x:x['submitted_at'], reverse=True)
        a=approvals[0]
        final_head=pr['head']['sha']
        changed=final_head != a['commit_id']
        rows.append({
          'pr':n,
          'url':pr.get('html_url'),
          'title':pr.get('title'),
          'state':pr.get('state'),
          'merged':pr.get('merged') is True,
          'approval_actor':(a.get('user') or {}).get('login'),
          'approval_commit':a['commit_id'],
          'final_head':final_head,
          'head_changed_after_latest_approval':changed
        })
    return {
      'repository':repo_full_name,
      'archived':archived,
      'query':q,
      'search_hits_considered':len(items),
      'scan_limit':limit,
      'valid_cases':len(rows),
      'head_changed_after_latest_approval':sum(x['head_changed_after_latest_approval'] for x in rows),
      'cases':rows,
      'skipped':skipped,
      'truth_boundary':'Public GitHub metadata only. This approval-continuity scan is not a vulnerability finding and does not claim upstream controls were bypassed.'
    }

def write_markdown(result, path):
    total=result['valid_cases']
    changed=result['head_changed_after_latest_approval']
    rate=(changed/total*100) if total else 0
    lines=[
      '## DETERMA public historical scan',
      '',
      f"Repository: **{result['repository']}**",
      f"Valid approved PR histories: **{total}**",
      f"Exact head changed after latest captured approval: **{changed}/{total} ({rate:.1f}%)**" if total else 'No valid approved PR histories were found in the bounded query.',
      '',
      'DETERMA model action when a head change is observed:',
      '',
      '`REVALIDATE_EXACT_HEAD_BEFORE_EXECUTION`',
      '',
      '| PR | Result | Approved commit | Final/current head |',
      '| ---: | --- | --- | --- |'
    ]
    for x in result['cases']:
      verdict='REVALIDATE' if x['head_changed_after_latest_approval'] else 'NO_EXACT_HEAD_SIGNAL'
      lines.append(f"| [#{x['pr']}]({x['url']}) | {verdict} | `{x['approval_commit'][:12]}` | `{x['final_head'][:12]}` |")
    lines += [
      '',
      '> '+result['truth_boundary'],
      '',
      'If this result is operationally relevant, reply on this issue with **shadow pilot** to continue with a bounded design-partner review.'
    ]
    Path(path).write_text('\n'.join(lines)+'\n')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--event',required=True)
    ap.add_argument('--json-out',required=True)
    ap.add_argument('--md-out',required=True)
    args=ap.parse_args()
    req=parse_issue(args.event)
    if not req['authorized']:
        raise SystemExit('FAIL_CLOSED_AUTHORIZATION_CHECKBOX_MISSING')
    m=REPO_RE.match(req['repo_url'])
    if not m:
        raise SystemExit('FAIL_CLOSED_INVALID_PUBLIC_GITHUB_REPOSITORY_URL')
    repo=f'{m.group(1)}/{m.group(2)}'
    result=scan(repo)
    result['request_mode']=req['mode']
    result['mutation_performed']=False
    result['external_effect_on_scanned_repo']='NONE'
    Path(args.json_out).write_text(json.dumps(result,indent=2)+'\n')
    write_markdown(result,args.md_out)
    print(json.dumps({'ok':True,'repository':repo,'valid_cases':result['valid_cases'],'head_changed':result['head_changed_after_latest_approval']},indent=2))

if __name__=='__main__': main()
