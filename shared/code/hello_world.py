"""
Simple Hello World example for Python tutorial
"""


def greet(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def main():
    """Main function to demonstrate basic Python."""
    # Basic greeting
    message = greet()
    print(message)

    # Custom greeting
    custom_message = greet("Python Learner")
    print(custom_message)

    # Multiple greetings
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        print(greet(name))


if __name__ == "__main__":
    main()
