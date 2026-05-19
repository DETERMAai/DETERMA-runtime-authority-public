# Runtime Drift Failures

## Stale Approval

An approval was issued under one runtime state.

The environment changed before execution.

The mutation still executed.

## Replayable Authority

Previously consumed authority was reused under different runtime conditions.

## Delegation Drift

An approved capability expanded beyond the original authority boundary.

## Topology Drift

Execution occurred under a runtime topology different from the one originally approved.

## Core Principle

Historical approval alone cannot guarantee current execution admissibility.
