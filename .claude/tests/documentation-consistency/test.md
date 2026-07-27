---
name: documentation-consistency
assertions:
  - CLAUDE.md and README.md both use the test path convention ./.claude/tests/<name>/test.md
  - CLAUDE.md's Architecture section lists these components and no others - commands/run.md, agents/test-runner.md, bin/junit.py, plugin.json, marketplace.json
  - None of README.md, CLAUDE.md, commands/run.md or agents/test-runner.md claims the evaluator agent can run shell commands
  - None of README.md, CLAUDE.md, commands/run.md or agents/test-runner.md states or implies that a test can declare its own tools, or that more than one evaluator profile exists
  - README.md and CLAUDE.md refer to the command as /test:run, never as a bare /run or as a shell command
  - The frontmatter fields documented in README.md are exactly the fields commands/run.md parses - name and assertions
  - Every file listed in README.md's plugin structure tree exists on disk
---

Check that conventions are described consistently across the documentation.
Documentation drift is the primary risk in a multi-file project like this.

1. Read `CLAUDE.md`, `README.md`, `commands/run.md`, and `agents/test-runner.md`.
   Judge only these four files. Design notes and analysis documents at the
   project root are not part of the shipped documentation and are out of scope.
2. For each assertion, find the relevant statement in each file and confirm the
   files agree with each other and with what `commands/run.md` actually does.
3. For the structure tree, check each listed path exists. Only paths the tree
   lists need to exist — files outside the tree are not a failure.
4. Quote the specific lines you judged each assertion on.
