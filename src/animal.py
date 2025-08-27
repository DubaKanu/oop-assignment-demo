class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def move(self):
        return "Running 🐕"


class Cat(Animal):
    def move(self):
        return "Jumping 🐈"