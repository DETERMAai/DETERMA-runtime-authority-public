# Stale Approval Example

## Sequence

```text
09:00 -> AI proposes mutation
09:01 -> Human approves mutation
09:07 -> Repository state changes
09:09 -> Execution attempts release
09:09 -> Runtime legitimacy recomputed
09:09 -> Execution denied
```

## Failure Without Runtime Legitimacy

A traditional approval-only system executes because approval exists.

The system does not verify whether the original authority context still survives.

## DETERMA Behavior

DETERMA binds release authority to the current runtime witness.

If runtime continuity diverges from the approved state:

```text
execution = denied
```

## Core Invariant

Historical approval alone is insufficient execution authority.
