## Overview

This is the `test` plugin for Claude Code — a test framework for assertions that cannot practically be checked deterministically. You write a check as a sentence of natural language; an isolated evaluator agent judges it PASS or FAIL and shows the evidence.

## Architecture

No build step:

- **`commands/run.md`** — `/test:run` command. Discovers and parses `./.claude/tests/*/test.md`, spawns one evaluator agent per test (in parallel for multiple tests), collects verdicts, writes JUnit XML via `bin/junit.py`, displays a summary.
- **`agents/test-runner.md`** — Isolated read-only evaluator agent (`tools: Read, Grep, Glob`). Receives only the test spec, never the implementation context. Follows the test body → evaluates each assertion with evidence → returns a structured VERDICT block.
- **`bin/junit.py`** — Reads a JSON array of verdicts on stdin, writes JUnit XML. Exists as a script so XML escaping is handled by a library rather than by the model: evidence text quotes source and docs, so it routinely contains `<`, `&`, and quote characters.
- **`.claude-plugin/plugin.json`** — Plugin manifest (name, description, version).
- **`.claude-plugin/marketplace.json`** — Marketplace metadata for installation.

## Key Conventions

- Test files live in the consuming project at `./.claude/tests/<name>/test.md` with YAML frontmatter (`name`, `assertions`) and a freeform markdown body.
- Assertions are natural language pass/fail statements. No scoring, weights, or severity levels — a test passes only if every assertion passes.
- The evaluator is read-only (`Read`, `Grep`, `Glob`), enforced by the agent definition's own `tools:` field. There is no per-test tool scoping: the Agent tool fixes a subagent's tools by its definition, so a test cannot request more.
- Tests are independent — no ordering or dependencies between them.
- This framework is for checks that need judgment. Anything a script can settle should be a script; see the note in `README.md`.

## Publishing

No build step. Push to GitHub and users install via:

```
/plugin marketplace add <owner>/fuzzy-assertions
/plugin install test@fuzzy-assertions
```

Marketplace config lives in `.claude-plugin/marketplace.json`. Bump `version` in `.claude-plugin/plugin.json` when releasing changes.
