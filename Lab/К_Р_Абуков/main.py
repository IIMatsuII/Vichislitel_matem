import numpy as np

def solve_ode(f, y0, t0, tN, N):
    # Создаем массив времени
    t = np.linspace(t0, tN, N+1)
    
    # Создаем массив начальных условий
    y = [y0]
    
    # Проходим по всем шагам разностной схемы
    for i in range(N):
        h = t[i+1] - t[i]
        k1 = h  *  f(t[i], y[-1])
        k2 = h  *  f(t[i] + 0.5  *  h, y[-1] + 0.5  *  k1)
        k3 = h  *  f(t[i] + 0.5  *  h, y[-1] + 0.5  *  k2)
        k4 = h  *  f(t[i+1], y[-1] + k3)
        
        y.append(y[-1] + (k1 + 2  *  k2 + 2  *  k3 + k4) / 6)
    
    return t, np.array(y)

# Определение функции f(t, y)
def f(t, y):
    return -y / t ** 2

# Начальные условия
y0 = 1
t0 = 0
tN = 1
N = 1000

# Решение уравнения
t, y = solve_ode(f, y0, t0, tN, N)

# Вывод результата
for i in range(len(t)):
    print(f"t = {t[i]:.4f}, y = {y[i]:.4f}")
