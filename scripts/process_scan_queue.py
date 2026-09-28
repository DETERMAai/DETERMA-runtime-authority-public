#!/usr/bin/env python3
import json, os, subprocess, tempfile
from pathlib import Path

REPO='DETERMAai/DETERMA-runtime-authority-public'
RECEIPT_PREFIX='<!-- determa-self-serve-scan:v1 issue='

def run(args, check=True):
    p=subprocess.run(args,text=True,capture_output=True)
    if check and p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout).strip() or 'command failed')
    return p

def gh_json(args):
    p=run(['gh']+args)
    return json.loads(p.stdout)

def labels(issue):
    return {x['name'] for x in issue.get('labels',[])}

def already_receipted(number):
    comments=gh_json(['api',f'repos/{REPO}/issues/{number}/comments?per_page=100'])
    marker=f'{RECEIPT_PREFIX}{number} -->'
    return any(marker in (x.get('body') or '') for x in comments)

def edit_labels(number, add=None, remove=None):
    cmd=['issue','edit',str(number),'--repo',REPO]
    for x in add or []: cmd += ['--add-label',x]
    for x in remove or []: cmd += ['--remove-label',x]
    run(['gh']+cmd)

def comment(number, body_path):
    run(['gh','issue','comment',str(number),'--repo',REPO,'--body-file',str(body_path)])

def event_file(issue):
    f=tempfile.NamedTemporaryFile('w',delete=False,suffix='.json')
    json.dump({'issue':{'number':issue['number'],'body':issue.get('body') or ''}},f)
    f.close()
    return f.name

def process(issue):
    n=issue['number']
    if already_receipted(n):
        edit_labels(n,add=['scan-complete'],remove=['scan-processing','scan-failed'])
        print(f'ISSUE_{n}=ALREADY_RECEIPTED')
        return
    edit_labels(n,add=['scan-processing'],remove=['scan-failed'])
    ev=event_file(issue)
    out_json=tempfile.NamedTemporaryFile(delete=False,suffix='.json').name
    out_md=tempfile.NamedTemporaryFile(delete=False,suffix='.md').name
    env=os.environ.copy(); env['DETERMA_SCAN_TRANSPORT']='authenticated-gh'
    p=subprocess.run(['python3','scripts/scan_requested_repo.py','--event',ev,'--json-out',out_json,'--md-out',out_md],text=True,capture_output=True,env=env)
    if p.returncode != 0:
        fail=Path(tempfile.NamedTemporaryFile(delete=False,suffix='.md').name)
        fail.write_text(
            f'{RECEIPT_PREFIX}{n} -->\n## DETERMA scan did not run\n\n'
            'The server-side scan failed closed. No mutation was performed on the submitted repository. '
            'The request remains available for bounded retry after the failure is reviewed.\n'
        )
        comment(n,fail)
        edit_labels(n,add=['scan-failed'],remove=['scan-processing'])
        print(f'ISSUE_{n}=FAILED:{p.stderr.strip()[:300]}')
        return
    result=json.loads(Path(out_json).read_text())
    md=Path(out_md)
    md.write_text(f'{RECEIPT_PREFIX}{n} -->\n'+md.read_text())
    comment(n,md)
    edit_labels(n,add=['scan-complete'],remove=['scan-processing','scan-failed','scan-invalid'])
    print(f"ISSUE_{n}=COMPLETE valid_cases={result['valid_cases']} head_changed={result['head_changed_after_latest_approval']}")

def main():
    issues=gh_json(['issue','list','--repo',REPO,'--state','open','--label','scan-request','--limit','100','--json','number,title,body,labels'])
    todo=[]
    for issue in issues:
        ls=labels(issue)
        if 'scan-complete' in ls or 'scan-invalid' in ls:
            continue
        todo.append(issue)
    print(f'QUEUE_DEPTH={len(todo)}')
    for issue in sorted(todo,key=lambda x:x['number']):
        process(issue)

if __name__=='__main__': main()
