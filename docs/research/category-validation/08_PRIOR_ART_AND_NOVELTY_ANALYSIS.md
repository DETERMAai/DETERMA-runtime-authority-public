# 08 — Prior Art and Novelty Analysis

**Status:** Candidate Prior-Art Analysis Scaffold  
**Scope:** Research / Category Validation / Novelty Assessment  
**Runtime Authority:** None  
**Product Claim:** None  
**Public Claim Status:** Not approved for external use

## 1. Purpose

This document defines the prior-art review required before DETERMA can treat State Reconstruction Tax or Verified Execution State Infrastructure as a defensible category candidate.

This document is intentionally conservative. Its purpose is to find overlap, not to prove novelty.

## 2. Core Novelty Question

Is there a distinct infrastructure abstraction for agentic systems that:

1. compiles execution-relevant operational state,
2. verifies freshness and provenance,
3. binds state to a specific intent and decision boundary,
4. supports invalidation and replay resistance,
5. reduces repeated state reconstruction across agents or steps,
6. and is distinct from memory, workflow, authorization, tool protocols, and generic agent framework state?

If the answer is no, the thesis should be downgraded.

## 3. Prior-Art Domains to Review

### 3.1 Memory and RAG Systems

Questions:

- Do memory systems already manage execution state rather than only knowledge state?
- Do they provide freshness, invalidation, and revocation semantics?
- Do they support policy-aware execution boundaries?
- Do they reduce token use enough to make verified state unnecessary?

Potential overlap:

- persistent memory
- episodic memory
- semantic memory
- agent memory graphs
- context compression
- retrieval pipelines

Novelty test:

> If a memory system can safely answer what is executable now, this thesis weakens.

### 3.2 Agent Frameworks

Examples to review:

- LangGraph-style graph state and checkpoints
- AutoGen-style multi-agent coordination
- Semantic Kernel-style planning and memory
- CrewAI-style role-based orchestration
- OpenAI Agents SDK-style tool use and tracing

Questions:

- Do frameworks already preserve reusable execution state?
- Is framework state independently verifiable?
- Does it include authority, policy, risk, freshness, provenance, and invalidation?
- Is it portable across frameworks?

Novelty test:

> If framework state can serve as verified execution state across workloads, this thesis weakens.

### 3.3 Authorization and Policy Systems

Examples to review:

- OPA
- ABAC
- RBAC
- XACML
- Cedar
- Zanzibar-like relationship authorization
- capability systems
- object-capability models

Questions:

- Do policy systems already represent the relevant execution state compactly?
- Do they include environment, risk, provenance, execution history, and temporal drift?
- Do they expose reusable state objects or only decisions?
- Do they solve stale approval and replay issues?

Novelty test:

> If authorization systems already provide a reusable execution-state primitive, this thesis weakens.

### 3.4 Workflow and Orchestration Systems

Examples to review:

- workflow engines
- BPM systems
- Temporal-like durable execution systems
- CI/CD workflow state
- approval workflows

Questions:

- Do workflow engines already maintain all relevant state across steps?
- Is workflow state verified and signed?
- Does workflow state include dynamic external environment and authority state?
- Can agents safely rely on it without reconstructing context?

Novelty test:

> If workflow systems already provide complete verified action state, this thesis weakens.

### 3.5 Tool Protocols and MCP-like Systems

Questions:

- Do tool protocols define capability metadata, trust boundaries, and state freshness?
- Do they solve cross-tool implicit trust propagation?
- Can they compile cross-source operational state?
- Do they support invalidation across tools?

Novelty test:

> If tool protocols standardize verified execution state, this thesis becomes a protocol feature rather than a category.

### 3.6 Provenance, Audit, and Supply Chain Systems

Examples to review:

- signed provenance
- SLSA-style attestations
- audit logs
- event sourcing
- append-only journals
- software supply-chain metadata

Questions:

- Do provenance systems already provide action-time state verification?
- Are they consumed before execution or after the fact?
- Can they reduce state reconstruction?

Novelty test:

> If provenance systems provide live execution-state objects, this thesis weakens.

### 3.7 Distributed Systems and Databases

Examples to review:

- materialized views
- caching and invalidation
- snapshots
- transactions
- consistency models
- control planes
- state machines
- event sourcing

Questions:

- Is Verified Execution State simply a materialized view over operational sources?
- If so, what is uniquely agentic about it?
- Does intent binding and authority validation create a distinct abstraction?

Novelty test:

> If existing state-management abstractions fully cover the use case, the category should be framed as application of known systems principles to agents, not as a new category.

### 3.8 Operating Systems and Capability Models

Questions:

- Are capability tokens, handles, leases, and access-control checks prior art for Verified State Objects?
- Does the thesis add agent-specific state reconstruction economics?
- Is the model closer to OS capability leasing than AI governance?

Novelty test:

> If OS capability models fully describe the abstraction, the novelty lies only in application context.

## 4. Potential Novelty Claim — Conservative Version

A defensible novelty claim may be:

> The candidate contribution is not authorization, memory, workflow, or caching individually. It is the composition of verified, freshness-bounded, intent-bound, provenance-aware operational state as an agent-consumable execution primitive, evaluated through the lens of repeated state reconstruction cost.

This is a hypothesis, not a fact.

## 5. Potential Novelty Claim — Strong Version

A stronger claim would require evidence:

> Agentic AI systems require a new infrastructure layer for Verified Execution State because existing memory, workflow, authorization, and framework-state systems do not provide reusable, freshness-bounded, provenance-aware, intent-bound operational state with measurable reduction in reconstruction cost and no safety regression.

This claim must not be used externally before empirical validation.

## 6. Required Evidence Before Promotion

Before the category thesis can advance, the team must produce:

1. a cited prior-art review
2. benchmark results
3. baseline comparison
4. failure analysis
5. terminology validation
6. implementation feasibility review
7. safety and correctness evaluation

## 7. Outcome Taxonomy

Possible outcomes:

### Outcome A — New Category Candidate

The thesis survives prior art and benchmarks.

### Outcome B — Architectural Pattern

The thesis is useful but not market-category-worthy.

### Outcome C — Product Feature

The thesis is best treated as a feature inside DETERMA runtime authority.

### Outcome D — Rejected Thesis

Existing systems solve the problem or the cost is not material.

## 8. Governance Note

This document is a scaffold. It is not a completed literature review and contains no final novelty conclusion.
