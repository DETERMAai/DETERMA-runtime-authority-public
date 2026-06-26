# 12 — PR Review Checklist

**Status:** Candidate Review Checklist  
**Scope:** Research Governance / PR Review / Merge Control  
**Runtime Authority:** None  
**Product Claim:** None  
**Public Claim Status:** Not approved for external use

## 1. Purpose

This checklist defines what maintainers should review before moving the State Reconstruction Tax research PR out of draft or merging it.

The checklist is designed to preserve the distinction between research hypotheses, canonical facts, product claims, and runtime contracts.

## 2. Scope Review

Confirm that the PR remains:

- docs-only
- research-only
- non-runtime
- non-product-claiming
- non-public-messaging

Reject or revise if any document implies production capability, customer deployment, benchmark result, or external category proof.

## 3. Governance Review

Each document should clearly state:

- status
- scope
- runtime authority
- product-claim status
- public-use status

Documents should not modify:

- runtime behavior
- system contracts
- worker contracts
- database policy
- execution authority protocols
- security guarantees

## 4. Truthfulness Review

Check for unsupported claims, especially:

- measured token savings
- category creation
- superiority over memory infrastructure
- production readiness
- customer or partner usage
- completed empirical validation
- completed prior-art review

Any unsupported claim must be rewritten as hypothesis, research question, or required validation.

## 5. Category Discipline Review

Confirm that the documents do not overreach into:

- generic AI memory
- generic governance platform
- generic authorization engine
- generic reality layer
- broad enterprise source-of-truth claims

Preferred internal framing should remain:

- State Reconstruction Tax — problem
- Verified Execution State Infrastructure — candidate solution layer
- Verified State Object — candidate technical primitive

## 6. Falsification Review

Confirm that the track includes serious paths to disprove the thesis.

Required adversarial checks:

- memory/RAG may solve the problem
- authorization systems may solve the problem
- workflow engines may solve the problem
- agent frameworks may solve the problem
- tool protocols may absorb the abstraction
- measured cost may be immaterial
- complexity may exceed benefit

## 7. Benchmark Review

Confirm that benchmark design includes strong baselines:

- raw-context agent
- RAG/memory agent
- authorization-engine agent
- workflow-engine agent
- agent-framework-state agent
- verified-execution-state candidate

Confirm that metrics include:

- token usage
- tool calls
- latency
- false allow
- false deny
- stale-state detection
- invalidation correctness
- audit completeness

## 8. Safety Review

Confirm that the research plan treats safety as non-negotiable.

A token-reduction mechanism must not be promoted if it increases false allow rate or hides material policy detail.

## 9. Prior-Art Review

Confirm that prior-art analysis is marked as scaffold, not completed literature review.

The PR should not claim novelty until cited prior-art review exists.

## 10. Merge Readiness

The PR can move out of draft only if:

- all documents are internally consistent
- no unsupported product claims remain
- scope boundaries are explicit
- red-line claims are documented
- maintainers agree that the track is useful as research

The PR should remain draft if:

- claims sound external-facing
- status labels are inconsistent
- the distinction from product capability is unclear
- the validation plan is missing or weak

## 11. Post-Merge Requirements

If merged, next steps should be limited to research validation:

- cited prior-art review
- benchmark implementation
- baseline comparison
- safety evaluation
- evidence package
- promotion/rejection decision

No public positioning should be derived directly from this PR.

## 12. Governance Note

This checklist is a merge-control artifact. It does not approve the thesis, the category, or any product capability.
