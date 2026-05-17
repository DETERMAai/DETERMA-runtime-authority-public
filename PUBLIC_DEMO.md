# Public Demo Concept

## Purpose

This public demo is intentionally conceptual.

It is designed to explain the problem without exposing implementation-sensitive enforcement mechanics.

## Scenario

An AI system proposes a change to a code repository.

At approval time, the change appears acceptable.

Before execution, the runtime environment changes.

A traditional approval-only system may still execute the previously approved change.

A runtime authority system should ask a stricter question:

> Is this exact execution still legitimate under the current state?

## Public-safe flow

1. AI proposes a patch.
2. Human approval is requested.
3. The system records the approval.
4. Runtime state changes.
5. Execution is re-evaluated.
6. If the state no longer matches the approved context, execution halts.
7. Evidence records the decision.

## What this demonstrates

The public demo demonstrates the category:

> Historical approval is not always sufficient execution authority.

## What this does not expose

This public demo does not expose:
- proof scripts
- witness generation
- execution release mechanics
- replay invalidation logic
- audit-chain internals
- implementation-bearing runtime semantics

For technical review, request private access.
