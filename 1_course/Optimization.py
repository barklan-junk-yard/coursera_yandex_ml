import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.optimize as sp

def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)

x = np.linspace(1, 30, 100)
f1 = np.vectorize(f)
plt.plot(x, f1(x))
plt.show()

res11 = sp.minimize(f, 2, method="BFGS")
print("Res 11:", res11)

res12 = sp.minimize(f, 30, method="BFGS")
print("Res 12:", res12)

bounds = [(1, 30)]
res2 = sp.differential_evolution(f, bounds)
print("Res 2:", res2)


def h0(x):
    return int(f(x))
h = np.vectorize(h0)

res31 = sp.minimize(h, 30, method="BFGS")
print("Res 31:", res31)

bounds = [(1, 30)]
res32 = sp.differential_evolution(h, bounds)
print("Res 32:", res32)

# x = np.linspace(1, 30, 100)
# plt.plot(x, f(x))
# plt.show()

# res3 = sp.minimize(h, 30, method="BFGS")
# print(res3)