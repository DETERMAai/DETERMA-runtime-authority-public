# Public Demo

## The Problem

An AI system receives approval to perform a mutation.

Before execution occurs, runtime conditions change.

Most systems still execute because approval exists.

DETERMA asks a stricter question:

> Is this exact execution still legitimate right now?

---

## Demo Flow

```text
AI proposes mutation
-> human approval issued
-> runtime state changes
-> execution attempts release
-> legitimacy recomputed
-> execution denied
-> replay denied
-> append-only audit preserved
```

---

## What The Demo Proves

The demo demonstrates one runtime invariant:

> Historical approval alone is insufficient execution authority.

---

## What Is Intentionally Not Public

The public demo does not expose:

- enforcement internals
- release mechanics
- replay invalidation internals
- witness generation semantics
- constitutional kernel mechanics
- implementation-bearing runtime code
