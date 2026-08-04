# DETERMA Runtime Authority

![Status](https://img.shields.io/badge/status-public_architecture-1f5fae)
![Authority](https://img.shields.io/badge/authority_effect-none-5b6573)
![Scope](https://img.shields.io/badge/scope-runtime_legitimacy-12324a)
![Production](https://img.shields.io/badge/production_claim-none-7a3e00)

**Public category and architecture surface for execution-time legitimacy in autonomous systems.**

DETERMA addresses one narrow but consequential question:

> Is this exact action still authorized to execute now?

Approval, identity, permissions, policy checks and CI results remain necessary. DETERMA focuses on continuity between the authority granted earlier and the exact artifact, target and live state presented at execution time.

## Repository Boundary

| Dimension | Classification |
|---|---|
| Repository role | Public explanation and category architecture |
| Runtime authority | None |
| Mutation capability | None |
| Customer deployment claim | None |
| Intended audience | Engineering, Security, Platform, Architecture and Design Partners |

This repository explains the category and public runtime model. It intentionally excludes implementation-bearing authority code, private diligence artifacts and unreleased enforcement mechanics.

## Enterprise Architecture View

```mermaid
flowchart TB
    A[Human, Agent or Workflow proposes an action]
    B[Approval and authority context is established]
    C[Time passes and material state may drift]

    subgraph E[Existing Enterprise Controls]
      E1[Identity and IAM]
      E2[GitHub and CI/CD]
      E3[Policy and AppSec]
      E4[Ticketing, exceptions and release state]
    end

    subgraph D[DETERMA Runtime Execution Authority]
      D1[Action Envelope]
      D2[Evidence and live-state resolution]
      D3[Approval-continuity evaluation]
      D4[Deterministic authority decision]
      D5[Reason-coded Authority Receipt]
      D1 --> D2 --> D3 --> D4 --> D5
    end

    F{Execution-time outcome}
    G[ALLOW]
    H[NEEDS_REVIEW]
    I[DENY]
    J[Execute through the existing system]
    K[Route to an accountable reviewer]
    L[Preserve evidence and halt mutation]

    A --> B --> C --> D1
    E1 -. evidence .-> D2
    E2 -. evidence .-> D2
    E3 -. evidence .-> D2
    E4 -. evidence .-> D2
    D5 --> F
    F --> G --> J
    F --> H --> K
    F --> I --> L

    classDef primary fill:#e8f1ff,stroke:#1f5fae,color:#102a43,stroke-width:2px;
    classDef authority fill:#eef7ff,stroke:#0f4c81,color:#102a43,stroke-width:2px;
    classDef outcome fill:#f7fafc,stroke:#5b6573,color:#102a43;
    class A,B,C,E1,E2,E3,E4 primary;
    class D1,D2,D3,D4,D5 authority;
    class F,G,H,I,J,K,L outcome;
```

### What the diagram means

1. Existing systems remain authoritative for identity, permissions, workflow state, policy findings and source records.
2. DETERMA normalizes the proposed action and the supporting evidence into an action-level decision context.
3. Material evidence is resolved again at the execution checkpoint.
4. The output is deterministic, explainable and accompanied by a receipt.
5. `NEEDS_REVIEW` is the canonical reviewer-routing outcome; it does not authorize execution.
6. Execution still occurs through the existing enterprise system or a separately governed executor.

## Core Runtime Failure

```text
Approved earlier
!=
Legitimate now
```

State can change between approval and execution:

- artifact or commit movement;
- target or environment change;
- policy, waiver or release-state change;
- concurrent mutation;
- stale runtime witness;
- replay of a consumed authority grant.

## Runtime Flow

```text
proposal
-> approval context
-> runtime drift window
-> evidence and live-state resolution
-> legitimacy recomputation
-> ALLOW, NEEDS_REVIEW or DENY
-> reason-coded receipt
```

## Runtime Concepts

- [Why approval is insufficient](docs/runtime/why-approval-is-insufficient.md)
- [Runtime legitimacy](docs/runtime/runtime-legitimacy.md)
- [Runtime legitimacy sequence](docs/runtime/runtime-sequence.md)
- [Mutation commit integrity](docs/runtime/mutation-commit-integrity.md)
- [Runtime drift failures](docs/runtime/runtime-drift-failures.md)

## Failure Examples

- [Stale approval](docs/examples/stale-approval.md)
- [Replay authority](docs/examples/replay-authority.md)
- [Topology drift](docs/examples/topology-drift.md)
- [CI/CD runtime drift](docs/examples/ci-cd-runtime-drift.md)

## Public Demo

- [Canonical MVP demo](docs/mvp/canonical-demo.md)
- [Public demo](PUBLIC_DEMO.md)

## Truth Boundary

This repository does **not** claim:

- a production-deployed enterprise control plane;
- customer validation or an active customer pilot;
- universal coverage of every execution path;
- a packaged customer-hosted deployment;
- replacement of IAM, CI/CD, AppSec, policy engines or human approval.

## Core Sentence

**Permissions define what an identity may do in principle. DETERMA evaluates whether this exact action is still authorized now.**
