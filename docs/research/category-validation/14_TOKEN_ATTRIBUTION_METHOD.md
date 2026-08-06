# 14 — Token Attribution Method

**Status:** Candidate Measurement Method v0.1  
**Scope:** Measurement / Benchmarking / Category Validation  
**Runtime Authority:** None  
**Product Claim:** None  
**Public Claim Status:** Not approved for external use

## 1. Purpose

This document defines a measurement method for attributing agent token usage to different functions, with special focus on State Reconstruction Tax.

The purpose is to prevent vague claims such as “saves tokens” and replace them with reproducible attribution.

## 2. Measurement Goal

Determine how much of an agent workflow's token usage is spent on reconstructing execution-relevant operational state.

The method must distinguish state reconstruction from:

- task reasoning
- knowledge retrieval
- policy evaluation
- execution instruction
- audit / explanation
- coordination between agents

## 3. Core Unit of Analysis

The core unit is a **message segment**.

A message segment is a contiguous part of a prompt, tool result, model output, or agent-to-agent message that serves one primary function.

Each segment should be labeled before token counting.

## 4. Attribution Labels

### SR — State Reconstruction

Tokens used to establish what is operationally true and action-relevant now.

Examples:

- current repository head
- current CI status
- current approval state
- current role or permission state
- current policy version
- current deployment window
- current incident state
- current environment state
- current execution history relevant to replay or idempotency

### KR — Knowledge Retrieval

Tokens used to provide domain knowledge, documentation, product knowledge, codebase knowledge, or background context not specifically tied to current execution validity.

Examples:

- README content
- API documentation
- product requirements
- design docs
- previous Slack discussions
- general coding conventions

### PE — Policy Evaluation

Tokens used to reason about rules, constraints, allow/deny decisions, escalation, compliance, or governance requirements.

This is distinct from SR when the state is already known and the segment is evaluating what policy implies.

### TR — Task Reasoning

Tokens used for planning, comparing alternatives, decomposing the task, selecting a method, or deciding how to complete the intended work.

### EX — Execution Instruction

Tokens used to specify or perform the concrete action.

Examples:

- patch instructions
- API mutation payloads
- deployment commands
- CRM update payloads

### AU — Audit / Explanation

Tokens used to explain, justify, summarize, log, or document the decision and evidence after or around execution.

### CO — Coordination

Tokens used to coordinate between multiple agents, roles, reviewers, tools, or workflow participants.

Examples:

- handoff messages
- reviewer summaries
- executor instructions
- auditor requests

### OT — Other

Tokens that do not fit the above categories.

Use sparingly.

## 5. Segment Labeling Rules

### Rule 1 — Primary Function

Label a segment by its primary function, not by every possible secondary use.

### Rule 2 — Split Mixed Segments

If a prompt section contains both state reconstruction and task reasoning, split it into separate segments.

### Rule 3 — Currentness Matters

If the segment exists to determine whether something is true now, label it SR.

If it exists to explain background knowledge regardless of current system state, label it KR.

### Rule 4 — Decision Logic vs Decision Inputs

Decision inputs are usually SR.

Decision logic is usually PE.

Example:

- “CI status is passing” → SR
- “Policy allows merge only if CI is passing” → PE

### Rule 5 — Repeated Context

If the same state is repeated across agents or steps, each repetition should be counted separately, and marked with a repeat identifier.

## 6. Attribution Record Format

Each benchmark run should produce a token attribution record:

```json
{
  "run_id": "...",
  "case_id": "...",
  "baseline": "raw_context|rag_memory|authorization_engine|workflow_engine|agent_framework|verified_state",
  "segments": [
    {
      "segment_id": "s1",
      "message_id": "m1",
      "label": "SR",
      "repeat_group": "repo_head_state_v1",
      "source": "prompt|tool_result|model_output|agent_message",
      "token_count": 0,
      "notes": "current repository head and CI state"
    }
  ],
  "totals": {
    "SR": 0,
    "KR": 0,
    "PE": 0,
    "TR": 0,
    "EX": 0,
    "AU": 0,
    "CO": 0,
    "OT": 0
  }
}
```

## 7. Derived Metrics

### State Reconstruction Token Share

```text
SR_share = SR_tokens / total_tokens
```

### Repeated State Token Share

```text
Repeated_SR_share = repeated_SR_tokens / total_tokens
```

### State Reconstruction Reduction

```text
SR_reduction = (baseline_SR_tokens - candidate_SR_tokens) / baseline_SR_tokens
```

### Total Token Reduction

```text
Total_reduction = (baseline_total_tokens - candidate_total_tokens) / baseline_total_tokens
```

### Safety-Adjusted Token Reduction

Token reduction should be ignored or penalized if false allow rate increases.

```text
SafetyAdjustedReduction = SR_reduction if false_allow_delta <= 0 else invalid
```

## 8. Required Baseline Comparisons

The method must be applied to:

- raw-context agent
- RAG / memory agent
- authorization-engine agent
- workflow-engine agent
- agent-framework-state agent
- verified-execution-state candidate

## 9. Human Review Requirement

Automated labeling is not sufficient for early validation.

At least two human reviewers should independently label a sample of benchmark runs.

Disagreements should be recorded and used to refine labeling rules.

## 10. Ambiguity Handling

If a segment cannot be confidently labeled, mark it as:

```text
OT_WITH_REASON
```

and include the reason.

Do not force ambiguous segments into SR to inflate the thesis.

## 11. Failure Conditions

This method fails if:

- reviewers cannot consistently distinguish SR from KR, PE, or TR
- token attribution is too subjective
- repeated state cannot be identified
- baseline prompts are artificially weak
- candidate prompts hide important state in opaque objects without preserving auditability

## 12. Minimum Evidence Threshold

Before any token-saving claim, the benchmark must show:

- measurable SR token share,
- reproducible labeling,
- candidate reduction versus strong baselines,
- no false-allow increase,
- audit completeness preserved or improved.

## 13. Governance Note

This document defines a measurement method. It does not report results and does not support any public token-saving claim by itself.
