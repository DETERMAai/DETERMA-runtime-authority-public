# Materiality labeling rubric V1

## Goal

Create an independent ground-truth layer for the 29 V4 cases where the approval-bound commit and captured head have different Git trees.

This rubric does not ask whether the repository was vulnerable or whether policy was bypassed. It asks a narrower counterfactual question:

> If a reviewer approved the approval-bound commit, would the content difference present in the captured head reasonably require renewed human review before a consequential execution or merge decision?

## Labels

### MATERIAL_REVIEW_REQUIRED

Use when the post-approval content difference can reasonably change behavior, security, permissions, data handling, build/release behavior, dependencies, user-visible behavior, or the substantive meaning of the approved change.

Examples include:

- executable code changes;
- dependency or lockfile changes with behavioral/security impact;
- CI/CD or release logic changes;
- authentication, authorization, secrets, network, or policy changes;
- schema or data-model changes;
- substantive configuration changes;
- substantive documentation changes when the approved action itself is documentation/publication and the content meaning changes.

### NON_MATERIAL_OR_MECHANICAL

Use when the difference is mechanically equivalent for the decision being reviewed and does not change the substantive content requiring approval.

Examples may include:

- commit identity changes with no tree change — note: these are excluded from this 29-case labeling queue;
- formatting-only changes;
- generated metadata with no decision-relevant semantic effect;
- mechanical rebases whose resulting reviewed content is demonstrably equivalent.

Do not use this label merely because the diff is small.

### UNCERTAIN

Use when public evidence is insufficient to decide materiality without repository-specific context.

## Review protocol

1. Two reviewers label each case independently.
2. Reviewers should see the approval-bound commit, captured head, content diff, PR context, and relevant changed files.
3. Reviewers should **not** see a DETERMA verdict before submitting their own label.
4. Each reviewer provides a short reason.
5. Disagreements are adjudicated and the reason is recorded.
6. The adjudicated label becomes the benchmark ground truth for later counterfactual evaluation.

## Metrics after adjudication

Once labels are complete, freeze the case set and run DETERMA counterfactually. Report:

- true positives;
- true negatives;
- false positives;
- false negatives;
- sensitivity / recall;
- specificity;
- false-positive rate;
- false-negative rate;
- NEEDS_REVIEW rate;
- coverage of cases not already blocked by the observable GitHub baseline;
- reason-code agreement.

## Critical separation

The benchmark must preserve four separate concepts:

1. **Commit identity mismatch** — SHA differs.
2. **Content-state mismatch** — Git tree differs.
3. **Material review need** — independent human judgment says renewed review is warranted.
4. **DETERMA effectiveness** — the runtime decision matches the frozen ground truth.

No layer may be presented as proof of the next one.
