# f-string do not work with structural pattern bc.
# f-stirng typically involve string interpolation,
# which must be done at runtime.

COMMAND = "read"

match input("Type the command: "):
    case f"help {COMMAND}":
        print("Showing help on the 'read' command")
