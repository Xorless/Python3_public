"""
 Последовательность треугольных чисел образуется
путем сложения натуральных чисел. К примеру,
7-е треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
Первые десять треугольных чисел:

  1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

 Перечислим делители первых семи треугольных чисел:

  1: 1
  3: 1, 3
  6: 1, 2, 3, 6
  10: 1, 2, 5, 10
  15: 1, 3, 5, 15
  21: 1, 3, 7, 21
  28: 1, 2, 4, 7, 14, 28

 Как мы видим, 28 - первое треугольное число,
у которого более пяти делителей.

 Каково первое треугольное число, у которого более пятисот делителей?
"""


import math


def is_perf_sq(n):
    """
    Проверка на то, является ли число идеальным квадратным корнем
    или нет
    """
    x = math.ceil((math.sqrt(n)))
    if x*x == n:
        return True
    else:
        return False


def triang_num(n):
    """Возвращает n-ое треугольное число."""
    number = 0
    for j in range(1, n + 1):
        number += j

    return number


def max_triangular(m):
    """Возвращает треугольное число с m делителей."""
    x = 3
    n = 2
    while n <= m:
        n = 2
        num = triang_num(x)
        for i in range(2, math.ceil(math.sqrt(num))):
            if num % i == 0:
                n += 2
                
        if is_perf_sq(num):
                n -= 1
        x += 1
        
    return num


# Вывод треугольного числа с пятьюстами делителями
print(max_triangular(500))
