"""
 Начиная с вершины представленного ниже треугольника
и переходя к прилежащим числам в следующем ряду,
максимальная возможная сумма пройденных чисел по пути
от вершины до основания равна 23.

  3
  7 4
  2 4 6
  8 5 9 3

 Т.е., 3 + 7 + 4 + 9 = 23.

 Найти максимальную сумму при переходе от вершины
до основания треугольника, представленного текстовым файлом
размером 15КБ triangle.txt
(щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'),
в котором содержится треугольник с одной сотней строк.

 ПРИМЕЧАНИЕ: Это намного усложненная версия 18-й задачи.
Данную задачу нельзя решить, испробовав каждый возможный вариант,
поскольку всего их 2^99! Если бы удалось проверять один триллион (10^12)
вариантов в секунду, потребовалось бы двадцать биллионов лет,
чтобы испробовать их все.
Существует эффективный алгоритм решения данной задачи. ;o)
"""

f = open('p067_triangle.txt', 'r')

# Создание пирамиды
triangle = list(n for n in f.read().split('\n'))[:-1]

for i in range(len(triangle)):
    if len(triangle[i]) < len(triangle[-1]):
        while len(triangle[i]) < len(triangle[-1]):
            triangle[i] += ' 00'
            
    triangle[i] = triangle[i].split(' ')
    for j in range(len(triangle[i])):
        triangle[i][j] = int(triangle[i][j])


def max_path_sum(tri, m):
    # цикл для восходящего расчета
    for i in range(m - 1, -1, -1):
        for j in range(i + 1):
            # для каждого элемента отметьте оба элементы чуть ниже числа
            # и ниже справа от номера добавить максимум к нему
            if tri[i + 1][j] > tri[i + 1][j + 1]:
                tri[i][j] += tri[i + 1][j]
            else:
                tri[i][j] += tri[i + 1][j + 1]

    # вернуть верхний элемент, где хранится максимальная сумма
    return tri[0][0]


# Программа драйвера для проверки вышеуказанной функции
print(max_path_sum(triangle, len(triangle) - 1))
