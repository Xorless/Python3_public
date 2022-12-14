# Жадные алгоритмы

"""
 Задача составления расписания

 Допустим, имеется учебный класс,
в котором нужно провести как можно больше уроков.
Вы получаете список уроков.

 Провести в классе все уроки не получится,
потому что некоторые из них перекрываются по времени.

 Требуется провести в классе как можно больше уроков.
Как отобрать уроки, чтобы полученный набор
оказался самым большим из возможных? Вроде бы сложная задача, верно?
На самом деле алгоритм оказывается на удивление простым.
Вот как он работает:

  1. Выбрать урок, завершающийся раньше всех. Это первый урок,
 который будет проведен в классе.
  2. Затем выбирается урок, начинающийся после завершения первого урока.
 И снова следует выбрать урок,
 который завершается раньше всех остальных.
 Он становится вторым уроком в расписании.

 Продолжайте действовать по тому же принципу - и вы получите ответ!
Давайте попробуем. Рисование заканчивается раньше всех уроков (в 10:00),
поэтому мы выбираем именно его.

 Теперь нужно найти следующий урок, который начинается после 10:00
и завершается раньше остальных.

 Английский язык отпадает - он перекрывается с рисованием,
но математика подходит. Наконец,
информатика перекрывается с математикой, но музыка подходит.

 И так, эти три урока должны проводиться в классе.

 Я очень часто слышу, что этот алгоритм подозрительно прост.
Он слишком очевиден, а значит, должен быть неправильным.
Но в этом и заключается красота жадных алгоритмов: они просты!
Жадный алгоритм прост: на каждом шаге он выбирает оптимальный вариант.
В нашем примере при выборе урока выбирается тот урок,
который завершается раньше других. В технической терминологии:
на каждом шаге выбирается локально-оптимальное решение,
а в итоге вы получаете глобально-оптимальное решение. Хотите верьте,
хотите нет, но этот простой алгоритм
успешно находит оптимальное решение задачи составления расписания!

 Конечно, жадные алгоритмы работают не всегда.
Но они так просто реализуются! Рассмотрим другой пример.


 Задача о рюкзаке

 Представьте, что вы жадный воришка. Вы забрались в магазин с рюкзаком,
и перед вами множество товаров, которые вы можете украсть.
Однако емкость рюкзака не бесконечна: он выдержит не более 35 фунтов.

 Требуется подобрать набор товаров максимальной стоимости,
которые можно сложить в рюкзак. Какой алгоритм вы будете использовать?

 И снова жадная стратегия выглядит очень просто:

  1. Выбрать самый дорогой предмет, который поместится в рюкзаке.
  2. Выбрать следующий по стоимости предмет,
 который поместится в рюкзаке... И так далее.

 Бот только на этот раз она не работает! Предположим, есть три предмета.

 Б рюкзаке поместятся товары общим весом не более 35 фунтов.
Самый дорогой товар - магнитофон, вы выбираете его.
Теперь ни для чего другого места уже не осталось.

 Бы набрали товаров на $3000. Погодите-ка!
Если бы вместо магнитофона вы выбрали ноутбук и гитару,
то стоимость добычи составила бы $3500!

 Очевидно, жадная стратегия не дает оптимального решения.
Впрочем, результат не так уж далек от оптимума.
В следующей главе я расскажу, как вычислить правильное решение. Но вор,
забравшийся в магазин , вряд ли станет стремиться к идеалу.
«достаточно хорошего~ решения должно хватить.

 Второй пример приводит нас к следующему выводу: иногда идеальное -
враг хорошего. В некоторых случаях достаточно алгоритма,
способного решить задачу достаточно хорошо.
И в таких областях жадные алгоритмы работают просто отлично,
потому что они просто реализуются,
а полученное решение обычно близко к оптимуму.


 Упражнения

 8.1 Вы работаете в фирме по производству мебели
и поставляете мебель по всей стране.
Коробки с мебелью размещаются в грузовике.
Все коробки имеют разный размер,
и вы стараетесь наиболее эффективно использовать доступное пространство.
Как выбрать коробки для того,
чтобы загрузка имела максимальную эффективность?
Предложите жадную стратегию. Будет ли полученное решение оптимальным?
 ответ: 1. Выбрать коробки с вместимостью по возрастанию.
 2. В каждую коробку складывать самую габаритную мебель по очерёдности
 до заполнения.
 Полученное решение не будет оптимальноым, но будет близко к нему.

 8.2 Вы едете в Европу, и у вас есть семь дней на знакомство
с достопримечательностями. Вы присваиваете каждой достопримечательности
стоимость в баллах (насколько вы хотите ее увидеть)
и оцениваете продолжительность поездки.
Как обеспечить максимальную стоимость (увидеть все самое важное)
во время поездки? Предложите жадную стратегию.
Будет ли полученное решение оптимальным?
 Ответ: Нужно посещать самые большие по баллам достопримечательности
 в объёмаж поезди, а следующую выбирать по убывающей. Нет,
 это решение не буде оптимальным, но оно будет близко к нему.

 Рассмотрим еще один пример,
в котором без жадных алгоритмов практически не обойтись.


 Задача о покрытии множества

 Вы открываете собственную авторскую программу на радио и хотите,
чтобы вас слушали во всех 50 штатах. Нужно решить,
на каких радиостанциях должна транслироваться ваша передача.
Каждая станция стоит денег,
поэтому количество станций необходимо свести к минимуму.
Имеется список станций.

 Каждая станция покрывает определенный набор штатов,
эти наборы перекрываются.

 Как найти минимальный набор станций, который бы покрывал все 50 штатов?
Вроде бы простая задача, верно? Оказывается, она чрезвычайно сложна.
Вот как это делается:

  1. Составить список всех возможных подмножеств станций -
 так называемое степен.н.ое множество.
 В нем содержатся 2^n возможных подмножеств.
  2. Из этого списка выбирается множество с наименьшим набором станций,
 покрывающих все 50 штатов.

 Проблема в том, что вычисление всех возможных подмножеств станций
займет слишком много времени. Для п станций оно потребует времени
0(2^n). Если станций немного, скажем от 5 до 10, - это допустимо.
Но подумайте, что произойдет во всех рассмотренных примерах
при большом количестве элементов. Предположим,
вы можете вычислять по 10 подмножеств в секунду.

 Не существует алгоритма, который будет вычислять подмножества
с приемле. мой скоростыо! Что же делать?

  Колисество   Необходимое
  станций      время
  5            3,2с
  10           102,2с
  32           13,6 года
  100          4 * 10^23 года


 Приближенные алгоритмы

 На помощь приходят жадные алгоритмы! Вот как выглядит жадный алгоритм,
который выдает результат, достаточно близкий к оптимуму:

  1. Выбрать станцию, покрывающую наибольшее количество штатов,
 еще не входящих в покрытие.
 Если станция будет покрывать некоторые штаты, уже входящие в покрытие,
 это нормально.
  2. Повторять, пока остаются штаты, не входящие в покрытие.

 Этот алгоритм является приближеняым.
Когда вычисление точного решения занимает слишком много времени,
применяется приближенный алгоритм.
Эффективность приближенного алгоритма оценивается по:

  быстроте;

  близости полученного решения к оптимальному.

 Жадные алгоритмы хороши не только тем,
что они обычно легко формулируются, но и тем,
что простота обычно оборачивается быстротой выполнения.
В данном случае жадный алгоритм выполняется за время О(n^2),
где п - количество радиостанций.

 А теперь посмотрим, как эта задача выглядит в программном коде.


 Подготовительный код

 В этом примере для простоты будет использоваться
небольшое подмножество штатов и станций.
Сначала составьте список штатов:
"""

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "са", "az"}

'''
 В этой реализации я использовал множество. 
Эта структура данных похожа на список, 
но каждый элемент может встречаться в множестве не более одного раза.
Множества не содержат дубликатов. Предположим, имеется следующий список:

>>> arr = [1, 2, 2, 3, 3, 3]

 Этот список преобразуется в множество:
 
»> set(arr)
set([1, 2, 3])

 Значения 1, 2 и 3 встречаются в списке по одному разу.
 
 Также понадобится список станций,
из которого будет выбираться покрытие. Я решил воспользоваться хешем:
'''

stations = {"kone": {"id", "nv", "ut"},
            "ktwo": {"wa", "id", "mt"},
            "kthree": {"or", "nv", "са"},
            "kfour": {"nv", "ut"},
            "kfive": {"ca", "az"}}

'''
Ключи - названия станций, а значения - сокращенные обозначения штатов, 
входящих в зону охвата. Таким образом, 
в данном примере станция kone вещает в штатах Айдахо (id), Невада (nv) 
и Юта (ut). Все значения являются множествами. Как вы вскоре увидите, 
хранение данных во множествах упрощает работу.

Наконец, нам понадобится структура данных
для хранения итогового набора станций:
'''

final_stations = set()

'''
 Вычисление ответа
 
 Теперь необходимо вычислить набор используемых станций. 
Взгляните на диаграмму и попробуйте предсказать, 
какие станции следует использовать.

 Учтите, что правильных решений может быть несколько.
Вы перебираете все станции и выбираете ту,
которая обслуживает больше всего штатов, не входящих в текущее покрытие.
Будем называть ее best_station:


best_station = None
states_covered = set()
for station, states_for_station in stations.items():

 Множество states_covered содержит все штаты, 
обслуживаемые этой станцией, которые еще не входят в текущее покрытие. 
Цикл for перебирает все станции и находит среди них наилучшую. 
Рассмотрим тело цикла for:

    covered = states_needed & states_for_station
    if len(covered) > len(states_covered):
        best_station = station
        states_covered = covered

 В коде встречается необычная строка:

covered = states_needed & states_for_station

 Что здесь происходит?


 Множества

 Допустим, имеется множество с названиями фруктов.
 
 Также имеется множество с названиями овощей.
 
 С двумя множествами можно выполнить ряд интересных операций.

  Элементы, которые являются фруктами или овощами
                  Объединение
                  
  Элементы, которые являются фруктами и овощами
                  Пересечение
                   
  Элементы, которые являются фруктами, но не овощами
                  Разность
                  
  Объединение множеств означает слияние элементов обоих множеств.
  
  Под операцией пересечения множеств понимается поиск элементов,
 входящих в оба множества (в данном случае - только помидор).
  Под разностью множеств понимается исключение 
 из одного множества элементов, присутствующих в другом множестве.
 
 Пример:
 
>>> fruits = set(["avocado", "tomato", "bапапа"])
>>> vegetables = set(["beets", "carrots", "tomato"])
>>> fruits | vegetables                             Обьедмненме множеств
set(["avocado", "beets", "carrots", "tomato", "bапапа"])
»> fruits & vegetables                              Пересечение множеств
set([ "tomato"])
>>> fruits - vegetables                                Разность множеств
set(["avocado", "bапапа"])
>>> vegetables - fruits   Как вы думаете, как будет выгnядеть резуnьтат?

 Еще раз напомню основные моменты:
 
  множества похожи на списки, но множества не содержат дубликатов;
  
  с множествами можно выполнять различные интересные операции -
 вычислять их объединение, пересечение и разность.
 
 
 Вернемся к коду

 Продолжим рассматривать исходный пример.
 
 Пересечение множеств:
 
covered = states_needed & states_for_station

 Множество covered содержит штаты, присутствующие как в states_needed,
так и в states_for station. Таким образом, covered - множество штатов, 
не входящих в покрыти е, которые покрываются текущей станцией!
Затем мы проверяем, покрывает ли эта станция больше штатов, 
чем текущая станция best_station:

if len(covered) > len(states_covered):
    best_station = station
    states_covered = covered
    
 Если условие выполняется, то станция сохраняется в best_station. 
Наконец, после завершения цикла best_station 
добавляется в итоговый список станций:

final_stations.add(best_station)

 Также необходимо обновить содержимое states_needed. Те штаты,
которые входят в зону покрытия станции, больше не нужны:

states_needed -= states_covered

 Цикл продолжается, пока множество states_needed не станет пустым.
Полный код цикла for выглядит так:
'''

while states_needed:

    best_station = None
    states_covered = set()

    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)

'''
 Этот результат совпадает с вашими ожиданиями? 
Вместо станций 1, 2, 3 и 5 можно было выбрать станции 2, 3, 4 и 5. 
Сравним время выполнения жадного алгоритма 
со временем точного алгоритма.

 Колисество  O(n!)            O(n^2)
 станций     Точный           Жадный 
             алгоритм         алгоритм
             
 5           3,2с             2,5с
 10          102,4с           10с
 32          13,6 года        102,4с
 100         4 * 10^21 года   16,67 минут
 

 Упражнения

 Для каждого из приведенных ниже алгоритмов укажите, 
является этот алгоритм жадным или нет.

 8.3 Быстрая сортировка.
 Ответ: нет.
 
 8.4 Поиск в ширину.
 Ответ: является.
 
 8.5 Алгоритм Дейкстры.
 Ответ: является.
'''
