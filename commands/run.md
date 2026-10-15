---
description: Run AI-evaluated tests
argument-hint: [name | --all]
allowed-tools: Read, Glob, Agent, Bash
---

Run AI-evaluated tests from `./.claude/tests/`.

**Step 1 — Parse arguments:**

- If `$ARGUMENTS` is empty or `--all`: run all tests
- Otherwise: `$ARGUMENTS` is the test name to run

**Step 2 — Discover tests:**

Glob for `.claude/tests/*/test.md` in the current project.

If no test files are found, display "No test files found in `./.claude/tests/`." and stop.

Read each file and parse the YAML frontmatter to extract `name` and `assertions`. The body is freeform markdown — instructions for the evaluator.

A test file is malformed if it can't be parsed, has no `name`, or has no assertions. Two files with the same `name` are both malformed — never let one quietly win. A malformed test is not spawned; it becomes an ERROR verdict named by its path (or by its name if it has one), with the problem as the error message. Never skip it silently.

If a specific test name was given, find the file whose `name` frontmatter matches. If no match, list the available test names and stop.

**Step 3 — Execute tests:**

If running multiple tests, assemble all agent prompts first, then spawn all agents in a single message (parallel Agent tool calls — do not call them one at a time).

For each test, spawn `test:test-runner` (`subagent_type`). Its tools are fixed by its own definition to `Read`, `Grep`, `Glob`, `Bash` — every test gets the same reach, and nothing is passed to scope it per spawn. Evaluators can run commands, so a run may change the working tree, and tests run in parallel may affect each other; keeping their commands apart is the test author's job.

Do not pass a `name` to the spawn. An unnamed agent runs to completion and delivers its final message — the VERDICT block — automatically. A named agent becomes a persistent teammate that finishes its work, goes idle, and delivers nothing until asked, which turns every run into a round of chasing verdicts by mailbox.

Assemble the agent prompt from the test file. Include the test's directory so the evaluator can locate any co-located fixtures (its working directory is the project root, not the test directory):

```
Test: <name>
Test directory: .claude/tests/<name>
Files referenced by this test live in its test directory unless stated otherwise; resolve relative paths against it.

Assertions:
1. <first assertion>
2. <second assertion>
...

<body from test file>
```

**Step 4 — Collect verdicts:**

Parse each agent's VERDICT block. If an agent's response has no parseable VERDICT block, treat that test as ERROR (distinct from PASS/FAIL) and keep the raw response snippet as the error message.

Take each test's duration from its own completion report, which times the agent individually — the agent does not track time itself, and parallel tests do not share a wall-clock. If no per-agent duration is available, record the batch wall-clock rather than inventing per-test figures.

**Step 5 — Write JUnit XML:**

Build a JSON array of the verdicts and pipe it to the report writer. Use a quoted heredoc so nothing in the evidence text is expanded by the shell:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/bin/junit.py" test-results.xml <<'VERDICTS'
[
  {
    "name": "<test name>",
    "result": "PASS",
    "duration": 47.2,
    "error": null,
    "assertions": [
      {"assertion": "<assertion text>", "result": "PASS", "evidence": "<what you observed>"},
      {"assertion": "<assertion text>", "result": "FAIL", "evidence": "<what you observed>", "reason": "<why it fails>"}
    ]
  }
]
VERDICTS
```

Pass the evidence and reason through exactly as the agent reported them — do not shorten or reword. The script handles all XML escaping; never hand-write XML yourself.

**Step 6 — Report results:**

Display the summary:

```
═══ Test Results ═══

[PASS] happy-path              (11/11 assertions, 157s)
[FAIL] insufficient-context    (3/5 assertions, 45s)

─────────────────────
Total: 1/2 passed

JUnit XML written to test-results.xml
```

For any FAIL result, include the failed assertions with their evidence and reason. For any ERROR, include its error message.
