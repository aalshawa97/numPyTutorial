#Abdullah Mutaz Alshawa
#6/28/23
import numpy as np
import sys

a = np.array([1, 2, 3], dtype='int8')
b = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print('NumPy library array of type int8')
#Print matrix
print(a)
#Print matrix
print(b)
#Get dimension
print("Dimension", a.ndim)
#Get dimension
print("Dimension", b.ndim)
#Get shape
print(a.shape)
#Get shape
print(b.shape)
#Get total size
print(a.size * a.itemsize)
#Get total size
print(b.size * b.itemsize)
#Get type/size
print("Type", a.dtype, "Size", a.itemsize, "bytes")
#Get type/size
print("Type", b.dtype, "Size", b.itemsize, "bytes")
#Get dimension
print("Dimension", a.ndim)
#Get dimension
print("Dimension", b.ndim)
#Get a specific element
print("Get specific element", b[0,0])
#Get a specific row
print("Get specific column", b[0, :])
#Get a specific column
print("Get specific column", b[:,0])
#print(np.zeros)
#Get bytes
#print("Bytes", a.bytes)
#Get bytes
#print("Bytes", b.bytes)
