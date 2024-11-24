# type: ignore
# ruff: noqa
# Use capture patterns to extract subcommand and subcommand-options


from dataclasses import dataclass
from typing import Self


@dataclass
class Command:
    name: str
    options: tuple[str, ...]
    subcommand: None | Self = None


command = Command(
    name="git",
    options=(),
    subcommand=Command(
        name="commit",
        options=("-a", "-m", "'Initial commit'"),
    ),
)

# vvvvvvvvvvvvvvvvvv


print(f"{subcommand=}\n{options=}")
