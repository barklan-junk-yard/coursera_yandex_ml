import numpy as np
import math
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x / 5.) * np.exp(x / 10.) + 5 * np.exp(-x / 2.)


# approximate at the given points (feel free to experiment: change/add/remove)
points = np.array([1, 4, 10, 15])
n = points.size


# fill A-matrix, each row is 1 or xi^0, xi^1, xi^2, xi^3 .. xi^n
A = np.zeros((n, n))
for index in range(0, n):
    A[index] = np.power(np.full(n, points[index]), np.arange(0, n, 1))


# fill b-matrix, i.e. function value at the given points
b = f(points)


# solve to get approximation polynomial coefficents
solve = np.linalg.solve(A,b)
print(solve)


# define the polynome approximation of the function
def polinom(x): 
    # Yi = solve * Xi where Xi = x^i
    tiles = np.tile(x, (n, 1))
    tiles[0] = np.ones(x.size)
    for index in range(1, n):
        tiles[index] = tiles[index]**index
    return solve.dot(tiles)


# plot the graphs of original function and its approximation
x = np.linspace(1, 15, 100)
plt.plot(x, f(x))
plt.plot(x, polinom(x))
plt.show()

# print out the coefficients of polynome approximating our function
print(solve)