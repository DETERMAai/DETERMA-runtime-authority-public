# Why Approval Is Insufficient

Traditional systems assume:

```text
approval = durable execution authority
```

That assumption breaks under autonomous execution.

---

## The Problem

Approval is historical.

Execution happens later.

Between approval and execution:

- repositories change
- infrastructure changes
- topology changes
- capabilities change
- delegation chains change
- runtime semantics change

The approved reality may no longer exist.

---

## The Failure

Most systems still execute because approval exists.

They do not recompute whether the mutation is still admissible under current runtime conditions.

This creates:

- stale authority
- replayable authority
- topology drift
- execution under invalid assumptions
- silent authority expansion

---

## DETERMA

DETERMA treats approval as a historical claim.

Execution authority must be recomputed against the current runtime witness before mutation commit.

If legitimacy continuity fails:

```text
execution denied
```

---

## Core Principle

```text
Approved earlier
!=
Legitimate now
```
