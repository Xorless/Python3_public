"""
 Совершенным числом называется число,
у которого сумма его делителей равна самому числу.
Например, сумма делителей числа 28 равна 1 + 2 + 4 + 7 + 14 = 28,
что означает, что число 28 является совершенным числом.

 Число n называется недостаточным, если сумма его делителей меньше n,
и называется избыточным, если сумма его делителей больше n.

 Так как число 12 является наименьшим избыточным числом
(1 + 2 + 3 + 4 + 6 = 16), наименьшее число,
которое может быть записано как сумма двух избыточных чисел, равно 24.
Используя математический анализ, можно показать,
что все целые числа больше 28123 могут быть записаны
как сумма двух избыточных чисел.
Эта граница не может быть уменьшена дальнейшим анализом,
даже несмотря на то, что наибольшее число,
которое не может быть записано как сумма двух избыточных чисел,
меньше этой границы.

 Найдите сумму всех положительных чисел,
которые не могут быть записаны как сумма двух избыточных чисел.
"""


def compute():
    """
    Функция возвращает сумму чисел,
    которая может быть суммой избыточных чисел.
    """
    LIMIT = 28124

    # Создаётся список суммы делителей каждого числа
    # в индексируемом списке
    divisor_sum = [0] * LIMIT
    for i in range(1, LIMIT):
        for j in range(i * 2, LIMIT, i):
            divisor_sum[j] += i

    # Создаётся список чисел,
    # сумма делителей которых больше самого числа
    abundant_nums = [i for (i, x) in enumerate(divisor_sum) if x > i]

    # Создаётся список чисел (индексов) с булевыми значениями,
    # где True присваивается числам,
    # которые могут быть представлены как сумма избыточных чисел
    expressible = [False] * LIMIT
    for i in abundant_nums:
        for j in abundant_nums:
            if i + j < LIMIT:
                expressible[i + j] = True
            else:
                break

    # Суммируются числа, которые нельзя представить
    # как сумму двух избыточных чисел
    ans = sum(i for (i, x) in enumerate(expressible) if not x)
    return str(ans)


"""
 Функция enumerate() вернет кортеж, 
содержащий отсчет от start и значение, 
полученное из итерации по объекту. 
Переданный в функцию объект должен быть последовательностью,
итератором или другим объектом, 
который поддерживает метод итератора __next__().

 Функция enumerate() применяется в случаях, 
когда необходим счётчик количества элементов в последовательности. 
Позволяет избавиться от необходимости инициировать 
и обновлять отдельную переменную-счётчик.

 Функцию enumerate() можно записать так:

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
"""

if __name__ == "__main__":
    print(compute())
