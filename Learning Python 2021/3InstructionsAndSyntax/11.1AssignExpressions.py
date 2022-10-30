"""
 Присваивание, выражения и print


 Инструкции присваивания

 Ранее мы уже использовали инструкции присваивания для назначения имен
объектам. В канонической форме цель инструкции присваивания записывается
слева от знака равно, а объект, который присваивается, – справа. Цель
слева может быть именем или компонентом объекта, а объектом справа может
быть произвольное выражение, которое в результате дает объект.
В большинстве случаев присваивание выполняется достаточно просто,
однако оно обладает следующими особенностями, которые вам следует иметь
в виду:

  Инструкция присваивания создает ссылку на объект. Как говорилось
 в главе 6, в языке Python инструкция присваивания сохраняет ссылки
 на объекты в переменных или в элементах структур данных. Они всегда
 создают ссылки на объекты и никогда не создают копии объектов.
 Вследствие этого переменные в языке Python больше напоминают указатели,
 чем области хранения данных.

  Переменные создаются при первом присваивании. Интерпретатор Python
 создает переменные, когда им впервые присваиваются значения (то есть
 ссылки на объекты), благодаря этому отсутствует необходимость
 предварительного объявления переменных. Иногда (но не всегда)
 в результате операции присваивания создаются элементы структур данных
 (например, элементы в словарях, некоторые атрибуты объектов).
 После выполнения операции присваивания всякий раз, когда имя переменной
 будет встречено в выражении, оно замещается объектом, на который
 ссылается эта переменная.

  Прежде чем переменную можно будет использовать, ей должно быть
 присвоено значение. Нельзя использовать переменную, которой еще не было
 присвоено значение. В этом случае интерпретатор возбуждает исключение
 вместо того, чтобы вернуть какое-либо значение по умолчанию, – если бы
 он возвращал значение по умолчанию, это только осложнило бы поиск
 опечаток в программном коде.

  Некоторые инструкции неявно тоже выполняют операцию присваивания.
 В этом разделе мы сосредоточим все свое внимание на инструкции =,
 однако в языке Python присваивание может выполняться в самых разных
 контекстах. Например, далее мы увидим, что импорт модуля, определение
 функции или класса, указание переменной в цикле for и передача
 аргументов функции неявно выполняют присваивание. Операция присваивания
 выполняется одинаково в любом месте, где бы она ни происходила, поэтому
 во всех этих контекстах просто выполняется связывание имен со ссылками
 на объекты.


 Формы инструкции присваивания

 Несмотря на то, что в языке Python присваивание является универсальным
и повсеместным понятием, в этой главе мы впервые сосредоточимся
на инструкциях присваивания.

  Операция                   Интерпретация
  spam = ‘Spam’              Каноническая форма

  spam, ham = ‘yum’, ‘YUM’   Присваивание кортежей (позиционное)

  [spam, ham] = [‘yum’,      Присваивание списков (позиционное)
  ‘YUM’]

  a, b, c, d = ‘spam’        Присваивание последовательностей,
                             обобщенное

  a, *b = ‘spam’             Расширенная операция распаковывания
                             последовательностей (Python 3.0)

  spam = ham = ‘lunch’       Групповое присваивание одного значения

  spams += 42                Комбинированная инструкция присваивания
                             (эквивалентно инструкции
                             spams = spams + 42)

 Первая форма из табл. является наиболее распространенной: она
связывает переменную (или элемент структуры данных) с единственным
объектом. Другие формы в таблице имеют особое назначение и являются
необязательными, но многие программисты находят очень удобными:

 Присваивание кортежей и списков

  Вторая и третья формы в таблице являются родственными. Когда слева
 от оператора = указывается кортеж или список, интерпретатор связывает
 объекты справа с именами слева, согласно их местоположениям, выполняя
 присваивание слева направо. Например, во второй строке табл. с именем
 spam ассоциируется строка ‘yum’, а с именем ham ассоциируется строка
‘YUM’. Внутри интерпретатор Python сначала создает элементы кортежа
 справа, поэтому часто эта операция называется распаковыванием кортежа.

 Присваивание последовательностей

  В недавних версиях Python операции присваивания кортежей и списков
 были обобщены в то, что теперь называется операцией присваивания
 последовательностей, – любая последовательность имен может быть связана
 с любой последовательностью значений, и интерпретатор свяжет элементы
 согласно их позициям. Фактически в последовательностях мы можем
 смешивать разные типы. Инструкция присваивания в четвертой строке
 табл., например, связывает кортеж имен со строкой символов:
 имени a присваивается символ ‘s’, имени b присваивается символ ‘p’
 и так далее.

 Расширенное распаковывание последовательностей

  В Python 3.0 появилась новая форма инструкции присваивания,
 позволяющая более гибко выбирать присваиваемые фрагменты
 последовательностей. В пятой строке табл. 11.1, например, переменной
 a будет присвоен первый символ из строки справа, а переменной b –
 оставшаяся часть строки, то есть переменной a будет присвоено значение
 ‘s’, а переменной b – значение ‘pam’. В результате мы получаем простую
 альтернативу операции извлечения срезов.

 Групповое присваивание одного значения

  Шестая строка в табл. демонстрирует форму группового присваивания.
 В этой форме интерпретатор присваивает ссылку на один и тот же объект
 (самый правый объект) всем целям, расположенным слева. Инструкция
 в таблице присвоит обоим именам spam и ham ссылку на один и тот же
 объект, строку ‘lunch’. Результат будет тот же, как если бы были
 выполнены две инструкции: ham = ‘lunch’ и spam = ham, поскольку здесь
 ham интерпретируется как оригинальный объект-строка (то есть
 не отдельная копия этого объекта).

 Групповое присваивание одного значения

  Последняя строка в табл. – это пример комбинированной инструкции
 присваивания – краткая форма, которая объединяет в себе выражение
 и присваивание. Например, инструкция spam += 42 даст тот же результат,
 что и инструкция spam = spam + 42; единственное отличие состоит в том,
 что комбинированная форма имеет более компактный вид и обычно
 выполняется быстрее. Кроме того, если объект справа относится
 к категории изменяемых объектов и поддерживает указанную операцию,
 комбинированная инструкция присваивания может выполняться даже быстрее,
 за счет непосредственного изменения объекта вместо создания и изменения
 его копии. Для каждого двухместного оператора в языке Python существует
 своя комбинированная инструкция присваивания.


 Присваивание последовательностей

 В этой книге мы уже использовали инструкцию присваивания в канонической
форме. Ниже приводится несколько примеров инструкций присваивания
последовательностей в действии:

python
\>>> nudge = 1
\>>> wink = 2
\>>> A, B = nudge, wink  # Присваивание кортежей
\>>> A, B  # Что равносильно A = nudge; B = wink
(1, 2)
\>>> [C, D] = [nudge, wink]  # Присваивание списков
\>>> C, D
(1, 2)

 Обратите внимание: в третьей инструкции этого примера
в действительности присутствует два кортежа, просто мы опустили
охватывающие их круглые скобки. Интерпретатор Python сопоставляет
значения элементов кортежа справа от оператора присваивания
с переменными в кортеже слева и выполняет присваивание значений
в одной инструкции.

 Операция присваивания кортежей дает возможность использовать прием,
который представлен в упражнениях ко второй части книги. Так как
в процессе выполнения инструкции интерпретатор создает временный кортеж,
где сохраняются оригинальные значения переменных справа, данная форма
присваивания может использоваться для реализации обмена значений
переменных без создания временной переменной – кортеж справа
автоматически запоминает предыдущие значения переменных:

\>>> nudge = 1
\>>> wink = 2
\>>> nudge, wink = wink, nudge  # Кортежи: обмен значениями
\>>> nudge, wink  # То же, что и T = nudge; nudge = wink; wink = T
(2, 1)

 В конечном итоге формы присваивания кортежей и списков были обобщены,
чтобы обеспечить возможность указывать любые типы последовательностей
справа при условии, что они будут иметь ту же длину. Допускается
присваивать кортеж значений списку переменных, строки символов – кортежу
переменных и так далее. В любом случае интерпретатор свяжет элементы
последовательности справа с переменными в последовательности слева
согласно их позициям в направлении слева направо:

\>>> [a, b, c] = (1, 2, 3)  # Кортеж значений присваивается
\>>> a, c                   # списку переменных
(1, 3)
\>>> (a, b, c) = “ABC”  # Строка символов присваивается
\>>> a, c               # кортежу переменных
(‘A’, ‘C’)

 С технической точки зрения в правой части инструкции присваивания
последовательностей допускается указывать не только последовательности,
но и любые объекты, обеспечивающие возможность итераций по элементам.
Эту, еще более общую концепцию, мы будем рассматривать в главах 14 и 20.


 Дополнительные варианты инструкции присваивания последовательностей

 Даже при том, что допускается смешивать разные типы последовательностей
по обе стороны оператора =, обе последовательности должны иметь одно
и то же число элементов, в противном случае мы получим сообщение
об ошибке.

 В Python 3.0 допускается использовать еще более обобщенную форму
присваивания, применяя расширенный синтаксис распаковывания
последовательностей, который описывается в следующем разделе. Но,
как правило (и всегда в Python 2.X), количество переменных слева должно
соответствовать количеству элементов последовательности справа:

\>>> string = ‘SPAM’
\>>> a, b, c, d = string  # Одинаковое число элементов с обеих сторон
\>>> a, d
(‘S’, ‘M’)
\>>> a, b, c = string  # В противном случае выводится
# сообщение об ошибке
...текст сообщения об ошибке опущен...
ValueError: too many values to unpack

 В общем случае нам необходимо получить срез. Существует несколько
вариантов извлечения среза, чтобы исправить дело:

\>>> a, b, c = string[0], string[1], string[2:]  # Элементы и срез
\>>> a, b, c
(‘S’, ‘P’, ‘AM’)

\>>> a, b, c = list(string[:2]) + [string[2:]]  # Срезы и конкатенация
\>>> a, b, c
(‘S’, ‘P’, ‘AM’)

\>>> a, b = string[:2]  # То же самое, только проще
\>>> c = string[2:]
\>>> a, b, c
(‘S’, ‘P’, ‘AM’)

\>>> (a, b), c = string[:2], string[2:]  # Вложенные последовательности
\>>> a, b, c
(‘S’, ‘P’, ‘AM’)

 Последний пример демонстрирует, что мы можем присваивать даже вложенные
последовательности, и интерпретатор распаковывает их части
в соответствии с представлением, как и ожидается. В данном случае
выполняется присваивание кортежа из двух элементов, где первый элемент –
это вложенная последовательность (строка), что точно соответствует
следующему случаю:

\>>> ((a, b), c) = (‘SP’, ‘AM’)  # Связывание производится
\>>> a, b, c   # в соответствии с формой и местоположением
(‘S’, ‘P’, ‘AM’)

 Интерпретатор связывает первую строку справа (‘SP’) с первым кортежем
слева ((a, b)), присваивая каждому его элементу по одному символу,
а затем выполняет присваивание второй строки целиком (‘AM’)
переменной c. В этом случае вложенная последовательность слева, имеющая
форму объекта, должна соответствовать объекту справа. Присваивание
вложенных последовательностей - это достаточно сложная операция, которая
редко встречается на практике, но такой способ присваивания может
оказаться удобным для присваивания части структуры данных
известной формы.

 Например, как будет показано в главе 13, этот прием можно использовать
в циклах for для присваивания элементов итерируемой последовательности
нескольким переменным, указанным в инструкции цикла:

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: ...  # Простое присваивание
                                              # кортежей
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: ...  # Присваивание
                                                    # вложенных кортежей

 В главе 18 мы увидим, что форма присваивания вложенных кортежей
(в действительности – последовательностей) может также использоваться
в списках аргументов функций в Python 2.6 (но не в Python 3.0),
потому что передача аргументов выполняется присваиванием
для распаковывания списков аргументов функций:

def f(((a, b), c)):  # Для распаковывания аргументов в Python 2.6,
f(((1, 2), 3))       # но не в 3.0

 Кроме того, операция присваивания последовательности с распаковыванием
дает начало еще одному распространенному обороту программирования на
языке Python – присваиванию последовательности целых чисел множеству
переменных:

\>>> red, green, blue = range(3)
\>>> red, blue
(0, 2)

 В этом примере три переменные инициализируются целочисленными
значениями 0, 1 и 2 соответственно (это эквивалент перечислимых типов
данных в языке Python, которые, возможно, вам приходилось встречать
в других языках программирования). Чтобы понять происходящее, вы должны
знать, что встроенная функция range генерирует непрерывный список
последовательных целых чисел:

\>>> range(3) # Используйте list(range(3)) в Python 3.0
[0, 1, 2]

 Поскольку функция range часто используется в циклах for, мы еще
поговорим о ней в главе 13.

 Другой случай применения операции присваивания кортежей – разделение
последовательности на начальную и остальную части в циклах, как показано
ниже:

\>>> L = [1, 2, 3, 4]
\>>> while L:
... front, L = L[0], L[1:]  # Вариант для 3.0 приводится в след. разделе
... print(front, L)
...
1 [2, 3, 4]
2 [3, 4]
3 [4]
4 []

 Присваивание кортежа в цикле здесь можно было бы заменить двумя
следующими строками, но часто бывает удобнее объединить их
в одну строку:

... front = L[0]
... L = L[1:]

 Обратите внимание: в этом примере список используется в качестве
стека – структуры данных, поведение которой реализуют методы списков
append и pop.

 В данном случае эффект, который дает операция присваивания кортежа,
можно было бы получить инструкцией front = L.pop(0), но это будет
операция непосредственного изменения объекта. О циклах while и о других
(часто лучших) способах обхода последовательностей с помощью циклов for
вы узнаете больше в главе 13.


 Расширенная операция распаковывания последовательностей в Python 3.0

 В предыдущем примере демонстрировалось, как вручную организовать
извлечение срезов, чтобы сделать инструкцию присваивания
последовательностей более универсальной. В Python 3.0 (но не в 2.6)
инструкция присваивания последовательностей была обобщена еще больше,
что еще больше упростило ее использование. В двух словах: чтобы описать
более общий случай присваивания, слева от оператора присваивания
допускается указывать одно имя со звездочкой, например *X, –
имени со звездочкой будет присвоен список всех элементов
последовательности, не присвоенных другим переменным слева. Это особенно
удобно для реализации таких распространенных операций, как разбиение
последовательности на «начало» и «остаток», как было показано
в последнем примере предыдущего раздела.


 Расширенная операция распаковывания в действии

 Рассмотрим пример. Как мы уже знаем, в операции распаковывания
последовательностей количество имен слева от оператора присваивания
должно точно соответствовать количеству элементов в последовательности
справа. При несоблюдении этого правила мы будем получать сообщение
об ошибке (если вручную не предусмотрим извлечение срезов
из последовательности справа, как было показано в предыдущем разделе):

C:\misc> c:\python30\python
\>>> seq = [1, 2, 3, 4]
\>>> a, b, c, d = seq
\>>> print(a, b, c, d)
1 2 3 4
\>>> a, b = seq
ValueError: too many values to unpack

 Однако в Python 3.0 в списке переменных слева можно указать одно имя
со звездочкой, чтобы ослабить правило соответствия. В представленном
ниже продолжении предыдущего интерактивного сеанса переменной a
присваивается первый элемент последовательности, а переменной b –
все остальные:

\>>> a, *b = seq
\>>> a
1
\>>> b
[2, 3, 4]

 Когда в левой части инструкции присутствует имя со звездочкой,
количество переменных в левой части необязательно должно
соответствовать количеству элементов в последовательности справа.
Фактически имя со звездочкой может указываться в любой позиции слева.
Например, в примере ниже переменной b соответствует последний элемент
последовательности, а переменной a – все элементы, предшествующие
последнему:

\>>> *a, b = seq
\>>> a
[1, 2, 3]
\>>> b
4

 Когда имя со звездочкой указывается в середине списка переменных,
ей присваиваются все элементы последовательности справа, которые
остаются после присваивания остальным переменным без звездочек.
То есть в следующем примере переменным a и c будут присвоены первый
и последний элементы, а переменной b – все остальные, что находятся
между ними:

\>>> a, *b, c = seq
\>>> a
1
\>>> b
[2, 3]
\>>> c
4

 В более широком смысле, в какой бы позиции ни появлялась переменная
со звездочкой, ей будет присвоен список, содержащий все не присвоенные
элементы, соответствующие этой позиции:

\>>> a, b, *c = seq
\>>> a
1
\>>> b
2
\>>> c
[3, 4]

 Естественно, как и обычная операция присваивания последовательностей,
расширенная операция распаковывания последовательностей может
применяться к последовательностям любых типов, не только к спискам.
Ниже приводится пример распаковывания символов строки:

\>>> a, *b = ‘spam’
\>>> a, b
(‘s’, [‘p’, ‘a’, ‘m’])
\>>> a, *b, c = ‘spam’
\>>> a, b, c
(‘s’, [‘p’, ‘a’], ‘m’)

 Этот прием напоминает способ, основанный на извлечении срезов, но это
не совсем одно и то же – инструкция присваивания последовательностей
всегда возвращает список с множеством соответствующих элементов,
тогда как операция извлечения среза возвращает последовательность
того же типа, что и последовательность, из которой извлекается срез:

\>>> S = ‘spam’
\>>> S[0], S[1:]  # Тип среза зависит от типа исходной
(‘s’, ‘pam’)  #  последовательности, расширенная операция распаковывания
\>>> S[0], S[1:3], S[3]                       # всегда возвращает список
(‘s’, ‘pa’, ‘m’)

 Используя эту новую возможность, появившуюся в Python 3.0,
применительно к спискам, мы можем еще больше упростить последний пример
из предыдуще


 Граничные случаи

 Расширенная операция распаковывания последовательностей обладает
достаточной гибкостью, тем не менее нам следует отметить некоторые
граничные случаи. Во-первых, переменной со звездочкой может
соответствовать единственный элемент, но ей всегда присваивается список:

\>>> seq
[1, 2, 3, 4]
\>>> a, b, c, *d = seq
\>>> print(a, b, c, d)
1 2 3 [4]

 Во-вторых, если на долю переменной со звездочкой не остается
неприсвоенных элементов, ей присваивается пустой список, независимо
от того, в какой позиции эта переменная находится. В следующем примере
каждой из переменных a, b, c и d соответствует свой элемент
последовательности, но вместо того, чтобы возбудить исключение,
интерпретатор присваивает переменной e пустой список:

\>>> a, b, c, d, *e = seq
\>>> print(a, b, c, d, e)
1 2 3 4 []
\>>> a, b, *e, c, d = seq
\>>> print(a, b, c, d, e)
1 2 3 4 []

 Наконец, ошибкой будет считаться, если указать несколько переменных
со звездочкой; если значений окажется недостаточно, а слева не окажется
переменной со звездочкой (как и ранее) и если переменная со звездочкой
окажется единственной вне последовательности:

\>>> a, *b, c, *d = seq
SyntaxError: two starred expressions in assignment

\>>> a, b = seq
ValueError: too many values to unpack

\>>> *a = seq
SyntaxError: starred assignment target must be in a list or tuple

\>>> *a, = seq
\>>> a
[1, 2, 3, 4]


 Полезное удобство

 Имейте в виду, что расширенная операция распаковывание
последовательностей – это всего лишь удобство. Мы можем добиться того же
эффекта, используя явно операции индексирования и извлечения среза
(и фактически эту альтернативу придется использовать в Python 2.X),
но расширенная инструкция распаковывания выглядит компактнее.
Типичный прием разбиения последовательности «первый, остаток», например,
можно реализовать тем или иным способом, но операция извлечения среза
более трудозатратна:

\>>> seq
[1, 2, 3, 4]
\>>> a, *b = seq  # Первый, остаток
\>>> a, b
(1, [2, 3, 4])
\>>> a, b = seq[0], seq[1:]  # Первый, остаток: традиционная реализация
\>>> a, b
(1, [2, 3, 4])

 Прием разбиения последовательности «остаток, последний» может быть
реализован похожим способом, но с применением новой расширенной
инструкции распаковывания последовательностей требуется заметно меньшее
количество нажатий на клавиши:

\>>> *a, b = seq  # Остаток, последний
\>>> a, b
([1, 2, 3], 4)
\>>> a, b = seq[:-1], seq[-1]  # Остаток, последний:
\>>> a, b                      # традиционная реализация
([1, 2, 3], 4)

 Расширенная инструкция распаковывания последовательностей выглядит
не только проще, но и естественнее, поэтому со временем она наверняка
получит широкое распространение в программах на языке Python.


 Использование в циклах for

 Поскольку переменные цикла в инструкции for также участвуют
в присваивании, расширенная операция распаковывания последовательностей
может применяться и к ним. Мы уже немного познакомились с инструкцией
for во второй части книги и продолжим знакомство с ней в главе 13.
В Python 3.0 расширенная инструкция распаковывания может помещаться
после слова for, где обычно указывается простое имя переменной:

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
...

 При таком использовании в каждой итерации интерпретатор будет просто
присваивать очередной кортеж значений кортежу переменных. На первом
проходе, например, будет выполнено присваивание, как если бы оно было
реализовано в виде выражения:

a, *b, c = (1, 2, 3, 4)  # Переменная b получит значение [2, 3]

 Переменные a, b и c можно использовать в теле цикла для ссылки
на извлеченные компоненты. В действительности в этом вообще нет ничего
особенного – это лишь разновидность более общей операции присваивания.
Как мы видели выше в этой главе, того же эффекта можно добиться
с помощью простой операции присваивания кортежей в обеих версиях
Python 2.X и 3.X:

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: # a, b, c = (1, 2, 3), ...

 И мы всегда сможем имитировать поведение расширенной инструкции
распаковывания последовательностей в Python 2.6, применив операцию
извлечения среза:

for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
a, b, c = all[0], all[1:3], all[3]

 Мы пока недостаточно подготовлены к анализу подробностей синтаксиса
цикла for, поэтому мы еще вернемся к этой теме в главе 13.


 Групповое присваивание

 При групповом присваивании объект, расположенный справа, присваивается
всем указанным переменным. В следующем примере трем переменным a, b и c
присваивается строка ‘spam’:

\>>> a = b = c = ‘spam’
\>>> a, b, c
(‘spam’, ‘spam’, ‘spam’)

 Эта инструкция эквивалентна (но записывается компактнее) следующим трем
инструкциям присваивания:

\>>> c = ‘spam’
\>>> b = c
\>>> a = b


 Групповое присваивание и разделяемые ссылки

 Имейте в виду, что в этом случае существует всего один объект,
разделяемый всеми тремя переменными (все они указывают на один и тот же
объект в памяти). Такой способ присваивания хорошо подходит
для неизменяемых объектов, например для инициализации нескольких
счетчиков нулевым значением (не забывайте, что в языке Python переменная
должна быть инициализирована, прежде чем к ней можно будет обратиться,
поэтому вам всегда придется устанавливать начальные значения
в счетчиках, прежде чем они смогут использоваться для счета):

\>>> a = b = 0
\>>> b = b + 1
\>>> a, b
(0, 1)

 Здесь изменение переменной b затронет только переменную b, потому что
числа не допускают возможность непосредственного изменения. Если
присваиваемый объект является неизменяемым, совершенно не важно,
как много ссылок на него будет создано.

 Но, как обычно, следует проявлять осторожность, выполняя присваивание
переменным изменяемых объектов, таких как списки или словари:

\>>> a = b = []
\>>> b.append(42)
\>>> a, b
([42], [42])

 На этот раз, поскольку a и b ссылаются на один и тот же объект,
непосредственное добавление значения к объекту через переменную b будет
воздействовать и на переменную a. В действительности это всего лишь
другой пример взаимовлияния разделяемых ссылок, с которым мы впервые
встретились в главе 6.

 Чтобы избежать этой проблемы, инициализацию изменяемыми объектами
следует производить в отдельных инструкциях, чтобы в каждой из них
создавался новый пустой объект с помощью от дельных литеральных
выражений:

\>>> a = []
\>>> b = []
\>>> b.append(42)
\>>> a, b
([], [42])


 Комбинированные инструкции присваивания

 Начиная с версии Python 2.0, в языке появился набор дополнительных
инструкций присваивания, перечисленных в табл. 11.2. Известные как
комбинированные инструкции присваивания и заимствованные из языка C,
они по существу являются лишь более компактной формой записи. Они
комбинируют в себе выражение и операцию присваивания. Например,
следующие две формы записи практически эквивалентны:

X = X + Y  # Традиционная форма записи
X += Y   # Новая, комбинированная форма записи

  X += Y   X &= Y   X -= Y   X |= Y
  X *= Y   X ^= Y   X /= Y   X >>= Y
  X %= Y   X <<= Y  X **= Y  X //= Y

 Комбинированные операции присваивания существуют для любого
поддерживаемого двухместного оператора. Например, ниже приводится два
способа прибавления 1 к значению переменной:

\>>> x = 1
\>>> x = x + 1  # Традиционная форма записи
\>>> x
2
\>>> x += 1  # Комбинированная
\>>> x
3

 Если комбинированную инструкцию применить к строкам, будет выполнена
операция конкатенации. Таким образом, вторая строка ниже эквивалентна
более длинной инструкции S = S + “SPAM”:

\>>> S = “spam”
\>>> S += “SPAM”  # Выполняется операция конкатенации
\>>> S
‘spamSPAM’

 Как показано в табл. 11.2, для каждого двухместного оператора
(то есть для оператора, слева и справа от которого располагаются
значения, участвующие в операции) в языке Python существует своя
комбинированная инструкция присваивания. Например, инструкция X *= Y
выполняет умножение и присваивание, X >>= Y – сдвиг вправо
и присваивание, и так далее. Инструкция X //= Y (деление
с округлением вниз) была добавлена в версии Python 2.2. Комбинированные
инструкции присваивания обладают следующими преимуществами:

  Уменьшается объем ввода с клавиатуры. Нужно ли мне продолжать?

  Левая часть инструкции должна быть получена всего один раз.
 В инструкции «X += Y» X может оказаться сложным выражением, которое
 в комбинированной форме должно быть вычислено всего один раз. В более
 длинной форме записи «X = X + Y» X появляется дважды, и поэтому данное
 выражение должно быть вычислено дважды. Вследствие этого
 комбинированные инструкции присваивания выполняются обычно быстрее.

  Автоматически выбирается оптимальный алгоритм выполнения.
 Для объектов, поддерживающих возможность непосредственного изменения,
 комбинированные инструкции присваивания автоматически выполняются
 непосредственно на самих объектах, вместо выполнения более медленной
 операции копирования.

 И последний момент, который требует дополнительных разъяснений.
Комбинированные инструкции присваивания, при применении к изменяемым
объектам, могут служить для оптимизации. Вспомним, что списки могут
расширяться разными способами. Чтобы добавить в список единственный
элемент, мы можем выполнить операцию конкатенации или вызвать
метод append:

\>>> L = [1, 2]
\>>> L = L + [3]  # Конкатенация: более медленная
\>>> L
[1, 2, 3]
\>>> L.append(4)  # Более быстрая, но изменяет сам объект
\>>> L
[1, 2, 3, 4]

 А чтобы добавить несколько элементов, мы можем либо снова выполнить
операцию конкатенации, либо вызвать метод extend:

\>>> L = L + [5, 6]  # Конкатенация: более медленная
\>>> L
[1, 2, 3, 4, 5, 6]
\>>> L.extend([7, 8])  # Более быстрая, но изменяет сам объект
\>>> L
[1, 2, 3, 4, 5, 6, 7, 8]

 В обоих случаях операция конкатенации несет в себе меньше побочных
эффектов при работе с разделяемыми ссылками на объекты, но вообще она
выполняется медленнее, чем эквивалентные операции, воздействующие
на объект непосредственно. Операция конкатенации должна создать новый
объект, копию списка слева, и затем скопировать в него список справа.
В противовес ей метод, воздействующий на объект непосредственно, просто
добавляет новый элемент в конец блока памяти.

 При использовании комбинированной инструкции присваивания
для расширения списка мы можем не думать об этих деталях – интерпретатор
Python автоматически вызовет более быстрый метод extend вместо
использования более медленной операции конкатенации, которую
предполагает оператор +:

\>>> L += [9, 10]  # Выполняется как L.extend([9, 10])
\>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 Комбинированные инструкции присваивания и разделяемые ссылки

 Такой порядок вещей чаще всего именно то, что нам требуется,
но необходимо учитывать – он предполагает, что применительно к спискам
операция += выполняет изменения непосредственно в объекте, а это далеко
не то же самое, что операция конкатенации +, в результате которой всегда
создается новый объект. Как всегда, в случае использования разделяемых
ссылок, различия в поведении этих операций могут иметь значение,
если имеются другие ссылки на изменяемый объект:

\>>> L = [1, 2]
\>>> M = L  # L и M ссылаются на один и тот же объект
\>>> L = L + [3, 4]  # Операция конкатенации создает новый объект
\>>> L, M  # Изменяется L, но не M
([1, 2, 3, 4], [1, 2])

\>>> L = [1, 2]
\>>> M = L
\>>> L += [3, 4]  # Операция += предполагает вызов метода extend
\>>> L, M  # Значение M тоже изменилось!
([1, 2, 3, 4], [1, 2, 3, 4])

 Все это имеет значение только для изменяемых объектов, таких как списки
и словари, и к тому же это не совсем ясный случай (по крайней мере,
пока его влияние не скажется на вашем программном коде!). Если вам
требуется избежать создания системы разделяемых ссылок, создавайте копии
изменяемых объектов.
"""