# OOP Assignment

## Project Overview
This project is an Object-Oriented Programming (OOP) assignment that demonstrates the creation and usage of various classes representing real-world entities. The project includes classes for a Smartphone, Book, Superhero, and polymorphic implementations for Animals and Vehicles.

## Project Structure
```
oop-assignment
├── src
│   ├── main.py          # Entry point of the application
│   ├── smartphone.py    # Class representing a smartphone
│   ├── book.py          # Class representing a book
│   ├── superhero.py     # Class representing a superhero
│   ├── animal.py        # Base class for animals
│   └── vehicle.py       # Base class for vehicles
├── tests
│   └── test_main.py     # Unit tests for the application
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Classes Overview

### Smartphone
- **Attributes**: brand, model, storage
- **Methods**: 
  - `make_call()`: Simulates making a call.
  - `send_message()`: Simulates sending a message.

### Book
- **Attributes**: title, author, pages
- **Methods**: 
  - `read()`: Simulates reading the book.
  - `get_summary()`: Provides a summary of the book.

### Superhero
- **Attributes**: name, power, city
- **Methods**: 
  - `save_the_day()`: Simulates the superhero saving the day.
  - `get_identity()`: Reveals the superhero's identity.

### Animal
- **Base Class**: Animal
- **Method**: 
  - `move()`: Abstract method to be implemented by subclasses.

#### Subclasses
- **Dog**: Implements `move()` to print "Running".
- **Cat**: Implements `move()` to print "Pouncing".

### Vehicle
- **Base Class**: Vehicle
- **Method**: 
  - `move()`: Abstract method to be implemented by subclasses.

#### Subclasses
- **Car**: Implements `move()` to print "Driving".
- **Plane**: Implements `move()` to print "Flying".

## Running the Application
To run the application, execute the `main.py` file in the `src` directory. This will create instances of the classes and demonstrate their functionality.

## Running Tests
To run the unit tests, navigate to the `tests` directory and execute the `test_main.py` file. Ensure that all dependencies listed in `requirements.txt` are installed.

## Requirements
Make sure to install the required dependencies by running:
```
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License.