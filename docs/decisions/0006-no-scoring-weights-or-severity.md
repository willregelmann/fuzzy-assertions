# Assertions are pass or fail, with no scoring, weights or severity

Written after the fact, from the project's earlier statement of intent.

## Context and Problem Statement

A judged claim could carry more than pass or fail: a score, a weight that counts it more than others, or a severity that lets some failures through. Should assertions carry any of these?

## Considered Options

* Pass or fail only, and a test passes only when every assertion passes
* Scores, weights or severity tiers on assertions

## Decision Outcome

Chosen option: "Pass or fail only", because, in the owner's words, "the small mental model and the unambiguous verdict are worth more than the expressiveness."

### Consequences

* Good, because every verdict reads the same way and a test's verdict follows from its assertions with no arithmetic.
* Bad, because a claim that matters less can't be marked as such; it has to be left out or split into its own test.

### Confirmation

"An assertion is true or false, never partly" and "No assertion carries a score, a weight or a severity" in [ASSERTION.md](../primitives/ASSERTION.md), and "A test's verdict is read off its assertions, never judged on its own" in [VERDICT.md](../primitives/VERDICT.md).
