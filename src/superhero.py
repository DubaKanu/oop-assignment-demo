class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def save_the_day(self):
        return f"{self.name} is saving the day with their power of {self.power} in {self.city}!"

    def get_identity(self):
        return f"My name is {self.name}, and I protect {self.city}!"