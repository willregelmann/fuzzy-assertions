# No promise that a run leaves the project unchanged

## Context and Problem Statement

Once the evaluator can run commands (ADR-0007), a run can change the project: a test suite writes caches and build output, and a command can edit files. The host does not stop the evaluator from doing so. What does the project promise about the state it leaves behind?

## Considered Options

* Say it plainly: the evaluator can do what the host lets it do, and a run can change the project
* Promise that the evaluator never edits the project's own files on purpose, allowing commands' by-products
* Run each evaluator in a throwaway copy of the project, so a run never changes it

## Decision Outcome

Chosen option: "Say it plainly", chosen by the owner. It keeps the rule that the project never describes a limit the host doesn't enforce. Further reasoning: TODO.

### Consequences

* Good, because nothing in the project claims a sandbox that isn't there.
* Bad, because a run can leave the working tree changed, and tests running at the same time can get in each other's way.

### Confirmation

"Nothing promises that a run leaves the project as it found it" and "What the evaluator is said to be able to do is exactly what the host lets it do" in [RUN.md](../capabilities/RUN.md).
