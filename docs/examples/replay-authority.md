# Replay Authority Example

## Sequence

```text
Approval issued
-> execution completed
-> authority artifact consumed
-> second execution attempted
-> replay detected
-> execution denied
```

## Failure Without Replay Protection

A consumed approval artifact is reused.

The system treats previously valid authority as still executable.

## DETERMA Behavior

Execution authority is single-consumption.

Previously consumed release artifacts cannot authorize additional mutations.

## Core Invariant

Execution authority must be replay-resistant.
