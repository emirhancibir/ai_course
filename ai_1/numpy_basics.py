# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 14:48:46 2022

@author: emirh
"""
# %%
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
arr = arr.reshape(3, 5)
print(arr.shape)
print("dimension : ", arr.ndim)
print("dtype : ", arr.dtype.name)
print("size : ", arr.size)

zeros = np.zeros((3, 4))
zeros[0, 3] = 31
print(zeros)

ar = np.arange(10, 50, 5)  # output -> array([10, 15, 20, 25, 30, 35, 40, 45])

a = np.linspace(10, 50, 20)
""" array([10.        , 12.10526316, 14.21052632, 16.31578947, 18.42105263,
       20.52631579, 22.63157895, 24.73684211, 26.84210526, 28.94736842,
       31.05263158, 33.15789474, 35.26315789, 37.36842105, 39.47368421,
       41.57894737, 43.68421053, 45.78947368, 47.89473684, 50.        ])
"""
# %%

# %%

a = np.array([[1, 2, 3], [5, 7, 9], [11, 13, 29]])
b = np.array([[4, 5], [5, 6], [3, 31]])

print(np.sin(a))
print(a < 2)
# matrix product
res = a.dot(b)  # A x B(transpose)
"""array([[  23,  110],
       [  82,  346],
       [ 196, 1032]])"""


a = np.random.random((5, 5))
a.sum()
res = a.sum(axis=0)

# %%

# %%

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[0:3])
reverse_arr = arr[::-1]
print(reverse_arr)

# %%

# %%
# shape manipulation

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr)
a = arr.ravel()
print(a)

print("------------")
arr2 = a.reshape(3, 3)
print(arr2)
print("------------")

arr3 = np.array([[1, 2], [3, 4], [5, 6]])

# arr3.reshape(2,3)
print("reshaped matrix")
print(arr3)
print("resized matrix")
arr3.resize((6, 1))
print(arr3)
# %%

# %%
# stacking array

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[-1, -2], [-3, -4]])

"""   
    vertical stacking
     [[1, 2],
       [3, 4]]
        [[-1, -2],
       [-3, -4]]

"""
arr3 = np.vstack((arr1, arr2))
"""
      [[ 1,  2],
       [ 3,  4],
       [-1, -2],
       [-3, -4]]
"""
arr4 = np.hstack((arr1, arr2))
"""
        [[ 1,  2, -1, -2],
       [ 3,  4, -3, -4]]
"""
# %%

# %%
# converting and coping array

liste = [1, 2, 3, 4]
arr = np.array(liste)

liste2 = list(arr)

a = np.array([1, 2, 3])
b = a
c = a
b[0] = 3 # a[0] = b[0] = c[0] = 3

d = a.copy()
d[0] = 16
# %%
