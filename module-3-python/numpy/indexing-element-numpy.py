import numpy as np
# Create a 2-dimensional array (matrix)
result = np.array([1,2,3,4,5,6])
# access indexing element
print(result[0])  # Output: 1
print(result[1])  # Output: 2
print(result[2])  # Output: 3
print(result[3])  # Output: 4
print(result[4])  # Output: 5
print(result[5])  # Output: 6

print(result[1] + result[4])  # Output: 7 (2 + 5)
print(result[0] * result[5])  # Output: 6 (1 * 6)
print(result[2] - result[3])  # Output: -1 (3 - 4)

# slicing
print(result[1:4])  # Output: [2 3 4]
print(result[:3])   # Output: [1 2 3]
print(result[3:])   # Output: [4 5 6]

#reverse slicing
print(result[::-1])  # Output: [6 5 4 3 2 1]

# concatenation
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))
print(concatenated)  # Output: [1 2 3 4 5 6]

# reshaping
reshaped = concatenated.reshape(2, 3)
print(reshaped)  # Output: [[1 2 3]
                 #          [4 5 6]]

# multplications
print(arr1 * arr2)  # Output: [4 10 18] (element-wise multiplication)

# dot product
dot_product = np.dot(arr1, arr2)
print(dot_product)  # Output: 32 (1*4 + 2*5 + 3*6)

# inserting element
arr1 = np.insert(arr1, 1, 10)  # Insert 10 at index 1
print(arr1)  # Output: [ 1 10  2  3]

# deleting element
arr1 = np.delete(arr1, 2)  # Delete element at index 2
print(arr1)  # Output: [ 1 10  3]

# appending element
arr1 = np.append(arr1, 20)  # Append 20 to the end
print(arr1)  # Output: [ 1 10  3 20]

# update element
arr1[0] = 5  # Update element at index 0 to 5
print(arr1)  # Output: [ 5 10  3 20]

# slicing with step
print(result[0:6:2])  # Output: [1 3 5] (every 2nd element from index 0 to 5)

# boolean indexing
bool_index = result > 3
print(result[bool_index])  # Output: [4 5 6] (elements greater than 3)





