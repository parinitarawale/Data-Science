!pip install numpy 

import numpy as np

print(np.array([1, 2, 3]))

print(np.array([[1, 2], [3, 4]]))

print(np.zeros((2, 3)))

print(np.ones((3, 3)))

print(np.arange(0, 10, 2))

print(np.linspace(0, 1, 5))

print(np.eye(3))

print(np.array([1, 2, 3, 4]).reshape(2, 2))

print(np.array([[1, 2], [3, 4]]).T)

print(np.array([[1, 2], [3, 4]]).flatten())

######

import random from nupmy

print(np.random.randint(0, 10))

print(np.random.rand())

print(np.random.randn())

print(np.random.randint(1, 100, size=(3, 3)))

np.random.seed(42)

arr = np.array([1, 2, 3, 4]); np.random.shuffle(arr); print(arr)

print(np.random.choice([10, 20, 30, 40]))

print(np.random.uniform(0, 1, 5))

print(np.random.normal(loc=0, scale=1, size=5))

######

print(np.frompyfunc(lambda x: x**2, 1, 1)([1, 2, 3]))

print(np.add([1, 2], [3, 4]))

print(np.floor([1.9, 2.1, 3.7]))

print(np.log10([1, 10, 100]))

print(np.sum([1, 2, 3, 4]))

print(np.cumsum([1, 2, 3, 4]))

print(np.prod([1, 2, 3, 4]))

print(np.cumprod([1, 2, 3, 4]))

print(np.diff([1, 3, 6, 10]))

print(np.lcm.reduce([4, 6, 8]))

print(np.gcd.reduce([8, 16, 24]))

print(np.sin(np.pi / 2))

print(np.tanh(1))

print(np.intersect1d([1, 2, 3], [2, 3, 4]))
