"""
Basic Python examples for the tutorial
"""

def demonstrate_variables():
    """Show different variable types and operations."""
    print("=== Variable Examples ===")
    
    # Basic types
    name = "Python"
    version = 3.12
    is_awesome = True
    
    print(f"Language: {name}")
    print(f"Version: {version}")
    print(f"Awesome: {is_awesome}")
    
    # Type checking
    print(f"Type of name: {type(name)}")
    print(f"Type of version: {type(version)}")
    print(f"Type of is_awesome: {type(is_awesome)}")


def demonstrate_strings():
    """Show string operations and formatting."""
    print("\n=== String Examples ===")
    
    text = "Python Programming"
    
    # String methods
    print(f"Original: {text}")
    print(f"Upper: {text.upper()}")
    print(f"Lower: {text.lower()}")
    print(f"Length: {len(text)}")
    print(f"Contains 'Python': {'Python' in text}")
    
    # String slicing
    print(f"First 6 chars: {text[:6]}")
    print(f"Last word: {text[7:]}")
    print(f"Reverse: {text[::-1]}")


def demonstrate_math():
    """Show mathematical operations."""
    print("\n=== Math Examples ===")
    
    a, b = 10, 3
    
    print(f"a = {a}, b = {b}")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b:.2f}")
    print(f"Floor division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Power: {a} ** {b} = {a ** b}")


def demonstrate_formatting():
    """Show different formatting techniques."""
    print("\n=== Formatting Examples ===")
    
    name = "Alice"
    age = 25
    height = 5.75
    
    # f-strings (recommended)
    print(f"Name: {name}, Age: {age}, Height: {height:.1f}ft")
    
    # .format() method
    print("Name: {}, Age: {}, Height: {:.1f}ft".format(name, age, height))
    
    # % formatting (older style)
    print("Name: %s, Age: %d, Height: %.1fft" % (name, age, height))
    
    # Number formatting
    import math
    pi = math.pi
    print(f"Pi: {pi:.2f}")
    print(f"Pi (scientific): {pi:.2e}")
    print(f"Padded number: {42:05d}")


def main():
    """Run all demonstration functions."""
    demonstrate_variables()
    demonstrate_strings()
    demonstrate_math()
    demonstrate_formatting()


if __name__ == "__main__":
    main()