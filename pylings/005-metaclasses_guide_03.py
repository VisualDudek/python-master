# create syntax magic
# replace `.do_it()` wiht simple call `()`


import subprocess


class Action:
    def __init__(self, actions: list[list[str]]):
        self.actions = actions

    def do_it(self):
        for action in self.actions:
            subprocess.run(action)


hellos = Action([["echo", "hello world"], ["echo", "good morning"]])
hellos.do_it()


# TODO: replace `.do_it()` wiht simple call `()`
class ActionCall:
    pass


# make it work
hellos_call = ActionCall(
    [
        ["echo", "hello world from dunder"],
        ["echo", "good morning, says dunder __call__"],
    ]
)
# vvvvvvvvvvvvv
hellos_call()
