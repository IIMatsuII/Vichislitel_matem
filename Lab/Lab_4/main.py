import numpy as np
#Запомни A^-1 это обозначение обратной матрицы
# Исходная матрица A
A = np.array([[2.57, -2.57, 3.29, 0.14],
              [0.00, -1.00, 4.00, 0.00],
              [-1.00, -4.00, 8.00, 1.00],
              [-0.29, -7.71, 4.86, 6.43]])

# Правая часть системы уравнений
b = np.array([4.87, 9.00, 12.00, -2.41])

# Расширенная матрица [A | I]
A_extended = np.hstack([A, np.eye(A.shape[0])])

# Прямой ход метода Гаусса
n = len(A_extended)
for i in range(n):
    # Поиск максимального элемента в текущем столбце
    max_row = max(range(i, n), key=lambda r: abs(A_extended[r, i]))
    # Перестановка строк, если нужно
    A_extended[[i, max_row]] = A_extended[[max_row, i]]
    # Преобразование столбца i в верхнетреугольный вид
    for j in range(i + 1, n):
        ratio = A_extended[j, i] / A_extended[i, i]
        A_extended[j, i:] -= ratio * A_extended[i, i:]

# Обратный ход метода Гаусса
for i in range(n - 1, -1, -1):
    A_extended[i, :] /= A_extended[i, i]
    for j in range(i - 1, -1, -1):
        A_extended[j, :] -= A_extended[j, i] * A_extended[i, :]

# Искомая обратная матрица
A_inv = A_extended[:, n:]

print("Обратная матрица:")
print(A_inv)

# Проверка решения: A * A_inv должна быть единичной матрицей
identity_matrix = np.dot(A, A_inv)
print("Результат проверки:")
print(identity_matrix)