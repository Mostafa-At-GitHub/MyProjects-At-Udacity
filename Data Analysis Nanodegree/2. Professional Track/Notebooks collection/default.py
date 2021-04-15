import time
import numpy as np
import pandas as pd

X = np.random.randint(1,20, size=(50,5))
print("Shape of X is: ", X.shape)
# Create a rank 1 ndarray that contains a randomly chosen 10 values between `0` to `len(X)` (50)
# The row_indices would represent the indices of rows of X
row_indices = np.random.randint(0,50, size=10)
print("Random 10 indices are: ", row_indices)
# To Do 1 - Print those rows of X whose indices are represented by entire row_indices ndarray
# Hint - Use the row_indices ndarray to select specified rows of X
X_subset = X[row_indices, :]
print(X_subset)

# To Do 2 - Print those rows of X whose indices are present in row_indices[4:8]
X_subset = X[row_indices[4:8], :]
print(X_subset)


"""
# Press the green button in the gutter to run the script.
s=time.time()
# We create a rank 1 ndarray of floats but set the dtype to int64
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)
# create numpy array of letters a-j
letter_array = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],dtype=str)
print("Array:", letter_array)

# get dtype of array
print("Dtype:", letter_array.dtype)

# get shape of array
print("Shape:", letter_array.shape)

# get size of array
print("Size:", letter_array.size)
""""""
print (s)
i, j, k = 0, 1, 2
i, j, k = i + 1, j + 1, k + 1
x = np.array([1, 2, 3, 4, 5])
x.shape
def max(numbers):
    max_num=-1
    for i in range(0,len(numbers)):
        if numbers[i]>max_num:
            max_num= numbers[i]
    return max_num
print()
print(max([6,7,0,2,4]))
""""""
X = np.random.randint(4,15,size=(3,2))
# We create a 3 x 3 rank 2 ndarray that contains integers from 1 to 9
X = np.array([[1,2,3],[4,5,6],[7,8,9]])
w=np.delete(x,[])
"""