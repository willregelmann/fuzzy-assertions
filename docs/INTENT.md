# Fuzzy Assertions

A test framework where every check is a sentence, judged by an agent that has to show its evidence.

Before a change lands, Fuzzy Assertions answers one question: **does this still hold, and what shows it?**

What a project needs to be true is split across kinds of check that never meet. "The unit tests pass" lives in a test runner. "Every error tells the reader what to do next" lives nowhere, because no test is worth writing for it, so it gets skipped, and the gap is where regressions live. Asking a model "does this look right?" in the session that wrote the code is only half the job: it knows what was meant, it agrees with itself, and its answer is gone when the session ends.

So every check is written once, as a plain sentence beside the project, whether running something settles it or only reading can. A fresh evaluator that knows nothing of how the work was done runs what it needs, reads what it needs, and returns pass or fail with the evidence quoted: the command and what came back, or the lines it judged on. A judgment counts only when it carries the evidence it was made on.

If a check passes on evidence nobody can follow, or would have come out differently had the evaluator known how the code was written, Fuzzy Assertions has failed at the one thing it exists to do.
