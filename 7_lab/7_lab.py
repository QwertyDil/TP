import numpy as np
import matplotlib.pyplot as plt

# Генерируем массивы точек
x = np.linspace(-1.5, 1.5, 1000)
y = np.linspace(-1.5, 1.5, 1000)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

# Рисуем график
plt.figure()
plt.contour(X, Y, Z, [0], colors='r')
plt.title('График сердца')
plt.axis('equal')
plt.show()
