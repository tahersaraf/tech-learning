## JSON in Python

Python has a built-in package called `json`, which can be used to work with JSON data.


Convert from JSON to Python:
```
#importing the json package
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(type(y))
print(len(y))
print(y)

# <class 'dict'>
# 3
# {'name': 'John', 'age': 30, 'city': 'New York'}
```

Convert from Python to JSON:
```
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
```

You can convert Python objects of the following types, into JSON strings:

* dict
* list
* tuple
* string
* int
* float
* True
* False
* None

When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent.

```
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
```

The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The json.dumps() method has parameters to make it easier to read the result:

```
json.dumps(x, indent=4)
```

The json.dumps() method has parameters to order the keys in the result:

```
json.dumps(x, indent=4, sort_keys=True)
```

You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

```
json.dumps(x, indent=4, separators=(". ", " = ")
```