# POC: example that shows problems with maintaining code
# when realaying only on duck-typing
# besides typechecker (losing information of type, vehicle is any) it works fine
# will see in next file where is the problem and solution to it


class Car:
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


class Truck:
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


# main code:
vehicles = [Car("Ford", "Mustang", "Red"), Truck("Ford", "F-150", "Blue")]

for vehicle in vehicles:
    vehicle.start()
    vehicle.drive()
    vehicle.stop()
