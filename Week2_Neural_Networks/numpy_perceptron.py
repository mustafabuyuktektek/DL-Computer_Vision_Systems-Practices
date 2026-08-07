import numpy as np

x = np.random.rand(3)
print(x)

w = np.random.rand(3)
b = np.random.randn(1)
print(w)
print(b)

z = np.dot(x, w) + b
print(z)

def sigmoid(z):
    return 1 / (1+np.exp(-z))

print(sigmoid(z))