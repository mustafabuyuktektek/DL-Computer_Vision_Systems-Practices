import numpy as np

x = np.random.rand(3)
print(x)

w = np.random.rand(3)
b = np.random.randn(1)
print(w)
print(b)
y_true=1
lr=0.1


def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for epoch in range(100):
    z = np.dot(x, w) + b

    print(sigmoid(z))
    tahmin=sigmoid(z)

    hata=tahmin-y_true

    turev = tahmin * (1 - tahmin)
    dz=hata*turev
    dw = x * dz
    db = dz
    w = w - (lr * dw)
    b = b - (lr * db)
    print(f"Epoch: {epoch}, Hata: {hata}")