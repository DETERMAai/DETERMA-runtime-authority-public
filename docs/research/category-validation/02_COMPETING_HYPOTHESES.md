# 02 — Competing Hypotheses

**Status:** Candidate Research Analysis  
**Scope:** Theory / Category Validation / Falsification  
**Runtime Authority:** None  
**Product Claim:** None  
**Public Claim Status:** Not approved for external use

## 1. Purpose

This document defines alternative explanations that may weaken or invalidate the State Reconstruction Tax thesis.

A strong category thesis must survive comparison against simpler explanations.

## 2. Primary Thesis Under Test

**H0-Candidate:** Agentic AI systems incur a material State Reconstruction Tax that is not fully addressed by memory, RAG, authorization engines, workflow engines, or agent frameworks.

The candidate solution is a distinct infrastructure layer for verified execution state.

## 3. Competing Hypothesis A — Memory Solves It

Memory systems may already solve most state reconstruction by retaining relevant organizational context and execution history.

If true, Verified Execution State Infrastructure may be a feature of memory infrastructure rather than a distinct category.

### Evidence that would support this hypothesis

- memory systems reduce most repeated policy/context loading
- memory systems preserve enough freshness and provenance for execution
- memory systems handle invalidation and revocation effectively
- measured residual state-reconstruction cost is small

### Evidence that would weaken this hypothesis

- memory recalls stale approvals or stale environment state
- memory lacks strong invalidation boundaries
- memory reduces knowledge reconstruction but not authority/risk/environment reconstruction
- execution decisions still require repeated verification outside memory

## 4. Competing Hypothesis B — Authorization Engines Solve It

OPA, ABAC, XACML, Cedar, Zanzibar-like systems, or similar authorization engines may already provide the necessary decision layer.

If true, Verified Execution State Infrastructure may be an extension of policy decision infrastructure rather than a new category.

### Evidence that would support this hypothesis

- authorization engines capture all action-relevant state
- policy decision inputs are compact and reusable
- freshness and revocation are already handled
- audit and explainability are sufficient

### Evidence that would weaken this hypothesis

- agents still reconstruct surrounding operational state outside the authorization engine
- permit/deny is too narrow for execution-state reuse
- state provenance, environment drift, and execution history remain external
- multi-agent coordination still repeats context reconstruction

## 5. Competing Hypothesis C — Workflow Engines Solve It

Workflow engines may already maintain state across steps, participants, and approvals.

If true, the correct category may be workflow orchestration for AI agents rather than verified execution state.

### Evidence that would support this hypothesis

- workflow engines preserve all relevant execution context
- agents can consume workflow state without reconstructing it
- workflow state is sufficient for authority, risk, and environment checks
- measured reconstruction cost drops with workflow alone

### Evidence that would weaken this hypothesis

- workflow state captures sequence but not verified authority
- dynamic external state still requires fresh reconstruction
- policy and risk state remain outside the workflow engine
- multi-agent reasoning still repeats context interpretation

## 6. Competing Hypothesis D — MCP and Tool Protocols Solve It

Tool protocols may evolve to include capability descriptions, trust metadata, authorization boundaries, and execution state.

If true, the proposed layer may become part of tool-connectivity standards rather than a separate category.

### Evidence that would support this hypothesis

- tool protocols standardize capability attestation and state metadata
- tool servers provide verified freshness and decision boundaries
- agents can safely rely on tool-provided state
- ecosystem adoption consolidates around protocol-level enforcement

### Evidence that would weaken this hypothesis

- protocols connect tools but do not compile cross-tool operational state
- implicit trust propagation remains unresolved
- policy and risk remain fragmented across tool servers
- cross-source invalidation is not standardized

## 7. Competing Hypothesis E — Agent Frameworks Solve It

LangGraph, AutoGen, Semantic Kernel, CrewAI, OpenAI Agents SDK, or similar frameworks may absorb state reconstruction into graph state, checkpoints, memory, and guardrails.

If true, the category may belong inside agent frameworks.

### Evidence that would support this hypothesis

- frameworks provide reusable verified state across agents
- frameworks enforce freshness and invalidation
- frameworks support policy-aware execution gates
- state reconstruction cost is low when using mature frameworks

### Evidence that would weaken this hypothesis

- framework state is not independently verifiable
- policy authority is application-specific
- audit and replay resistance are external
- cross-framework state reuse is weak

## 8. Competing Hypothesis F — The Cost Is Not Material

State reconstruction may exist but may not be large enough to justify a category.

If true, Verified Execution State Infrastructure may be technically interesting but commercially weak.

### Evidence that would support this hypothesis

- token cost is dominated by task reasoning or knowledge retrieval
- state reconstruction accounts for a small percentage of total cost
- latency overhead is negligible
- failure modes are rare or already controlled

### Evidence that would weaken this hypothesis

- repeated governance/context prompts dominate execution-heavy workflows
- multi-agent workflows multiply reconstruction cost
- stale approvals or environment drift produce frequent failures
- tool-call overhead is high

## 9. Competing Hypothesis G — This Is a Security Feature, Not a Category

The thesis may be valuable but too narrow to be a category. It may be a feature within AI security, governance, or runtime authorization.

### Evidence that would support this hypothesis

- buyers understand it only as security control
- no independent developer ecosystem forms around state objects
- no standalone benchmark emerges
- no repeatable terminology gains adoption

### Evidence that would weaken this hypothesis

- multiple products and frameworks need the abstraction
- benchmarks show cross-domain value
- developers adopt verified state objects independently of DETERMA
- analysts recognize a distinct layer

## 10. Decision Rule

The category thesis should advance only if it outperforms competing hypotheses across:

- measurement
- scope
- implementation feasibility
- buyer clarity
- developer adoption potential
- safety and correctness
- distinction from prior art

## 11. Governance Note

These competing hypotheses are intended to weaken overconfident claims. They must remain part of the research record until empirical validation is complete.
