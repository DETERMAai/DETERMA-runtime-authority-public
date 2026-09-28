#!/usr/bin/env python3
"""Read-only V4 enrichment for the public approval-continuity benchmark."""

import argparse
import json
import subprocess
import sys
import urllib.parse
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def gh(path):
    p = subprocess.run(["gh", "api", path], text=True, capture_output=True)
    if p.returncode != 0:
        return {"_error": (p.stderr or p.stdout).strip()[:800]}
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError:
        return {"_error": "invalid_json", "_raw": p.stdout[:500]}


def classify(tree_a, tree_h, relation):
    if tree_a and tree_h and tree_a == tree_h:
        return "SAME_TREE_DIFFERENT_COMMIT_ID"
    if relation == "ahead":
        return "CONTENT_CHANGED_DIRECT_DESCENDANT"
    if relation == "diverged":
        return "CONTENT_CHANGED_DIVERGED_HISTORY"
    if relation == "behind":
        return "CONTENT_CHANGED_HEAD_BEHIND_APPROVAL"
    if tree_a and tree_h:
        return "CONTENT_CHANGED_OTHER_RELATION"
    return "UNRESOLVED"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    src = json.loads(Path(args.input).read_text())
    changed = [x for x in src["cases"] if x.get("head_changed_after_latest_approval")]
    rules_cache = {}
    branch_cache = {}
    rows = []

    for idx, x in enumerate(changed, 1):
        repo = x["repository"]
        n = x["pull_request_number"]
        approval = x["approval"]
        approval_sha = approval["commit_id"]
        captured_head = x["final_head"]
        base_ref = x["base_ref"]
        print(f"[{idx}/{len(changed)}] {repo}#{n}", file=sys.stderr)

        ac = gh(f"repos/{repo}/git/commits/{approval_sha}")
        hc = gh(f"repos/{repo}/git/commits/{captured_head}")
        cmp = gh(f"repos/{repo}/compare/{approval_sha}...{captured_head}")
        reviews = gh(f"repos/{repo}/pulls/{n}/reviews?per_page=100")

        key = (repo, base_ref)
        encoded_branch = urllib.parse.quote(base_ref, safe="")
        if key not in rules_cache:
            rules_cache[key] = gh(f"repos/{repo}/rules/branches/{encoded_branch}")
        if key not in branch_cache:
            branch_cache[key] = gh(f"repos/{repo}/branches/{encoded_branch}")

        tree_a = (ac.get("tree") or {}).get("sha") if isinstance(ac, dict) else None
        tree_h = (hc.get("tree") or {}).get("sha") if isinstance(hc, dict) else None
        relation = cmp.get("status") if isinstance(cmp, dict) else None
        files = cmp.get("files") if isinstance(cmp, dict) and isinstance(cmp.get("files"), list) else []

        review_id = None
        try:
            review_id = int((approval.get("review_url") or "").rsplit("-", 1)[-1])
        except Exception:
            pass
        matched_review = None
        if isinstance(reviews, list):
            if review_id:
                matched_review = next((rv for rv in reviews if rv.get("id") == review_id), None)
            if matched_review is None:
                matched_review = next(
                    (
                        rv
                        for rv in reviews
                        if rv.get("commit_id") == approval_sha
                        and (rv.get("user") or {}).get("login") == approval.get("actor")
                        and rv.get("submitted_at") == approval.get("submitted_at")
                    ),
                    None,
                )

        rules = rules_cache[key]
        pr_rules = []
        if isinstance(rules, list):
            for rule in rules:
                if rule.get("type") != "pull_request":
                    continue
                prm = rule.get("parameters") or {}
                pr_rules.append(
                    {
                        "ruleset_id": rule.get("ruleset_id"),
                        "ruleset_source": rule.get("ruleset_source"),
                        "ruleset_source_type": rule.get("ruleset_source_type"),
                        "dismiss_stale_reviews_on_push": prm.get("dismiss_stale_reviews_on_push"),
                        "require_last_push_approval": prm.get("require_last_push_approval"),
                        "required_approving_review_count": prm.get("required_approving_review_count"),
                        "require_code_owner_review": prm.get("require_code_owner_review"),
                        "require_review_thread_resolution": prm.get("required_review_thread_resolution"),
                    }
                )

        branch = branch_cache[key]
        rows.append(
            {
                "repository": repo,
                "pull_request_number": n,
                "pull_request_url": x["pull_request_url"],
                "pull_request_title": x["pull_request_title"],
                "state": x["state"],
                "merged": x["merged"],
                "base_ref": base_ref,
                "approval_commit": approval_sha,
                "captured_final_or_current_head": captured_head,
                "approval_tree": tree_a,
                "captured_head_tree": tree_h,
                "same_tree": bool(tree_a and tree_h and tree_a == tree_h),
                "content_delta_class": classify(tree_a, tree_h, relation),
                "comparison": {
                    "compare_status": relation,
                    "ahead_by": cmp.get("ahead_by") if isinstance(cmp, dict) else None,
                    "behind_by": cmp.get("behind_by") if isinstance(cmp, dict) else None,
                    "total_commits": cmp.get("total_commits") if isinstance(cmp, dict) else None,
                    "files_reported": len(files),
                    "additions_reported": sum((f.get("additions") or 0) for f in files),
                    "deletions_reported": sum((f.get("deletions") or 0) for f in files),
                    "changed_paths_sample": [f.get("filename") for f in files[:20]],
                },
                "captured_approval_review_current_state": matched_review.get("state") if matched_review else None,
                "review_lookup_status": "MATCHED" if matched_review else "NOT_MATCHED",
                "current_branch_rules_snapshot": {
                    "scope": "CURRENT_RULESETS_ONLY_NOT_HISTORICAL",
                    "pull_request_rules": pr_rules,
                    "rules_api_error": rules.get("_error") if isinstance(rules, dict) else None,
                    "branch_metadata_protected": branch.get("protected") if isinstance(branch, dict) else None,
                    "branch_metadata_error": branch.get("_error") if isinstance(branch, dict) else None,
                    "historical_rule_state_at_approval": "NOT_RECONSTRUCTED",
                },
                "human_materiality_label": "NOT_YET_LABELED",
                "determa_counterfactual_verdict": "NOT_YET_RUN",
                "ground_truth": "NOT_YET_ESTABLISHED",
            }
        )

    pairs = {}
    for row in rows:
        pairs.setdefault((row["repository"], row["base_ref"]), row["current_branch_rules_snapshot"])

    summary = {
        "source_cases": len(src["cases"]),
        "commit_id_mismatches": len(rows),
        "mismatch_rate_percent": round(len(rows) / len(src["cases"]) * 100, 1),
        "different_git_tree": sum(not x["same_tree"] for x in rows),
        "same_git_tree_different_commit_id": sum(x["same_tree"] for x in rows),
        "direct_descendant_relation": sum(x["comparison"]["compare_status"] == "ahead" for x in rows),
        "direct_descendant_with_content_change": sum(
            x["content_delta_class"] == "CONTENT_CHANGED_DIRECT_DESCENDANT" for x in rows
        ),
        "diverged_history_with_content_change": sum(
            x["content_delta_class"] == "CONTENT_CHANGED_DIVERGED_HISTORY" for x in rows
        ),
        "captured_head_behind_approval_commit": sum(
            x["comparison"]["compare_status"] == "behind" for x in rows
        ),
        "captured_approval_review_current_state_approved": sum(
            x["captured_approval_review_current_state"] == "APPROVED" for x in rows
        ),
        "unique_repository_base_branch_pairs": len(pairs),
        "current_branch_pairs_protected_true": sum(
            v.get("branch_metadata_protected") is True for v in pairs.values()
        ),
        "current_branch_pairs_protected_false": sum(
            v.get("branch_metadata_protected") is False for v in pairs.values()
        ),
        "current_branch_pairs_missing_or_unavailable": sum(
            v.get("branch_metadata_protected") is None for v in pairs.values()
        ),
        "current_branch_pairs_with_visible_pull_request_ruleset_rule": sum(
            bool(v.get("pull_request_rules")) for v in pairs.values()
        ),
        "visible_pull_request_rules_with_stale_review_dismissal_enabled": sum(
            any(pr.get("dismiss_stale_reviews_on_push") is True for pr in v.get("pull_request_rules", []))
            for v in pairs.values()
        ),
        "visible_pull_request_rules_with_last_push_approval_enabled": sum(
            any(pr.get("require_last_push_approval") is True for pr in v.get("pull_request_rules", []))
            for v in pairs.values()
        ),
    }

    result = {
        "version": 4,
        "source_dataset": Path(args.input).name,
        "source_methodology_id": src.get("methodology_id"),
        "captured_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "signal_name": "APPROVAL_COMMIT_DIFFERS_FROM_CAPTURED_FINAL_OR_CURRENT_HEAD",
        "purpose": "Enrich the 30 observed approval/head mismatches without treating commit-ID change as equivalent to material risk.",
        "summary": summary,
        "truth_boundary": [
            "A different commit ID does not by itself prove a material code change, unsafe execution, policy bypass, or vulnerability.",
            "Current branch rules are a point-in-time snapshot and do not establish which GitHub controls were enabled when the historical approval occurred.",
            "Automated content-delta classes are descriptive, not human materiality judgments.",
            "No DETERMA effectiveness, false-positive, false-negative, or customer outcome claim is made by this enrichment.",
        ],
        "changed_cases": rows,
    }
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
