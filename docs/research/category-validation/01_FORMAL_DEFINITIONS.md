# 01 — Formal Definitions

**Status:** Candidate Formal Research Definitions  
**Scope:** Theory / Category Validation  
**Runtime Authority:** None  
**Product Claim:** None  
**Public Claim Status:** Not approved for external use

## 1. Purpose

This document defines the minimum vocabulary required to evaluate the State Reconstruction Tax thesis without relying on ambiguous marketing language.

The definitions are provisional and should be revised when challenged by prior art, experiments, or implementation constraints.

## 2. Definition: Intent

**Intent** is a normalized representation of an action an agent or user seeks to perform.

Examples:

- open a pull request
- merge a branch
- deploy a service
- update a CRM record
- modify a contract clause

Intent should not be defined solely by raw natural-language prompt text, because prompt text can be ambiguous, adversarial, or semantically unstable.

## 3. Definition: Operational State

**Operational State** is the minimal set of verified facts required to evaluate and execute an intended action safely, correctly, and within policy.

Operational State may include:

- knowledge state
- authority state
- identity state
- delegation state
- approval state
- environment state
- dependency state
- risk state
- temporal state
- provenance state
- execution-history state

## 4. Definition: Execution-Relevant State

**Execution-Relevant State** is the subset of Operational State that can materially affect whether an intended action should be allowed, denied, delayed, escalated, modified, audited, or rolled back.

A fact is execution-relevant if changing it can change the execution decision or required control path.

## 5. Definition: State Reconstruction

**State Reconstruction** is the process by which an autonomous system derives execution-relevant state from one or more dynamic sources before reasoning or execution.

Sources may include:

- prompts
- memory systems
- retrieval systems
- policy engines
- identity providers
- workflow engines
- source control systems
- CI/CD systems
- cloud control planes
- ticketing systems
- human approvals
- audit logs

## 6. Definition: State Reconstruction Tax

**State Reconstruction Tax** is the computational, latency, coordination, token, tool-call, and risk cost associated with repeated state reconstruction.

Formally:

```text
SRT = Cost(repeatedly reconstructing execution-relevant state)
```

Expanded:

```text
SRT = TokenCost + ToolCallCost + LatencyCost + CoordinationCost + ErrorRisk + AuditCost
```

This is a research model, not a measured claim.

## 7. Definition: Verified Execution State

**Verified Execution State** is a bounded, cryptographically verifiable representation of execution-relevant operational state that is valid only within explicit freshness, provenance, and decision constraints.

Verification includes integrity and provenance checks, but does not automatically prove semantic correctness.

## 8. Definition: Verified State Object

A **Verified State Object** is a concrete representation of Verified Execution State.

It should include:

- schema version
- state identifier
- intent fingerprint
- subject identity digest
- authority digest
- policy digest
- approval digest
- environment digest
- risk digest
- execution-history digest
- freshness window
- invalidation triggers
- source provenance
- decision boundary
- signature

## 9. Definition: State Compiler

A **State Compiler** is a candidate architectural component that collects, verifies, normalizes, bounds, and signs execution-relevant state into a Verified State Object.

The compiler does not replace source-of-truth systems. It produces an execution-oriented representation derived from them.

## 10. Definition: Decision Boundary

A **Decision Boundary** is the explicit set of conditions under which a Verified State Object may be used.

Examples:

- only for a specific intent fingerprint
- only while a repository HEAD remains unchanged
- only for a specific subject identity
- only for a specific policy version
- only until a short TTL expires
- only while an approval remains unrevoked

## 11. Definition: Invalidation Trigger

An **Invalidation Trigger** is an event or state change that makes a Verified State Object unsafe or invalid for reuse.

Examples:

- policy update
- approval revocation
- branch movement
- CI failure
- permission change
- risk threshold change
- incident opening
- environment drift

## 12. Definition: Authority Compression

**Authority Compression** is the candidate mechanism by which repeated natural-language or multi-tool reconstruction of authority-relevant state is replaced by a compact, verified state representation.

This term should remain internal until validated, because it may be misunderstood as compressing or weakening policy detail.

## 13. Definition: Category Candidate

A **Category Candidate** is a proposed market or technical category that has not yet satisfied evidence requirements for public category creation.

A Category Candidate requires:

- clear problem definition
- distinct prior-art boundary
- measurable cost or risk
- reusable abstraction
- empirical validation
- defensible terminology

## 14. Minimal Formal Model

Let:

```text
I = Intent
S = Operational State
E = Execution Decision
A = Action
```

Then:

```text
E = f(I, S)
A = execute(I, E)
```

If S is reconstructed repeatedly across agents or steps:

```text
TotalCost = ReasoningCost + ExecutionCost + ReconstructionCost
```

The thesis is that ReconstructionCost may be material and reducible through verified state reuse.

## 15. Governance Note

These definitions are candidate research definitions. They do not create canonical runtime contracts, public claims, or product obligations.
