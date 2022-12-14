"""
 Внимательно сосчитав, можно понять,
что в прямоугольной сетке 3 на 2 содержится
восемнадцать прямоугольников:


 Несмотря на то, что не существует такой прямоугольной сетки,
которая содержит ровно два миллиона прямоугольников,
найдите площадь сетки с ближайшим количеством прямоугольников.
"""

import math


def num_rectangles(m, n):
    return (m + 1) * m * (n + 1) * n // 4  # A bit more than m^2 n^2 / 4


def compute():
    TARGET = 2000000
    end = int(math.sqrt(TARGET)) + 1
    # Генерация сетки
    gen = ((w, h) for w in range(1, end) for h in range(1, end))
    # Вычисление самого близкого к 2 000 000 размера сетки
    func = lambda wh: abs(num_rectangles(*wh) - TARGET)
    # Применение вышеперечисленного условия
    # к минимальному прямоугольнику
    ans = min(gen, key=func)
    # Возвращение произведения длины и ширины
    return str(ans[0] * ans[1]) + ' ' + str(ans)


if __name__ == '__main__':
    print(compute())
