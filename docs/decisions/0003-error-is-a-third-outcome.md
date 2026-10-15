# ERROR is a third outcome, separate from pass and fail

## Context and Problem Statement

Sometimes nothing judgeable comes back for a test: the evaluator's answer can't be read, or the evaluation broke. Should that count as a failure of the test, or as something else?

## Considered Options

* A third outcome, ERROR, counted as neither pass nor fail
* A FAIL, like any other result that isn't a clean pass

## Decision Outcome

Chosen option: "A third outcome, ERROR", chosen by the owner. Reason: TODO.

### Consequences

* Good, because "the evaluator broke" is never reported as "the project is wrong".
* Good, because it matches the error outcome the JUnit report format already has.
* Bad, because readers of the results have three outcomes to handle instead of two.

### Confirmation

"ERROR is neither pass nor fail" in [VERDICT.md](../primitives/VERDICT.md).
