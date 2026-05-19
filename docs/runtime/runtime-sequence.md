# Runtime Legitimacy Sequence

## Autonomous Mutation Lifecycle

```text
AI proposes mutation
        ↓
Approval issued
        ↓
Runtime conditions drift
        ↓
Execution attempts release
        ↓
Runtime legitimacy recomputed
        ↓
Replay validation performed
        ↓
Admissibility decision computed
        ↓
Commit allowed OR denied
        ↓
Append-only audit recorded
```

---

## Key Runtime Principle

The approval is historical.

The runtime state is current.

Execution legitimacy exists only if the approved authority context still survives at release time.

---

## Failure Without Runtime Legitimacy

Traditional systems often assume:

```text
approval = durable execution trust
```

Under runtime drift, that assumption becomes invalid.

---

## DETERMA Runtime Model

DETERMA treats mutation release as a governed runtime commit.

Execution pauses until admissibility is recomputed against the current runtime witness.
