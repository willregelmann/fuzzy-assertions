# Reports

After a [run](../capabilities/RUN.md), its [verdicts](../primitives/VERDICT.md) reach the outside in two forms: a summary shown in the session, for the person who ran it, and a JUnit XML file, for any tool that reads test results.

## What passes

| Report | Shows |
|---|---|
| Summary in the session | Each test's verdict, how many of its assertions passed and how long it took; each failed assertion with its evidence and reason; the total; where the file was written |
| `test-results.xml` | One test suite per test and one test case per [assertion](../primitives/ASSERTION.md); a FAIL as a failure carrying its evidence and reason; an ERROR as an error carrying what came back |

## Invariants

- **The summary and the file say the same thing.** Same tests, same verdicts, same evidence.
- The file is always well-formed JUnit XML, whatever the evidence quotes: source code, `<`, `&`, quote marks.
- An ERROR appears as an error, never as a failure and never as a pass.
- Each run writes a fresh file. A report never mixes verdicts from two runs.
- A duration shown is real: each test's own when it was measured, otherwise the whole run's, never invented.
