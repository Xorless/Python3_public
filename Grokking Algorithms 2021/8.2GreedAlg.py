# Жадные алгоритмы

"""
 NР-полные задачи

 Для решения задачи о покрытии множества необходимо вычислить
каждое возможное подмножество.

 Вероятно, вы вспомнили задачу о коммивояжере из главы 1.
В этой задаче коммивояжер должен был посетить пять разных городов.

 Коммивояжер пытается найти кратчайший путь,
который включит все пять городов. Чтобы найти кратчайший путь,
сначала необходимо вычислить все возможные пути.

 Сколько маршрутов необходимо вычислить для пяти городов?


 Задача о коммивояжере - шаг за шагом

 Начнем с малого. Допустим, городов всего два.
Выбирать приходится всего из двух маршрутов.

 Логично спросить: в задаче о коммивояжере существует ли
конкретный город, с которого нужно начинать? Допустим,
коммивояжер живет в СанФранциско и должен посетить еще четыре города.
Сан-Франциско должен быть первым городом в маршруте.

 Однако в каких-то ситуациях начальный город не задан. Допустим,
вы работаете в курьерской службе FedEx
и должны доставить пакет в пределах города.
Пакет перевозится из Чикаго в один из 50 филиалов FedEx.
Затем пакет будет перегружен в машину,
которая разъезжает по разным местам и доставляет пакеты.
В какой филиал отгрузить пакет? На этот раз начальная точка неизвестна,
и в задаче о коммивояжере вам придется вычислить как оптимальный путь,
так и начальную точку.

 Время выполнения обеих версий одинаково.
Однако отсутствие определенного начального города упрощает пример,
поэтому я выберу эту версию.

 Два города = два возможных маршрута.


 Сколько маршрутов?

 На первый взгляд может показаться, что это один маршрут.
Разве расстояние СФ>Марин не совпадает с расстоянием Марин>СФ?
Не всегда. В некоторых городах ( в том числе и в Сан-Франциско)
много луиц с одностороним движением,
и тогда вам не удасться вернуться по тому пути, по которому вы приехали.
Иногда приходиться проехать лишь пару миль, чтобы найти выезд на шоссе.
Так что эти два маршрута не всегда совпадают.


 Три города

 Теперь добавим к двум городам еще один.
Сколько возможных маршрутов существует в этой конфигурации?

Если начать в Беркли, вы можете посетить два города.

 Всего шесть возможных маршрутов: по два для каждого города,
с которого вы можете начать.

 Итак, три города= шесть возможных маршрутов.


 Четыре города

 Добавим еще один город - Фремонт. Тепе рь допустим,
что вы начали с Фремонта.

 Мы знаем, что во Фремонте начинаются шесть возможных маршрутов. Ого!
Да они очень похожи на шесть маршрутов, которые вы вычислили ранее,
когда городов было всего три!
Только теперь во всех маршрутах появился дополнительный город, Фремонт!
Начинает проявляться закономерность. Предположим,
из четырех городов выбирается начальный город Фремонт.
Остается еще три города. И вы знаете,
что для перемещения между тремя городами есть шесть разных маршрутов.
Итак, если начать с Фремонта, существуют шесть возможных маршрутов.
Также возможно начать с одного из других городов.

 Четыре возможных начальных города,
шесть возможных маршрутов для каждого начального города =
4 х 6 = 24 возможных маршрута.

 Замечаете закономерность? Каждый раз, когда вы добавляете новый город,
увеличивается количество вычисляемых маршрутов.

 Сколько возможных маршрутов существует для шести городов?
720, говорите? Да, вы правы. 5040 для 7 городов, 40 320 для 8 городов.

 Такая зависимость называется факториалъной
(помните, что об этом говорилось в главе З?) Итак, 5! = 120. Допустим,
есть 10 городов. Сколько существует возможных маршрутов?
10! = 3 628 800. Уже для 10 городов приходится вычислять
более 3 мwи~ионов возможных маршрутов. Как видите,
количество возможных маршрутов стремительно растет!
Вот почему невозможно вычислить "правильное" решение
задачи о коммивояжере при очень большом количестве городов.

 У задачи о коммивояжере и задаче покрытия множества есть кое-что общее:
вы вычисляете каждое возможное решение
и выбираете кратчайшее/минимальное. Обе эти задачи являются NР-полными.

Короткое объяснение NР-полноты:
некоторые задачи прославились сложностью своего решения.
Задача о коммивояжере и задача о покрытии множества -
два классических примера. Многие эксперты считают,
что написать быстрый алгоритм для решения таких задач невозможно.


 Как определить, что задача является NР-полной?

 Джон подбирает игроков для своей команды по американскому футболу.
У него есть список нужных качеств: хорошо играет в нападении,
хорошо играет в защите, хорошо играет под дождем,
хорошо играет под давлением и т. д. Также имеется список игроков,
в котором каждый игрок обладает определенными качествами.

 Джон хочет подобрать команду, которая обладает полным набором качеств,
но размер команды ограничен . «Минутку, - осознает Джон, -
но ведь это задача покрытия множества!»

 Для создания команды Джон может воспользоваться
тем же приближенным алгоритмом:

  1. Найти игрока с большинством качеств,
 которые еще не были реализованы.

  2. Повторять до тех пор, пока не будут реализованы все качества
 (или пока не кончатся свободные места в команде).

 NР - полные задачи встречаются очень часто. И было бы полезно,
если бы вы могли понять, что решаемая задача является NР-полной.
В этот момент можно прекратить поиски идеального решения
и перейти к решению с при менением приближенного алгоритма.
Но определить, является ли ваша задача NР - полной, непросто.
Обычно различия между легко решаемыми
и NР-полными задачами весьма незначительны. Например,
в предыдущих главах я много говорил о кратчайших путях.
Вы знаете, как вычислить кратчайший путь из точки А в точку В.

 Но если вы хотите найти кратчайший путь, соединяющий несколько точек,
то это уже задача о коммивояжере, которая является NР-полной.
Короче говоря, не существует простого способа определить,
является ли задача, с которой вы работаете, NР-полной.
Несколько характерных признаков:

  ваш алгоритм быстро работает при малом количестве элементов,
 но сильно замедляется при увеличении их числа;

  формулировка ~все комбинации х~ часто указывает на NР-полноту задачи;

  вам приходится вычислять все возможные варианты Х,
 потому что задачу невозможно разбить на меньшие подзадачи?
 Такая задача может оказаться NР-полной;

  если в задаче встречается некоторая последовательность
 (например, последовательность городов, как в задаче о коммивояжере)
 и задача не имеет простого решения, она может оказаться NР-полной;

  если в задаче встречается некоторое множество
 (например, множество радиостанций) и задача не имеет простого решения,
 она может оказаться NР-полной;

  можно ли переформулировать задачу в условиях задачи
 покрытия множества или задачи о коммивояжере?
 В таком случае ваша задача определенно является NР-полной.


 Упражнения

 8.6 Почтальон должен доставить письма в 20 домов.
Ему нужно найти кратчайший путь, проходящий через все 20 домов.
Является ли эта задача NР-полной?
 Ответ: да, является.

 8.7 Имеется задача поиска максимальной клики в множестве людей
(кликой называется множество людей,
каждый из которых знаком со всеми остальными).
Является ли эта задача NР-полной?
 Ответ: да, является.

 8.8 Вы рисуете карту США, на которой два соседних штата
не могут быть окрашены в одинаковый цвет.
Требуется найти минимальное количество цветов,
при котором любые два соседних штата будут окрашены в разные цвета.
Является ли эта задача NР-полной?
 Ответ: да, является.


  Жадные алгоритмы стремятся к локальной оптимизации в расчете на то,
 что в итоге будет достигнут глобальный оптимум.

  У NР-полных задач не существует известных быстрых решений.

  Если у вас имеется NР-полная задача,
 лучше всего воспользоваться приближенным лгоритмом.

  Жадные алгоритмы легко реализуются и быстро выполняются,
 поэтому из них получаются хорошие приближенные алгоритмы.
"""
