# Test Files

Whoever writes tests meets the project here: each [test](../primitives/TEST.md) is a file kept inside the project it checks.

## What passes

| Part | Holds |
|---|---|
| `.claude/tests/<name>/` | The test's own directory, with any files it needs beside it |
| `test.md`, frontmatter `name` | The test's name, unique in the project |
| `test.md`, frontmatter `assertions` | The [assertions](../primitives/ASSERTION.md), one sentence each |
| `test.md`, body | Freeform markdown the evaluator follows before judging |

## Invariants

- Tests are found only at `.claude/tests/<name>/test.md` in the project being checked. A file anywhere else is not part of the suite.
- **No field in a test file changes what the evaluator can reach or how strictly it judges.** The frontmatter holds a name and assertions, nothing that grants anything.
- The body reaches the evaluator as written, along with the test's directory, so paths in it can be read against that directory.
- A test file that can't be read is reported by its path. It is never skipped quietly.
