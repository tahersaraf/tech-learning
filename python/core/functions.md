## What is a function ?
A function is a reusable block of code that executes only when called, allowing you to organize code and avoid repetition.

To create a function, use the `def` keyword, followed by a unique name, parentheses, and a colon. The function body must be indented.

```
# Defining a function
def greet_user():
    print("Hello! Welcome back.")

# Calling the function
greet_user()
```
### Arguments vs Parameters
```
def greet_person(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet_person("Alice")   # "Alice" is an argument
```

## `return`
Functions use the `return` keyword to send data back to the caller. If no return statement is specified, the function automatically returns `None`.

```
def add_numbers(a, b):
    return a + b  # Exits the function and outputs the sum

result = add_numbers(5, 7)
print(result)  # Outputs: 12
```

### Built-in vs. User-Defined Functions

1. __Built-in Functions:__ Standard functions always available in Python, such as `print()`, `len()`, `max()`, and `type()`. Built-in functions are written in C (for CPython), making them highly optimized and extremely fast.
2. __User-Defined Functions:__ Custom blocks created by programmers to fulfill specific tasks.

### Naming Collisions
Because built-in functions are always accessible, you must avoid naming your user-defined functions (or variables) after them. Doing so overwrites (shadows) the built-in behavior.

```
# BAD PRACTICE: Overwriting a built-in
def sum(a, b):
    return a + b

# The built-in sum() that takes a list no longer works here!
# numbers = [1, 2, 3]
# print(sum(numbers)) -> This will now crash with a TypeError!
```