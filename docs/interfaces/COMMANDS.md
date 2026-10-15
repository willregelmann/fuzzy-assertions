# Commands

A person in a Claude Code session starts a [run](../capabilities/RUN.md) by typing a slash command. The command lives inside the session: there is no way to run tests from outside one.

## What passes

| Command | Does |
|---|---|
| `/test:run` | Runs every test in the project |
| `/test:run <name>` | Runs the one test with that name |

## Invariants

- The command is `/test:run`, in the plugin's `test` namespace. It is typed into a session, never into a shell.
- With no name, every [test](../primitives/TEST.md) in the project runs. With a name, exactly that test runs, or none does and the names that exist are listed.
- A run always ends by showing its summary and where its report was written, even when every test failed or errored.
