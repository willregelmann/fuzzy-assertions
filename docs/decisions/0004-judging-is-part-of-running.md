# Judging is part of running, not a capability of its own

Superseded by ADR-0009.

## Context and Problem Statement

Two processes cross the primitives: one evaluator judging one test, and a run that picks tests, has each judged and reports the verdicts. Should judging be a capability with its own file, holding the isolation rules, or part of running?

## Considered Options

* One capability, Run, with judging inside it
* Two capabilities, Judge and Run

## Decision Outcome

Chosen option: "One capability, Run, with judging inside it", chosen by the owner. Reason: TODO.

### Consequences

* Good, because judging is never started except by a run, so there is one process to reach and observe.
* Bad, because the evaluator's isolation rules and the run's bookkeeping rules share one file.

### Confirmation

[RUN.md](../capabilities/RUN.md) is the only capability and holds "Every test is judged by a fresh evaluator that knows only the test and the project" and "The evaluator can look but never change".
