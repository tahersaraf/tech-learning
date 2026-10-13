### What is PyPI

When python is installed, it includes a standard set of utilities called the Python Standard Library. Beyond that, developers can publish their own libraries for the Python community through PyPI - the Python Package Index.

PyPI is the central repository where developers upload and share libraries, and where users download them. It contains thousands of packages covering a wide range of use cases - many of which have become industry standards. 

### How to import a library

```py
import numpy
```

### Using a library

```py
import numpy

numpy.sqrt(4.0)

# Output:
# np.float64(2.0)
```

### Using an alias

You can assign a shorter alias to a library at import time using the `as` keyword. This reduces typing when calling library functions repeatedly.

```py
import numpy as np

np.sqrt(4.0)

# Output:
# np.float64(2.0)
```

### Importing Specific Functions

You can import a single function directly from a library using `from ... import` syntax. This brings the function into the local namespace so you can call it without the library prefix


```py
from numpy import sqrt

sqrt(4.0)
```