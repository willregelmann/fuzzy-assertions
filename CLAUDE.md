## Overview

This is the `test` plugin for Claude Code — a test framework where every check is a sentence of natural language, whether running a command settles it or only reading can. An isolated evaluator agent judges it PASS or FAIL and shows the evidence.

## Architecture

No build step:

- **`commands/run.md`** — `/test:run` command. Discovers and parses `./.claude/tests/*/test.md`, spawns one evaluator agent per test (in parallel for multiple tests), collects verdicts, writes JUnit XML via `bin/junit.py`, displays a summary.
- **`agents/test-runner.md`** — Isolated evaluator agent (`tools: Read, Grep, Glob, Bash`). Receives only the test spec, never the implementation context. Follows the test body → evaluates each assertion with evidence → returns a structured VERDICT block.
- **`bin/junit.py`** — Reads a JSON array of verdicts on stdin, writes JUnit XML. Exists as a script so XML escaping is handled by a library rather than by the model: evidence text quotes source and docs, so it routinely contains `<`, `&`, and quote characters.
- **`.claude-plugin/plugin.json`** — Plugin manifest (name, description, version).
- **`.claude-plugin/marketplace.json`** — Marketplace metadata for installation.

## Key Conventions

- Test files live in the consuming project at `./.claude/tests/<name>/test.md` with YAML frontmatter (`name`, `assertions`) and a freeform markdown body.
- Assertions are natural language pass/fail statements. No scoring, weights, or severity levels — a test passes only if every assertion passes.
- The evaluator can read the project and run commands in it (`Read`, `Grep`, `Glob`, `Bash`), fixed by the agent definition's own `tools:` field. There is no per-test tool scoping: the Agent tool fixes a subagent's tools by its definition, so a test cannot request more or less. Nothing sandboxes those commands; the docs never claim otherwise.
- Tests are independent — no ordering or dependencies between them. They run in parallel, so keeping their commands from colliding is the test author's job.
- A claim about what something does when run is judged by running it, never by reading. Evidence from a command names the command, its exit status and its output.

## Publishing

No build step. Push to GitHub and users install via:

```
/plugin marketplace add <owner>/fuzzy-assertions
/plugin install test@fuzzy-assertions
```

Marketplace config lives in `.claude-plugin/marketplace.json`. Bump `version` in `.claude-plugin/plugin.json` when releasing changes.

## The Map

This project has a map in `docs/`: what it's for, what it's made of and what must always hold, with decision records for why. Read `docs/README.md` before changing code, and work with the `develop-project` skill.
