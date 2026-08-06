# Verified State Object Specification

**Version:** v0.1  
**Status:** Candidate Product Architecture / Research Specification  
**Scope:** Research / Architecture / Category Formation  
**Runtime Authority:** None  
**Product Claim:** None  
**Public Claim Status:** Not approved for external use

## 1. Purpose

This document defines an initial candidate structure for a **Verified Execution State Object**.

The object is intended to represent execution-relevant operational state in a compact, signed, bounded, and reusable form for AI agents and execution runtimes.

This specification is exploratory. It does not define a production protocol, API contract, or runtime contract.

## 2. Design Goals

A Verified Execution State Object should help evaluate whether agentic systems can reduce repeated reconstruction of operational state.

Primary goals:

- represent action-relevant state explicitly
- distinguish state sources from derived state
- preserve provenance
- define freshness and invalidation boundaries
- support auditability
- support deterministic enforcement where possible
- reduce repeated context loading where empirically justified

Non-goals:

- replace source-of-truth systems
- replace identity systems
- replace authorization engines
- replace workflow engines
- claim token reduction without measurement

## 3. Conceptual Model

```text
Intent + Subject + Sources + Policy + Environment + Time
        ↓
State Collection
        ↓
State Verification
        ↓
State Compilation
        ↓
VerifiedExecutionState
        ↓
Agent / Runtime / Auditor
```

## 4. Candidate Object Shape

```json
{
  "schema_version": "0.1",
  "state_id": "ves_...",
  "created_at": "2026-06-26T00:00:00Z",
  "expires_at": "2026-06-26T00:05:00Z",
  "freshness_window_ms": 300000,
  "intent_fingerprint": "sha256:...",
  "subject_identity_digest": "sha256:...",
  "authority_digest": "sha256:...",
  "policy_digest": "sha256:...",
  "approval_digest": "sha256:...",
  "environment_digest": "sha256:...",
  "dependency_digest": "sha256:...",
  "risk_digest": "sha256:...",
  "execution_history_digest": "sha256:...",
  "source_provenance": [],
  "decision_boundary": {},
  "invalidation_triggers": [],
  "trust_level": "candidate",
  "signature": "ed25519:..."
}
```

## 5. Field Semantics

### state_id

Unique identifier for the compiled state object.

### intent_fingerprint

Normalized fingerprint of the requested action or intent.

The fingerprint should avoid using raw prompt text as the sole identifier. It should be derived from structured intent fields where possible.

### subject_identity_digest

Digest of the relevant actor identity and delegated-agent identity context.

This may include user, agent, service account, tenant, role, and delegation chain.

### authority_digest

Digest of the authority state relevant to the intent.

This may include permissions, capability grants, policy decision inputs, active constraints, and bounded approval references.

### policy_digest

Digest of applicable policy versions.

This must identify policy source, version, and evaluation boundary.

### approval_digest

Digest of human or system approvals relevant to the action.

The digest must be time-bounded and revocation-aware.

### environment_digest

Digest of relevant environment state.

Examples may include repository head, branch, CI status, deployment environment, feature flags, runtime environment, and cloud state.

### dependency_digest

Digest of dependencies that materially affect the decision or execution.

### risk_digest

Digest of risk signals relevant to the action.

Examples may include sensitive resource classification, blast radius, production impact, incident state, or anomaly signals.

### execution_history_digest

Digest of prior executions relevant to replay prevention, audit, or idempotency.

### source_provenance

List of source systems and evidence references used to compile the state.

This must not contain secrets.

### decision_boundary

Explicit statement of the conditions under which the object is valid.

Examples:

- valid only for a specific intent fingerprint
- valid only until policy version changes
- valid only while repository HEAD remains unchanged
- valid only for a specific environment
- valid only within a time window

### invalidation_triggers

Events that should invalidate the object.

Examples:

- policy update
- approval revocation
- branch head change
- CI status change
- role change
- incident state change
- risk threshold change

### signature

Cryptographic signature over canonicalized object content.

The signature supports integrity verification, but does not by itself prove semantic correctness.

## 6. Validity Requirements

A Verified Execution State Object is valid only if:

1. its signature verifies
2. it has not expired
3. its invalidation triggers have not fired
4. its source provenance is sufficient for the decision boundary
5. its intent fingerprint matches the requested action
6. the consuming runtime understands the schema version

## 7. Security Considerations

Risks:

- stale-state reuse
- overbroad decision boundaries
- weak intent normalization
- missing invalidation triggers
- provenance gaps
- unsafe compression of policy-relevant detail
- signature without semantic verification

Required mitigations:

- short TTLs for volatile states
- explicit invalidation triggers
- strict intent binding
- conservative fallback to fresh reconstruction
- append-only audit trail
- replay denial
- separation between evidence and generated explanation

## 8. Token-Efficiency Hypothesis

If state objects can safely replace repeated natural-language reconstruction of policy, authority, environment, and execution context, they may reduce input tokens, tool calls, and multi-agent coordination overhead.

This is a hypothesis. It requires benchmark evidence before any external claim.

## 9. Open Questions

1. Which state fields should be mandatory?
2. What canonicalization format should be used before signing?
3. How should intent fingerprints be normalized?
4. What is the correct TTL model for different state classes?
5. Which invalidation triggers are required for code, workflow, and business-process actions?
6. Can the object remain compact without hiding material policy detail?
7. Should agents consume the object directly or through a runtime adapter?
8. How should false allow and false deny be measured?

## 10. Governance Note

This document is a candidate specification for research only. It must not be treated as a canonical runtime protocol until reviewed, tested, and explicitly promoted.
