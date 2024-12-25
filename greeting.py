def greet(name):
    greetings = {
        "Alice": "Hello, Alice! Welcome back!",
        "Bob": "Hey Bob! How's it going?",
        "Charlie": "Hi Charlie! Nice to see you!",
    }
    return greetings.get(name, "Hello! Nice to meet you!")

# Example usage
names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    print(greet(name))
