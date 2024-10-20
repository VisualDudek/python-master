# POC: example that shows problems with maintaining code
# when realaying only on duck-typing
# What if you want to create a Jeep class that also works in this loop?
# In that case, you need to know the interface that Jeep must implement.
# Knowing the interface will require reviewing
# the code of Car and Truck or its documentation.
# SOLUTION: ABC called Vehicle
# typechecker will complain which methods are not implemented
# TAKEAWAY: `@abstractmethod` decorator is just to enforce implementation
# given method


from abc import ABC, abstractmethod
from typing import List


class Vehicle(ABC):
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    @abstractmethod
    def start(self):
        raise NotImplementedError("start() must be implemented")

    @abstractmethod
    def stop(self):
        raise NotImplementedError()

    @abstractmethod
    def drive(self):
        raise NotImplementedError()


class Car(Vehicle):
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("The car is starting")

    def stop(self):
        print("The car is stopping")

    def drive(self):
        print("The car is driving")


class Truck(Vehicle):
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("The truck is starting")

    def stop(self):
        print("The truck is stopping")

    def drive(self):
        print("The truck is driving")


class Jeep(Vehicle):
    def start(self):
        print("The jeep is staring")


# main code:
vehicles: List[Vehicle] = [
    Car("Ford", "Mustang", "Red"),
    Truck("Ford", "F-150", "Blue"),
    Jeep("Land Rover", "Defender", "Black"),
]

for vehicle in vehicles:
    vehicle.start()
    vehicle.drive()
    vehicle.stop()
