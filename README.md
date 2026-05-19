# DETERMA

## Runtime legitimacy infrastructure for autonomous execution systems

AI approvals decay after issuance.

Runtime conditions change.

Most systems still execute anyway.

DETERMA recomputes execution legitimacy before autonomous mutations commit.

## Core runtime flow

```text
proposal
-> approval
-> runtime drift
-> legitimacy recomputation
-> replay validation
-> execution or denial
-> append-only audit
```

## Canonical behavior

```text
Approved yesterday.
Runtime changed.
Execution attempted.
DETERMA blocked execution.
Replay denied.
Audit preserved.
```

## Public boundary

This repository explains:

- runtime legitimacy
- runtime drift
- stale authority
- replay-safe execution
- governed mutation release

This repository does not expose:

- enforcement internals
- patent materials
- private kernel semantics
- unreleased runtime mechanics

## Public materials

- [Runtime legitimacy](docs/runtime/runtime-legitimacy.md)
- [Runtime drift failures](docs/runtime/runtime-drift-failures.md)
- [Canonical MVP demo](docs/mvp/canonical-demo.md)
- [Public demo concept](PUBLIC_DEMO.md)

## Core sentence

DETERMA is the runtime legitimacy layer for autonomous execution systems.
