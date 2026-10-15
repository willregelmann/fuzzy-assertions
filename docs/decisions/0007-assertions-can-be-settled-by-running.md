# Assertions can be settled by running, and the evaluator can run commands

## Context and Problem Statement

Until now, both the project's stated intent and its evaluator treated an assertion as something settled by reading. The evaluator could read and search but not run anything, and claims a script could settle were meant to stay out of the suite. But some of what a project needs to be true is settled by running something: "The unit tests pass". Is that kind of claim an assertion, and if it is, how is it judged?

## Considered Options

* Every check is a sentence, settled by running or by reading, and the evaluator can run commands
* Keep unwritten, reading-only checks as the lead, and allow assertions settled by running without centring them

## Decision Outcome

Chosen option: "Every check is a sentence, settled by running or by reading", chosen by the owner, who wanted this made central because earlier versions had not made it clear. Further reasoning: TODO.

Settled with it:

* A claim about what something does when run is judged by running it, never by reading.
* Evidence from a command names what was run and what came back, including how it exited.
* A command that can't be run, or doesn't finish, fails the assertions that rest on it.
* Every test still gets the same evaluator with the same reach, and a test can't ask for more or for less.

### Consequences

* Good, because one suite can hold every check a project cares about, in one form and one report.
* Good, because "the tests pass" can't be passed on how the tests look.
* Bad, because an agent reading a command's result can misread it, where a script would not.
* Bad, because the evaluator's reach is now as wide as the host allows; see ADR-0008.

### Confirmation

[INTENT.md](../INTENT.md) covers both kinds of check. [ASSERTION.md](../primitives/ASSERTION.md) names both as one kind of thing. [VERDICT.md](../primitives/VERDICT.md) holds "A claim about what something does when run is judged by running it" and the rules for evidence from a command. [RUN.md](../capabilities/RUN.md) holds "The evaluator can read the project and run commands in it".
