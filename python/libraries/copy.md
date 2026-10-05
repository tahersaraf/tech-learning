## copy
In Python, the copy module provides the necessary functions to duplicate objects safely. 

It is critical to understand that standard assignment (=) does not copy objects at all; it merely creates a new reference (binding) to the existing object in memory.

To actually duplicate data and avoid unintended side effects, the Python copy module offers two main operations: `copy.copy()` (shallow copy) and` copy.deepcopy()` (deep copy). 

| Feature | Shallow Copy (copy.copy()) | Deep Copy (copy.deepcopy()) |
| --- | --- | --- |
| Definition | Copies the outermost object but inserts references to the original nested elements. | Recursively copies the object and all nested elements inside it.
| Nested Modifications | Changes to nested mutable elements will affect the original. | Changes to nested mutable elements will not affect the original.
| Memory Usage | Lower, because it reuses references for inner objects. | Higher, because it allocates new memory for every sub-object.
| Performance | Faster. | Slower due to recursive duplication.
Best Used For | Flat or immutable structures (e.g., lists of strings or integers). | Compound, nested mutable objects (e.g., list of lists, nested dicts).

## Shallow Copy 
A shallow copy creates a new container list, but the inner list elements point to the same memory addresses as the original.

```py
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)

# Modifying the outer structure does NOT affect the original
shallow_copied.append([7, 8, 9]) 

# Modifying a nested mutable element DOES affect the original
shallow_copied[0][0] = 'CHANGED'

print("Original:", original)
# Output: Original: [['CHANGED', 2, 3], [4, 5, 6]]

print("Shallow:", shallow_copied)
# Output: Shallow: [['CHANGED', 2, 3], [4, 5, 6], [7, 8, 9]]
```

## Deep Copy
A deep copy forces Python to walk through the entire structure recursively, making a separate and completely independent clone of every child object it encounters.

```py
import copy

original = [[1, 2, 3], [4, 5, 6]]
deep_copied = copy.deepcopy(original)

# Modifying a nested mutable element does NOT affect the original
deep_copied[0][0] = 'CHANGED'

print("Original:", original)
# Output: Original: [[1, 2, 3], [4, 5, 6]]

print("Deep Copy:", deep_copied)
# Output: Deep Copy: [['CHANGED', 2, 3], [4, 5, 6]]
```