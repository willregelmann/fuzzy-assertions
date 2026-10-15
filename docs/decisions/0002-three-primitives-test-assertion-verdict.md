# Three primitives: test, assertion and verdict, with suite and evidence folded in

## Context and Problem Statement

The project needs a small set of things it is made of, so that every build shares the same core. Several candidates turned up in the code and docs: a test file, the assertions in it, a suite of tests, the evaluator that judges, the evidence it gathers, a verdict per assertion and per test, and the report. Which of these are primitives, and which are parts or views of others?

## Considered Options

* Test, Assertion and Verdict
* Test and Verdict only, with assertions as part of a test
* Test, Assertion, Evidence and Verdict

## Decision Outcome

Chosen option: "Test, Assertion and Verdict", chosen by the owner. Reason: TODO.

What was folded in or left out while drawing this list:

* A suite is every test in the project and has no rules of its own, so it is part of Test.
* Evidence is what a verdict rests on, and never exists without one, so it is part of Verdict.
* A test's result and an assertion's result are one kind of thing at two sizes, so both are Verdict.
* The report and the summary are views of verdicts, and belong to the surfaces that produce them.
* The evaluator is who judges, not a thing the project is made of. Its rules belong to judging.

### Consequences

* Good, because the per-assertion rules (one claim, no degrees, judged on its own) have a home that isn't crowded by test-level rules.
* Good, because the project's central idea, that a judgment counts only with its evidence, sits in one primitive.
* Bad, because rules about evidence on its own, if any appear, have to live inside Verdict.

### Confirmation

[TEST.md](../primitives/TEST.md), [ASSERTION.md](../primitives/ASSERTION.md) and [VERDICT.md](../primitives/VERDICT.md) are the only primitives, and "No evidence, no pass" holds in Verdict.
