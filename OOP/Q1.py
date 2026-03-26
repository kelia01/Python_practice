#Create a Dog class that has:
#Attributes: name, age, breed
#Method: bark() that prints "Woof! My name is [name]"
#Method: human_years() that returns age × 7
#Create 2 different dogs and make them bark.

class Dog():
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"Woof! My name is {self.name}")

    def human_years(self):
        return self.age * 7

dog1 = Dog("Tommy", 3, "Hybrid")

dog1.bark()
print(dog1.human_years())
