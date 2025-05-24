"""
Control flow examples for the Python tutorial
"""


def grade_calculator_demo():
    """Demonstrate conditional statements with grade calculation."""
    print("=== Grade Calculator Demo ===")

    scores = [85, 92, 78, 96, 88]
    print(f"Scores: {scores}")

    average = sum(scores) / len(scores)
    print(f"Average: {average:.1f}")

    # Determine letter grade
    if average >= 90:
        grade = "A"
        message = "Excellent work!"
    elif average >= 80:
        grade = "B"
        message = "Good job!"
    elif average >= 70:
        grade = "C"
        message = "Keep working!"
    elif average >= 60:
        grade = "D"
        message = "Need improvement"
    else:
        grade = "F"
        message = "Must retake"

    print(f"Grade: {grade}")
    print(f"Message: {message}")


def loop_examples():
    """Demonstrate different types of loops."""
    print("\n=== Loop Examples ===")

    # For loop with list
    fruits = ["apple", "banana", "cherry"]
    print("Fruits:")
    for fruit in fruits:
        print(f"  - {fruit}")

    # For loop with range
    print("\nCounting to 5:")
    for i in range(1, 6):
        print(f"  {i}")

    # While loop
    print("\nCountdown:")
    count = 5
    while count > 0:
        print(f"  {count}")
        count -= 1
    print("  Blast off!")

    # Enumerate example
    print("\nNumbered fruits:")
    for index, fruit in enumerate(fruits, 1):
        print(f"  {index}. {fruit}")


def fizzbuzz_demo():
    """Classic FizzBuzz implementation."""
    print("\n=== FizzBuzz Demo ===")

    for i in range(1, 21):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def number_classifier():
    """Classify numbers as positive, negative, or zero."""
    print("\n=== Number Classifier ===")

    numbers = [5, -3, 0, 12, -7, 0, 8, -1]
    positive = []
    negative = []
    zeros = []

    for num in numbers:
        if num > 0:
            positive.append(num)
        elif num < 0:
            negative.append(num)
        else:
            zeros.append(num)

    print(f"Original: {numbers}")
    print(f"Positive: {positive}")
    print(f"Negative: {negative}")
    print(f"Zeros: {zeros}")


def prime_checker():
    """Find prime numbers up to a given limit."""
    print("\n=== Prime Number Finder ===")

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    limit = 30
    primes = []

    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)

    print(f"Prime numbers up to {limit}:")
    print(primes)


def pattern_printer():
    """Print various patterns using loops."""
    print("\n=== Pattern Printer ===")

    # Triangle pattern
    height = 5
    print("Triangle pattern:")
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    # Number pyramid
    print("\nNumber pyramid:")
    for i in range(1, 6):
        # Leading spaces
        print(" " * (5 - i), end="")
        # Ascending numbers
        for j in range(1, i + 1):
            print(j, end="")
        # Descending numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()


def password_validator():
    """Validate password strength."""
    print("\n=== Password Validator ===")

    def validate_password(password):
        if len(password) < 8:
            return False, "Password must be at least 8 characters"

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        special_chars = "!@#$%^&*"

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in special_chars:
                has_special = True

        requirements = []
        if not has_upper:
            requirements.append("uppercase letter")
        if not has_lower:
            requirements.append("lowercase letter")
        if not has_digit:
            requirements.append("digit")
        if not has_special:
            requirements.append("special character")

        if requirements:
            return False, f"Missing: {', '.join(requirements)}"
        else:
            return True, "Strong password!"

    test_passwords = ["weak", "StrongPass1!", "NoSpecial123", "short"]

    for pwd in test_passwords:
        is_valid, message = validate_password(pwd)
        status = "✓" if is_valid else "✗"
        print(f"{status} '{pwd}': {message}")


def main():
    """Run all demonstration functions."""
    grade_calculator_demo()
    loop_examples()
    fizzbuzz_demo()
    number_classifier()
    prime_checker()
    pattern_printer()
    password_validator()


if __name__ == "__main__":
    main()
