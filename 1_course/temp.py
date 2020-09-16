import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
import time
import random

size = 90
# start = time.time()  # начало замера
# end = time.time()  # конец замера
# print(end-start)

def insertion(data):
	for i in range(len(data)):
		j = i - 1
		key = data[i]
		while data[j] > key and j >= 0:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = key

def somesort(a):
	for j in range(1, len(a)):
		for i in range(j, -1, -1):
			if i != 0:
				if a[i] < a[i-1]:
					a[i],a[i-1] = a[i-1],a[i]

def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)



kolmas = 10
arr = []
arrlen = []
while kolmas != 0:
    kolmas -= 1
    temp = list(np.random.randint(-50, 50, size * (1 + kolmas)))
    arr.insert(0, temp)
    arrlen.insert(0, len(temp))


# x = np.arange(-50, 50)  # x - массив np.array
x = arrlen.copy()
y1 = []
for i in range(10):
    start = time.time()
    arr[i].sort()
    end = time.time()
    tm = end-start
    y1.append(tm)

kolmas = 10
arr = []
arrlen = []
while kolmas != 0:
    kolmas -= 1
    temp = list(np.random.randint(-50, 50, size * (1 + kolmas)))
    arr.insert(0, temp)
    arrlen.insert(0, len(temp))

y2 = []
for i in range(10):
    start = time.time()
    insertion(arr[i])
    end = time.time()
    tm = end-start
    y2.append(tm)


kolmas = 10
arr = []
arrlen = []
while kolmas != 0:
    kolmas -= 1
    temp = list(np.random.randint(-50, 50, size * (1 + kolmas)))
    arr.insert(0, temp)
    arrlen.insert(0, len(temp))

y3 = []
for i in range(10):
    start = time.time()
    heapSort(arr[i])
    end = time.time()
    tm = end-start
    y3.append(tm)

kolmas = 10
arr = []
arrlen = []
while kolmas != 0:
    kolmas -= 1
    temp = list(np.random.randint(-50, 50, size * (1 + kolmas)))
    arr.insert(0, temp)
    arrlen.insert(0, len(temp))

y4 = []
for i in range(10):
    start = time.time()
    somesort(arr[i])
    end = time.time()
    tm = end-start
    y4.append(tm)

fig, ax = plt.subplots()
fig.canvas.set_window_title("Графики функций")

# Настройки диаграммы и осей
ax.set_title("Асимптотики алгоритмов")
ax.set_xlabel("Размер массива")
ax.set_ylabel("Время работы алгоритма")
ax.grid(False)

# 2 графика
ax.plot(x, y1, 'r', linewidth=3, label="Встроенная сортировка")
ax.plot(x, y2, label="Сортировка вставками")
ax.plot(x, y3, 'b', label="Сортировка кучей")
ax.plot(x, y4, 'g', label="Сортировка дурака")

# Аннотации и текст
# ax.annotate(r"Экстремум функции = $\frac{-b}{2a} = \frac{-4}{2} = -2$",
#             xy=(-2, 9), xytext=(-4.8, 15.5),
#             arrowprops=dict(facecolor="black", shrink=0.05))
# ax.text(-7, 24.5, "На диаграмме 2 графика:\nпарабола и линия экстремума")

# Легенда
ax.legend()
plt.show()