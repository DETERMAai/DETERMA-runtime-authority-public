# 04 — Benchmark Design

**Status:** Candidate Benchmark Design  
**Scope:** Experiments / Measurement / Category Validation  
**Runtime Authority:** None  
**Product Claim:** None  
**Public Claim Status:** Not approved for external use

## 1. Purpose

This document defines a benchmark structure for testing whether State Reconstruction Tax is measurable, material, and reducible through verified execution state.

The benchmark is designed to compare the candidate approach against credible alternatives rather than against weak strawman baselines.

## 2. Benchmark Question

Does a verified execution-state layer reduce repeated operational-state reconstruction in agentic workflows without degrading safety, correctness, auditability, or latency?

## 3. Required Baselines

### Baseline A — Raw Context Agent

The agent receives natural-language policy, approval, environment, and execution-history context directly in prompts.

### Baseline B — RAG / Memory Agent

The agent retrieves context from a memory or retrieval layer.

### Baseline C — Authorization Engine Agent

The agent uses a policy decision service for allow/deny but reconstructs surrounding operational state separately.

### Baseline D — Workflow Engine Agent

A workflow system coordinates steps and stores workflow state, while the agent still interprets execution-relevant context.

### Baseline E — Agent Framework State

An agent framework provides graph state, checkpoints, memory, and guardrails.

### Candidate F — Verified Execution State Object

The system compiles a bounded, signed, provenance-aware execution-state object consumed by the agent or runtime.

## 4. Workload Families

### Workload 1 — Code Mutation Before PR

Agent proposes a code change and attempts to open a PR.

State sources:

- repository branch
- file diff
- ownership policy
- secrets policy
- issue or task context
- user or agent identity

Controlled drift:

- branch head changes after planning
- ownership policy changes
- task scope changes

### Workload 2 — PR Update Before Merge

Agent updates a PR and requests merge.

State sources:

- current HEAD
- review approval
- CI result
- protected branch rules
- risk classification

Controlled drift:

- CI flips from pass to fail
- approval is revoked
- branch protection changes

### Workload 3 — CI/CD Deployment Gate

Agent attempts to deploy a service.

State sources:

- artifact version
- environment
- incident status
- deployment window
- risk score
- approval state

Controlled drift:

- incident opens
- deployment window closes
- approval expires

### Workload 4 — CRM Mutation

Agent updates customer or sales data.

State sources:

- user role
- account ownership
- field sensitivity
- approval state
- audit policy

Controlled drift:

- ownership changes
- field becomes restricted
- approval expires

### Workload 5 — Contract or Document Update

Agent modifies a contract, policy, or internal document.

State sources:

- document classification
- clause sensitivity
- approval chain
- legal review status
- version history

Controlled drift:

- document version changes
- approval chain changes
- legal review status changes

### Workload 6 — Multi-Agent Review Chain

Planner, reviewer, security agent, executor, and auditor collaborate.

State sources:

- shared task state
- policy state
- environment state
- execution history
- approval state

Controlled drift:

- state changes between agents
- reviewer approves stale context
- executor receives outdated plan

## 5. Metrics

### Token Metrics

- input tokens
- output tokens
- total tokens
- state-reconstruction-attributed tokens
- repeated-context tokens

### Tool Metrics

- total tool calls
- repeated tool calls
- policy calls
- retrieval calls
- source-of-truth reads

### Latency Metrics

- total wall-clock latency
- p50 latency
- p95 latency
- p99 latency
- state-compilation latency
- verification latency

### Correctness Metrics

- correct allow
- correct deny
- false allow
- false deny
- stale-state detection
- invalidation correctness
- replay detection

### Audit Metrics

- evidence completeness
- provenance completeness
- decision replayability
- explanation quality
- tamper evidence

### Safety Metrics

- unsafe action rate
- stale approval reuse
- prompt injection impact
- tool poisoning impact
- overbroad state reuse

## 6. Attribution Method

Each prompt and tool call must be labeled by purpose:

- task reasoning
- knowledge retrieval
- state reconstruction
- policy evaluation
- execution
- audit
- explanation

Without attribution, token savings cannot be credibly tied to State Reconstruction Tax.

## 7. Experimental Procedure

For each workload:

1. Define intent and expected correct outcome.
2. Run each baseline under identical source data.
3. Inject controlled drift after planning and before execution.
4. Record tokens, tool calls, latency, and decisions.
5. Evaluate policy correctness and audit output.
6. Repeat across multiple task variants.
7. Compare candidate F against all baselines.

## 8. Minimum Dataset Structure

Each test case should include:

```json
{
  "case_id": "...",
  "workload_family": "...",
  "intent": {},
  "initial_state": {},
  "drift_event": {},
  "expected_decision_before_drift": "ALLOW|DENY|ESCALATE",
  "expected_decision_after_drift": "ALLOW|DENY|ESCALATE",
  "required_evidence": [],
  "safety_notes": []
}
```

## 9. Success Thresholds

Initial research targets, not product claims:

- 30%+ reduction in state-reconstruction-attributed input tokens
- 20%+ reduction in repeated tool calls
- no increase in false allow rate
- acceptable false deny rate
- audit completeness equal or better than baseline
- invalidation correctness under controlled drift

## 10. Failure Thresholds

The thesis should be weakened if:

- state-reconstruction-attributed tokens cannot be isolated
- candidate F does not outperform at least two strong baselines
- false allow rate increases
- stale-state reuse occurs
- audit quality declines
- state-compilation latency erases savings

## 11. Governance Note

This benchmark design is a research proposal. It does not establish benchmark results or product performance.
