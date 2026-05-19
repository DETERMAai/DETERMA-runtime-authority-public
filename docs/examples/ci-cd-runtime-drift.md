# CI/CD Runtime Drift Example

## Scenario

An AI-assisted deployment system receives approval to release infrastructure changes.

Before deployment occurs:

- repository state changes
- deployment topology changes
- runtime dependencies change
- execution scope changes

A traditional pipeline may still execute because approval already exists.

---

## Runtime Failure

```text
Approved deployment
!=
Currently admissible deployment
```

---

## DETERMA Behavior

Before mutation release:

- runtime witness recomputed
- topology continuity validated
- replay validation executed
- admissibility recalculated

If legitimacy continuity fails:

```text
deployment denied
```

---

## Core Invariant

Autonomous deployment commits require runtime legitimacy recomputation.
