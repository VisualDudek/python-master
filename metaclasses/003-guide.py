# How to make objects invokable/callable?
# use dunder `__call__`
# see this great example
# do the "syntax suger" and replace .do_it() with just ()

import subprocess


class Action:
    def __init__(self, actions: list[list[str]]):
        self.actions = actions

    def do_it(self):
        for action in self.actions:
            subprocess.run(action)


hellos = Action([["echo", "hello world"], ["echo", "good morning"]])
hellos.do_it()


class ActionCall:
    def __init__(self, actions: list[list[str]]):
        self.actions = actions

    # vvvvvvvvvvvvvvvvvvvvvvvvv
    def __call__(self):
        for action in self.actions:
            subprocess.run(action)


hellos_call = ActionCall(
    [["echo", "hello world from dunder"], ["echo", "good morning, says dunder _call__"]]
)
# vvvvvvvvvvvvv
hellos_call()
