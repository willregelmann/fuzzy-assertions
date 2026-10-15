# Run inside a session, not as an unattended CI gate

## Context and Problem Statement

Earlier versions shipped a headless runner so a CI pipeline could run the suite as a merge gate, and the first statement of intent named a CI pipeline as a user. The 2.0 cut removed that runner, leaving the suite runnable only from a live session, while results still come out as JUnit XML. Is running unattended in CI something the project promises?

## Considered Options

* Out: the project runs inside a session, and its report format is for portability, not a promise of CI
* Part of the project, deferred: map an unattended surface now and build it later
* Part of the project, now: map an unattended surface as first-class and bring the code up to it

## Decision Outcome

Chosen option: "Out", chosen by the owner. Reason: TODO.

### Consequences

* Good, because the map promises only what the project can do from where it runs.
* Good, because one way of running means one evaluator setup to keep honest.
* Bad, because a pipeline that wants the suite as a merge gate has to arrange a session itself.

### Confirmation

[INTENT.md](../INTENT.md) promises a report in the format other test results use, and makes no promise about pipelines. No interface in the map describes an unattended entry point.
