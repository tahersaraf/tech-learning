## Sets
Sets are used to store multiple items in a single variable.

A set is a collection which is unordered, unchangeable*, and unindexed.

> * Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.

```py
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))

# {'banana', 'cherry', 'apple'}
# <class 'set'>
```

> Note: Sets are unordered, so you cannot be sure in which order the items will appear.

Set items are unordered, unchangeable, and do not allow duplicate values.

Sets cannot have two items with the same value.

```py
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# {"apple", "banana", "cherry"}
```

> Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

> Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

```py
thisset = {"apple", "banana", "cherry", True, 1, 2, False, True, 0}
print(thisset)

# {False, True, 2, 'cherry', 'apple', 'banana'}
```

It is also possible to use the set() constructor to make a set.

```py
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# {'banana', 'cherry', 'apple'}
```

You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a `for` loop, or ask if a specified value is present in a set, by using the `in` keyword.

```py
thisset = {"apple", "banana", "cherry", "orange"}

if "apple" in thisset:
    print("Apple is in this set")
```

Once a set is created, you cannot change its items, but you can add new items.

To add one item to a set use the `add()` method.

```py
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# {"apple", "banana", "cherry", "orange"}
```

To add items from another set into the current set, use the `update()` method.

```py
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# {'banana', 'apple', 'papaya', 'mango', 'cherry', 'pineapple'}
```

The object in the `update()` method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

To remove an item in a set, use the `remove()`, or the `discard()` method.

```py
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
```

> Note: If the item to remove does not exist, `remove()` will raise an error.

> Note: If the item to remove does not exist, `discard()` will __NOT__ raise an error.

## Python frozenset

`frozenset` is an immutable version of a set.

Like sets, it contains unique, unordered, unchangeable elements.

Unlike sets, elements cannot be added or removed from a frozenset.

Use the `frozenset()` constructor to create a frozenset from any iterable.

```py
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# frozenset({'cherry', 'apple', 'banana'})
# <class 'frozenset'>
```