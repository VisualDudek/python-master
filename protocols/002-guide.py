# type hints is a solution BUT immediately rase issue
# when you try to use common method of different objects (classes)
class Duck:
    def quack(self):
        return "The duck is quacking!"


def make_it_quack(duck: Duck) -> str:  # type hints SOLUTION
    return duck.quack()


class Person:
    def quack(self):
        return "The person is imitating a duck quacking!"


print(make_it_quack(Duck()))  # OK

print(make_it_quack(Person()))  # will run OK in runtime BUT mypy raise PROBLEM
