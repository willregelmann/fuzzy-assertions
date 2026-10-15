# test

[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A test framework where every check is a sentence.

What a project needs to be true is split across kinds of check that never meet. "The unit tests pass" lives in a test runner. "Every error tells the reader what to do next" lives nowhere, because no test is worth writing for it — so it gets skipped, and the gap is where regressions live.

Here you state either kind as a sentence of natural language. An isolated agent that knows nothing of how the code was written runs what it needs, reads what it needs, and returns pass or fail with the evidence attached: the command and what came back, or the lines it judged on. Results come out as JUnit XML.

## Installation

**Prerequisites:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and Python 3.

```
/plugin marketplace add willregelmann/fuzzy-assertions
/plugin install test@fuzzy-assertions
```

Verify it loaded — `/test:run` should appear:

```
/plugin
```

## Writing a test

Tests live in your project at `./.claude/tests/<name>/test.md`:

```yaml
---
name: error-messages
assertions:
  - The CLI test suite passes
  - Every error raised in src/cli/ tells the reader what to do next, not just what failed
  - No error message exposes an internal stack trace to the end user
---

Run the CLI tests with `pytest tests/cli`.
Read every file under `src/cli/` and find each raised exception.
For each assertion, quote the specific lines or command output you judged it on.
```

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique test identifier (kebab-case) |
| `assertions` | Yes | Natural language pass/fail checks |

The body is freeform markdown — instructions the evaluator follows before judging. If a test needs fixtures, put them in its own directory; the evaluator is told that directory and resolves relative paths against it.

## Running tests

From inside a Claude Code session (it's a slash command, not a shell command):

```
/test:run                 # all tests
/test:run error-messages  # one test by name
```

Multiple tests run in parallel. You get a summary and a `test-results.xml`:

```
═══ Test Results ═══

[PASS] error-messages          (3/3 assertions, 31s)
[FAIL] migration-guide         (1/3 assertions, 45s)

─────────────────────
Total: 1/2 passed

JUnit XML written to test-results.xml
```

Failed assertions include their evidence and reason.

## Writing good assertions

The evaluator is strict: evidence is required for every judgment, partial compliance is FAIL, and missing evidence is FAIL. A claim about what something does when run is judged by running it, and a command that can't be run or doesn't finish is FAIL. Write with that in mind.

- **Be specific** — "No TODO or FIXME placeholders in committed code", not "code is good quality"
- **Reference observable evidence** — the evaluator must be able to prove it
- **State exact expectations** — "Exit code is 0", not "command succeeds"
- **Test absence explicitly** — "No PRs were created", not "nothing happened"
- **Qualify subjective judgments** — "a professional summary mentioning PR links", not "note is good"
- **One check per assertion** — split compound checks into separate items
- **Say how to run it** — when an assertion is settled by a command, name the command in the body so the evaluator runs the one you mean

**Commands run for real.** The evaluator can run any command in your project, and nothing sandboxes it: a run can change your working tree. Tests run in parallel, so if two tests' commands could collide (the same build output, the same database), keep them apart yourself.

## How it works

```
/test:run error-messages
  │
  ▼
commands/run.md (orchestrator)
  │  discovers ./.claude/tests/error-messages/test.md
  │  parses frontmatter + body
  │
  ▼
agents/test-runner.md (isolated evaluator)
  │  no implementation context — only the test spec
  │  reads files, runs commands → judges each assertion
  │  returns a VERDICT with evidence
  │
  ▼
bin/junit.py → test-results.xml   +   summary displayed
```

The evaluator runs in a fresh subagent with no memory of the session that wrote the code. It sees the spec and whatever evidence it gathers itself — so a verdict depends on the artifact, not on how the artifact came to be.

Its tools are fixed by the agent definition to `Read`, `Grep`, `Glob`, `Bash`. There is no per-test tool scoping: a subagent's tools come from its own definition, so a test cannot request more or less than the evaluator has.

## Plugin structure

```
test/
├── .claude-plugin/
│   ├── plugin.json            # Plugin manifest
│   └── marketplace.json       # Marketplace metadata
├── commands/
│   └── run.md                 # /test:run
├── agents/
│   └── test-runner.md         # Isolated evaluator
└── bin/
    └── junit.py               # Verdicts JSON → JUnit XML
```

## License

MIT
