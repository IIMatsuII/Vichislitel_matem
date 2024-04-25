import math #

def f(x): #
    return x - math.sin(x**(1/3)) #

def g(x): #
    return math.sin(x**(1/3)) + x #

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