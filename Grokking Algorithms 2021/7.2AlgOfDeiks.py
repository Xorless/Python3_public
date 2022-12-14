# Алгоритм Дейкстры

"""
 Ребра с отрицательным весом

 В предыдущем примере Алекс предложил в обмен на книгу
один из двух предметов.

 Предположим, Сара предложила обменять пластинку на постер
и при этом она еще и даст Раме $7.
Рама ничего не тратит при этом обмене, вместо этого он получит $7.
Как изобразить это предложение на графе?

 Ребро, ведущее от пластинки к постеру, имеет отрицательный вес!
Если Рама пойдет на этот обмен, он получит $7.
Теперь к постеру можно добраться двумя способами.

 А значит, во втором обмене появляется смысл - Рама получает $2!
Теперь , если вы помните, Рама может обменять постер на барабан.
И здесь возможны два пути.

 Второй путь обойдется на $2 дешевле,
поэтому нужно выбрать этот путь, верно?

 И знаете что? Если применить алгоритм Дейкстры к этому графу,
Рама выберет неверный путь.
Он пойдет по более длинному пути.
Алгоритм Дейкстры не может использоваться при наличии ребер,
имеющих отрицательныйвес. Такие ребра нарушают работу алгоритма.
Посмотрим, что произойдет,
если попытаться применить алгоритм Дейкстры к этому графу.
Все начинается с построения таблицы стоимостей.

 Теперь найдем узел с наименьшей стоимостью
и обновим стоимости его соседей.
В этом случае постер оказывается узлом с наименьшей стоимостью.
Итак , в соответствии с алгоритмом Дейкстры,
к постеру невозможно перейmu более дешевым способом,
чем с оплатой $0 (а вы знаете, что это неверно!)
Как бы то ни было, обновим стоимости его соседей.

 Получается , что теперь стоимость барабана составляет $35.

 Перейдем к следующему по стоимости узлу, который еще не был обработан.

 Обновим стоимости его соседей.

 Узел "постер" уже был обработан, однако вы обновляете его стоимость.
Это очень тревожный признак - обработка узла означает,
что к нему невозможно добраться с меньшими затратами.
Но вы только что нашли более дешевый путь к постеру!
У барабана соседей нет, поэтому работа алгоритма завершена.
Ниже приведены итоговые стоимости.

  пластинка   5

  постер     -2

  барабан    35

 Чтобы добраться до барабанов, Раме потребовалось $35.
Вы знаете, что существует путь, который стоит всего $33,
но алгоритм Дейкстры его не находит. Алгоритм Дейкстры предположил,
что, поскольку вы обрабатываете узел «постер»,
к этому узлу невозможно добраться быстрее.
Это предположение работает только в том случае,
если ребер с отрицательным весом не существует.
Следовательно, использование алгоритма Дейкстры с графом,
содержащим ребра с отрицательным весом, невозможно.
Если вы хотите найти кратчайший путь в графе,
содержащем ребра с отрицательным весом,
для этого существует специальный алгоритм,
называемый алгоритмом Беллмана - Форда.
Рассмотрение этого алгоритма выходит за рамки этой книги,
но вы сможете найти хорошие описания в Интернете.


 Реализация

 Посмотрим , как алгоритм Дейкстры реализуется в программном коде.
Ниже изображен граф, который будет использоваться в этом примере.

 Для реализации этого примера понадобятся три хеш - таблицы.

 Хеш-таблицы стоимостей и родителей будут обновляться по ходу работы
алгоритма. Сначала необходимо реализовать граф. Как и в главе 6,
для этого будет использована хеш-таблица:

graph = {}

 В предыдущей главе все соседи узла были сохранены в хеш-таблице:

graph["you"] = ["alice", "ЬоЬ", "claire"]

 Но на этот раз необходимо сохранить как соседей,
так и стоимость перехода к соседу.
Предположим, у начального узла есть два соседа, А и В.

 Как представить веса этих ребер?
Почему бы не воспользоваться другой хеш-таблицей?

graph["start"] = {}
graph["start"]["a"] = б
graph["start"]["b"] = 2

 Итак , graph("start"] является хеш-таблицей.
Для получения всех соседей начального узла
можно воспользоваться следующим выражением:

print graph["start"].keys()
["а", "Ь"]

 Одно ребро ведет из начального узла в А,
а другое - из начального узла в В.
А если вы захотите узнать веса этих ребер?

print graph["start"]["a"]
2
print graph["start"]["b"]
б

Включим в граф остальные узлы и их соседей:
"""

graph = {"start": {}}

graph["start"]["a"] = 6
graph["start"]["b"] = 2

print(graph["start"].keys())

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

"""
 Также понадобится хеш-таблица для хранения стоимо стей всех узлов.

 Стоимость узла определяет, сколько времени потребуется 
для перехода к этому узлу от начального узла. 
Вы знаете, что переход от начального узла к узлу В занимает 2 минуты.
Вы знаете, что для перехода к узлу А требуется 6 минут 
(хотя, возможно, вы найдете более быстрый путь). 
Вы не знаете, сколько времени потребуется для достижения конечного узла.
Если стоимость еще неизвестна, она считается бесконечной. 
Можно ли представить бесконечность в Python? Оказывается, можно:
"""

infinity = float("inf")

costs = {"a": 6, "b": 2, "fin": infinity}

# Для родителей также создается отдельная таблица:
# Код создания хеш-таблицы родителей:
parents = {"a": "start", "b": "start", "in": None}

# Наконец, вам нужен массив для отслеживания всех
# уже обработанных узлов,
# так как один узел не должен обрабатываться многократно:
processed = []


# На этом подготовка завершается. Теперь обратимся к алгоритму.
# Сначала я приведу код, а потом мы разберем его более подробно .
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # Перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            # Если это узел с наименьшей стоимостью из уже виденных
            # и он еще не был обработан...
            lowest_cost = cost
            # ...он назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = node
            
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # это узел В

while node is not None:
    cost = costs[node]  # стоимость 2
    neighbors = graph[node]  # хэш-таблица
    for n in neighbors.keys():  # содержит список узлов
        new_cost = cost + neighbors[n]
        # сумма стоимости В и расстояния до А
        if costs[n] > new_cost:  # Сравним эти стоимости.
            costs[n] = new_cost  # Обновим стоимость.
            parents[n] = node
            # Новый путь проходит через узел В,
            # поэтому В назначается новым родителем.
            
    processed.append(node)
    # Порядок, мы обновили стоимости всех соседей узла В.
    # Узел помечается как обработанный.
    node = find_lowest_cost_node(costs)
    # Найти следующий узел для обработки.

'''
 Так выглядит алгоритм Дейкстры на языке Python! 
Код функции будет приведен далее, 
а пока рассмотрим пример использования алгоритма в действии.

 Найти узел с наименьшей стоимостью.
 
node = find_lowest_cost_node(costs)
 
 Получить стоимость и соседей этого узла.
 
cost = costs[node]
neighbors = graph[node]
 
 Перебрать соседей.
 
for n in neighbors.keys():
 
 У каждого узла имеется стоимость, которая определяет, 
сколько времени потребуется для достижения этого узла от начала.
Здесь мы вычисляем, сколько времени потребуется 
для достижения узла А по пути Начало > Узел В> Узел А 
(вместо Начало> Узел А).

new_cost = cost + neighbors[n]

 Сравним эти стоимости.
 
if cost[n] > new_cost:
 
 Старая стоимость перехода к А равна 6.
 
 Новая стоимость при проходе через В равна 5.
 
 Мы нашли более короткий путь к узлу А! Обновим стоимость.
 
cost[n] = new_cost
     ^       ^
     A       5
 
 Новый путь проходит через узел В, 
поэтому В назначается новым родителем.
 
parents[n] = node
        ^      ^
        A      B
 
 Мы снова вернул ись к началу цикла. 
Следующим соседом в цикле for является конечный узел.
 
for n in neighbors.key():
    ^ 
  'fin'    
 
 Сколько времени потребуется для достижения конечного узла, 
если идти через уз ел В?
 
new_cost = cost + neighbors[n]
            ^        ^
            2     расстояние от В до конца: 5
 
 Потребуется 7 минут. Предыдущая стоимость была бесконечной, 
а 7 минут определе нно меньше бесконечности.
 
if costs[n] > new_cost:
     ^            ^
бесконечность     7
(прежде стоимость достижения конечного узла была неопределена)
 
 Конечному узлу назначается новая стоимость и новый родитель.
 
costs[n] = new_cost
      ^       ^
    'fin'     7
    
parents[n] = node
        ^     ^
      'fin'   B
 
 Порядок, мы обновили стоимости всех соседей узла В. 
Узел помечается как обработанный.
 
processed.append(node)
                  ^
                  B
 
 Найти следующий узел для обработки.
 
node = find_lowest_cost_node(costs)
  ^
  A  (необработанный узел с минимальной стоимостью)
 
 Получить стоимость и соседей узла А.
 
cost = costs[node]
  ^
  5
  
neighbors = graph[node]
 
 У узла А всего один сосед: конечный узел.
 
for n in neighbors.keys():
    ^
  'fin'
 
 Время достижения конечного узла составляет 7 минут. 
Сколько времени потребуется для достижения конечного узла, 
если идти через узел А?

new_cost = cost + neighbors[n]   <----------                 
            ^                              ^
стоимость перехода к А     стоимость перехода от А 
          от начала: 5        до конечного узла: 1
                  
if costs[n] > new_cost:   <-----------------------------           
     ^                                                 ^
старая стоимость перехода    стоимость при перехое через А: 6
      к конечному узлу: 7
 
 Через узел А можно добраться быстрее! Обновим стоимость и родителя.
 
costs[n] = new_cost
      ^       ^
    'fin'     6
    
parents[n] = node
        ^      ^
      'fin'    A
 
 После того как все узлы будут обработаны, алгоритм завершается.
Надеюсь, этот пошаговый разбор помог вам чуть лучше понять алгоритм.


 Упражнения

 7.1 Каков вес кратчайшего пути от начала до конца 
в каждом из следующих графов?
 Ответ: А. 8; В. 60; С. кратчайшего пути не существует 
из-за наличия цикла с отрицательным весом.
 
 
  Поиск в ширину вычисляет кратчайший путь в невзвешенном графе.
  
  Алгоритм Дейкстры вычисляет кратчайший путь во взвешенном графе.
  
  Алгоритм Дейкстры работает только в том случае, 
если все веса положительны.
  
  При наличии отрицательных весов используйте алгоритм БеллманаФорда.
'''
