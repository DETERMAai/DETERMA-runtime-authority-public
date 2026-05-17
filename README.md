# DETERMA

## Runtime authority for AI-initiated actions

DETERMA is a runtime authority layer for systems where AI agents, automation, or workflow software can propose actions that may affect real systems.

The core principle is simple:

> AI may propose. Authority decides. Execution is constrained. Evidence is recorded.

DETERMA is not an AI agent framework.

DETERMA is not a monitoring dashboard.

DETERMA is not a prompt filter.

DETERMA is designed around a different question:

> When an AI system is about to trigger a real-world change, what proves that this exact action is still authorized, scoped, current, and accountable?

## The problem

Modern AI systems increasingly interact with tools, code repositories, APIs, cloud systems, business workflows, and operational environments.

Most governance approaches focus on:
- policies
- dashboards
- model monitoring
- prompt and output controls
- post-event audit

These are useful, but they do not by themselves create a deterministic execution boundary.

The risk is not only that AI may produce a bad answer.

The deeper risk is that AI-generated intent may become machine-executed change without a runtime authority layer.

## DETERMA’s position

DETERMA separates proposal from execution.

A safe execution path should include:

1. AI proposes an action.
2. External authority evaluates scope and risk.
3. Human approval can act as a hard stop.
4. Execution is constrained to the approved action.
5. Current state is checked before mutation.
6. The result is verified after execution.
7. Evidence is recorded in an immutable audit trail.

## Public boundary

This repository is intentionally narrow.

It explains:
- the category
- the problem
- the high-level architecture
- AI Act readiness relevance
- the public-safe operating principle

It does not include:
- runnable proof scripts
- enforcement internals
- implementation-sensitive runtime mechanics
- private technical diligence materials
- product source code

Detailed technical materials are available only through controlled private review.

## Why now

AI systems are moving from text generation to action initiation.

Enterprises will need more than written AI governance policies. They will need enforceable runtime controls that can demonstrate who approved what, under which scope, against which system state, and with what verified outcome.

DETERMA is being built for that execution-control gap.

## Public materials

- [Why DETERMA](WHY_DETERMA.md)
- [AI Act readiness framing](AI_ACT_READINESS.md)
- [Public demo concept](PUBLIC_DEMO.md)
- [Request private review](REQUEST_PRIVATE_REVIEW.md)
- [Security and disclosure](SECURITY.md)

## Status

DETERMA is in early MVP development.

The current public repository is an overview surface, not a complete product implementation and not a full technical disclosure.

## Core sentence

DETERMA turns AI governance from written policy into enforceable runtime control.
