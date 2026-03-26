# Create a Car class that has:
# Attributes: make, model, year, fuel_level (starts at 100%)
# Method: drive(distance) reduces fuel by 10% per 100km (print warning if low)
# Method: refuel() sets fuel to 100%
# Method: info() prints all car details
# Create a car, drive it, and refuel it.
from re import fullmatch


class Car:
    def __init__(self, make, model, year):
        self.fuel_level = 100
        self.make = make
        self.model = model
        self.year = year

    def drive(self, distance):
        if self.fuel_level < 20:
            print("ur fuel is low might consider first refilling")

        fuel_used = (distance / 100) * 10
        self.fuel_level -= fuel_used


def refuel(self):
    self.fuel_level = 100


def info(self):
    print(f"The car make, model, year: {self.make}, {self.model}, {self.year}")


toyota = Car("2024", "toyota", "30")
toyota.drive()
