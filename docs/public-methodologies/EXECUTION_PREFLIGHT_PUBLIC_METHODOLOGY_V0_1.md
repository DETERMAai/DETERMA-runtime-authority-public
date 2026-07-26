# Execution Preflight

## The gate between a good plan and an authorized change

**By Idan Plaut**  
**Public Methodology v0.1 — July 2026**  
**Status: PROVISIONAL PUBLIC METHODOLOGY — NOT BINDING CANON**

> A plan may be technically brilliant and still not be authorized to execute.

Most engineering teams invest heavily in determining whether a plan is correct: whether the architecture is sound, edge cases are covered, requirements are understood, and the agent has inspected the relevant code.

Those questions matter, but they answer only half of the problem.

Before allowing an AI agent to build, modify a repository, open a pull request, update a database, or invoke an API that changes state, I run two distinct processes:

1. **Decision Interrogation** — systematically expose assumptions, alternatives, and hidden decisions.
2. **Execution Preflight** — determine whether the exact proposed action is authorized to execute now.

Decision Interrogation asks:

> Did we decide correctly?

Execution Preflight asks:

> Is this exact action still authorized to execute now?

These are not two versions of the same checklist. They solve different failure classes.

## The failure: assumption silently becoming authority

The most expensive failures do not always begin with bad code. They often begin with quiet assumptions:

- “It is probably fine to update this additional file.”
- “The branch still looks the same.”
- “The approval from earlier is probably still valid.”
- “The user said proceed, so execution must be allowed.”
- “The tests passed, therefore the change was authorized.”
- “The agent needs broad credentials to finish the task.”

Each statement contains a dangerous transition:

```text
Assumption → Decision → Authority
```

An unexamined assumption becomes a decision. An implicit decision becomes permission. Ambiguous permission becomes real mutation.

Execution Preflight exists to stop that transition.

## Definition

**Execution Preflight is a bounded execution contract created or validated immediately before mutation.**

It defines:

- the exact target;
- the target's current state;
- the exact action allowed;
- the permitted scope;
- explicitly forbidden actions;
- invariants that must remain true;
- hard-stop conditions;
- the constrained executor permitted to act;
- the evidence required to prove that execution matched approval.

Mutation includes more than writing code. It includes file changes, commits, branches, pull requests, comments, reviews, CI changes, deployments, database writes, permission or secret changes, document edits, and external API calls that create or alter state.

## Decision Interrogation vs. Execution Preflight

| Dimension | Decision Interrogation | Execution Preflight |
|---|---|---|
| Core question | Did we decide correctly? | Is this action authorized now? |
| Focus | Assumptions, options, decisions | Scope, state, authority, evidence |
| Output | Explicit plan | Bounded execution contract |
| Typical failure prevented | Missing or incorrect decision | Unauthorized or over-broad mutation |
| Timing | During planning | Immediately before mutation |

Decision Interrogation turns assumptions into explicit decisions.

Execution Preflight prevents decisions from automatically becoming authority.

## The nine parts of Execution Preflight

### 1. Exact Target

Identify the target without ambiguity: repository, branch, pull request, database, environment, document, API resource, account, file path, or commit SHA.

“The project repository” is not an exact target. A full repository identifier, branch, pull request number, and expected head SHA are.

### 2. Current-State Binding

Approval is granted relative to a particular state. If the state changes, the approval may no longer apply.

Bind the operation to evidence such as:

- current commit SHA;
- file hashes;
- pull-request state;
- changed-file set;
- unresolved review threads;
- CI status;
- database version;
- deployment revision;
- permission state.

Approval granted yesterday is not necessarily approval to execute against state that changed this morning.

### 3. Exact Allowed Scope

Define positively what may change.

Avoid:

> Update the document as needed.

Prefer:

> Modify this exact file only, and only the explicitly listed subjects.

A strong scope identifies allowed files, fields, operations, semantic changes, expected result, and maximum attempts.

Anything omitted from scope is not implied permission.

### 4. Explicit Forbidden Actions

Define what must not occur, for example:

- no merge;
- no deployment;
- no comments;
- no review-thread resolution;
- no dependency changes;
- no formatting sweep;
- no unrelated refactor;
- no secret access;
- no permission changes;
- no additional files.

Agents often try to help beyond the task. In a governed system, initiative outside scope is not a bonus. It is a violation.

### 5. Preserved Invariants

An invariant must remain true before, during, and after execution.

Examples:

- the pull request remains Draft;
- the changed-file count remains one;
- an unrelated branch remains unchanged;
- approval cannot be replayed;
- audit remains append-only;
- the executor receives no general shell;
- required CI passes;
- unrelated review threads remain unchanged.

A requirement describes what should be created. An invariant describes what must not be broken while creating it.

### 6. Hard-Stop Conditions

Define in advance when execution must stop rather than “work around” uncertainty.

Hard stops include:

- SHA mismatch;
- branch drift;
- dirty working tree;
- unexpected file changes;
- ambiguous scope;
- missing or mismatched approval;
- failed CI;
- a new review thread that changes requirements;
- missing target;
- unavailable audit;
- credentials broader than required;
- unavailable post-execution verification.

Fail-closed is not inflexibility. It is a deliberate refusal to convert uncertainty into permission.

### 7. Fresh and Bounded Authority

Human approval is necessary, but the word “approved” alone is not a complete execution contract.

Effective authority should be:

- bound to an exact target;
- bound to exact state;
- limited in time;
- limited to one action class;
- limited to one executor;
- single-use where required;
- impossible to broaden through inference.

A general instruction such as “proceed” may authorize further analysis or discovery. It does not automatically authorize undefined mutation.

### 8. Constrained Executor

The component that decides should not be the component that performs unrestricted mutation.

The executor should receive only the capability required for the exact action, such as:

- editing one approved file;
- opening one Draft PR;
- running one signed migration;
- updating one specific API resource.

It should not receive a general shell, broad organization token, access to every repository, authority to expand scope, or the ability to approve its own output.

> A capable agent is not automatically an authorized executor.

### 9. Post-Execution Evidence

Success is not “the command completed without an exception.”

Success is evidence that the action performed matches the action approved.

Possible evidence includes:

- resulting commit SHA;
- exact changed-file list;
- actual diff;
- CI result;
- pull-request state;
- database receipt;
- deployment revision;
- API response and readback;
- audit record;
- before-and-after hashes;
- verification result.

The evidence contract must be defined before execution. Otherwise, it is too easy to select convenient evidence after the fact.

## Recommended flow

```text
DISCOVERY
    ↓
DECISION INTERROGATION
    ↓
PLAN / SPEC
    ↓
EXECUTION PREFLIGHT
    ↓
HUMAN APPROVAL GATE
    ↓
CONTROLLED MUTATION
    ↓
POST-EXECUTION VERIFICATION
    ↓
EVIDENCE / RECEIPT
```

Each stage has a separate responsibility:

- Discovery observes reality.
- Decision Interrogation exposes assumptions and decisions.
- Plan defines the desired action.
- Execution Preflight defines authority boundaries.
- Approval authorizes explicit scope.
- Executor performs a constrained action.
- Verification compares approved intent with actual outcome.
- Evidence proves what happened.

No stage should impersonate the next:

- A plan is not approval.
- Approval is not execution.
- Execution is not verification.
- Verification is not authority.

## Minimal template

```yaml
execution_preflight:
  operation_id: ""

  target:
    system: ""
    repository: ""
    branch: ""
    pull_request: ""
    resource: ""
    expected_state:
      head_sha: ""
      file_hashes: {}
      status: ""

  allowed_scope:
    operations: []
    files: []
    fields: []
    semantic_changes: []
    max_attempts: 1

  forbidden_actions:
    - scope_expansion
    - unrelated_changes
    - permission_changes
    - secret_access
    - merge
    - deployment

  invariants: []

  hard_stops:
    - target_state_drift
    - ambiguous_scope
    - missing_approval
    - unexpected_changed_file
    - verification_unavailable
    - audit_failure

  authority:
    approver: ""
    approved_scope_hash: ""
    valid_until: ""
    single_use: true

  executor:
    type: ""
    identity: ""
    allowed_capabilities: []

  validation:
    pre_execution: []
    post_execution: []

  required_evidence:
    - resulting_sha
    - actual_changed_files
    - actual_diff
    - validation_results
    - final_target_state
    - execution_receipt
```

## Three adoption levels

### Level 1 — Manual Preflight

A standard document or prompt is completed before mutation. Suitable for teams beginning to use coding agents.

### Level 2 — Tool-Assisted Preflight

A tool automatically collects repository state, SHA, changed files, CI, review threads, and permissions. A human still approves the exact scope.

### Level 3 — Enforced Execution Authority

Infrastructure prevents mutation when approval is missing, state has changed, scope does not match, authority has expired, the executor is unauthorized, or required evidence cannot be produced.

At this level, Execution Preflight stops being text and becomes infrastructure.

## The principle

Decision Interrogation prevents us from building the wrong thing.

Execution Preflight prevents us from executing the right thing in an unauthorized way.

As AI agents become more capable, the important question is no longer only:

> Can the agent do it?

It is:

> Is this exact action still authorized to execute now?

A plan may be brilliant and still not be authorized to execute.

The most expensive failures do not always begin with bad code.

They begin where assumption quietly becomes authority.

## License and use

This public methodology may be cited and adapted with attribution to **Idan Plaut**.

It is a conceptual operating framework, not a claim that any specific system is production-ready or fully implemented.
