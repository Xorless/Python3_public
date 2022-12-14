"""
 Итерации и генераторы, часть 1


 Итераторы: первое знакомство

 В предыдущей главе упоминалось, что цикл for может работать
с последовательностями любого типа, включая списки, кортежи и строки,
например:

\>>> for x in [1, 2, 3, 4]: print(x ** 2, end=’ ‘)
...
1 4 9 16
\>>> for x in (1, 2, 3, 4): print(x ** 3, end=’ ‘)
...
1 8 27 64
\>>> for x in ‘spam’: print(x * 2, end=’ ‘)
...
ss pp aa mm

 Фактически цикл for имеет еще более универсальную природу, чем было
показано, – он способен работать с любыми итерируемыми объектами,
поддерживающими возможность выполнения итераций. На самом деле это верно
для всех средств выполнения итераций, которые выполняют сканирование
объектов слева направо, включая циклы for, генераторы списков, оператор
in проверки на вхождение, встроенную функцию map и другие.

 Понятие «итерируемого объекта» является относительно новым
в языке Python, но оно успело прочно внедриться в модель языка.
По существу оно является обобщением понятия последовательности – объект
считается итерируемым, либо если он физически является
последовательностью, либо если он является объектом, который
воспроизводит по одному результату за раз в контексте инструментов
выполнения итераций, таких как цикл for. В некотором смысле в категорию
итерируемых объектов входят как физические последовательности,
так и последовательности виртуальные, которые вычисляются по требованию.


 Протокол итераций: итераторы файлов

 Один из самых простых способов понять, что такое итераторы, – это
посмотреть, как они работают со встроенными типами, такими как файлы.
В главе 9 говорилось, что объекты открытых файлов имеют метод с именем
readline, который читает по одной строке текста из файла за одно
обращение – каждый раз, вызывая метод readline, мы перемещаемся
к следующей строке. По достижении конца файла возвращается пустая
строка, что может служить сигналом для выхода из цикла:

\>>> f = open(‘script1.py’)  # Прочитать 4 строки из файла сценария
\>>> f.readline()  # Метод readline загружает одну строку
‘import sys\n’
\>>> f.readline()
‘print(sys.path)\n’
\>>> f.readline()
‘x = 2\n’
\>>> f.readline()
‘print(2 ** 33)\n’
\>>> f.readline()  # Вернет пустую строку по достижении конца файла
‘’


 Кроме того, файлы имеют также метод __next__, который производит
практически тот же эффект, – всякий раз, когда его вызывают,
он возвращает следующую строку. Единственное значимое различие состоит
в том, что по достижении конца файла метод __next__ возбуждает
встроенное исключение StopIteration вместо того, чтобы возвращать
пустую строку:

\>>> f = open(‘script1.py’)  # Метод __next__ загружает одну строку
\>>> f.__next__()  # и возбуждает исключение по достижении конца файла
‘import sys\n’
\>>> f.__next__()
‘print(sys.path)\n’
\>>> f.__next__()
‘x = 2\n’
\>>> f.__next__()
‘print(2 ** 33)\n’
\>>> f.__next__()
Traceback (most recent call last):
  ...текст сообщения об ошибке опущен...
StopIteration

 Такое поведение в точности соответствует тому, что мы в языке Python
называем протоколом итераций, – объект реализует метод __next__, который
возвращает следующее значение и возбуждает исключение StopIteration
в конце серии результатов. Подобные объекты в языке Python считаются
итерируемыми. Любой такой объект доступен для сканирования с помощью
цикла for или других итерационных инструментов, потому что все
инструменты выполнения итераций вызывают метод __next__ в каждой
итерации и определяют момент выхода по исключению StopIteration.

 Следствие всего вышесказанного: лучший способ построчного чтения
текстового файла, как уже упоминалось в главе 9, состоит не в том,
чтобы прочитать его целиком, а в том, чтобы позволить циклу for
автоматически вызывать метод __next__ для перемещения к следующей строке
в каждой итерации. Например, следующий фрагмент читает содержимое файла
строку за строкой (попутно приводит символы к верхнему регистру
и выводит их) без явного обращения к методам файла:

\>>> for line in open(‘script1.py’):  # Использовать итератор файла
... print(line.upper(), end=’’)  # Вызывает метод __next__,
...                # перехватывает исключение StopIteration
IMPORT SYS
PRINT(SYS.PATH)
X = 2
PRINT(2 ** 33)

 Обратите внимание на аргумент end=’’ в вызове функции print; он
подавляет вывод символа \n, потому что строки, прочитанные из файла,
уже содержат этот символ (если этот аргумент опустить, выводимые строки
будут перемежаться пустыми строками). Такой способ построчного чтения
текстовых файлов считается лучшим по трем причинам: программный код
выглядит проще, он выполняется быстрее и более экономно использует
память. Более старый способ достижения того же эффекта с помощью цикла
for состоит в том, чтобы вызвать метод readlines для загрузки
содержимого файла в память в виде списка строк:

\>>> for line in open(‘script1.py’).readlines():
...     print(line.upper(), end=’’)
...
IMPORT SYS
PRINT SYS.PATH
X = 2
PRINT 2 ** 33

 Способ, основанный на использовании метода readlines, по-прежнему может
использоваться, но на сегодня он проигрывает из-за неэкономного
использования памяти. Так как в этом случае файл загружается целиком,
данный способ не позволит работать с файлами, слишком большими, чтобы
поместиться в память компьютера. При этом версия, основанная
на применении итераторов, не подвержена таким проблемам с памятью,
так как содержимое файла считывается по одной строке за раз. Кроме того,
способ на базе итераторов должен иметь более высокую производительность,
хотя это во многом может зависеть от версии (в Python 3.0 это
преимущество становится менее очевидным из-за того, что библиотека
ввода-вывода была полностью переписана с целью обеспечить поддержку
Юникода и сделать ее еще более платформно-зависимой).

 Как упоминалось во врезке «Придется держать в уме: сканирование файлов»
в предыдущей главе, существует возможность построчного чтения файлов
с помощью цикла while:

\>>> f = open(‘script1.py’)
\>>> while True:
...     line = f.readline()
...     if not line: break
...     print(line.upper(), end=’’)
...
...вывод тот же самый...

 Однако такой вариант наверняка будет работать медленнее версии,
основанной на использовании итератора в цикле for, потому что итераторы
внутри интерпретатора выполняются со скоростью, присущей программам,
написанным на языке C, тогда как версия на базе цикла while работает
со скоростью интерпретации байт-кода виртуальной машиной Python.
Всякий раз, когда код на языке Python подменяется кодом на языке C,
скорость его выполнения обычно увеличивается. Однако это не всегда так,
особенно в Python 3.0; далее в книге будут представлены приемы оценки
времени выполнения, позволяющие измерить относительную скорость
выполнения вариантов, подобных этим.


 Выполнение итераций вручную: iter и next

 Для поддержки возможности выполнения итераций вручную (и уменьшения
объема ввода с клавиатуры) в Python 3.0 имеется встроенная функция next,
которая автоматически вызывает метод __next__ объекта. Допустим,
что у нас имеется итерируемый объект X, тогда вызов next(X) будет
равносилен вызову X.__next__(), но выглядит намного проще. Применительно
к файлам, например, можно использовать любую из этих двух форм:

\>>> f = open(‘script1.py’)
\>>> f.__next__()  # Непосредственный вызов метода
‘import sys\n’
\>>> f.__next__()
‘print(sys.path)\n’

\>>> f = open(‘script1.py’)
\>>> next(f)  # Встроенная функция next вызовет метод __next__
‘import sys\n’
\>>> next(f)
‘print(sys.path)\n’

 С технической точки зрения итерационный протокол имеет еще одну
сторону. В самом начале цикл for получает итератор из итерируемого
объекта, передавая его встроенной функции iter, которая возвращает
объект, имеющий требуемый метод __next__. Это станет более очевидным,
если посмотреть, на то, как внутренние механизмы циклов for обрабатывают
такие встроенные типы последовательностей как списки:

\>>> L = [1, 2, 3]
\>>> I = iter(L)  # Получить объект-итератор
\>>> I.__next__()  # Вызвать __next__, чтобы перейти к следующему
1                  # элементу
\>>> I.__next__()
2
\>>> I.__next__()
3
\>>> I.__next__()
Traceback (most recent call last):
...текст сообщения об ошибке опущен...
StopIteration

 При работе с файлами этот начальный этап не нужен, потому что объект
файла имеет собственный итератор. То есть объекты файлов имеют
собственный метод __next__, и потому для работы с файлами не требуется
получать другой объект:

\>>> f = open(‘script1.py’)
\>>> iter(f) is f
True
\>>> f.__next__()
‘import sys\n’

 Списки и многие другие встроенные объекты не имеют собственных
итераторов, потому что они поддерживают возможность участия сразу
в нескольких итерациях. Чтобы начать итерации по таким объектам,
необходимо предварительно вызвать функцию iter:

\>>> L = [1, 2, 3]
\>>> iter(L) is L
False
\>>> L.__next__()
AttributeError: ‘list’ object has no attribute ‘__next__’

\>>> I = iter(L)
\>>> I.__next__()
1
\>>> next(I)  # То же, что и вызов метода I.__next__()
2

 Инструменты итераций в языке Python вызывают эти функции автоматически,
однако мы также можем пользоваться ими при выполнении итераций вручную.
Следующий фрагмент наглядно демонстрирует эквивалентность
автоматического и ручного способов организации итераций.

 Строго говоря, цикл for вызывает внутренний эквивалент метода
I.__next__, а не функцию next(I), которая используется в примере.
Различия между ними весьма незначительны, но, как мы увидим в следующем
разделе, в версии 3.0 имеются встроенные объекты
(такие, как возвращаемое значение функции os.popen), поддерживающие
первый вариант и не поддерживающие второй, и при этом они обеспечивают
возможность обхода с помощью цикла for. Вообще говоря,
при реализации итераций вручную, вы можете использовать
любую схему вызова. Если вам интересно, в версии 3.0 объект,
возвращаемый функцией os.popen, был переписан
с использованием модуля subprocess и класса-обертки.
Его метод __getattr__ больше не вызывается в версии 3.0
при неявном обращении к методу __next__ из встроенной функции next,
но он вызывается при явном обращении по имени – это изменение
в версии 3.0, которое будет рассматриваться в главах 37 и 38,
затронуло даже программный код в стандартной библиотеке! Кроме того,
в Python 3.0 были ликвидированы родственные функции os.popen2/3/4,
имевшиеся в Python 2.6, – теперь вместо них следует использовать
функцию subprocess. Popen с соответствующими аргументами
(за дополнительными сведениями обращайтесь к руководству
по стандартной библиотеке Python 3.0).

\>>> L = [1, 2, 3]
\>>>
\>>> for X in L:  # Автоматический способ выполнения итераций
... print(X ** 2, end=’ ‘)  # Получает итератор, вызывает __next__,
...                         # обрабатывает исключение
1 4 9

\>>> I = iter(L)  # Ручной способ итераций: имитация цикла for
\>>> while True:
... try:  # Инструкция try обрабатывает исключения
... X = next(I)  # Или I.__next__
... except StopIteration:
... break
... print(X ** 2, end=’ ‘)
...
1 4 9

 Чтобы понять, как действует этот программный код, необходимо знать,
что инструкция try выполняет операцию и перехватывает исключения,
которые могут возникнуть в ходе этой операции (мы будем исследовать
исключения в седьмой части книги). Следует также отметить, что цикл for
и другие средства выполнения итераций иногда могут действовать иначе,
при работе с пользовательскими классами, многократно производя операцию
индексирования объекта вместо использования протокола итераций.
Обсуждение этой особенности мы отложим до тех пор, пока в главе 29
не познакомимся с возможностью перегрузки операторов.


 Другие итераторы встроенных типов

 Кроме файлов и фактических последовательностей, таких как списки,
удобные итераторы также имеют и другие типы. Классический способ
выполнить обход всех ключей словаря, например, состоит в том, чтобы явно
запросить список ключей:

\>>> D = {‘a’:1, ‘b’:2, ‘c’:3}
\>>> for key in D.keys():
...     print(key, D[key])
...
a 1
c 3
b 2

 В последних версиях Python словари имеют итератор, который
автоматически возвращает по одному ключу за раз в контексте итераций:

\>>> I = iter(D)
\>>> next(I)
‘a’
\>>> next(I)
‘c’
\>>> next(I)
‘b’
\>>> next(I)
Traceback (most recent call last):
  ...текст сообщения об ошибке опущен...
StopIteration

 Благодаря этому больше не требуется вызывать метод keys, чтобы
выполнить обход ключей словаря, – цикл for автоматически будет
использовать протокол итераций, извлекая ключи по одному
в каждой итерации:

\>>> for key in D:
...     print(key, D[key])
...
a 1
c 3
b 2

 Мы пока не можем углубляться в дальнейшее обсуждение этой темы,
но замечу, что объекты других типов в языке Python также поддерживают
протокол итераций и поэтому могут использоваться в циклах for. Например,
хранилища объектов (объекты файлов с доступом по ключу, используемые
для хранения объектов Python) и объекты, возвращаемые функцией os.popen
(используется для чтения вывода команд системной оболочки), также
являются итерируемыми:

\>>> import os
\>>> P = os.popen(‘dir’)
\>>> P.__next__()
‘ Volume in drive C is SQ004828V03\n’
\>>> P.__next__()
‘ Volume Serial Number is 08BE-3CD4\n’
\>>> next(P)
TypeError: _wrap_close object is not an iterator

 Обратите внимание, что объекты, возвращаемые функцией popen,
в Python 2.6 поддерживают метод P.next(). В версии 3.0 они поддерживают
метод P.__next__(), но не поддерживают встроенную функцию next(P).
Последняя определена так, что вызывает метод P.next(), и пока не совсем
ясно, будет ли изменено такое ее поведение в будущих версиях
(как описывалось в сноске выше, это явная проблема реализации).
Впрочем, данная проблема возникает только при организации итераций
вручную – если используется механизм автоматической итерации через
эти объекты, с помощью цикла for и других инструментов итераций
(которые описываются в следующих разделах), они возвращают
последовательности строк в любых версиях Python.

 Кроме того, поддержка протокола итераций является причиной, по которой
мы вынуждены были обертывать некоторые результаты в вызов функции list,
чтобы увидеть все значения сразу. Итерируемые объекты возвращают
элементы не в виде списка, а по одному элементу за раз:

\>>> R = range(5)
\>>> R  # Диапазоны в версии 3.0 – это итерируемые объекты
range(0, 5)
\>>> I = iter(R)  # Используйте протокол итераций для обхода элементов
\>>> next(I)
0
\>>> next(I)
1
\>>> list(range(5))  # Или функцию list для получения всех элементов
                       сразу
[0, 1, 2, 3, 4]

 Теперь, когда вы получили неплохое представление об этом протоколе,
вы должны суметь объяснить, почему функция enumerate, представленная
в предыдущей главе, действует, как показано ниже:

\>>> E = enumerate(‘spam’)  # enumerate возвращает итерируемый объект
\>>> E
<enumerate object at 0x0253F508>
\>>> I = iter(E)
\>>> next(I)  # Получить результаты с помощью протокола итераций
(0, ‘s’)
\>>> next(I)
(1, ‘p’)
\>>> list(enumerate(‘spam’))  # или с помощью функции list
[(0, ‘s’), (1, ‘p’), (2, ‘a’), (3, ‘m’)]

 Обычно весь этот механизм скрыт от нас, потому что он автоматически
используется циклом for. Фактически любые инструменты, выполняющие обход
объектов слева направо, используют протокол итераций таким же точно
способом, включая инструменты, которые рассматриваются
в следующем разделе.


 Генераторы списков: первое знакомство

 Теперь, когда мы узнали, как действует протокол итераций, обратимся
к наиболее частому случаю его использования. Наряду с циклом for,
генераторы списков представляют один из самых заметных инструментов,
где используется протокол итераций.

 В предыдущей главе мы узнали о возможности использовать функцию range
для изменения списков в ходе выполнения итераций:

\>>> L = [1, 2, 3, 4, 5]
\>>> for i in range(len(L)):
...     L[i] += 10
...
\>>> L
[11, 12, 13, 14, 15]

 Этот способ работает, но, как я уже упоминал, он может быть далеко
не самым оптимальным в языке Python. В наши дни генераторы списков
переводят многое из того, что использовалось раньше, в разряд устаревших
приемов. Например, в следующем фрагменте цикл был заменен единственным
выражением, которое в результате воспроизводит требуемый список:

\>>> L = [x + 10 for x in L]
\>>> L
[11, 12, 13, 14, 15]

 Конечный результат получается тем же самым, но от нас потребовалось
меньше усилий и, скорее всего, этот вариант работает быстрее. Выражения
генераторов списков нельзя считать равнозначной заменой инструкции
цикла for, потому что они создают новые объекты списков (что может иметь
значение при наличии нескольких ссылок на первоначальный список),
но это подходящая замена для большинства применений, к тому же
распространенная и достаточно удобная, чтобы заслужить внимательного
изучения здесь.


 Основы генераторов списков

 Впервые с генераторами списков мы встретились в главе 4. Синтаксис
генераторов списков происходит от конструкций, используемых в теории
множеств для описания операций над каждым элементом множества,
но вам совсем не обязательно знать теорию множеств,
чтобы использовать их. Многие считают, что генераторы списков
в языке Python напоминают цикл for, записанный задом наперед.

 Чтобы получить представление о синтаксисе, рассмотрим пример
из предыдущего раздела более подробно:

\>>> L = [x + 10 for x in L]

 Генераторы списков записываются в квадратных скобках, потому что это,
в конечном счете, способ создания нового списка. Генератор списка
начинается с некоторого составленного нами выражения, которое использует
введенную нами переменную цикла (x + 10). Далее следует то, что вы без
труда опознаете как заголовок цикла for, в котором объявляется
переменная цикла и итерируемый объект (for x in L).

 Чтобы найти значение выражения, Python выполняет обход списка L,
присваивая переменной x каждый очередной элемент, и собирает результаты,
пропуская все элементы через выражение слева. Полученный в результате
список является точным отражением того, что «говорит» генератор списков,
– новый список, содержащий x+10 для каждого x в L.

 С технической точки зрения всегда можно обойтись без генераторов
списков, потому что существует возможность создавать список результатов
выражения вручную, с помощью цикла for:

\>>> res = []
\>>> for x in L:
... res.append(x + 20)
...
\>>> res
[21, 22, 23, 24, 25]

 Фактически это и есть точное представление внутреннего механизма
генератора списков.

 Но генераторы списков записываются компактнее, и данный способ сборки
списков получил широкое распространение в языке Python, поэтому они
оказываются очень удобными во многих ситуациях. Более того, генераторы
списков могут выполняться значительно быстрее (зачастую почти
в два раза), чем инструкции циклов for, потому что итерации выполняются
со скоростью языка C, а не со скоростью программного кода
на языке Python. Такое преимущество в скорости особенно важно
для больших объемов данных.


 Использование генераторов списков для работы с файлами

 Рассмотрим еще один распространенный случай использования генераторов
списков, чтобы подробнее исследовать их работу. Вспомним, что у объекта
файла имеется метод readlines, который загружает файл целиком в список
строк:

\>>> f = open(‘script1.py’)
\>>> lines = f.readlines()
\>>> lines
[‘import sys\n’, ‘print(sys.path)\n’, ‘x = 2\n’, ‘print(2 ** 33)\n’]

 Этот фрагмент работает, но все строки в списке оканчиваются символом
новой строки (\n). Символ новой строки является препятствием для многих
программ – приходится быть осторожным, чтобы избежать появления пустых
строк при выводе и так далее. Было бы совсем неплохо, если бы мы могли
одним махом избавиться от этих символов новой строки.

 Всякий раз, когда мы заговариваем о выполнении операций над каждым
элементом последовательности, мы попадаем в сферу действий генераторов
списков. Например, предположим, что переменная lines находится в том же
состоянии, в каком она была оставлена в предыдущем примере. Тогда
следующий фрагмент обработает каждую строку в списке функцией rstrip,
чтобы удалить завершающие пробельные символы (также можно было бы
использовать выражение извлечения среза line[:-1], но только если бы мы
были абсолютно уверены, что все строки завершаются символом
новой строки):

\>>> lines = [line.rstrip() for line in lines]
\>>> lines
[‘import sys’, ‘print(sys.path)’, ‘x = 2’, ‘print(2 ** 33)’]

 Этот метод действует, как ожидалось, генераторы списков – это другой
итерационный контекст, но точно так же, как и в простом цикле for,
нам не требуется даже открывать файл заранее. Если открыть его внутри
выражения, генератор списков автоматически будет использовать
итерационный протокол, с которым мы познакомились выше в этой главе.
То есть он будет читать из файла по одной строке за раз – вызовом метода
__next__ файла, пропускать строку через функцию rstrip и добавлять
результат в список. И снова мы получаем именно то, что запрашиваем, –
результат работы метода rstrip для каждой строки в файле:

\>>> lines = [line.rstrip() for line in open(‘script1.py’)]
\>>> lines
[‘import sys’, ‘print(sys.path)’, ‘x = 2’, ‘print(2 ** 33)’]

 Это выражение значительную часть работы выполняет неявно –
интерпретатор сканирует файл и автоматически собирает список результатов
выполнения операции. Кроме того, это наиболее эффективный способ,
потому что большая часть действий выполняется внутри интерпретатора
Python, который работает наверняка быстрее, чем эквивалентная инструкция
for. Напомню еще раз, что при работе с большими файлами выигрыш
в скорости от применения генераторов списков может оказаться весьма
существенным.

 Генераторы списков не только обладают высокой эффективностью, они еще
весьма выразительны. В этом примере мы могли бы выполнить над строками
в файле любые строковые операции. Ниже приводится генератор списков,
эквивалентный примеру, рассматривавшемуся выше, в котором использовался
итератор файла и все символы преобразовывались в верхний регистр,
а также несколько других (составление цепочки из вызовов методов
во втором примере стало возможным благодаря тому, что строковые методы
возвращают новую строку, к которой и применяется другой
строковый метод):

\>>> [line.upper() for line in open(‘script1.py’)]
[‘IMPORT SYS\n’, ‘PRINT(SYS.PATH)\n’, ‘X = 2\n’, ‘PRINT(2 ** 33)\n’]

\>>> [line.rstrip().upper() for line in open(‘script1.py’)]
[‘IMPORT SYS’, ‘PRINT(SYS.PATH)’, ‘X = 2’, ‘PRINT(2 ** 33)’]

\>>> [line.split() for line in open(‘script1.py’)]
[[‘import’,’sys’], [‘print(sys.path)’], [‘x’,’=’,’2’],
[‘print(2’,’**’,’33)’]]

\>>> [line.replace(‘ ‘, ‘!’) for line in open(‘script1.py’)]
[‘import!sys\n’, ‘print(sys.path)\n’, ‘x!=!2\n’, ‘print(2!**!33)\n’]

\>>> [(‘sys’ in line, line[0]) for line in open(‘script1.py’)]
[(True, ‘i’), (True, ‘p’), (False, ‘x’), (False, ‘p’)]


 Расширенный синтаксис генераторов списков

 В действительности генераторы списков могут иметь еще более сложный
вид. Например, в цикл for, вложенный в выражение, можно добавить
оператор if, чтобы отобрать результаты, для которых условное выражение
дает истинное значение.

 Например, предположим, что нам требуется повторить предыдущий пример,
но при этом необходимо отобрать только строки, начинающиеся с символа p
(возможно, первый символ в каждой строке – код действия некоторого
вида). Достичь поставленной цели можно, если добавить фильтрующий
оператор if:

\>>> lines = [line.rstrip() for line in open(‘script1.py’)
             if line[0] == ‘p’]
\>>> lines
[‘print(sys.path)’, ‘print(2 ** 33)’]

 В этом примере оператор if проверяет, является ли первый символ
в строке символом p. Если это не так, строка не включается в список
результатов. Это достаточно длинное выражение, но его легко понять,
если преобразовать в эквивалентный простой цикл for (вообще любой
генератор списков можно перевести в эквивалентную реализацию на базе
инструкции for, добавляя отступы к каждой последующей части):

\>>> res = []
\>>> for line in open(‘script1.py’):
...     if line[0] == ‘p’:
...         res.append(line.rstrip())
...
\>>> res
[‘print(sys.path)’, ‘print(2 ** 33)’]

 Эта инструкция for выполняет эквивалентные действия, но занимает четыре
строки вместо одной и работает существенно медленнее.

 В случае необходимости генераторы списков могут иметь еще более сложный
вид. Например, они могут содержать вложенные циклы, оформленные в виде
серии операторов for. На самом деле полный синтаксис допускает указывать
любое число операторов for, каждый из которых может иметь
ассоциированный с ним оператор if (подробнее о синтаксисе генераторов
выражений рассказывается в главе 20).

 Например, следующий фрагмент создает список результатов операции
конкатенации x+y для всех x в одной строке и для всех y – в другой.
В результате получаются сочетания символов в двух строках:

\>>> [x + y for x in ‘abc’ for y in ‘lmn’]
[‘al’, ‘am’, ‘an’, ‘bl’, ‘bm’, ‘bn’, ‘cl’, ‘cm’, ‘cn’]

 Чтобы проще было понять это выражение, его также можно преобразовать
в форму инструкции, добавляя отступы к каждой последующей части.
Следующий фрагмент представляет собой эквивалентную, но более медленную
реализацию:
\>>> res = []
\>>> for x in ‘abc’:
...     for y in ‘lmn’:
...         res.append(x + y)
...
\>>> res
[‘al’, ‘am’, ‘an’, ‘bl’, ‘bm’, ‘bn’, ‘cl’, ‘cm’, ‘cn’]

 Даже с повышением уровня сложности выражения генераторов списков могут
иметь очень компактный вид. Вообще они предназначены для реализации
простых итераций – для реализации сложных действий более простая
инструкция for наверняка будет проще и для понимания, и для изменения
в будущем.

 Обычно если что-то в программировании для вас оказывается слишком
сложным, возможно, это не самое лучшее решение.

 Мы еще вернемся к итераторам и генераторам списков в главе 20,
где будем рассматривать их в контексте функций, где вы увидите,
что они связаны с функциями не менее тесно, чем с инструкциями циклов.
"""
