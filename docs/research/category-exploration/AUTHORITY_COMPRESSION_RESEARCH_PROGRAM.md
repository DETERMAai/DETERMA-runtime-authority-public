# Authority Compression Research Program

**Version:** v0.1  
**Status:** Candidate Research Program  
**Scope:** Research / Measurement / Category Validation  
**Runtime Authority:** None  
**Product Claim:** None  
**Public Claim Status:** Not approved for external use

## 1. Purpose

This research program defines how to test whether DETERMA can reduce repeated governance, authority, environment, and execution-state reconstruction in agentic systems.

The program does not assume that token savings exist. It defines how to measure them.

## 2. Research Question

Can verified execution state objects reduce token usage, tool calls, latency, and coordination overhead without degrading policy correctness, audit quality, or safety?

## 3. Core Hypothesis

Agentic systems spend a measurable portion of execution cost reconstructing authority-relevant state.

If that state is compiled into a fresh, signed, bounded, and reusable object, repeated reconstruction may be reduced.

## 4. Baselines

Experiments must compare against the following baselines:

### Baseline A — Raw Context Agent

The agent receives natural-language policies, approval context, environment state, and execution history directly in the prompt.

### Baseline B — RAG / Memory Agent

The agent retrieves relevant policies and context from a retrieval or memory layer.

### Baseline C — Authorization Engine Only

The agent uses an OPA/ABAC/XACML-style decision service for permit/deny, but still reconstructs surrounding operational state.

### Baseline D — Workflow Engine Only

A workflow engine coordinates steps, but state interpretation remains distributed across agent prompts and tool calls.

### Candidate E — Verified Execution State Object

The agent consumes a compact state object with explicit provenance, freshness boundaries, invalidation triggers, and signed digests.

## 5. Experimental Workloads

Initial workloads should include:

1. AI-generated code change before PR creation
2. PR update before merge
3. CI/CD deployment gate
4. CRM data mutation by an agent
5. Contract or document update workflow
6. Multi-agent planning / review / execution / audit chain

Each workload should include at least one stale-approval, stale-policy, or environment-drift scenario.

## 6. Metrics

### Cost Metrics

- input tokens
- output tokens
- total tokens
- model calls
- tool calls
- policy calls
- retrieval calls
- total wall-clock latency
- p50 / p95 / p99 latency

### Correctness Metrics

- policy correctness
- false allow rate
- false deny rate
- stale approval detection
- replay detection
- invalidation correctness
- decision reproducibility

### Audit Metrics

- audit completeness
- provenance completeness
- explanation quality
- evidence traceability
- replayability of decision

### Safety Metrics

- unsafe action rate
- overbroad authority reuse
- prompt injection impact
- tool poisoning impact
- state tampering detection

## 7. Measurement Method

For each workload:

1. Run baseline A with raw context.
2. Run baseline B with retrieval/memory.
3. Run baseline C with authorization engine only.
4. Run baseline D with workflow engine only.
5. Run candidate E with verified execution state object.
6. Record all tokens, tool calls, latency, decisions, and audit artifacts.
7. Inject controlled state changes between planning and execution.
8. Measure whether stale state is detected or incorrectly reused.

## 8. Minimum Evidence Threshold

The thesis should not be promoted unless experiments show:

- material token reduction in at least two execution-heavy workloads
- no increase in false allow rate
- acceptable false deny rate
- clear auditability improvement or parity
- stable invalidation behavior under state drift
- latency overhead that does not erase the savings

A suggested initial target:

- 30%+ reduction in state-reconstruction-related input tokens
- 20%+ reduction in tool calls
- no measurable safety regression

These targets are research targets, not product claims.

## 9. Failure Conditions

The thesis should be weakened or rejected if:

- state reconstruction is not a material cost driver
- retrieval/memory layers solve most of the problem
- authorization-engine baselines provide equivalent value
- verified state objects introduce excessive invalidation complexity
- compact state hides policy-relevant evidence
- false allow rates increase
- audit quality declines

## 10. Required Instrumentation

The prototype must log:

- prompt token counts
- completion token counts
- tool call counts
- policy decision inputs and outputs
- state object IDs
- source provenance
- invalidation events
- decision timestamps
- audit entries
- replay attempts
- stale-state attempts

## 11. Candidate Prototype Architecture

```text
Agent Intent
    ↓
Intent Normalizer
    ↓
State Collector
    ↓
Policy / Authority Evaluator
    ↓
State Compiler
    ↓
Verified Execution State Object
    ↓
Agent / Runtime Consumer
    ↓
Execution Gate
    ↓
Append-only Audit Journal
```

## 12. Governance Note

This research program is designed to prevent premature marketing claims.

No token-saving, safety, or category-creation claims should be made externally until measured evidence exists and maintainers explicitly promote the relevant documents.
