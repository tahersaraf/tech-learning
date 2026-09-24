## List 

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

```py
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

List items are __ordered__, __changeable__, and __allow duplicate__ __values__.

List items are indexed, the first item has index `[0]`, the second item has index `[1]` etc.

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

To determine how many items a list has, use the `len()` function:

```py
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # 3
```

List items can be of any data type:

```py
list1 = ["abc", 34, True, 40, "male"]
```

It is also possible to use the `list()` constructor when creating a new list.

```py
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
```

List items are indexed and you can access them by referring to the index number:

```py
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # banana
print(thislist[-1]) # cherry
```

`-1` refers to the last item, `-2` refers to the second last item etc.


You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

```py
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# ["cherry", "orange", "kiwi"]
```
Note: The search will start at index 2 (included) and end at index 5 (not included).

By leaving out the start value, the range will start at the first item:

```py
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# ["apple", "banana", "cherry", "orange"]
```

By leaving out the end value, the range will go on to the end of the list:

```py
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
```

## Add/Remove/Change List Items

To change the value of a specific item, refer to the index number:

```py
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # ['apple', 'blackcurrant', 'cherry']
```

You can also change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

```py
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) 

# ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
```

If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

```py
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # ['apple', 'watermelon']
```

## `append()`

To add an item to the end of the list, use the `append()` method:

```py
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ["apple", "banana", "cherry", "orange"]
```

## `insert()`

To insert a list item at a specified index, use the `insert()` method.

The `insert()` method inserts an item at the specified index:

```py
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # ['apple', 'orange', 'banana', 'cherry']
```

## `extend()`

To append elements from another list to the current list, use the `extend()` method.

```py
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

The `extend()` method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

## `remove()`

The `remove()` method removes the specified item.

```py
thislist = ["apple", "banana", "cherry"]4
thislist.remove("banana")
print(thislist) # ['apple', 'cherry']
```

If there are more than one item with the specified value, the `remove()` method removes the first occurrence:

```py
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry', 'banana', 'kiwi']
```

The `pop()` method removes the specified index.

```py
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # ['apple', 'cherry']
```

If you do not specify the index, the `pop()` method removes the last item.

The `del` keyword also removes the specified index:

The `del` keyword can also delete the list completely.

```py
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # ['banana', 'cherry']

del thislist
print(thislist) # NameError: name 'thislist' is not defined
```