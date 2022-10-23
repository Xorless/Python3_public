"""
 Кортежи, файлы и всё остальное


 Кортежи

 Последний тип коллекций в нашем обзоре – это кортежи. Кортежи
представляют собой простые группы объектов. Они действуют точно так же,
как списки, за исключением того, что не допускают непосредственного
изменения (они являются неизменяемыми) и в литеральной форме
записываются как последовательность элементов в круглых,
а не в квадратных скобках. Хотя кортежи и не поддерживают многих методов
списков, тем не менее они обладают большинством свойств, присущим
спискам. Ниже коротко рассматриваются их свойства. Кортежи:

 Это упорядоченные коллекции объектов произвольных типов

 Подобно строкам и спискам, кортежи являются коллекциями объектов,
упорядоченных по позициям (то есть они обеспечивают упорядочение своего
содержимого слева направо). Подобно спискам, они могут содержать объекты
любого типа.

 Обеспечивают доступ к элементам по смещению

  Подобно строками и спискам, доступ к элементам кортежей
 осуществляется по смещению (а не по ключу) – они поддерживают все
 операции, которые основаны на использовании смещения, такие как
 индексирование и извлечение среза.

 Относятся к категории неизменяемых последовательностей

  Подобно строкам и спискам, кортежи являются последовательностями
 и поддерживают многие операции над последовательностями. Однако,
 подобно строкам, кортежи являются неизменяемыми объектами, поэтому
 они не поддерживают никаких операций непосредственного изменения,
 которые применяются к спискам.

 Имеют фиксированную длину, гетерогенны и поддерживают произвольное
число уровней вложенности

  Поскольку кортежи являются неизменяемыми объектами, вы не можете
 изменить размер кортежа, минуя процедуру создания копии. С другой
 стороны, кортежи могут хранить другие составные объекты (то есть
 списки, словари и другие кортежи), а следовательно, поддерживают
 произвольное число уровней вложенности.

 Массивы ссылок на объекты

  Подобно спискам, кортежи проще представлять, как массивы ссылок
 на объекты, – кортежи хранят указатели (ссылки) на другие объекты,
 а операция индексирования над кортежами выполняется очень быстро.

  Операция                 Интерпретация
  ()                       Пустой кортеж

  T = (0,)                 Кортеж из одного элемента (не выражение)

  T = (0, ‘Ni’, 1.2, 3)    Кортеж из четырех элементов

  T = 0, ‘Ni’, 1.2, 3      Еще один кортеж из четырех элементов
                           (тот же самый, что и строкой выше)

  T = (‘abc’, (‘def’,      Вложенные кортежи
  ‘ghi’))

  T = tuple(‘spam’) Создание кортежа из итерируемого объекта

  T[i]                     Индекс,
  T[i][j]                  индекс индекса,
  T[i:j]                   срез,
  len(T)                   длина

  T1 + T2                  Конкатенация,
  T * 3                    повторение

  for x in T: print(x)     Обход в цикле,
  ‘spam’ in t2             проверка вхождения
  [x ** 2 for x in T]

  T.index(‘Ni’)            Методы кортежей в версиях 2.6 и 3.0: поиск,
  T.count(‘Ni’)            подсчет вхождений


 Кортежи в действии

 Обратите внимание: как указано в табл. 9.1, кортежи не обладают
методами, которые имеются у списков (например, кортежи не имеют метода
append). Зато кортежи поддерживают обычные операции
над последовательностями, которые применяются к строкам и к спискам:

\>>> (1, 2) + (3, 4)  # Конкатенация
(1, 2, 3, 4)
\>>> (1, 2) * 4  # Повторение
(1, 2, 1, 2, 1, 2, 1, 2)
\>>> T = (1, 2, 3, 4)  # Индексирование, извлечение среза
\>>> T[0], T[1:3]
(1, (2, 3))

 Особенности синтаксиса определения кортежей: запятые и круглые скобки

 Вторая и четвертая строки в табл. 9.1 заслуживают дополнительных
пояснений. Поскольку круглые скобки могут также окружать выражения
(глава 5), необходимо что-то предпринять, чтобы дать интерпретатору
понять, что единственный объект в круглых скобках – это кортеж,
а не простое выражение. Если вам действительно необходимо получить
кортеж с единственным элементом, нужно просто добавить запятую
после этого элемента, перед закрывающей круглой скобкой:

\>>> x = (40)  # Целое число
\>>> x
40

\>>> y = (40,)  # Кортеж, содержащий целое число
\>>> y
(40,)

 В виде исключения при определении кортежей интерпретатор позволяет
опускать открывающую и закрывающую круглые скобки, если синтаксически
конструкция интерпретируется однозначно. Например, в четвертой строке
таблицы кортеж создается простым перечислением четырех элементов,
разделенных запятыми. В контексте операции присваивания интерпретатор
распознает, что это кортеж, даже при отсутствии круглых скобок.

 Кто-то может посоветовать всегда заключать кортежи в круглые скобки,
а кто-то – посоветовать никогда не использовать их (найдутся и те,
кто вообще ничего не скажет, что делать с кортежами!). Единственное
место, где круглые скобки являются обязательными, – при передаче
кортежей функциям в виде литералов (где круглые скобки имеют важное
значение) и при передаче их инструкции print в версии Python 2.X
(где важное значение имеют запятые).


 Преобразования, методы и неизменяемость

 Несмотря на отличия в синтаксисе литералов, операции, выполняемые
над кортежами (последние три строки в табл. 9.1), идентичны операциям,
применяемым к строкам и спискам. Единственное отличие состоит в том,
что операции +, * и извлечения среза при применении к кортежам
возвращают новые кортежи, а также в том, что в отличие от строк,
списков и словарей, кортежи имеют сокращенный набор методов. Если,
к примеру, необходимо отсортировать содержимое кортежа, его сначала
следует преобразовать в список, чтобы превратить в изменяемый объект
и получить доступ к методу сортировки или задействовать новую функцию
sorted, которая принимает объекты любых типов последовательностей
(и не только):

\>>> T = (‘cc’, ‘aa’, ‘dd’, ‘bb’)
\>>> tmp = list(T)  # Создать список из элементов кортежа
\>>> tmp.sort()  # Отсортировать списка
\>>> tmp
[‘aa’, ‘bb’, ‘cc’, ‘dd’]
\>>> T = tuple(tmp)  # Создать кортеж из элементов списка
\>>> T
(‘aa’, ‘bb’, ‘cc’, ‘dd’)
\>>> sorted(T)  # Или использовать встроенную функцию sorted
[‘aa’, ‘bb’, ‘cc’, ‘dd’]

 Здесь list и tuple – это встроенные функции, которые используются для
преобразования в список и затем обратно в кортеж. В действительности
обе функции создают новые объекты, но благодаря им создается эффект
преобразования.

 Для преобразования кортежей можно также использовать генераторы
списков. Например, ниже из кортежа создается список, причем попутно
к каждому элементу прибавляется число 20:

\>>> T = (1, 2, 3, 4, 5)
\>>> L = [x + 20 for x in T]
\>>> L
[21, 22, 23, 24, 25]

 Генераторы списков в действительности являются операциями
над последовательностями – они всегда создают новые списки, но они могут
использоваться для обхода содержимого любых объектов
последовательностей, включая кортежи, строки и другие списки. Как будет
показано дальше, они могут применяться даже к программным компонентам,
которые физически не являются последовательностями, – к любым объектам,
поддерживающим возможность выполнения итераций, включая файлы, которые
автоматически читаются строка за строкой.

 Кортежи имеют весьма ограниченный набор методов, по сравнению
со списками и строками. В версиях Python 2.6 и 3.0 они обладают всего
двумя методами – index и count, которые действуют точно так же,
как одноименные методы списков:

\>>> T = (1, 2, 3, 2, 4, 2)  # Методы кортежей в Python 2.6 и 3.0
\>>> T.index(2)  # Первое вхождение находится в позиции 2
1
\>>> T.index(2, 2)  # Следующее вхождение за позицией 2
3
\>>> T.count(2)  # Определить количество двоек в кортеже
3

 До выхода версий 2.6 и 3.0 кортежи вообще не имели методов – это было
древнее соглашение в языке Python, касающееся неизменяемых типов,
которое несколько лет тому назад было из практических соображений
нарушено для строк, а совсем недавно – для чисел и кортежей.

 Кроме того, следует заметить, что правило неизменяемости применяется
только к самому кортежу, но не к объектам, которые он содержит.
Например, список внутри кортежа может изменяться как обычно:

\>>> T = (1, [2, 3], 4)
\>>> T[1] = ‘spam’  # Ошибка: нельзя изменить сам кортеж
TypeError: object doesn’t support item assignment
\>>> T[1][0] = ‘spam’  # Допустимо: вложенный изменяемый объект
\>>> T                 # можно изменить
(1, [‘spam’, 3], 4)

 Для большинства программ такой одноуровневой неизменяемости
для обычного использования кортежей вполне достаточно. О чем, совершенно
случайно, и рассказывается в следующем разделе.


 Файлы

 Возможно, вы уже знакомы с понятием файла – так называются именованные
области постоянной памяти в вашем компьютере, которыми управляет
операционная система. Последний основной встроенный тип объектов,
который мы исследуем в нашем обзоре, обеспечивает возможность доступа
к этим файлам из программ на языке Python.

 Проще говоря, встроенная функция open создает объект файла, который
обеспечивает связь с файлом, размещенным в компьютере. После вызова
функции open можно выполнять операции чтения и записи во внешний файл,
используя методы полученного объекта.

 По сравнению с типами, с которыми вы уже знакомы, объекты файлов
выглядят несколько необычно. Они не являются ни числами,
ни последовательностями или отображениями – для задач работы с файлами
они предоставляют одни только методы. Большинство методов файлов связаны
с выполнением операций ввода-вывода во внешние файлы, ассоциированные
с объектом, но существуют также методы, которые позволяют переходить
на другую позицию в файле, выталкивать на диск буферы вывода
и так далее. В табл. приводятся наиболее часто используемые операции
над файлами.


  Операция                       Интерпретация
  output = open(r’C:\spam’, ‘w’) Открывает файл для записи
                                 (‘w’ означает write – запись)

  input = open(‘data’, ‘r’)      Открывает файл для чтения
                                 (‘r’ означает read – чтение)

  input = open(‘data’)           То же самое, что и в предыдущей строке
                                 (режим ‘r’ используется по умолчанию)

  aString = input.read()         Чтение файла целиком в единственную
                                 строку

  aString = input.read(N)        Чтение следующих N символов
                                 (или байтов) в строку

  aString = input.readline()     Чтение следующей текстовой строки
                                 (включая символ конца строки) в строку

  aList = input.readlines()      Чтение файла целиком в список строк
                                 (включая символ конца строки)

  output.write(aString)          Запись строки символов (или байтов)
                                 в файл

  output.writelines(aList)       Запись всех строк из списка в файл

  output.close()                 Закрытие файла вручную (выполняется
                                 по окончании работы с файлом)

  output.flush()                 Выталкивает выходные буферы на диск,
                                 файл остается открытым

  anyFile.seek(N)                Изменяет текущую позицию в файле
                                 для следующей операции, смещая ее
                                 на N байтов от начала файла.

  for line in open(‘data’):      Итерации по файлу, построчное чтение
  операции над line

  open(‘f.txt’,                  Файлы с текстом Юникода в Python 3.0
  encoding=’latin-1’)            (строки типа str)

  open(‘f.bin’, ‘rb’)            Файлы с двоичными данными в Python 3.0
                                 (строки типа bytes)


 Открытие файлов

 Чтобы открыть файл, программа должна вызвать функцию open, передав ей
имя внешнего файла и режим работы. Обычно в качестве режима
используется строка ‘r’, когда файл открывается для чтения
(по умолчанию), ‘w’ – когда файл открывается для записи или ‘a’ –
когда файл открывается на запись в конец. В строке режима могут также
указываться другие параметры:

  Добавление символа b в строку режима означает работу с двоичными
 данными (в версии 3.0 отключается интерпретация символов конца строки
 и кодирование символов Юникода).

  Добавление символа + означает, что файл открывается для чтения
 и для записи (то есть вы получаете возможность читать и записывать
 данные в один и тот же объект файла, часто совместно с операцией
 позиционировании в файле).

 Оба аргумента функции open должны быть строками. Кроме того, функция
может принимать третий необязательный аргумент, управляющий буферизацией
выводимых данных, – значение ноль означает, что выходная информация
не будет буферизироваться (то есть она будет записываться во внешний
файл сразу же, в момент вызова метода записи). Имя внешнего файла может
включать платформозависимые префиксы абсолютного или относительного пути
к файлу. Если путь к файлу не указан, предполагается, что он находится
в текущем рабочем каталоге (то есть в каталоге, где был запущен
сценарий).


 Использование файлов

 Как только будет получен объект файла, вы можете вызывать его методы
для выполнения операций чтения или записи. В любом случае содержимое
файла в программах на языке Python принимает форму строк – операция
чтения возвращает текст в строках, и метод записи принимает информацию
в виде строк.

 Для чтения строк лучше использовать итераторы файлов

  Несмотря на то, что методы чтения и записи, перечисленные в таблице,
 являются наиболее часто используемыми, имейте в виду, что самый лучший,
 пожалуй, способ чтения строк из файла на сегодняшний день состоит
 в том, вообще не использовать операцию чтения из файла – как будет
 показано в главе 14, файлы имеют итератор, который автоматически читает
 информацию из файла строку за строкой в контексте цикла for,
 в генераторах списков и в других итерационных контекстах.

 Содержимое файлов находится в строках, а не в объектах

  Обратите внимание: в табл. 9.2 показано, что данные, получаемые
 из файла, всегда попадают в сценарий в виде строки, поэтому вам
 необходимо будет выполнять преобразование данных в другие типы объектов
 языка Python, если эта форма представления вам не подходит.
 Точно так же, при выполнении операции записи данных в файл, в отличие
 от инструкции print, интерпретатор Python не выполняет автоматическое
 преобразование объектов в строки – вам необходимо передавать методам
 уже сформированные строки. Поэтому при работе с файлами вам пригодятся
 рассматривавшиеся ранее инструменты преобразования данных из строкового
 представления в числовое и наоборот (например, int, float, str, а также
 выражения форматирования строк и метод format). Кроме того, в состав
 Python входят дополнительные стандартные библиотечные инструменты,
 предназначенные для работы с универсальным объектом хранилища данных
 (например, модуль pickle) и обработки упакованных двоичных данных
 в файлах (например, модуль struct). С действием обоих модулей
 мы познакомимся ниже, в этой же главе.

 Вызов метода close является необязательным

  Вызов метода close разрывает связь с внешним файлом.
 Как рассказывалось в главе 6, интерпретатор Python немедленно
 освобождает память, занятую объектом, как только в программе будет
 утеряна последняя ссылка на этот объект. Как только объект файла
 освобождается, интерпретатор автоматически закрывает ассоциированный
 с ним файл (что происходит также в момент завершения программы).
 Благодаря этому вам не требуется закрывать файл вручную, особенно
 в небольших сценариях, которые выполняются непродолжительное время.
 С другой стороны, вызов метода close не повредит, и его рекомендуется
 использовать в крупных системах. Строго говоря, возможность
 автоматического закрытия файлов не является частью спецификации языка,
 и с течением времени такое поведение может измениться. Следовательно,
 привычку вызывать метод close вручную можно только приветствовать.
 (Альтернативный способ автоматического закрытия файлов приводится ниже,
 в этом же разделе, где обсуждаются менеджеры контекста объектов файлов,
 которые используются в новой инструкции with/as, появившейся
 в Python 2.6 и 3.0.)

 Файлы обеспечивают буферизацию ввода-вывода и позволяют производить
позиционирование в файле

  В предыдущем абзаце отмечается важность явного закрытия файлов,
 потому что в этот момент освобождаются ресурсы операционной системы
 и выталкиваются выходные буферы. По умолчанию вывод в файлы всегда
 выполняется с помощью промежуточных буферов, то есть в момент записи
 текста в файл он не попадает сразу же на диск – буферы выталкиваются
 на диск только в момент закрытия файла или при вызове метода flush.
 Вы можете отключить механизм буферизации с помощью
 параметров функции open, но это может привести к снижению
 производительности операций ввода-вывода. Файлы в языке Python
 поддерживают также возможность позиционирования – метод seek позволяет
 сценариям управлять позицией чтения и записи.


 Файлы в действии

 Давайте рассмотрим небольшие примеры, демонстрирующие основы работы
с файлами. В первом примере выполняется открытие нового текстового файла
в режиме для записи, в него записываются две строки (завершающиеся
символом новой строки \n), после чего файл закрывается. Далее этот же
файл открывается в режиме для чтения и выполняется чтение строк из него.
Обратите внимание, что третий вызов метода readline возвращает пустую
строку – таким способом методы файлов в языке Python сообщают о том,
что был достигнут конец файла (пустая строка в файле возвращается
как строка, содержащая единственный символ новой строки, а не как
действительно пустая строка). Ниже приводится полный листинг сеанса:

\>>> myfile = open(‘myfile.txt’, ‘w’) #  Открывает файл
                                      # (создает/очищает)
\>>> myfile.write(‘hello text file\n’)  # Записывает строку текста
16
\>>> myfile.write(‘goodbye text file\n’)
18
\>>> myfile.close()  # Выталкивает выходные буферы на диск

\>>> myfile = open(‘myfile.txt’)  # Открывает файл: ‘r’ – по умолчанию
\>>> myfile.readline()  # Читает строку
‘hello text file\n’
\>>> myfile.readline()
‘goodbye text file\n’
\>>> myfile.readline()  # Пустая строка: конец файла
''

 Обратите внимание, что в Python 3.0 метод write возвращает количество
записанных символов – в версии 2.6 этого не происходит, поэтому
в интерактивном сеансе вы не увидите эти числа. Этот пример записывает
две строки текста в файл, добавляя в каждую из них символ конца строки
\n; методы записи не добавляют символ конца строки, поэтому нам
необходимо самостоятельно добавлять его в выводимые строки
(в противном случае следующая операция записи просто продолжит
текущую строку в файле).
 Если необходимо вывести содержимое файла, обеспечив правильную
интерпретацию символов конца строки, его следует  прочитать
в строку целиком, с помощью метода read, и вывести:

\>>> open(‘myfile.txt’).read()  # Прочитать файл целиком в строку
‘hello text file\ngoodbye text file\n’
\>>> print(open(‘myfile.txt’).read()) # Более дружественная
hello text file                       # форма отображения
goodbye text file

 А если необходимо просмотреть содержимое файла строку за строкой,
лучшим выбором будет итератор файла:

\>>> for line in open(‘myfile’):  # Используйте итераторы,
... print(line, end=’’)           # а не методы чтения
...
hello text file
goodbye text file

 В этом случае функцией open создается временный объект файла,
содержимое которого автоматически будет читаться итератором
и возвращаться по одной строке в каждой итерации цикла. Обычно такой
способ компактнее, эффективнее использует память и может оказаться
быстрее некоторых других вариантов (конечно, это зависит от множества
параметров). Так как мы еще не касались темы инструкций и итераторов,
вам придется подождать до главы 14, где дается более полное описание
этого примера.

 Текстовые и двоичные файлы в Python 3.0

 Строго говоря, в предыдущем примере выполняются операции с текстовыми
файлами. В версиях Python 3.0 и 2.6 тип файла определяется вторым
аргументом функции open – символ «b» в строке режима означает binary
(двоичный). В языке Python всегда существовала поддержка текстовых
и двоичных файлов, но в Python 3.0 между этими двумя типами файлов
была проведена более четкая грань:

  Содержимое текстовых файлов представляется в виде обычных строк типа
 str, выполняется автоматическое кодирование/декодирование символов
 Юникода и по умолчанию производится интерпретация символов
 конца строки.

  Содержимое двоичных файлов представляется в виде строк типа bytes,
 и оно передается программе без каких-либо изменений.

 В Python 2.6, напротив, текстовые файлы могли содержать текст
из 8-битных символов или двоичные данные, а для работы с текстом
из символов Юникода использовался специальный строковый тип и интерфейс
доступа к файлам (строки unicode и функция codecs.open). Изменения
в Python 3.0 определялись тем фактом, что обычный текст и текст
в Юникоде были объединены в единый строковый тип, что имеет определенный
смысл, если учесть, что любой текст может быть представлен в Юникоде,
включая ASCII и другие 8-битные кодировки.

 Большинству программистов приходится иметь дело только с текстом ASCII,
поэтому они могут пользоваться базовым интерфейсом доступа к текстовым
файлам, как показано в предыдущем примере, и обычными строками.
С технической точки зрения, все строки в версии 3.0 являются строками
Юникода, но для тех, кто использует только символы ASCII,
это обстоятельство обычно остается незамеченным. В действительности
операции над строками в версиях 3.0 и 2.6 выполняются одинаково,
если область применения сценария ограничивается такими простыми
формами текста.

 Если у вас имеется необходимость интернационализировать приложение или
обрабатывать двоичные данные, отличия в версии 3.0 окажут
большое влияние на программный код (обычно в лучшую сторону).
Вообще говоря, для работы с двоичными файлами следует использовать
строки bytes, а обычные строки str – для работы с текстовыми файлами.
Кроме того, так как текстовые файлы реализуют автоматическое
преобразование символов
Юникода, вы не сможете открыть файл с двоичными данными
в текстовом режиме – преобразование его содержимого в символы Юникода,
скорее всего, завершится с ошибкой.

 Рассмотрим пример. Когда выполняется операция чтения двоичных данных
из файла, она возвращает объект типа bytes – последовательность
коротких целых чисел, представляющих абсолютные значения байтов
(которые могут соответствовать символам, а могут и не соответствовать),
который во многих отношениях очень близко напоминает обычную строку:

\>>> data = open(‘data.bin’, ‘rb’).read()
# Открыть двоичный файл для чтения
\>>> data  # Строка bytes хранит двоичные данные
b’\x00\x00\x00\x07spam\x00\x08’
\>>> data[4:8]  # Ведет себя как строка
b’spam’
\>>> data[4:8][0]  # Но в действительности хранит 8-битные целые числа
115
\>>> bin(data[4:8][0])  # Функция bin() в Python 3.0
‘0b1110011’

 Кроме того, двоичные файлы не выполняют преобразование символов конца
строки – текстовые файлы по умолчанию отображают все разновидности
символов конца строки в и из символа \n в процессе записи и чтения,
и производят преобразование символов Юникода в соответствии с указанной
кодировкой. Так как операции с символами Юникода и с двоичными данными
представляют особый интерес для многих программистов, мы отложим полное
их обсуждение до главы 36. А пока перейдем к некоторым более насущным
примерам использования файлов.


 Сохранение и интерпретация объектов Python в файлах

 Следующий пример записывает различные объекты в текстовый файл.
Обратите внимание на использование средств преобразования объектов
в строки. Напомню, что данные всегда записываются в файл в виде строк,
а методы записи не выполняют автоматического форматирования строк
(для экономии пространства я опустил вывод значений, возвращаемых
методом write):

\>>> X, Y, Z = 43, 44, 45  # Объекты языка Python должны
\>>> S = ‘Spam’  # записываться в файл только в виде строк
\>>> D = {‘a’: 1, ‘b’: 2}
\>>> L = [1, 2, 3]
\>>>
\>>> F = open(‘datafile.txt’, ‘w’)  # Создает файл для записи
\>>> F.write(S + ‘\n’)  # Строки завершаются символом \n
\>>> F.write(‘%s,%s,%s\n’ % (X, Y, Z))  # Преобразует числа в строки
\>>> F.write(str(L) + ‘$’ + str(D) + ‘\n’)  # Преобразует
\>>> F.close()                              # и разделяет символом $

 Создав файл, мы можем исследовать его содержимое, открыв файл
и прочитав данные в строку (одной операцией). Обратите внимание,
что функция автоматического вывода в интерактивной оболочке дает
точное побайтовое представление содержимого, а инструкция print
интерпретирует встроенные символы конца строки, чтобы обеспечить более
удобочитаемое отображение:

\>>> chars = open(‘datafile.txt’).read()  # Отображение строки
\>>> chars  # в неформатированном виде
“Spam\n43,44,45\n[1, 2, 3]${‘a’: 1, ‘b’: 2}\n”
\>>> print(chars)  # Удобочитаемое представление
Spam
43,44,45
[1, 2, 3]${‘a’: 1, ‘b’: 2}

 Теперь нам необходимо выполнить обратные преобразования, чтобы получить
из строк в текстовом файле действительные объекты языка Python.
Интерпретатор Python никогда автоматически не выполняет преобразование
строк в числа или в объекты других типов, поэтому нам необходимо
выполнить соответствующие преобразования, чтобы можно было использовать
операции над этими объектами, такие как индексирование, сложение
и так далее:

\>>> F = open(‘datafile.txt’)  # Открыть файл снова
\>>> line = F.readline()  # Прочитать одну строку
\>>> line
‘Spam\n’
\>>> line.rstrip()  # Удалить символ конца строки
‘Spam’

 К этой строке мы применили метод rstrip, чтобы удалить завершающий
символ конца строки. Тот же эффект можно было бы получить с помощью
извлечения среза line[:-1], но такой подход можно использовать,
только если мы уверены, что все строки завершаются символом \n
(последняя строка в файле иногда может не содержать этого символа).

 Пока что мы прочитали ту часть файла, которая содержит строку. Теперь
прочитаем следующий блок, в котором содержатся числа, и выполним разбор
этого блока (то есть извлечем объекты):

\>>> line = F.readline() #  Следующая строка из файла
\>>> line  # Это - строка
‘43,44,45\n’
\>>> parts = line.split(‘,’)  # Разбить на подстроки по запятым
\>>> parts
[‘43’, ‘44’, ‘45\n’]

 Здесь был использован метод split, чтобы разбить строку на части
по запятым, которые играют роль символов-разделителей, – в результате
мы получили список строк, каждая из которых содержит отдельное число.
Теперь нам необходимо преобразовать эти строки в целые числа,
чтобы можно было выполнять математические операции над ними:

\>>> int(parts[1])  # Преобразовать строку в целое число
44
\>>> numbers = [int(P) for P in parts]  # Преобразовать весь список
\>>> numbers
[43, 44, 45]

 Как мы уже знаем, функция int преобразует строку цифр в объект целого
числа, а генератор списков, представленный в главе 4, позволяет
применить функцию ко всем элементам списка в одной инструкции
(подробнее о генераторах списков читайте далее в этой книге).
Обратите внимание: для удаления завершающего символа \n в конце
последней подстроки не был использован метод rstrip, потому что int
и некоторые другие функции преобразования просто игнорируют
символы-разделители, окружающие цифры.

 Наконец, чтобы преобразовать список и словарь в третьей строке файла,
можно воспользоваться встроенной функцией eval, которая интерпретирует
строку как программный код на языке Python (формально – строку,
содержащую выражение на языке Python):

\>>> line = F.readline()
\>>> line
“[1, 2, 3]${‘a’: 1, ‘b’: 2}\n”
\>>> parts = line.split(‘$’)  # Разбить на строки по символу $
\>>> parts
[‘[1, 2, 3]’, “{‘a’: 1, ‘b’: 2}\n”]
\>>> eval(parts[0])  # Преобразовать строку в объект
[1, 2, 3]
\>>> objects = [eval(P) for P in parts]  # То же самое для всех строк
\>>> objects                             # в списке
[[1, 2, 3], {‘a’: 1, ‘b’: 2}]

 Поскольку теперь все данные представляют собой список обычных объектов,
а не строк, мы сможем применять к ним операции списков и словарей.


 Сохранение объектов Python с помощью модуля pickle

 Функция eval, использованная в предыдущем примере для преобразования
строк в объекты, представляет собой мощный инструмент. И иногда даже
слишком мощный. Функция eval без лишних вопросов выполнит любое
выражение на языке Python, даже если в результате будут удалены
все файлы в компьютере, если передать в выражение соответствующие
права доступа! Если вам действительно необходимо извлекать объекты
Python из файлов, но вы не можете доверять источнику этих файлов,
идеальным решением будет использование модуля pickle, входящего
в состав стандартной библиотеки Python.

 Модуль pickle позволяет сохранять в файлах практически любые объекты
Python без необходимости с нашей стороны выполнять какие-либо
преобразования. Он напоминает супер универсальную утилиту форматирования
и преобразования данных. Чтобы сохранить словарь в файле, например,
мы передаем его непосредственно в функцию модуля pickle:
"""

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')

import pickle


pickle.dump(D, F)            # Модуль pickle запишет в файл любой объект
F.close()

"""
 Чтобы потом прочитать словарь обратно, можно просто еще раз 
воспользоваться возможностями модуля pickle:
"""

F = open('datafile.pkl', 'rb')
E = pickle.load(F)           # Загружает любые объекты из файла
print(E)

"""
 Нам удалось получить назад точно такой же объект словаря 
без необходимости вручную выполнять какие-либо преобразования. 
Модуль pickle выполняет то, что называется сериализацией объектов, –
преобразование объектов в строку байтов и обратно, не требуя от нас
почти никаких действий. В действительности, внутренняя реализация модуля
pickle выполнила преобразование нашего словаря в строку, при этом 
незаметно для нас (и может выполнить еще более замысловатые 
преобразования при использовании модуля в других режимах):
"""

print(open('datafile.pkl', 'rb').read())  # Формат может измениться!

"""
 Поскольку модуль pickle умеет реконструировать объекты из строкового
представления, нам не требуется самим возиться с этим. Дополнительную 
информацию о модуле pickle вы найдете в руководстве по стандартной 
библиотеке языка Python или попробовав импортировать модуль 
в интерактивном сеансе и передав его имя функции help. Когда будете 
заниматься исследованием этого модуля, обратите также внимание 
на модуль shelve – инструмент, который использует модуль pickle 
для сохранения объектов Python в файлах с доступом по ключу, описание
которых далеко выходит за рамки этой книги (впрочем, пример 
использования модуля shelve вы найдете в главе 27; кроме того,
дополнительные примеры использования модуля pickle приводятся 
в главах 30 и 36)


 Сохранение и интерпретация упакованных двоичных данных в файлах
 
 Прежде чем двинуться дальше, необходимо рассмотреть еще один аспект 
работы с файлами: в некоторых приложениях приходится иметь дело 
с упакованными двоичными данными, которые создаются, например,
программами на языке C. Стандартная библиотека языка Python включает
инструмент, способный помочь в этом, – модуль struct, который позволяет 
сохранять и восстанавливать упакованные двоичные данные. В некотором
смысле, это совершенно другой инструмент преобразования данных,
интерпретирующий строки в файлах как двоичные данные.

 Например, чтобы создать файл с упакованными двоичными данными,
откройте его в режиме ‘wb’ (write binary – запись двоичных данных) 
и передайте модулю struct строку формата и некоторый объект Python. 
В следующем примере используется строка формата, которая определяет 
пакет данных, содержащий 4-байтовое целое число, 4-символьную строку 
и 2-байтовое целое число, причем все представлены в формате big-endian –
в порядке следования байтов «от старшего к младшему» (существуют также
спецификаторы форматов, которые поддерживают наличие символов дополнения
слева, числа с плавающей точкой и многие другие):
"""

F = open('data.bin', 'wb')  # Открыть файл для записи в двоичном режиме

import struct


data = struct.pack(b'>i4sh', 7, b'spam', 8)  # Создать пакет
print(data)                                  # двоичных данных

F.write(data)  # Записать строку байтов
F.close()

"""
 Интерпретатор Python создаст строку bytes двоичных данных,
которую затем мы запишем в файл обычным способом (строка состоит
из экранированных последовательностей, представляющих шестнадцатеричные 
значения). Чтобы преобразовать эти значения в обычные объекты 
языка Python, достаточно просто прочитать строку обратно 
и распаковать ее с использованием той же строки формата. Следующий 
фрагмент извлекает значения, преобразуя их в обычные объекты 
(целые числа и строка):
"""

F = open('data.bin', 'rb')
data = F.read()  # Получить упакованные двоичные данные

print(data)

values = struct.unpack('>i4sh', data)  # Преобразовать в объекты
print(values)

"""
 Файлы с двоичными данными относятся к категории низкоуровневых средств,
которые мы не будем рассматривать подробно. За дополнительной 
информацией обращайтесь к главе 36 и к руководству по библиотеке языка
Python или импортируйте модуль struct в интерактивном сеансе и передайте
имя struct функции help. Обратите также внимание, что режимы доступа
к двоичным файлам ‘wb’ и ‘rb’ могут использоваться для обработки 
простейших двоичных файлов, таких как изображения или аудиофайлы, 
без необходимости выполнять распаковку их содержимого.


 Менеджеры контекста файлов

 Вам также необходимо будет прочитать обсуждение поддержки менеджеров
контекста файлов в главе 33, впервые появившейся в версиях Python 3.0 
и 2.6. Даже при том, что менеджеры контекста в основном применяются
для обработки исключений, тем не менее они позволяют обертывать 
программный код, выполняющий операции с файлами, дополнительным слоем 
логики, который гарантирует, что после выхода за пределы блока 
инструкций менеджера файл будет закрыт автоматически, и позволяет 
не полагаться на автоматическое закрытие файлов механизмом сборки 
мусора:

with open(r’C:\misc\data.txt’) as myfile:  # Подробности в главе 33
    for line in myfile:
        ...операции над строкой line...

 Аналогичную функциональность предоставляет конструкция try/finally,
с которой мы познакомимся в главе 33, но за счет избыточного 
программного кода – три дополнительных строки, если быть более точным 
(впрочем, мы можем не использовать ни один из вариантов и позволить 
интерпретатору самому закрывать файлы):

myfile = open(r’C:\misc\data.txt’)
try:
    for line in myfile:
        ...операции над строкой line...
    finally:
        myfile.close()

 Поскольку для подробного описания обоих способов необходимо иметь 
дополнительные знания, которыми мы еще не обладаем, мы обсудим в книге 
эти детали позже.


 Другие инструменты для работы с файлами
 
 Как показано в табл. 9.2, существуют более сложные инструменты 
для работы с файлами, более того, существуют и другие инструменты,
которые отсутствуют в таблице. Например, функция seek переустанавливает 
текущую позицию в файле (для следующей операции чтения или записи), 
функция flush принудительно выталкивает содержимое выходных буферов 
на диск (по умолчанию файлы всегда буферизуются) и так далее.

 Руководство по стандартной библиотеке и книги, упомянутые 
в предисловии, содержат полный перечень методов для работы с файлами. 
Чтобы кратко ознакомиться с ним, можно также воспользоваться функцией 
dir или help в интерактивном сеансе, передав ей объект открытого файла 
(в Python 3.0, но не в Python 2.6, где следует передать имя типа file).

 Следует также отметить, что функция open и объекты файлов, которые она
возвращает, являются в языке Python основным интерфейсом к внешним 
файлам, однако в арсенале Python существуют и другие инструменты, 
напоминающие файлы. Назовем некоторые из них:

 Стандартные потоки ввода-вывода

  Объекты уже открытых файлов в модуле sys, такие как sys.stdout
 (смотрите раздел «Инструкция print» в главе 11)

 Дескрипторы файлов в модуле os

  Целочисленные дескрипторы файлов, обеспечивающие поддержку 
 низкоуровневых операций, таких как блокировка файлов

 Сокеты, каналы и очереди (FIFO)

  Объекты, по своим характеристикам напоминающие файлы, используемые
 для синхронизации процессов или организации взаимодействий по сети
 Файлы с доступом по ключу, известные как «хранилища» («shelves»)
 Используются для хранения объектов языка Python по ключу (глава 27)

 Потоки командной оболочки

  Такие инструменты, как os.popen и subprocess.Popen, которые 
 поддерживают возможность запуска дочерних процессов и выполнения
 операций с их стандартными потоками ввода-вывода

 Среди сторонних открытых модулей можно отыскать еще больше 
инструментов, напоминающих файлы, включая реализацию поддержки обмена
данными через последовательный порт в расширении PySerial и поддержки
обмена данными с интерактивными программами в системе pexpect. 
Дополнительную информацию о подобных инструментах вы найдете 
в специализированной литературе по языку Python и в Сети.
"""
