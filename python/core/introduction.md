## Python Introdution

Python is a high-level, interpreted programming language known for its simple syntax and excellent readability. It is one of the most popular languages globally, used heavily in data science, artificial intelligence, web development, and automation.

Unlike languages like C++ or Java, Python does not require semicolons to end statements. Instead, it uses whitespace indentation to define blocks of code.

## Your First Program

To display text on the screen, use the built-in print() function:

```py
# This is a comment (ignored by the computer)
print("Hello, World!")
```

In larger programs, it is a standard convention to organize code inside functions. A main() function serves as the central entry point of the script.

```py
def greet_user(name):
    """This function takes a name and returns a greeting string."""
    return f"Hello, {name}! Welcome to Python."

def main():
    # Program starts here
    user_name = "Alice"
    
    # Call the helper function and store the result
    greeting_message = greet_user(user_name)
    
    # Print the result to the console
    print(greeting_message)

# Standard boilerplate to execute main()
if __name__ == "__main__":
    main()
```

The block if __name__ == "__main__": ensures that the main() function only runs when the script is executed directly (rather than imported into another file).


## Common Basic Data Types

| Data Type | Description | Example |
|---|---|---|
| Integer (int) | Whole numbers without decimals. | `score = 95`
| Float (float) | Numbers containing a decimal point.| `pi = 3.1415`
| String (str) | Text wrapped in single, double, or triple quotes. | `msg = "Hi!"`
| Boolean (bool) | Logical values: case-sensitive True or False. | `is_logged = True`