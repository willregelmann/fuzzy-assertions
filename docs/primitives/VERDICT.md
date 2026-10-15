# Verdict

A verdict is what judging produced. For an [assertion](ASSERTION.md) it is PASS or FAIL, with the evidence it was decided on and, for a FAIL, the reason. For a [test](TEST.md) it is read off its assertions' verdicts. When nothing judgeable came back for a test at all, its verdict is ERROR. An assertion's verdict and a test's verdict are the same kind of thing at two sizes.

A verdict is only as good as the evidence it carries. Evidence is what the evaluator itself observed: a command it ran and what came back, the lines it quotes, the paths it found or didn't. It is never the evaluator's assurance.

Deciding whether the evidence shows an assertion holds takes judgment, so the evaluator makes that call. That every verdict carries its evidence, and that no evidence means FAIL, is fixed.

## Invariants

- **No evidence, no pass.** A PASS always carries evidence a reader could follow back to the project.
- **A claim about what something does when run is judged by running it.** "The unit tests pass" is never passed by reading the tests and deciding they would.
- Evidence from a command names what was run and what came back, including how it exited, so a reader can run it again.
- When the evidence can't be gathered, because a file is missing or a command can't be run or doesn't finish, the assertion is FAIL and says why. It is never skipped, never passed by default, and never judged by reading instead.
- A FAIL names its assertion, its evidence and its reason, enough to act on without running the test again.
- **A test's verdict is read off its assertions, never judged on its own.** It is PASS only when every assertion passed, and FAIL when any failed.
- **ERROR is neither pass nor fail.** It means the project wasn't judged. It is never counted as either, and it carries whatever came back in place of a verdict.
- Evidence and reasons travel exactly as the evaluator gave them. Nothing between the evaluator and the reader shortens, rewords or tidies them.
