"""
 Простые делители числа 13195 - это 5, 7, 13 и 29.

 Каков самый большой делитель числа 600851475143,
являющийся простым числом?
"""

number = 600851475143

i = 2

while True:
    if number % i == 0:
        # Если число является делителем, то им делят исходное число
        number /= i
        if number == 1:
            print(i)
            break
    i += 1
