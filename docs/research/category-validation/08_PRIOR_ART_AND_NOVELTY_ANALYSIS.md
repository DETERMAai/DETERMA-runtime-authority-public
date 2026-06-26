# 08 — Prior Art and Novelty Analysis

**Status:** Candidate Prior-Art Analysis v0.2  
**Scope:** Research / Category Validation / Novelty Assessment  
**Runtime Authority:** None  
**Product Claim:** None  
**Public Claim Status:** Not approved for external use

## 1. Purpose

This document records an initial cited prior-art review for the State Reconstruction Tax and Verified Execution State Infrastructure theses.

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

## 3. Initial Evidence Summary

### 3.1 Memory research already touches execution-state management

**Finding:** The thesis is not completely novel at the level of terminology or systems concern.

A 2026 paper, **Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents**, explicitly argues that semantic memory and RAG can fragment trajectories and hinder coherent state reconstruction. It proposes MAGE, a memory system that stores interactions in a hierarchical state tree and lets the agent derive state from the active root-to-current path. The paper reports a 55.1% token-consumption reduction and 7.8–20.4 percentage-point task-success improvement over baselines.

Source:

- https://arxiv.org/abs/2606.06090

**Implication for DETERMA:**

This weakens any broad claim that DETERMA is first to identify execution-state reconstruction as a problem. The defensible distinction must be narrower:

> memory systems may manage execution trajectory state, while DETERMA's candidate thesis concerns verified, policy-aware, authority-bound, freshness-bounded operational state before execution.

**Novelty risk:** High for broad framing; medium for narrow verified-execution-state framing.

### 3.2 Agent action admission control has close prior art

**Finding:** There is close prior art around pre-action admission control for autonomous agents.

A 2026 paper/specification, **Agent Control Protocol: Admission Control for Agent Actions**, defines ACP as an admission-control layer between agent intent and system-state mutation. It includes cryptographic identity, capability-based authorization, deterministic risk evaluation, verifiable delegation, transitive revocation, and immutable auditing.

Source:

- https://arxiv.org/abs/2603.18829

**Implication for DETERMA:**

This is highly relevant and potentially close. It overlaps with runtime authority, cryptographic admission checks, delegation, revocation, and immutable audit. DETERMA must not claim that pre-action authorization or agent admission control is unoccupied.

Potential remaining distinction:

> DETERMA may focus on measuring and reducing State Reconstruction Tax through reusable verified state objects, not merely admission-control semantics.

That distinction is not yet proven.

**Novelty risk:** High.

### 3.3 Authorization systems are strong prior art, but usually narrower than verified operational state

**Finding:** Traditional authorization systems already provide mature policy decision models.

Relevant prior art includes:

- **XACML**: a long-standing OASIS standard for fine-grained, attribute-based access-control policy, Policy Enforcement Points, and Policy Decision Points.
- **Cedar**: an AWS-backed authorization policy language designed to be expressive, fast, safe, and analyzable, with formal modeling and proofs in Lean.
- **Zanzibar / ReBAC**: Google's globally consistent relationship-based authorization system, using relationship tuples and consistency tokens.

Sources:

- XACML overview: https://en.wikipedia.org/wiki/XACML
- Cedar paper: https://arxiv.org/abs/2403.04651
- Zanzibar overview / paper reference: https://en.wikipedia.org/wiki/Google_Zanzibar

**Implication for DETERMA:**

DETERMA must not frame the thesis as inventing authorization, policy decision points, relationship authorization, consistency tokens, or access-control requests.

Potential remaining distinction:

> authorization engines decide whether a request is permitted; verified execution state would compile a broader action-relevant state object containing authority, policy, approvals, environment, risk, provenance, execution history, freshness, and invalidation boundaries.

This distinction is plausible but requires proof that existing authorization architectures cannot provide equivalent value through policy-input materialization and caching.

**Novelty risk:** Medium-high.

### 3.4 Policy-aware agents are not new

**Finding:** The concept of agents acting in changing environments while complying with policies predates current LLM-agent infrastructure.

The 2021 paper **APIA: An Architecture for Policy-Aware Intentional Agents** extends an intentional-agent architecture with policy compliance, authorization and obligation policies, and behavior modes for policy adherence.

Source:

- https://arxiv.org/abs/2109.08287

**Implication for DETERMA:**

DETERMA should avoid implying that policy-aware autonomous agents are a new idea. The possible novelty is in LLM-era execution-state economics, verified state objects, and runtime enforcement at the moment of action.

**Novelty risk:** Medium.

### 3.5 MCP and tool protocols solve connectivity but expose security gaps

**Finding:** MCP-style protocols are strong prior art for connecting agents to tools and data sources, but current research identifies security and trust gaps.

Recent MCP security work identifies issues including missing capability attestation, bidirectional sampling without origin authentication, implicit trust propagation, prompt injection, tool poisoning, descriptor manipulation, and tool metadata attacks.

Sources:

- Breaking the Protocol: Security Analysis of MCP: https://arxiv.org/abs/2601.17549
- MCP threat modeling and tool poisoning: https://arxiv.org/abs/2603.22489
- Securing MCP against tool poisoning and adversarial attacks: https://arxiv.org/abs/2512.06556

**Implication for DETERMA:**

MCP may become the connectivity substrate, but it does not appear to fully solve cross-tool verified operational state, policy-aware invalidation, replay resistance, or authority-bound execution state.

Potential DETERMA framing:

> MCP connects agents to tools; verified execution state determines whether an intended tool-mediated action is still valid under current authority, risk, policy, and environment.

**Novelty risk:** Medium.

### 3.6 Workflow and durable execution systems are relevant but not sufficient by default

**Finding:** Workflow systems and durable execution frameworks maintain state across steps and failures, and therefore overlap with state continuity and replay.

Examples to review further include Temporal-like durable execution systems, BPM, CI/CD workflow state, approval workflows, and event-sourced systems.

**Current evidence status:** Initial review incomplete.

**Implication for DETERMA:**

A workflow engine may already preserve task state, but it may not independently verify authority, environment drift, approval freshness, policy provenance, and agent-specific intent binding. This must be validated through baselines rather than asserted.

**Novelty risk:** Medium; requires deeper review.

### 3.7 Distributed systems and databases are foundational prior art

**Finding:** The thesis clearly overlaps with known systems concepts:

- materialized views
- snapshots
- caching
- invalidation
- consistency tokens
- leases
- event sourcing
- append-only logs
- state machines
- control planes

**Implication for DETERMA:**

The category should not claim that snapshots, caching, invalidation, signed state, or materialization are new. The possible contribution is applying these primitives to LLM-agent execution with explicit measurement of State Reconstruction Tax and safety-preserving verified state reuse.

**Novelty risk:** Medium-high for systems primitives; lower for agent-specific composition if validated.

## 4. Prior-Art Domains Still Requiring Deeper Review

### 4.1 Memory and RAG Systems

Open questions:

- Do memory systems already manage execution state rather than only knowledge state?
- Do they provide freshness, invalidation, and revocation semantics?
- Do they support policy-aware execution boundaries?
- Do they reduce token use enough to make verified state unnecessary?

Known evidence so far:

- MAGE explicitly frames memory as execution-state management and reports token reduction.

Novelty test:

> If a memory system can safely answer what is executable now, this thesis weakens substantially.

### 4.2 Agent Frameworks

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

### 4.3 Authorization and Policy Systems

Examples to review further:

- OPA / Rego
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

### 4.4 Workflow and Orchestration Systems

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

### 4.5 Tool Protocols and MCP-like Systems

Questions:

- Do tool protocols define capability metadata, trust boundaries, and state freshness?
- Do they solve cross-tool implicit trust propagation?
- Can they compile cross-source operational state?
- Do they support invalidation across tools?

Novelty test:

> If tool protocols standardize verified execution state, this thesis becomes a protocol feature rather than a category.

### 4.6 Provenance, Audit, and Supply Chain Systems

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

### 4.7 Distributed Systems and Databases

Questions:

- Is Verified Execution State simply a materialized view over operational sources?
- If so, what is uniquely agentic about it?
- Does intent binding and authority validation create a distinct abstraction?

Novelty test:

> If existing state-management abstractions fully cover the use case, the category should be framed as application of known systems principles to agents, not as a new category.

### 4.8 Operating Systems and Capability Models

Questions:

- Are capability tokens, handles, leases, and access-control checks prior art for Verified State Objects?
- Does the thesis add agent-specific state reconstruction economics?
- Is the model closer to OS capability leasing than AI governance?

Novelty test:

> If OS capability models fully describe the abstraction, the novelty lies only in application context.

## 5. Updated Novelty Assessment

### 5.1 Broad claim — rejected for now

Rejected claim:

> DETERMA discovered a new category called execution state for agents.

Reason:

Memory research, policy-aware agents, authorization systems, workflow systems, and distributed systems already cover major parts of the conceptual space.

### 5.2 Conservative claim — still viable

Potentially defensible internal claim:

> The candidate contribution is not authorization, memory, workflow, MCP, or caching individually. It is the composition of verified, freshness-bounded, intent-bound, provenance-aware operational state as an agent-consumable execution primitive, evaluated through the lens of repeated state reconstruction cost.

Status:

- Hypothesis only.
- Requires benchmarks and safety evaluation.

### 5.3 Strong claim — not currently justified

Strong claim:

> Agentic AI systems require a new infrastructure layer for Verified Execution State because existing memory, workflow, authorization, and framework-state systems do not provide reusable, freshness-bounded, provenance-aware, intent-bound operational state with measurable reduction in reconstruction cost and no safety regression.

Status:

- Not justified yet.
- Must not be used externally before empirical validation.

## 6. Required Evidence Before Promotion

Before the category thesis can advance, the team must produce:

1. completed cited prior-art review,
2. benchmark results,
3. baseline comparison,
4. failure analysis,
5. terminology validation,
6. implementation feasibility review,
7. safety and correctness evaluation.

## 7. Outcome Taxonomy

### Outcome A — New Category Candidate

The thesis survives prior art and benchmarks.

### Outcome B — Architectural Pattern

The thesis is useful but not market-category-worthy.

### Outcome C — Product Feature

The thesis is best treated as a feature inside DETERMA runtime authority.

### Outcome D — Rejected Thesis

Existing systems solve the problem or the cost is not material.

## 8. Current Interim Conclusion

As of this v0.2 review, the thesis should be treated as:

> Architecture Pattern Candidate / Strategic Research Hypothesis

Not as:

> Proven new category

The strongest immediate research path is to test whether Verified State Objects outperform memory/RAG, authorization-only, workflow-only, MCP/tool-protocol, and agent-framework baselines on measured state-reconstruction tokens, tool calls, latency, false allow, false deny, stale-state detection, invalidation correctness, and audit completeness.

## 9. Governance Note

This document is an initial cited prior-art review, not a completed literature review and not a final novelty conclusion.
