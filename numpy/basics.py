# https://numpy.org/doc/stable/ (Documentation)

# Why Numpy: 50x faster than traditional Python lists.

# NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++

# https://github.com/numpy/numpy
import numpy as np

a = np.arange(15).reshape(3, 5)

# [[],[],[]]

print(a)
print(a.ndim)
print(a.dtype)

print(type(a))


print("VERSION NP: ", np.__version__)

# We create an array
arr = np.array([1, 2, 3, 4, 5])

print(arr)

#arr = np.array([1, 2, 3, 4], ndmin=3)
#print(arr)


print('number of dimensions :', arr.ndim)
print(arr.dtype)

# Numpy RANDOM
x = np.random.randint(100, size=(3, 5))
y = np.random.choice([3, 5, 7, 9], size=(3, 5))

# print(x)
# print(y)


print(np.random.permutation(arr))

# pip install seaborn
# https://www.superprof.es/apuntes/escolar/matematicas/estadistica/descriptiva/histograma.html
# https://seaborn.pydata.org/
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

import seaborn as sns
import matplotlib.pyplot as plt

sns.displot([1, 2, 3, 4, 5])
plt.show()
