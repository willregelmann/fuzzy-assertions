# Test

A test is one named check kept beside the project it checks: a short list of [assertions](ASSERTION.md), the instructions an evaluator follows before judging them, and any files those instructions need, kept together. A project's suite is just every test in it. There is nothing else to a suite.

A test is all the evaluator knows. Whatever it takes to judge the assertions fairly is in the test or in the project itself, never in the session that wrote either.

## Invariants

- **A test is the evaluator's whole brief.** Nothing about how the code was written, why, or by whom reaches the evaluator except what the test itself says.
- Each test's name is unique in the project. Two tests with one name are reported as a problem, never resolved by one quietly winning.
- A test has at least one assertion. A test with none, or one that can't be read, is reported as malformed and never passes.
- Tests are independent. No test relies on another having run, on the order they run in, or on another's [verdict](VERDICT.md).
- Files a test brings with it live with the test, and paths in it are read against the test's own place unless it says otherwise.
- A test can't widen what its evaluator is allowed to do. Every test is judged with the same reach.
