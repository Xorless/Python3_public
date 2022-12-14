"""
 Пусть d(n) определяется как сумма делителей n
(числа меньше n, делящие n нацело).

 Если d(a) = b и d(b) = a, где a ≠ b,
то a и b называются дружественной парой,
а каждое из чисел a и b - дружественным числом.

 Например, делителями числа 220 являются
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d(220) = 284.
Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.

 Подсчитайте сумму всех дружественных чисел меньше 10000.
"""


def d(n):
    """Функция возвращает список делителей числа."""
    divs = [1]
    m = n
    # Brute-force
    while True:
        if m == 1:
            if len(divs) > 1:
                divs.remove(divs[1])
                break
                
            break
            
        if n % m == 0:
            divs.append(m)
            m -= 1
        else:
            m -= 1

    return sum(divs)


sim_nums = []

# Перебор чисел для поиска дружественных пар
for a in range(1, 10000):
    b = d(a)
    if a != b and d(a) == b and d(b) == a and (a and b not in sim_nums):
        sim_nums.append(a)
        sim_nums.append(b)

# Вывод суммы этих чисел
print(sum(sim_nums))
