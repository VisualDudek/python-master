# fix it


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

# pyright: reportMatchNotExhaustive=false
match command:
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    case Command(main, _, Command(subcommand, _)) if main == subcommand:
        print(f"The main command and subsommand are the same")