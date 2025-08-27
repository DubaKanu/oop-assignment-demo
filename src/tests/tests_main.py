import unittest
from src.smartphone import Smartphone
from src.book import Book
from src.superhero import Superhero
from src.animal import Dog, Cat
from src.vehicle import Car, Plane

class TestClasses(unittest.TestCase):

    def test_smartphone(self):
        phone = Smartphone("Apple", "iPhone 14", "128GB")
        self.assertEqual(phone.brand, "Apple")
        self.assertEqual(phone.model, "iPhone 14")
        self.assertEqual(phone.storage, "128GB")
        self.assertEqual(phone.make_call("123456789"), "Calling 123456789...")
        self.assertEqual(phone.send_message("Hello!"), "Sending message: Hello!")

    def test_book(self):
        book = Book("1984", "George Orwell", 328)
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")
        self.assertEqual(book.pages, 328)
        self.assertEqual(book.read(), "Reading 1984...")
        self.assertEqual(book.get_summary(), "1984 by George Orwell, 328 pages.")

    def test_superhero(self):
        hero = Superhero("Spider-Man", "Web-slinging", "New York")
        self.assertEqual(hero.name, "Spider-Man")
        self.assertEqual(hero.power, "Web-slinging")
        self.assertEqual(hero.city, "New York")
        self.assertEqual(hero.save_the_day(), "Spider-Man saves the day!")
        self.assertEqual(hero.get_identity(), "I am Spider-Man from New York.")

    def test_animal_movement(self):
        dog = Dog()
        cat = Cat()
        self.assertEqual(dog.move(), "Running")
        self.assertEqual(cat.move(), "Sneaking")

    def test_vehicle_movement(self):
        car = Car()
        plane = Plane()
        self.assertEqual(car.move(), "Driving")
        self.assertEqual(plane.move(), "Flying")

if __name__ == '__main__':
    unittest.main()