# Canonical Governed Execution Demo

## Flow

```text
Approval issued
-> runtime changed
-> execution attempted
-> legitimacy recomputed
-> execution denied
-> replay denied
-> append-only audit preserved
```

## Purpose

The demo demonstrates one core runtime invariant:

> Autonomous execution should not commit unless runtime legitimacy still survives.

## What The Demo Shows

- runtime drift
- stale authority
- admissibility recomputation
- replay denial
- deterministic release gating
- append-only audit preservation
