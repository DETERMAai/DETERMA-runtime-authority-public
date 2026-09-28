# Benchmark V4 — approval/head mismatch enrichment

## Purpose

V3 asks one narrow question across 200 public GitHub pull-request approval histories: does the captured final/current PR head SHA differ from the exact commit ID attached to the latest captured APPROVED review?

V4 does **not** replace that corpus. It enriches only the 30 V3 mismatches so that a commit-ID mismatch is not silently treated as a material or unsafe change.

## Source corpus

- Source: `data/approval-continuity-benchmark-v3-200.json`
- 10 repositories for agentic / AI-agent projects, selected in advance.
- 20 valid recent approved PR histories per repository.
- 200 valid histories total.
- 30 approval-commit / captured-head mismatches (15% of this purposive corpus).

## V4 enrichment

For each of the 30 mismatches, V4 records:

1. The Git tree SHA for the approval-bound commit and the captured final/current head.
2. Whether the two commits have the same tree.
3. GitHub's commit-comparison relation (`ahead`, `behind`, `diverged`, or other).
4. File/addition/deletion counts returned by the compare API.
5. The current API state of the exact review object captured by V3.
6. A current point-in-time snapshot of public branch metadata and GitHub Rules API pull-request rules for the target branch where observable.
7. Explicit placeholders for human materiality labels, DETERMA counterfactual decisions, and ground truth. These remain unfilled until independently evaluated.

## Observed V4 descriptive result

Among the 30 V3 commit-ID mismatches:

- 29 have a different Git tree.
- 1 has the same Git tree despite a different commit ID.
- 26 captured heads are descendants of the approval commit; 25 of those 26 also have content changes.
- 3 have diverged history with different trees.
- 1 captured head is behind the approval commit.
- The exact captured review object currently reports `APPROVED` in all 30 cases at the V4 recapture time.

These are descriptive facts about the captured records. They are **not** materiality, safety, policy-bypass, or vulnerability judgments.

## GitHub control baseline

GitHub documents two relevant optional controls:

- dismiss stale pull-request approvals when reviewable commits change the PR diff;
- require approval of the most recent reviewable push.

Official references:

- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
- https://docs.github.com/en/rest/repos/rules

V4 records a **current** Rules API snapshot only. That snapshot does not reconstruct which rules were active at the time of each historical approval. A missing pull-request rule in the Rules API is not interpreted as proof that there was no classic branch protection.

## Current rules snapshot in this capture

Across 13 unique repository/base-branch pairs represented by the 30 mismatches:

- 10 current branch records report `protected=true`.
- 1 reports `protected=false`.
- 2 historical target branches are no longer retrievable by name.
- 5 branch targets expose at least one current pull-request rule through the Rules API.
- none of those visible current pull-request rules have stale-review dismissal enabled;
- one has last-push approval enabled.

These values are a point-in-time control snapshot, not historical control state.

## What V4 still does not prove

V4 does not prove:

- that any of the 29 tree-changing cases were materially risky;
- that a repository bypassed or violated its own controls;
- that GitHub's built-in controls were absent at the historical approval time;
- that DETERMA would make the correct decision on these cases;
- DETERMA false-positive or false-negative rates;
- runtime blocking, authoritative readback, receipt correctness, or customer outcomes.

## Next proof layer

The next benchmark layer should add two independent human labels per tree-changing case:

- `MATERIAL_REVIEW_REQUIRED`
- `NON_MATERIAL_OR_MECHANICAL`
- `UNCERTAIN`

Disagreements should be adjudicated. Only after that ground truth exists should DETERMA be run counterfactually on the same frozen cases and compared against both GitHub's observable baseline and the adjudicated labels.

Recommended metrics:

- sensitivity / recall for material re-review cases;
- specificity;
- false-positive rate;
- false-negative rate;
- incremental detections beyond the observable GitHub baseline;
- reason-code agreement;
- receipt completeness.

## Reproducibility

Run:

```bash
python3 scripts/enrich_benchmark_v4.py \
  --input data/approval-continuity-benchmark-v3-200.json \
  --output data/approval-continuity-benchmark-v4-enriched-30.json
```

The enrichment is read-only against public GitHub metadata. A GitHub CLI login is required because the request volume exceeds practical unauthenticated API limits.

## Truth boundary

A different commit ID is not equivalent to a different tree. A different tree is not equivalent to a material risk. A material risk is not equivalent to a policy bypass. And observing a problem class is not proof that DETERMA solves it.
