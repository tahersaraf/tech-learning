## Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

>As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
```

Dictionary items are ordered, changeable, and do not allow duplicates.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

It is also possible to use the `dict()` constructor to make a dictionary.

```py
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# {'name': 'John', 'age': 36, 'country': 'Norway'}
```

You can access the items of a dictionary by referring to its key name, inside square brackets:

There is also a method called `get()` that will give you the same result:

```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]
x = thisdict.get("model")
```

The `keys()` method will return a list of all the keys in the dictionary.

```py
x = thisdict.keys()

print(x)

# dict_keys(['brand', 'model', 'year'])
```
The `values()` method will return a list of all the values in the dictionary.

```py
x = thisdict.values()

print(x)

# dict_values(['Ford', 'Mustang', 1964])
```

The `items()` method will return each item in a dictionary, as tuples in a list.

```py
x = thisdict.items()

print(x)

# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
```

Adding an item to the dictionary is done by using a new index key and assigning a value to it:

The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs.

```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)
```

The `pop()` method removes the item with the specified key name:

```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# {'brand': 'Ford', 'year': 1964}
```

The `popitem()` method removes the last inserted item (in versions before 3.7, a random item is removed instead):

```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
```

The `del` keyword removes the item with the specified key name:

```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
```

The `del` keyword can also delete the dictionary completely: