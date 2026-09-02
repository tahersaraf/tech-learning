## Tuples

Tuples, like lists, are used to store multiple items in a single variable.

Tuples are written with round brackets or without the parentheses

```
thistuple1 = ("apple", "banana", "cherry")
print(thistuple)

thistuple2 = "apple", "banana", "cherry"
print(thistuple)

# Both ways are valid ways of creating a tuple
```

Tuple items are __ordered__, <ins>__unchangeable__</ins>, and _allow duplicate values_.

Just like lists, tuple items are indexed, the first item has index `[0]`, the second item has index `[1]` etc.

To determine how many items a tuple has, use the `len()` function

To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

```
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
```

To create an empty tuple, use round brackets with no content.

```
thistuple = ()
print(type(thistuple))
```

Tuple items can be of any data type AND can contain different data types

It is also possible to use the tuple() constructor to make a tuple.

```
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
```

You can access tuple items by referring to the index number, inside square brackets

```
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[1]) # banana
print(thistuple[-1]) # mango
print(thistuple[2:5]) # ("cherry", "orange", "kiwi")
```

## Check if Item Exists - `in` keyword

To determine if a specified item is present in a tuple or list use the `in` keyword:

```
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


thislist = ("china","india","russia")
if "india" in thislist:
  print("Yes, India is in this list")
```

## Unchangeable (Immutable)

Tuples are unchangeable, meaning that you cannot change, add, or remove items once the `tuple` is created.

But there are some workarounds; You can convert the tuple into a `list`, change the `list`, and convert the `list` back into a `tuple`.

```
x = ("apple", "banana", "cherry")
y = list(x)     # ["apple","banana","cherry] 
y[1] = "kiwi"   # ["apple","kiwi","cherry"]
x = tuple(y)    # ("apple","kiwi","cherry")

print(x)        # ("apple","kiwi","cherry")
```

The `del` keyword can delete the tuple completely

```
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) 
# NameError: name 'thistuple' is not defined
```

## Unpacking a Tuple

When we create a tuple, we normally assign values to it. This is called "packing" a tuple. 

But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"

```
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)    # apple
print(yellow)   # banana
print(red)      # cherry
```

The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

```
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)    # apple
print(yellow)   # banana
print(red)      # ['cherry', 'strawberry', 'raspberry']
```

If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

```
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)    # apple
print(tropic)   # ['mango', 'papaya', 'pineapple']
print(red)      # cherry
```