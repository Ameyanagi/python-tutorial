"""
Object-Oriented Programming examples for the Python tutorial
"""

import random
from abc import ABC, abstractmethod
from datetime import datetime


# Basic Class Example
class BankAccount:
    """Simple bank account class demonstrating basic OOP concepts."""

    bank_name = "Python Bank"  # Class attribute

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        self._account_number = self._generate_account_number()

    def _generate_account_number(self):
        """Private method to generate account number."""
        return f"ACC{random.randint(10000, 99999)}"

    def deposit(self, amount):
        """Deposit money to account."""
        if amount > 0:
            self.balance += amount
            self._add_transaction("Deposit", amount)
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self._add_transaction("Withdrawal", amount)
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def _add_transaction(self, transaction_type, amount):
        """Private method to add transaction to history."""
        self.transaction_history.append(
            {
                "type": transaction_type,
                "amount": amount,
                "timestamp": datetime.now(),
                "balance": self.balance,
            }
        )

    def get_statement(self):
        """Get account statement."""
        print("\n=== Account Statement ===")
        print(f"Bank: {self.bank_name}")
        print(f"Account: {self._account_number}")
        print(f"Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("\nRecent Transactions:")
        for transaction in self.transaction_history[-5:]:
            print(
                f"  {transaction['timestamp'].strftime('%Y-%m-%d %H:%M')} | "
                f"{transaction['type']}: ${transaction['amount']:.2f}"
            )

    def __str__(self):
        return (
            f"Account({self._account_number}): "
            f"{self.account_holder} - ${self.balance:.2f}"
        )


# Inheritance Example
class Animal:
    """Base animal class for inheritance examples."""

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100

    def eat(self, food):
        """Generic eating behavior."""
        self.energy += 10
        print(f"{self.name} eats {food} and gains energy. Energy: {self.energy}")

    def sleep(self):
        """Generic sleeping behavior."""
        self.energy += 20
        print(f"{self.name} sleeps and recovers energy. Energy: {self.energy}")

    def make_sound(self):
        """To be overridden by subclasses."""
        print(f"{self.name} makes a sound")

    def __str__(self):
        return f"{self.name} the {self.species}"


class Dog(Animal):
    """Dog class inheriting from Animal."""

    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
        self.tricks = []

    def make_sound(self):
        """Override parent method."""
        print(f"{self.name} barks: Woof! Woof!")

    def learn_trick(self, trick):
        """Dog-specific behavior."""
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}")

    def perform_trick(self):
        """Perform a random trick."""
        if self.tricks:
            trick = random.choice(self.tricks)
            print(f"{self.name} performs: {trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet")


class Cat(Animal):
    """Cat class inheriting from Animal."""

    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
        self.lives = 9

    def make_sound(self):
        """Override parent method."""
        print(f"{self.name} meows: Meow!")

    def climb(self):
        """Cat-specific behavior."""
        print(f"{self.name} climbs gracefully")


# Abstract Base Class Example
class Shape(ABC):
    """Abstract base class for shapes."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses."""
        pass

    def describe(self):
        """Describe the shape."""
        return f"This is a {self.name} with area {self.area():.2f}"


class Rectangle(Shape):
    """Rectangle implementation."""

    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle implementation."""

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        import math

        return math.pi * self.radius**2

    def perimeter(self):
        import math

        return 2 * math.pi * self.radius


# Magic Methods Example
class Vector2D:
    """2D vector with magic methods."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, int | float):
            return Vector2D(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5


# Polymorphism Example
def demonstrate_polymorphism():
    """Demonstrate polymorphism with different animals."""
    print("=== Polymorphism Demo ===")

    animals = [
        Dog("Buddy", "Golden Retriever"),
        Cat("Whiskers", "Orange"),
        Dog("Rex", "German Shepherd"),
    ]

    # Polymorphism: same method call works for all animal types
    for animal in animals:
        animal.make_sound()
        animal.eat("food")

        # Type-specific behavior
        if isinstance(animal, Dog):
            animal.learn_trick("sit")
            animal.perform_trick()
        elif isinstance(animal, Cat):
            animal.climb()

        print(f"{animal}\n")


def demonstrate_shapes():
    """Demonstrate abstract base classes and polymorphism."""
    print("=== Shape Polymorphism Demo ===")

    shapes = [Rectangle(5, 3), Circle(4), Rectangle(2, 8)]

    total_area = 0
    for shape in shapes:
        print(shape.describe())
        total_area += shape.area()

    print(f"Total area: {total_area:.2f}")


def demonstrate_banking():
    """Demonstrate the banking system."""
    print("=== Banking System Demo ===")

    # Create accounts
    account1 = BankAccount("Alice Johnson", 1000)
    account2 = BankAccount("Bob Wilson", 500)

    print(f"Created: {account1}")
    print(f"Created: {account2}")

    # Perform transactions
    account1.deposit(200)
    account1.withdraw(150)
    account2.deposit(100)

    # Show statements
    account1.get_statement()
    account2.get_statement()


def demonstrate_vectors():
    """Demonstrate magic methods with vectors."""
    print("=== Vector Magic Methods Demo ===")

    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"v1 + v2: {v1 + v2}")
    print(f"v1 * 2: {v1 * 2}")
    print(f"v1 == v2: {v1 == v2}")
    print(f"Magnitude of v1: {v1.magnitude():.2f}")


def main():
    """Run all demonstration functions."""
    demonstrate_banking()
    print("\n" + "=" * 50 + "\n")

    demonstrate_polymorphism()
    print("=" * 50 + "\n")

    demonstrate_shapes()
    print("\n" + "=" * 50 + "\n")

    demonstrate_vectors()


if __name__ == "__main__":
    main()
