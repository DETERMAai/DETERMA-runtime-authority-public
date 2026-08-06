# 05 — Reference Architecture

**Status:** Candidate Reference Architecture  
**Scope:** Research / Experiments / Category Validation  
**Runtime Authority:** None  
**Product Claim:** None  
**Public Claim Status:** Not approved for external use

## 1. Purpose

This document proposes a research-only reference architecture for testing whether verified execution state can reduce state reconstruction cost in agentic workflows.

It is not a production architecture and does not define a runtime contract.

## 2. Architecture Goal

The architecture must allow experiments to compare:

- agents that reconstruct state through prompts and tool calls
- agents that rely on RAG or memory
- agents that rely on authorization engines
- agents that rely on workflow state
- agents that consume a verified execution-state object

## 3. High-Level Flow

```text
User / Agent Intent
        ↓
Intent Normalizer
        ↓
State Collection Layer
        ↓
Source Verification Layer
        ↓
Policy / Authority Evaluation Layer
        ↓
State Compiler
        ↓
Verified Execution State Object
        ↓
Execution Gate
        ↓
Tool / System Execution
        ↓
Append-only Audit Journal
```

## 4. Components

### 4.1 Intent Normalizer

Transforms raw user or agent requests into structured intent.

Responsibilities:

- extract action type
- bind target resource
- bind subject identity
- bind delegated-agent identity
- compute intent fingerprint
- detect ambiguity

Failure mode:

- overbroad or unstable fingerprints may permit unsafe reuse

### 4.2 State Collection Layer

Collects execution-relevant state from source systems.

Possible sources:

- Git provider
- CI/CD system
- identity provider
- policy repository
- approval workflow
- risk system
- incident management system
- ticketing system
- audit log

Requirement:

- source data must be separately attributable

### 4.3 Source Verification Layer

Validates that collected state is authentic, fresh, and fit for use.

Checks may include:

- source identity
- timestamp
- version
- integrity
- freshness
- revocation status
- schema compatibility

Important limitation:

- cryptographic integrity does not prove semantic correctness

### 4.4 Policy / Authority Evaluation Layer

Evaluates whether the requested intent is permitted under current authority and policy.

This layer may call an authorization engine but should also preserve the surrounding inputs, provenance, and decision boundaries.

### 4.5 State Compiler

Compiles collected and verified state into a compact execution-oriented object.

Responsibilities:

- canonicalize state
- include source provenance
- include invalidation triggers
- define decision boundary
- apply TTL
- sign object
- emit audit reference

### 4.6 Verified Execution State Object

A bounded, signed representation of execution-relevant operational state.

It should not be treated as a general memory object.

### 4.7 Execution Gate

Consumes the Verified Execution State Object and decides whether execution may proceed.

Possible results:

- ALLOW
- DENY
- ESCALATE
- REQUIRE_FRESH_RECONSTRUCTION

### 4.8 Append-only Audit Journal

Records:

- intent
- state object ID
- source provenance
- policy decision inputs
- decision result
- execution result
- invalidation events
- replay attempts

## 5. Invalidation Model

A state object must become invalid when relevant source conditions change.

Candidate invalidation triggers:

- policy version change
- approval revocation
- branch HEAD movement
- CI status change
- permission change
- role change
- risk threshold change
- incident opening
- environment drift
- TTL expiration

## 6. Safety Model

Default behavior should be conservative.

If verification fails, invalidation cannot be checked, or state is ambiguous, the system should fall back to fresh reconstruction or escalation rather than reuse stale state.

## 7. Benchmark Instrumentation

The reference architecture must log:

- prompt tokens
- completion tokens
- tool calls
- model calls
- state-collection calls
- authorization calls
- verification latency
- compilation latency
- execution-gate latency
- false allow / false deny
- stale-state attempts
- replay attempts

## 8. Non-Goals

This architecture does not attempt to:

- replace RAG
- replace memory
- replace authorization engines
- replace workflow engines
- replace source-of-truth systems
- define public product architecture
- claim production readiness

## 9. Key Research Risk

The central risk is that the architecture may introduce too much complexity relative to the measured savings.

The benchmark must therefore measure total system cost, not only token reduction.

## 10. Governance Note

This is a candidate research architecture. It may inform future implementation only after experimental validation and maintainer review.
