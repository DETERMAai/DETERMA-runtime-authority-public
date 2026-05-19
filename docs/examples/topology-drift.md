# Topology Drift Example

## Sequence

```text
Approval issued for topology A
-> orchestration path changes
-> execution routed through topology B
-> legitimacy recomputed
-> execution denied
```

## Failure Without Topology Awareness

The mutation executes in a runtime environment different from the one originally approved.

The authority scope silently expands.

## DETERMA Behavior

Execution legitimacy depends on runtime topology continuity.

Topology divergence invalidates release admissibility.

## Core Invariant

Execution legitimacy must remain topology-aware.
