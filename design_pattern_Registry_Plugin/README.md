Based on ArjanCodes
this is venv inside venv, use `uv sync` before running

Examples of commands:

- uv run main.py text count "This is a registry pattern example"
- uv run main.py text shout "plugin power"
- uv run main.py text reverse "Was it a car or a cat I saw"

# TAKEAWAYS
- `get_registry()` is functioning as a **getter** (accessor method) for the priv variable. Classic encapsulation pattern where you protect internal state and only expose controlled ways to interact with it.