"""
 Упражнения к четвертой части

 В этих упражнениях вам будет предложено написать более сложные
программы. Обязательно проверьте решения в разделе «Часть IV, Функции»
в приложении B; оформляйте свои решения в виде файлов модулей.
Если будет допущена ошибка, будет очень сложно повторно ввести эти
упражнения с клавиатуры в интерактивной оболочке.

 1. Основы. В интерактивной оболочке интерпретатора Python напишите
функцию, которая выводит на экран единственный аргумент, и попробуйте
вызвать ее несколько раз, передавая объекты различных типов: строки,
целые числа, списки, словари. Затем попробуйте вызвать ее
без аргументов. Что произошло? Что произойдет, если передать функции
два аргумента?
"""


def give_one(x):
    return x


for i in ['Aber', 2001, [1, 5, 25, 253], dict(rer=56, par=100)]:
    print(give_one(i))

"""
 2. Аргументы. Напишите функцию с именем adder в файле модуля. Функция
должна принимать два аргумента и возвращать их сумму (или конкатенацию). 
Затем добавьте в конец файла модуля вызовы функции adder с объектами 
различных типов (две строки, два списка, два вещественных числа)
и запустите этот файл как сценарий из командной строки операционной
системы. Должны ли вы явно производить вывод результатов, чтобы они
появились на экране?
"""


def adder(x, y):
    return x + y


for i, j in [('gert', 'hant'), ([3, 8, 2], [5, 34, 205]), (0.0, 4.5)]:
    print(adder(i, j))

"""
 3. Переменное число аргументов. Обобщите функцию adder из предыдущего
упражнения, чтобы она вычисляла сумму произвольного числа аргументов, 
и измените вызовы функции так, чтобы ей передавалось больше или меньше 
двух аргументов. Какой тип имеет возвращаемое значение суммы?
(Подсказка: срез, такой как S[:0], возвращает пустую последовательность
того же типа, что и S, а с помощью встроенной функции type можно узнать
тип объекта – смотрите примеры с функцией min в главе 18, 
где используется подобный прием.) Что произойдет, если функции передать
аргументы разных типов? Что произойдет, если ей передать словари?
"""


def adder(*args):
    if len(args) < 1:
        return args, type(args)
    elif len(args) == 1:
        return args[0], type(args[0])

    fst = args[0]
    for arg in args[1:]:
        fst += arg
    return fst, type(fst)


for i in [('gert', 'hant', 'tres'), (7.4,)]:
    print(adder(*i))

"""
 4. Именованные аргументы. Измените функцию adder из упражнения 2 так,
чтобы она принимала и вычисляла сумму/конкатенацию трех аргументов:
def adder(good, bad,ugly). После этого определите значения по умолчанию
для каждого из аргументов и поэкспериментируйте с функцией
в интерактивной оболочке. Попробуйте передавать ей один, два,
три и четыре аргумента. Попробуйте передавать аргументы по именам.
Будет ли работать такой вызов: adder(ugly=1, good=2)? Почему? Наконец,
обобщите новую версию функции adder так, чтобы принимала
и вычисляла сумму/конкатенацию произвольного числа
именованных аргументов. Решение будет напоминать то,
что было получено в упражнении 3, с той лишь разницей,
что вам придется выполнить обход словаря, а не кортежа. (Подсказка:
метод dict.keys() возвращает список, который можно обойти с помощью 
цикла for или while, но не забудьте обернуть его вызовом функции list 
в Python 3.0, чтобы обеспечить возможность обращения к элементам 
по индексам!)
"""


def adder(good=7, bad=4, ugly=13):
    return good + bad + ugly


for i in [(3, 7, 12), (45,), (234, 67)]:
    print(adder(*i))

print(adder(ugly=1, good=2))


def adder(**kwargs):
    if len(kwargs) < 1:
        return kwargs, type(kwargs)
    elif len(kwargs) == 1:
        return list(kwargs.values())[1], type(list(kwargs.values())[1])

    ans = list(kwargs.values())[0]
    del kwargs[list(kwargs.keys())[0]]

    for key in kwargs:
        ans += kwargs[key]
    return ans


print(adder(hash=(3, 6, 134), cash=(10000,)))

"""
 5. Напишите функцию с именем copyDict(dict), которая копирует словарь,
получаемый в виде аргумента. Она должна возвращать новый словарь, 
содержащий все элементы аргумента. Используйте метод keys для выполнения
итераций (или, в Python 2.2, выполните обход ключей словаря без вызова
метода keys). Копирование последовательностей выполняется достаточно
просто (выражение X[:] выполняет поверхностное копирование); будет ли
этот метод работать со словарями?
"""


def copy_dict(d: dict) -> dict:
    return {key: d[key] for key in d}


"""
 6. Напишите функцию с именем addDict(dict1, dict2), которая вычисляет
объединение двух словарей. Она должна возвращать новый словарь,
содержащий все элементы обоих аргументов (которые, как предполагается, 
являются словарями). Если один и тот же ключ присутствует в обоих
аргументах, вы можете выбрать значение из любого словаря. Проверьте
свою функцию, добавив программный код проверки в файл и запустив его
как сценарий. Что произойдет, если вместо словарей передать списки? 
Как можно было бы обобщить функцию, чтобы она обрабатывала 
и этот случай? (Подсказка: смотрите встроенную функцию type, 
использовавшуюся ранее.) Имеет ли значение порядок следования 
аргументов?
"""


def add_dict(d1: dict, d2: dict) -> dict:
    if type(d1) == list and type(d2) == list:
        return d1 + d2

    d3 = {}
    for d in d1, d2:
        for key in d:
            d3[key] = d[key]

    return d3


"""
 7. Дополнительные примеры на сопоставление аргументов. Сначала 
определите следующие шесть функций (в интерактивной оболочке или в файле
модуля, который затем можно будет импортировать):

def f1(a, b): print(a, b)  # Обычные аргументы
def f2(a, *b): print(a, b)  # Переменное число позиционных аргументов
def f3(a, **b): print(a, b)  # Переменное число именованных аргументов
def f4(a, *b, **c): print(a, b, c)  # Смешанный режим
def f5(a, b=2, c=3): print(a, b, c) 
# Аргументы со значениями по умолчанию
def f6(a, b=2, *c): print(a, b, c) 
# Переменное число позиционных аргументов
# и аргументов со значениями по умолчанию

 Теперь протестируйте следующие вызовы в интерактивной оболочке 
и попробуйте объяснить полученные результаты – в некоторых случаях вам,
возможно, придется вернуться к обсуждению алгоритмов сопоставления
в главе 18. Как вы думаете, смешивание режимов сопоставления вообще
можно считать удачным выбором? Можете ли вы придумать ситуации, 
когда это могло бы оказаться полезным?

>>> f1(1, 2)
>>> f1(b=2, a=1)
>>> f2(1, 2, 3)
>>> f3(1, x=2, y=3)
>>> f4(1, 2, 3, x=2, y=3)
>>> f5(1)
>>> f5(1, 4)
>>> f6(1)
>>> f6(1, 3, 4)
"""


def f1(a, b): print(a, b)  # Обычные аргументы


def f2(a, *b): print(a, b)  # Переменное число позиционных аргументов


def f3(a, **b): print(a, b)  # Переменное число именованных аргументов


def f4(a, *b, **c): print(a, b, c)  # Смешанный режим


def f5(a, b=2, c=3): print(a, b, c)


# Аргументы со значениями по умолчанию


def f6(a, b=2, *c): print(a, b, c)


# Переменное число позиционных аргументов
# и аргументов со значениями по умолчанию


f1(1, 2)
f1(b=2, a=1)
f2(1, 2, 3)
f3(1, x=2, y=3)
f4(1, 2, 3, x=2, y=3)
f5(1)
f5(1, 4)
f6(1)
f6(1, 3, 4)

"""
 8. Снова простые числа. Вспомните следующий фрагмент из главы 13,
который определяет – является ли целое положительное число простым:

x = y // 2  # Для значений y > 1
while x > 1:
    if y % x == 0: # Остаток
        print(y, ‘has factor’, x)
        break  # Обойти блок else
    x = x-1
else:  # Обычный выход
    print(y, ‘is prime’)
    
 Оформите этот фрагмент в виде функции в файле модуля (значение 
y должно передаваться как аргумент) и добавьте несколько вызовов функции 
в конец этого файла. При этом замените оператор // на / в первой строке,
чтобы увидеть, как изменилось действие оператора деления в Python 3.0 
и как это изменение отрицательно влияет на работоспособность данного 
фрагмента (вернитесь к главе 5, если вам необходимо освежить 
свои знания). Что вы можете сказать об отрицательных значениях? Сумеете 
ли вы повысить скорость работы этой функции? Вывод из вашего модуля 
должен выглядеть примерно так, как показано ниже:

13 is prime
13.0 is prime
15 has factor 5
15.0 has factor 5.0
"""


def is_prime(n):
    x = round(n / 2) + 1
    for i in reversed(range(2, x)):
        if not n % i:
            return '{} has factor {}'.format(n, i)

    return '{} is prime'.format(n)


for i in 13, 13.0, 15, 15.0:
    print(is_prime(i))

"""
 9. Генераторы списков. Напишите программный код, который будет
создавать новый список, содержащий квадратные корни всех чисел 
из следующего списка: [2, 4, 9, 16, 25]. Начните с реализации на основе 
цикла for, затем на основе функции map и, наконец, в виде генератора 
списков. Для вычислений используйте функцию sqrt из модуля math (то есть
выполните import math и вызывайте функцию, как math.sqrt(x)). Какой 
из трех вариантов, на ваш взгляд, является лучшим?
"""

from math import sqrt

L = [2, 4, 9, 16, 25]

ans1 = []
for n in L:
    ans1.append(sqrt(n))

print(ans1)


ans2 = map(sqrt, L)
print(list(ans2))


ans3 = [sqrt(n) for n in L]
print(ans3)

"""
 10. Хронометраж. В главе 5 мы видели три способа вычисления квадратных
корней: math.sqrt(X), X ** .5 и pow(X, .5). Если в вашей программе часто 
возникает необходимость вычислять квадратные корни, сопоставление 
производительности этих трех методов может оказаться значимым. Чтобы 
увидеть, какой из способов является наиболее быстрым,
перепишите сценарий timerseqs.py, который был создан нами в этой главе,
так, чтобы он измерял производительность каждого из трех способов.
Используйте функцию best из модуля mytimer.py (вы можете использовать
версию для Python 3.0 с аргументами, которые могут передаваться
только по именам, или версию, совместимую с 2.6/3.0).
Для большего удобства вы можете также переписать реализацию испытаний
в этом сценарии так, чтобы имелась возможность передавать
испытуемые функции, например, в виде кортежа (для этого упражнения
вполне подойдет прием копирования и вставки фрагментов кода).
Какой из трех способов вычисления квадратных корней оказался
самым быстрым на вашем компьютере и в вашей версии Python? Наконец,
как можно было бы выполнить хронометраж производительности генераторов 
словарей и эквивалентных им циклов for в интерактивном сеансе?
"""

import time


trace = lambda *args: None  # or print
timefunc = time.time


def timer(func, *pargs, _reps=1000, **kargs):
    trace(func, pargs, kargs, _reps)
    start = timefunc()
    for _ in range(_reps):
        ret = func(*pargs, **kargs)
        
    elapsed = timefunc() - start
    return elapsed, ret


def best(func, *pargs, _reps=50, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        time1, ret = timer(func, *pargs, _reps=1, **kargs)
        if time1 < best:
            best = time1
            
    return best, ret


def pow1(a):
    return a ** .5


def pow2(a):
    return sqrt(a)


print(timer(pow1, 2, _reps=100000))

print(timer(pow2, 2, _reps=100000))

print(timer(pow, 2, .5, _reps=100000))

print(best(pow1, 2))

print(best(pow2, 2))

print(best(pow, 2, .5))
