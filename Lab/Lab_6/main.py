import numpy as np

# Определяем функцию f(x)
def f(x):
    return x - np.sin(x**(1/3))

# Определение интервала интегрирования [a, b]
a = 0.1
b = 10

# Точное значение интеграла (может быть получено аналитически или с помощью другого численного метода)
exact_value = 7.542105320819386

# Список для хранения значений интеграла при разных числах разбиений интервала
integral_values = []

# Вычисление интеграла для разных чисел разбиений интервала
for n in [10, 20, 40, 80, 160]:
    h = (b - a) / n  # Шаг
    integral = 0.5 * (f(a) + f(b))  # Первый и последний члены
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h  # Умножение суммы на шаг
    integral_values.append(integral)

# Вывод значений интеграла
print("Значения интеграла:", integral_values)

# Оценка эффективного порядка точности по Эйткену
orders = []
for i in range(len(integral_values) - 2):
    order = np.log((integral_values[i + 2] - integral_values[i + 1]) / (integral_values[i + 1] - integral_values[i])) / np.log(2)
    orders.append(order)

# Вывод эффективного порядка точности
print("Расчетные порядки сходимости (с использованием ускорения Эйткена):", orders)
