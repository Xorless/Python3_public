"""
 Треугольные, пятиугольные и шестиугольные числа
вычисляются по нижеследующим формулам:

  Треугольные	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
  Пятиугольные	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
  Шестиугольные	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...

 Можно убедиться в том, что T285 = P165 = H143 = 40755.

 Найдите следующее треугольное число,
являющееся также пятиугольным и шестиугольным.
"""

n = 100000

# Треугольные числа
triang_nums = set(round(i*(i+1)/2) for i in range(285, n))

# Пятиугольные числа
pent_nums = set(round(i*(3*i - 1)/2) for i in range(165, n))

# Шестиугольные числа
hex_nums = set(round(i*(2*i - 1)) for i in range(143, n))

# Вывод пересечения трёх множеств
print(list(triang_nums & pent_nums & hex_nums)[1])
