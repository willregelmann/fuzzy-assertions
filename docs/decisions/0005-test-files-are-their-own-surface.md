# Test files are a surface of their own, beside commands and reports

## Context and Problem Statement

The outside touches the project in three places: the command that starts a run, the files tests are written in, and the reports that come out. Is the test file format its own interface, or part of the command's contract?

## Considered Options

* Three surfaces: Commands, Test Files and Reports
* Two surfaces, with the test file format folded into Commands

## Decision Outcome

Chosen option: "Three surfaces: Commands, Test Files and Reports", chosen by the owner. Reason: TODO.

### Consequences

* Good, because whoever writes tests has a surface of their own, with its rules in one place.
* Bad, because there is one more file to keep in step with the code.

### Confirmation

[COMMANDS.md](../interfaces/COMMANDS.md), [TEST_FILES.md](../interfaces/TEST_FILES.md) and [REPORTS.md](../interfaces/REPORTS.md) are the interfaces.
