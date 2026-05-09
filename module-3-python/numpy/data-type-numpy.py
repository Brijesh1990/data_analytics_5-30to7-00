# int
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5], dtype=int)
# print(arr)  # Output: [1 2 3 4 5]
# print(arr.dtype)  # Output: int64 (or int32 depending on the system)


# float

# import numpy as np
# arr = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=float)
# print(arr)  # Output: [1. 2. 3. 4. 5.]
# print(arr.dtype)  # Output: float64 (or float32 depending on the system)


#string

import numpy as np
arr = np.array(['apple', 'banana', 'cherry'], dtype=str)
print(arr)  # Output: ['apple' 'banana' 'cherry']
print(arr.dtype)  # Output: <U6 (or <U7 depending on the longest string length)

# boolean

import numpy as np
arr = np.array([True, False, True, False], dtype=bool)
print(arr)  # Output: [ True False  True False]
print(arr.dtype)  # Output: bool


# complex
import numpy as np
arr = np.array([1 + 2j, 3 + 4j, 5 + 6j], dtype=complex)
print(arr)  # Output: [1.+2.j 3.+4.j 5.+6.j]
print(arr.dtype)  # Output: complex128 (or complex64 depending on the system)

# object
import numpy as np
arr = np.array([1, 'apple', 3.14, True], dtype=object)
print(arr)  # Output: [1 'apple' 3.14 True] 
print(arr.dtype)  # Output: object


# structured array
import numpy as np
dtype = [('name', 'U10'), ('age', 'i4'), ('height', 'f4')]
arr = np.array([('Alice', 25, 5.5), ('Bob', 30, 6.0)], dtype=dtype)
print(arr)  # Output: [('Alice', 25, 5.5) ('Bob', 30, 6.)]
print(arr.dtype)  # Output: [('name', '<U10'), ('age', '<i4'), ('height', '<f4')]