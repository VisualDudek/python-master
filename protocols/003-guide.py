# SOLUTION to PROBLEM from 002-guide using inheritance:
class QuackingThing:
    def quack(self):
        raise NotImplemented("Subclasses must implement this method")


class Duck(QuackingThing):
    def quack(self):
        return "The duck is quacking!"


class Person(QuackingThing):
    def quack(self):
        return "The person is imitating a duck quacking!"


def make_it_quack(duck: QuackingThing) -> str:  # crucial change
    return duck.quack()


print(make_it_quack(Duck()))  # OK

print(make_it_quack(Person()))  # Now at static type checker everything is ok
