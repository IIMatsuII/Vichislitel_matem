import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x - math.sin(x**(1/3))

def golden_section_search(a, b, tolerance, max_iterations):
    phi = (1 + math.sqrt(5)) / 2  # Золотое сечение
    c = b - (b - a) / phi
    d = a + (b - a) / phi
    fc = f(c)
    fd = f(d)
    for i in range(max_iterations):
        print(f"Итерация {i+1}: a = {a}, b = {b}, c = {c}, d = {d}, fc = {fc}, fd = {fd}")
        if abs(c - d) < tolerance:
            print("Сближение достигнуто.")
            return (c + d) / 2
        if fc < fd:
            b = d
            d = c
            c = b - (b - a) / phi
            fd = fc
            fc = f(c)
        else:
            a = c
            c = d
            d = a + (b - a) / phi
            fc = fd
            fd = f(d)
    print("Достигнуто максимальное количество итераций.")
    return None

# Начальный отрезок, требуемая точность и максимальное количество итераций
a, b = int(input("Введите начальную точку: ")), int(input("Введите конечную точку: "))
tolerance = 1e-4
max_iterations = int(input("Введите кол-во итераций: "))

# Вызов метода золотого сечения
solution = golden_section_search(a, b, tolerance, max_iterations)
if solution is not None:
    print("Приблизительное решение:", solution)
else:
    print("Невозможно найти решение в пределах заданного допуска.")

# Построение графика функции f(x)
x_values = np.linspace(a, b, 1000)  # Определяем значения x для графика
y_values = [f(x) for x in x_values]  # Вычисляем значения функции f(x) для каждого x
plt.plot(x_values, y_values, label='f(x) = x - sin(cbrt(x))')  # Построение графика
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График f(x)')
plt.axhline(0, color='red',linewidth=0.5)
plt.axvline(0, color='green',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
