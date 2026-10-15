# Run

Running takes the [tests](../primitives/TEST.md) a person asks for, all of them or one by name, has each one judged by its own fresh evaluator, and turns the [verdicts](../primitives/VERDICT.md) into [reports](../interfaces/REPORTS.md). The evaluator reads the test's instructions, gathers evidence by reading the project and running commands in it, and judges every [assertion](../primitives/ASSERTION.md).

Deciding whether the evidence shows an assertion holds takes judgment, so the evaluator makes that call. What the evaluator knows, what it can reach, and that every test asked for ends with a verdict are fixed.

## Invariants

- **Every test is judged by a fresh evaluator that knows only the test and the project.** Nothing from the session that started the run, or the one that wrote the code, reaches it, and no evaluator sees another test or its verdict.
- **The evaluator can read the project and run commands in it.** Every test is judged with that same reach. A test can't ask for more or for less.
- What the evaluator is said to be able to do is exactly what the host lets it do. The project never describes a limit or a reach the host doesn't enforce.
- **Every test asked for ends the run with exactly one verdict: PASS, FAIL or ERROR.** None goes missing. An answer from the evaluator that can't be read is ERROR, never a guess at what it meant.
- Tests asked for together are judged at the same time, and the project says so. Keeping one test's commands from getting in another's way is the test author's job.
- Asking for a test that doesn't exist names the tests that do. A project with no tests says so. Neither ever looks like a passing run.
- Nothing promises that a run leaves the project as it found it. Commands an evaluator runs can change it, and the project says so.
