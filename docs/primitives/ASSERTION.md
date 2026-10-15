# Assertion

An assertion is one claim about the project, written as a plain sentence, that is either true or false of the project as it is now. Some are settled by running something: "The unit tests pass", "The CLI exits non-zero on an unknown flag". Some can only be settled by reading: "Every error raised in `src/cli/` tells the reader what to do next". Both are the same kind of thing, and a test can hold either or both. An assertion belongs to exactly one [test](TEST.md), and it is the unit that is judged and the unit that is reported.

An assertion has no degree. It holds or it doesn't.

## Invariants

- **An assertion is true or false, never partly.** Partial compliance is false. "Mostly" is false.
- No assertion carries a score, a weight or a severity, and none counts for more than another.
- Each assertion is judged on its own. Its [verdict](VERDICT.md) never depends on how another assertion in the same test came out.
- Every assertion in a test is judged and reported. None is dropped, merged with another or split in two along the way.
- An assertion is reported in its author's own words, exactly as written.
