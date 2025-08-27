# Contents of /oop-assignment/oop-assignment/src/main.py

from smartphone import Smartphone
from book import Book
from superhero import Superhero
from animal import Dog, Cat
from vehicle import Car, Plane

def main():
    # Creating instances of Smartphone
    phone = Smartphone(brand="Apple", model="iPhone 14", storage="128GB")
    print(f"Smartphone: {phone.brand} {phone.model}, Storage: {phone.storage}")
    phone.make_call("123-456-7890")
    phone.send_message("Hello, World!")

    # Creating instances of Book
    book = Book(title="1984", author="George Orwell", pages=328)
    print(f"Book: {book.title} by {book.author}, Pages: {book.pages}")
    book.read()
    print(book.get_summary())

    # Creating instances of Superhero
    hero = Superhero(name="Spider-Man", power="Web-slinging", city="New York")
    print(f"Superhero: {hero.name}, Power: {hero.power}, City: {hero.city}")
    hero.save_the_day()
    print(hero.get_identity())

    # Demonstrating polymorphism with animals
    animals = [Dog(), Cat()]
    for animal in animals:
        animal.move()

    # Demonstrating polymorphism with vehicles
    vehicles = vehicles = [Car("Toyota", "Corolla"), Plane("Boeing", "747")]
    for vehicle in vehicles:
        vehicle.move()

if __name__ == "__main__":
    main()