## Lambda Functions
A lambda function is an anonymous, single-expression function defined with the lambda keyword instead of def. Because it has no name and no return statement, it is best suited for short throwaway operations - especially when passing a function as an argument to another function.

```py
lambda parameters: expression

add_ten = lambda a: a + 10

print(add_ten(5))   # 15
print(add_ten(22))  # 32
```

> Note: Assigning a lamda to a variable is useful for learning, but in production code a named `def` function is preferred because it supports docstrings and is easier to debug.

```py
# lambda function to convert dollars to euros

dollars_to_euros = lambda dollar_amount, conversion_rate=0.93: dollar_amount * conversion_rate

print(dollars_to_euros(10.0))
print(dollars_to_euros(10.0, 0.5))
```