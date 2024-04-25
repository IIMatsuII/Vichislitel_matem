import numpy as np
import scipy.interpolate as interp
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Определяем функцию f(x)
def f(x):
    return x - np.sin(x**(1/3))

# Выбираем интервал [a, b] и количество точек для интерполяции
a = float(input("Введите начальное значение интервала: "))
b = int(input("Введите конечное значение интервала: "))
num_points = int(input("Введите кол-во узлов: "))

# Генерируем точки на графике функции f(x)
x_points = np.linspace(a, b, num_points)
y_points = f(x_points)

# Строим интерполяционный многочлен Лагранжа
lagrange_poly = interp.lagrange(x_points, y_points)

# Находим корни многочлена Лагранжа (решение f(x) = 0) методом оптимизации
roots = []
for i in range(num_points - 1):
    if np.sign(f(x_points[i])) != np.sign(f(x_points[i+1])):
        root = opt.brentq(lagrange_poly, x_points[i], x_points[i+1])
        roots.append(root)

# Выводим найденные корни
print("Приблизительные корни (f(x) = 0):", roots)

# Строим график функции f(x) и интерполяционного многочлена
plt.plot(x_points, y_points, label='f(x) = x - sin(cbrt(x))')
plt.plot(x_points, lagrange_poly(x_points), label='Полином интерполяции')
plt.scatter(roots, [0]*len(roots), color='red', label='Корни')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Интерполяция f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
