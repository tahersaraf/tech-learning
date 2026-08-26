## What is a Python variable?
A variable is a named container used to store data values that points to an object in the computer's memory. Python has no command for declaring a variable; it is created the moment you first assign a value to it using the `=` operator.

## Rules for Naming Variables

Python identifiers must follow strict naming rules:
* __Allowed characters:__ Letters (`a-z`, `A-Z`), digits (`0-9`), and underscores (`_`).
* __No digit starts:__ A variable name cannot begin with a number.
* __Case-sensitive:__ age, Age, and AGE are three completely different variables.
* __Reserved keywords:__ You cannot use Python keywords like if, else, for, or class.
* __Naming convention:__ The official style guide recommends snake_case (e.g., user_age, total_price).

## Variable Assignment

You assign values using the = operator. Python also supports advanced assignment techniques:

```
# Basic assignment
x = 5
name = "Taher"

# Multiple variables, same value
a = b = c = 100

# Multiple variables, different values (Unpacking)
age, status = 25, "Active"

# Swapping two variables quickly without a temporary variable
x, y = y, x
```

## Dynamic Typing and Object References

Unlike languages like Java or C++, Python features dynamic typing.
* __No explicit declaration:__ You do not specify data types (like int or string).
* __Type shifting:__ A variable can change its type freely based on its current value.
* __Object references:__ Variables store pointers/references to objects in memory, not the actual values.
* __Type checking:__ Use the type() function to check a variable's data type.

```
x = 10        # x is an integer (int)
x = "Hello"   # x is now a string (str)
print(type(x)) # Output: <class 'str'>
```

## Variable Scope

Where you define a variable determines its visibility and lifetime within your program:
* __Local Scope:__ Variables created inside a function. They only exist within that function.
* __Global Scope:__ Variables created outside all functions. They can be accessed anywhere in the script.

## Deleting a Variable

If you need to remove a variable from memory entirely, use the `del` keyword. Trying to call the variable after deleting it triggers a `NameError`

```
score = 50
del score
print(score)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'score' is not defined
```