# Judging is part of running, and tests are judged side by side

Supersedes ADR-0004.

## Context and Problem Statement

ADR-0004 made judging part of running, with the evaluator only able to read. Once the evaluator can run commands (ADR-0007), tests judged at the same time can get in each other's way: two tests that both run the test suite, or both write the same build output, can each change what the other sees. Judging is still part of running. How does a run judge several tests, and what does the project promise about one test affecting another?

## Considered Options

* Judge tests side by side, say so, and leave keeping commands apart to the test author
* Judge tests one at a time whenever they run commands, so no two collide
* Promise that a test judged among the rest comes out the way it would alone, without saying how

## Decision Outcome

Chosen option: "Judge tests side by side, say so, and leave keeping commands apart to the test author", recommended by Claude and accepted by the owner. It keeps runs fast, matches ADR-0008's choice to state what isn't enforced rather than promise it, and keeps judging inside running, as ADR-0004 decided.

### Consequences

* Good, because a suite of many tests takes about as long as its slowest test.
* Good, because the project promises nothing it doesn't enforce.
* Bad, because two tests whose commands collide can come out differently together than alone, and only their author can prevent it.

### Confirmation

[RUN.md](../capabilities/RUN.md) is the only capability. It holds "Every test is judged by a fresh evaluator that knows only the test and the project", "The evaluator can read the project and run commands in it" and "Tests asked for together are judged at the same time, and the project says so". [TEST.md](../primitives/TEST.md) promises independence of order and verdicts, and nothing about tests run at the same time.
