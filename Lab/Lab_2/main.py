import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x - math.sin(x**(1/3))

def g(x):
    return math.sin(x**(1/3)) + x

def simple_iteration_method(initial_guess, tolerance, max_iterations):
    x_prev = initial_guess
    for i in range(max_iterations):
        x_next = g(x_prev)
        error = abs(x_next - x_prev)
        print(f"Итерация {i+1}: x_{i+1} = {x_next}, погрешность = {error}")
        if error < tolerance:
            print("Сближение достигнуто.")
            return x_next
        x_prev = x_next
    print("Достигнуто максимальное количество итераций.")
    return None

# Начальное приближение, требуемая точность и максимальное количество итераций
initial_guess = float(input("Введите начальное приближение: "))
tolerance = 1e-4
max_iterations = int(input("Введите кол-во итераций: "))

# Вызов метода простых итераций
solution = simple_iteration_method(initial_guess, tolerance, max_iterations)
if solution is not None:
    print("Приблизительное решение:", solution)
else:
    print("Невозможно найти решение в пределах заданного допуска.")

# Построение графика функции f(x)
x_values = np.linspace(0, 3, 100)  # Определяем значения x для графика
y_values = [f(x) for x in x_values]  # Вычисляем значения функции f(x) для каждого x
plt.plot(x_values, y_values, label='f(x) = x - sin(cbrt(x))')  # Построение графика
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x)')
plt.axhline(0, color='red',linewidth=0.5)
plt.axvline(0, color='red',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()