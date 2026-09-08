## Input/Output (I/O)

Input/Output (I/O) allows your program to interact with users, while Typecasting ensures that the data you receive or send is in the correct format for calculations and logic

## Standard Input: `input()`

The `input()` function pauses your program and waits for the user to type something into the terminal.
* __The Golden Rule:__ The `input()` function always returns the data as a string (`str`), even if the user types a number like `42` or `9.99`.

## Standard Output: `print()`

The `print()` function sends data to the console so the user can see it. You can pass multiple items separated by commas, and Python will automatically space them out.

Python offers multiple ways to format output strings. Below are all major approaches, with heavy focus on F-Strings (the modern standard) and the `.format()` method

### The .format() Method

#### 1. Positional Placeholders

```py
print("My name is {} and I am {}.".format("John", 25))

```

#### 2. Index-Based Placeholders

```py
print("{0} love {1}. {1} love {0}.".format("I", "you"))
# Output: I love you. you love I.

```

#### 3. Keyword/Named Placeholders

```py
print("The {item} costs {price}.".format(item="book", price=12.99))

```

#### 4. Formatting Modifiers with .format()

```py
print("Price: {:.2f}".format(19.999)) # Output: Price: 20.00

```

### F-Strings (Formatted String Literals)

#### 1. Basic Variable & Expression Substitution

```py
x, y = 10, 5
print(f"The sum of {x} and {y} is {x + y}")

# Output: The sum of 10 and 5 is 15
```

#### 2. Float Decimal Precision (:.Nf)

```py
pi = 3.14159265
print(f"Pi rounded: {pi:.2f}")

# Output: Pi rounded: 3.14
```

#### 3. Thousands Separators (:, or :_)

```py
money = 1000000
print(f"Balance: ${money:,}")  # Balance: $1,000,000
print(f"Balance: ${money:_}")  # Balance: $1_000_000
```

#### 4. Padding and Alignment (:<, :>, :^)

* `<` : Left align
* `>` : Right align
* `^` : Center align

```py
text = "test"
print(f"{text:>10}") # Output: '      test' (Right aligned in a 10-character block)
print(f"{text:^10}") # Output: '   test   ' (Centered in a 10-character block)

```

#### 5. Percentage Formatting (:.N%)

```py
percentage = 0.756
print(f"Accuracy: {percentage:.1%}")
# Output: Accuracy: 75.6%
```