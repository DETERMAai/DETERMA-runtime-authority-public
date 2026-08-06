# 03 — Falsification Plan

**Status:** Candidate Research Plan  
**Scope:** Theory / Experiments / Category Validation  
**Runtime Authority:** None  
**Product Claim:** None  
**Public Claim Status:** Not approved for external use

## 1. Purpose

This document defines how to disprove or weaken the State Reconstruction Tax and Verified Execution State Infrastructure theses.

The goal is to prevent category formation by narrative alone.

## 2. Thesis Under Test

Agentic AI systems incur a material State Reconstruction Tax that can be reduced by a distinct verified execution-state layer.

## 3. Falsification Principle

A thesis is only useful if it can fail.

This thesis should not advance unless it survives tests against:

- memory infrastructure
- retrieval systems
- authorization engines
- workflow engines
- agent frameworks
- tool protocols
- baseline prompt engineering
- application-specific engineering

## 4. Falsification Test A — Cost Immateriality

### Claim to test

State reconstruction is a material cost driver.

### Falsifying evidence

The thesis weakens if measured reconstruction cost is consistently small.

Example failure thresholds:

- less than 10% of input tokens are attributable to reconstruction
- less than 10% of tool calls are attributable to reconstruction
- reconstruction latency is not a meaningful contributor to p95 or p99 latency
- reconstruction is not a significant source of errors

## 5. Falsification Test B — Memory Sufficiency

### Claim to test

Memory does not fully solve execution-state reconstruction.

### Falsifying evidence

The thesis weakens if a memory/RAG baseline achieves equivalent or better results across:

- token usage
- latency
- state freshness
- stale approval detection
- policy correctness
- audit completeness
- multi-agent state reuse

## 6. Falsification Test C — Authorization Sufficiency

### Claim to test

Authorization engines are insufficient because execution-state reconstruction is broader than permit/deny.

### Falsifying evidence

The thesis weakens if OPA/ABAC/XACML/Cedar/Zanzibar-style baselines provide equivalent:

- correctness
- auditability
- compactness
- freshness
- invalidation
- replay resistance
- agent usability

## 7. Falsification Test D — Workflow Sufficiency

### Claim to test

Workflow engines do not fully solve verified execution-state reuse.

### Falsifying evidence

The thesis weakens if workflow engines preserve and expose all action-relevant state with equivalent safety and cost reduction.

## 8. Falsification Test E — Agent Framework Sufficiency

### Claim to test

Agent frameworks do not fully solve verified execution state.

### Falsifying evidence

The thesis weakens if agent framework state, checkpoints, memory, and guardrails provide equivalent:

- state reuse
- signed provenance
- invalidation boundaries
- policy correctness
- multi-agent coordination reduction

## 9. Falsification Test F — Complexity Overhead

### Claim to test

Verified state reduces total system cost.

### Falsifying evidence

The thesis weakens if verified state introduces more complexity than it removes:

- high invalidation complexity
- high implementation burden
- high latency overhead
- high false deny rates
- opaque audit artifacts
- brittle intent fingerprinting
- unsafe compression of policy detail

## 10. Falsification Test G — Category Weakness

### Claim to test

Verified Execution State Infrastructure is category-worthy.

### Falsifying evidence

The thesis weakens if:

- buyers understand it only as a feature
- developers do not adopt the abstraction independently
- no benchmark can isolate the problem
- terminology fails to distinguish from memory/governance/security
- analyst language collapses it into existing categories

## 11. Promotion Criteria

The thesis may advance only if:

1. state reconstruction is measurable
2. state reconstruction is material
3. baselines do not solve it adequately
4. verified state reduces cost or risk
5. safety does not regress
6. the abstraction is reusable across workloads
7. language is clear enough for external adoption

## 12. Rejection Criteria

The thesis should be rejected or downgraded if any of the following hold:

- memory/RAG solves most of the problem
- authorization engines solve most of the problem
- workflow engines solve most of the problem
- the remaining value is too narrow for a category
- experiments cannot isolate state reconstruction
- token savings are negligible
- safety or correctness regress

## 13. Governance Note

This document is intentionally adversarial. It should be preserved alongside positive thesis documents to prevent overfitting strategy to an attractive narrative.
