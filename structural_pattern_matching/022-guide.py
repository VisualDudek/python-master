# Capture patterns are the cornerstone of **destructuting**.
# You'll often use them as subpatterns to extract piece of information
# from complex objects that you want to decompose.
# BC mappings are unordered collections of key-value, it doesn't
# matttern how you arrange your key-value pairs in pattern


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
    case {"subcommand": {"options": options, "name": "commit"}}:
        print(options)
    case _:
        pass
