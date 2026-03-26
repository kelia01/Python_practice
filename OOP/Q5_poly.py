
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
            return "woof woof!"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
            return f"woof I'm {self.name}"

def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

Dog1 = Dog("pap")
