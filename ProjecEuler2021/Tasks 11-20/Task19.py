"""
 Дана следующая информация
(однако, вы можете проверить ее самостоятельно):

  1 января 1900 года - понедельник.
  В апреле, июне, сентябре и ноябре 30 дней.
  В феврале 28 дней, в високосный год - 29.
  В остальных месяцах по 31 дню.

 Високосный год - любой год, делящийся нацело на 4,
однако последний год века (ХХ00) является високосным в том
и только том случае, если делится на 400.
 Сколько воскресений выпадает на первое число месяца в двадцатом веке
(с 1 января 1901 года до 31 декабря 2000 года)?
"""

import calendar


cnt = 0

# Перебор всех месяцев в годах
for year in range(1901, 2001):
    for month in range(1, 13):
        # Если первый день месяца является 7-мым в неделе
        if calendar.monthrange(year, month)[0] == 6:
            cnt += 1

print(cnt)
