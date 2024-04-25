# f(x) = sin(x)

import numpy as np

from drawer import Drawer


X = np.arange(-np.pi, np.pi, 0.1)
Y = np.sin(X)


def main() -> None:
    drawer = Drawer()

    func = int(
        input(
            "Введите '1' для выбора аналитически заданнрй функции"
            "'f(x) = sin(x)', '2' для заданной таблично:"
        )
    )

    xscale = input("Введите коэффицент масштабирования для оси X: ")
    yscale = input("Введите коэффицент масштабирования для оси Y: ")

    if xscale != "":
        drawer.x_scale = float(xscale)
    if yscale != "":
        drawer.y_scale = float(yscale)

    match func:
        case 1:
            drawer.x = X
            drawer.y = Y
            drawer._set_lims()
        case 2:
            drawer.get_tabled_defined_func("C:/Users/Рустам/Desktop/Practic_For_Univer/Vichislitel_matem/Lab/Lab_1./table_defined_func.csv")
            drawer.smooth_func()
    drawer.draw_graph()

if __name__ == "__main__":
    main()