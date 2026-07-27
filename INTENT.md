## Purpose

Some things a project needs to be true have no deterministic test worth writing — that an error message would actually help the person reading it, that a migration guide still matches the API it documents, that no placeholder code survived review. They are checkable in principle and skipped in practice, and the gap is where regressions live. This is a test framework for those cases: each one is stated as a sentence of natural language, an agent evaluates it against evidence it gathers itself, and the result is pass or fail with that evidence attached. Fuzzy assertions get a suite, a runner, and a build gate that reports like JUnit — the same apparatus the mechanical half of a test suite has always had.

## Users

- **A developer with a check they cannot practically write** — has a requirement that genuinely matters and no deterministic test worth the effort; wants to spend a sentence rather than build a harness.
- **A CI pipeline** — runs the suite as a merge gate and ingests the results through the same machine-readable report and exit code as every other test job.
- **The framework's own maintainer** — applies the framework to the framework, so that what it documents cannot quietly diverge from what it does.

## Success Criteria

1. A check with no practical deterministic implementation can be added to the suite by writing one sentence of natural language — no fixture scaffolding, no matcher, no parsing code.
2. Adding the suite to an existing pipeline requires nothing a JUnit-reporting job does not already have: a standard result file, a non-zero exit on failure, and no bespoke reporting glue.
3. A verdict depends only on the test spec and the observable artifact — not on how the artifact was built, or why.
4. Every verdict is traceable to evidence the evaluator gathered; no assertion passes on assurance alone.
5. An assertion that mechanical tooling could practically decide is decided mechanically rather than by model judgment.
6. The same test file, unmodified, yields the same verdict wherever it is run.
7. A failing test names the specific assertion and the evidence that sank it, so the failure is actionable without re-running it.

## Non-Goals

- **Competing with deterministic tests where a deterministic test is practical** — the target is the checks that would otherwise go unwritten. Where an assertion has a cheap mechanical form, that form is the right one and this framework should defer to it.
- **Guaranteeing that the assertions themselves are any good** — an assertion inferred from current behavior and refined until it passes is tautological, and nothing here prevents that. Authoring guidance may exist; enforcement does not.
- **Scoring, weighting, or severity tiers** — assertions are pass/fail and a test passes only if all of them do. The small mental model and the unambiguous verdict are worth more than the expressiveness.
- **Claiming a capability the host platform does not actually enforce** — a documented sandbox that isn't real is worse than a smaller one that is.

## Open Questions

| # | Question | Why it matters | Status |
|---|----------|----------------|--------|
| 1 | Is judging prose and documentation the flagship case, or an accident of it being the easiest thing to point the framework at itself? | Both surviving self-tests judge prose. If it is the flagship, the framing and any future examples should lead with it rather than with command-backed checks. | Open |
| 2 | How large a suite is the JUnit comparison meant to survive? | A JUnit suite runs in seconds for thousands of assertions; here each test is a full agent invocation. Running on every change is implied by the CI ambition but bounds suite size, and nothing states that bound. | Open |
| 3 | Does delivery as a session-scoped plugin stay the only form, given that a CI pipeline is a named user it cannot currently reach? | Criterion 2 targets an unattended build gate; a slash command needs a live session. Either the plugin gains a headless sibling or the CI user is aspirational, and which one decides what gets built next. | Open |

---

Discovered 2026-07-25.
