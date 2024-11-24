# Capture patterns are the cornerstone of **destructuting**.
# You'll often use them as subpatterns to extract piece of information
# from complex objects that you want to decompose.


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
    # vvvvvvvvvvvv                 vvvvvvvvvvvvvvvvvvv
    case Command("git", _, Command(subcommand, options)):
        print(f"{subcommand=}\n{options=}")
