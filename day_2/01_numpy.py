import numpy as np

# 1d array
array = np.array([2, 4, 5, 6, 8, 7])
print(array)

# 2d array
my_array = np.array([[23, 43], [234, 456]])
print(my_array)

# More memory efficient than lists
# Can only have one data type

new_array = array * 10
print(new_array)

# Numpy methods
print(f"Mean: {np.mean(array)}")

print(f"Sum: {np.sum(array)}")

print(f"Maximum numner: {np.max(array)}")

print(f"Minimum number: {np.min(array)}")

# Indexing
a = np.array([1, 2, 3, 4, 6])
print(a[0])

# Slicing
print(a[0:2])
print(a[:-3])