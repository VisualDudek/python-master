# This example shows why capture pattern can be tricky
# SOLUTION: Value pattern


command = "help"

match input("Type your command: "):
    # vvvvvvvvvvvvv
    case (
        command
    ):  # you think that this is Literal Patten BUT in fact it is capture AND will
        # shadow your global command var.
        print("Showing help.")

# >>> Type your command: exit
# OUTPUT: Showing help
