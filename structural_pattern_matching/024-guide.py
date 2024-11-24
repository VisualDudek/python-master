# in mapping pattern you can use `**` (standard dict unpacking) to capture multiple key-value pairs into smaller dict

from dataclasses import dataclass, asdict
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

print(f"Using asdict: {asdict(command)=}\n")

# vvvvvvvvvvvvvvvvv
match asdict(command):
    case {"subcommand": _, **rest}:
        print(rest)
    case _:
        pass
