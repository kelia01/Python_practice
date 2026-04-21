class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Animal should talk"

    def move(self):
        return "Animal should move"

    def show_info(self):
        print(f"The name is {self.name} and has {self.age} years")
        print(self.make_sound())
        print(self.move())


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        return "I will woof woof!!"

    def move(self):
        return "I will run around as a walk"

    def show_info(self):
        super().show_info()
        print( "I am a valuable dog")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        return "I will meouw meouw!!"

    def move(self):
        return "I will walk quietly"

    def show_info(self):
        super().show_info()
        print("I am a valuable cat")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        return "I will chirp chirp!!"

    def move(self):
        return "I will fly in the sky"

    def show_info(self):
        super().show_info()
        print("I am a fast bird")

owl = Bird("owl", 20)
owl.show_info()






