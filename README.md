# DETERMA

## Runtime legitimacy infrastructure for autonomous execution systems

AI approvals decay after issuance.

Runtime conditions change.

Most systems still execute anyway.

DETERMA recomputes execution legitimacy before autonomous mutations commit.

---

## Core Runtime Failure

```text
Approved earlier
!=
Legitimate now
```

---

## Runtime Flow

```text
proposal
-> approval
-> runtime drift
-> legitimacy recomputation
-> replay validation
-> execution or denial
-> append-only audit
```

---

## Canonical Outcome

```text
Approved yesterday.
Runtime changed.
Execution attempted.
DETERMA blocked execution.
Replay denied.
Audit preserved.
```

---

## Runtime Concepts

- [Why approval is insufficient](docs/runtime/why-approval-is-insufficient.md)
- [Runtime legitimacy](docs/runtime/runtime-legitimacy.md)
- [Runtime legitimacy sequence](docs/runtime/runtime-sequence.md)
- [Mutation commit integrity](docs/runtime/mutation-commit-integrity.md)
- [Runtime drift failures](docs/runtime/runtime-drift-failures.md)

---

## Runtime Failure Examples

- [Stale approval](docs/examples/stale-approval.md)
- [Replay authority](docs/examples/replay-authority.md)
- [Topology drift](docs/examples/topology-drift.md)
- [CI/CD runtime drift](docs/examples/ci-cd-runtime-drift.md)

---

## Public Demo

- [Canonical MVP demo](docs/mvp/canonical-demo.md)
- [Public demo](PUBLIC_DEMO.md)

---

## Public Boundary

This repository intentionally excludes:

- enforcement internals
- kernel implementation details
- unreleased runtime mechanics
- private diligence artifacts
- implementation-bearing authority code

---

## Core Sentence

DETERMA is the runtime legitimacy layer for autonomous execution systems.
