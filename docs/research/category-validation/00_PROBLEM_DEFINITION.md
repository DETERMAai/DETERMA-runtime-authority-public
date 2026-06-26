# 00 — Problem Definition

**Status:** Candidate Research Definition  
**Scope:** Theory / Category Validation  
**Runtime Authority:** None  
**Product Claim:** None  
**Public Claim Status:** Not approved for external use

## 1. Problem Statement

Autonomous AI agents that execute work must determine not only what they know, but what is operationally true, permitted, fresh, and action-relevant at the moment of execution.

In many architectures, this operational state is reconstructed repeatedly through prompts, retrieval, tool calls, policy checks, workflow state, environment reads, and multi-agent coordination.

The candidate problem is that this repeated reconstruction may create a material system-level cost and risk surface.

## 2. Candidate Problem Name

**State Reconstruction Tax**

## 3. Problem Scope

The problem includes repeated reconstruction of:

- knowledge state
- authority state
- identity and delegation state
- policy state
- approval state
- environment state
- dependency state
- temporal state
- risk state
- execution-history state
- provenance state

The research focus is not generic knowledge retrieval alone. It is the execution-relevant subset of state required before action.

## 4. Why the Problem May Matter

If state reconstruction is material, it can increase:

- input-token usage
- output-token usage
- model-call count
- tool-call count
- latency
- coordination overhead
- policy inconsistency
- stale approval risk
- audit complexity
- replay risk
- prompt-injection exposure

## 5. Independence Test

The problem definition must survive an independence test:

> If DETERMA did not exist, would this still be a recognizable systems problem in agentic AI?

If not, this is likely a product narrative rather than a category problem.

## 6. Category Test

The problem may justify category formation only if all of the following are true:

1. The cost is measurable.
2. The cost is material.
3. The cost is not already solved by memory, RAG, workflow engines, authorization engines, or agent frameworks.
4. A distinct abstraction can reduce the cost.
5. The abstraction can be reused across workloads.
6. The abstraction improves or preserves safety and correctness.

## 7. Non-Problem Claims

This document does not claim:

- that DETERMA currently solves State Reconstruction Tax
- that token savings have been measured
- that a new category has been proven
- that existing memory or authorization systems are insufficient in all cases
- that verified execution state is production-ready

## 8. Initial Workloads for Validation

Candidate workloads:

1. AI-generated code change before PR creation
2. PR update before merge
3. CI/CD deployment gate
4. CRM mutation by an agent
5. contract or document update workflow
6. multi-agent planning / review / execution / audit chain

Each workload should include at least one controlled state-drift event between planning and execution.

## 9. Decision Criteria

The problem definition should be weakened or rejected if experiments show that:

- state reconstruction is not a material cost driver
- memory/RAG solves the majority of the measured cost
- authorization engines solve the majority of the measured correctness problem
- workflow engines provide equivalent state reuse
- verified state introduces more complexity than benefit

## 10. Governance Note

This is a research definition only. It is intended to constrain future claims, not expand them.
