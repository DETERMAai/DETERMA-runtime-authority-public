# Why DETERMA

## The execution gap

A growing number of AI systems can plan, recommend, trigger, or coordinate actions.

The important question is no longer only:

> Is the model output acceptable?

The harder question is:

> Is this machine-initiated action allowed to execute right now?

That question requires a different layer of infrastructure.

## Existing controls are not enough

Prompt filters can reduce unsafe outputs.

Monitoring can detect suspicious behavior.

Dashboards can show what happened.

Policies can describe intended behavior.

But none of these alone guarantee that a specific action cannot execute unless it passes a runtime authority boundary.

## DETERMA’s thesis

AI systems should not hold general mutation authority.

They should propose actions.

A separate authority layer should decide whether execution is allowed.

Execution should be:
- scoped
- time-bound
- state-aware
- auditable
- constrained
- fail-closed

## Example domain

The first narrow domain is governed code mutation:

1. AI proposes a code change.
2. A human approves or rejects.
3. The system issues a constrained execution permission.
4. A narrow executor applies only the approved change.
5. Tests and verification confirm the result.
6. Audit evidence records the full chain.

This domain is narrow enough for an MVP and concrete enough for enterprise buyers to understand.

## Strategic distinction

DETERMA is not trying to build “a better coding agent.”

DETERMA is trying to build the authority layer that determines whether any AI-initiated change is legitimate to execute.
