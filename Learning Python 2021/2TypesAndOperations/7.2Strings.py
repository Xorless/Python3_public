"""
 Изменение строк

 Помните термин «неизменяемая последовательность»? Слово «неизменяемая»
означает, что вы не можете изменить содержимое самой строки в памяти
(то есть невозможно изменить элемент строки, выполнив присваивание
по индексу):

\>>> S = ‘spam’
\>>> S[0] = “x”
Возникает ошибка!

 Тогда каким образом в языке Python производить изменение текстовой
информации? Чтобы изменить строку, необходимо создать новую строку
с помощью таких операций, как конкатенация и извлечение подстроки,
и затем, если это необходимо, присвоить результат первоначальному имени:

\>>> S = S + ‘SPAM!’  # Чтобы изменить строку, нужно создать новую
\>>> S
‘spamSPAM!’
\>>> S = S[:4] + ‘Burger’ + S[-1]
\>>> S
‘spamBurger!’

 Первый пример добавляет подстроку в конец строки S с помощью операции
конкатенации. В действительности здесь создается новая строка,
которая затем присваивается имени S, но вы можете представить себе
это действие как «изменение» первоначальной строки. Второй пример
замещает четыре символа шестью новыми – с помощью операций извлечения
подстроки и конкатенации. Как будет показано далее в этой главе,
похожего эффекта можно добиться с помощью строкового метода replace.
Вот как это выглядит:

\>>> S = ‘splot’
\>>> S = S.replace(‘pl’, ‘pamal’)
\>>> S
‘spamalot’

 Как и всякая операция, создающая новую строку, строковые методы создают
новые строковые объекты. Если вам необходимо сохранить эти объекты,
вы можете присвоить их переменной. Создание нового объекта строки
для каждого изменения – операция не столь неэффективная, как может
показаться, – вспомните, в предыдущей главе говорилось,
что интерпретатор автоматически производит сборку мусора
(освобождает память, занятую неиспользуемыми строковыми объектами),
поэтому новые объекты повторно используют память, ранее занятую прежними
значениями. Интерпретатор Python во многих случаях работает гораздо
быстрее, чем можно было бы ожидать.

 Наконец, дополнительно существует возможность сборки текстовых значений
с помощью выражений форматирования строк. Ниже приводятся два примера
подстановки значений объектов в строку, при этом происходит
преобразование объектов в строки и изменение первоначальной строки
в соответствии со спецификаторами формата:

\>>> ‘That is %d %s bird!’ % (1, ‘dead’)  # Выражение форматирования
That is 1 dead bird!
\>>> ‘That is {0} {1} bird!’.format(1, ‘dead’)  # Метод форматирования
‘That is 1 dead bird!’  # в 2.6 и 3.0

 Несмотря на впечатление, что происходит замена символов в строке,
в действительности в результате форматирования получаются новые
строковые объекты, а оригинальные строки не изменяются. Мы будем
рассматривать приемы форматирования ниже, в этой же главе,
где вы увидите, что операции форматирования могут иметь большую
практическую пользу, чем в этом примере. Второй пример представляет
строковый метод; и мы в первую очередь познакомимся с методами строк,
а потом перейдем к изучению приемов форматирования.


 Строковые методы

 В дополнение к операторам выражений строки предоставляют набор методов,
реализующих более сложные операции обработки текста. Методы –
это просто функции, которые связаны с определенными объектами. Формально
они являются атрибутами, присоединенными к объектам, которые ссылаются
на функции. В языке Python выражения и встроенные функции могут работать
с некоторым набором типов, но методы являются специфичными для типов
объектов: строковые методы, например, работают только со строковыми
объектами. В Python 3.0 некоторые методы могут относиться к разным типам
(например, многие типы имеют метод count), но при этом по своей
функциональности они в большей степени зависят от типа объекта,
чем другие инструменты. Если говорить более точно,
функции – это пакеты программного кода, а вызовы методов
объединяют в себе выполнение двух операций
(извлечение атрибута и вызов функции).


 Извлечение атрибута

 Выражение вида object.attribute означает: «извлечь значение атрибута
attribute из объекта object».


 Вызов функции

 Выражение вида function(arguments) означает: «вызвать программный код
функции function, передав ему ноль или более объектов-аргументов
arguments, разделенных запятыми, и вернуть значение функции».

 Объединение этих двух действий позволяет вызвать метод объекта.
Выражение вызова метода object.method(arguments) вычисляется
слева направо, то есть интерпретатор сначала извлекает метод объекта,
а затем вызывает его, передавая ему входные аргументы. Если метод
возвращает какой-либо результат, он становится результатом всего
выражения вызова метода. Как будет много раз показано в этой
части книги, большинство объектов обладает методами, которые можно
вызвать, и все они доступны с использованием одного и того же
синтаксиса вызова метода. Чтобы вызвать метод объекта, вам потребуется
существующий объект. Давайте перейдем к рассмотрению некоторых примеров.

  S.capitalize()                 S.ljust(width [, fill])

  S.center(width [, fill]))      S.lower()

  S.count(sub [, start [, end]]) S.lstrip([chars])

  S.encode([encoding [,errors]]) S.maketrans(x[, y[, z]])

  S.endswith(suffix              S.partition(sep)
  [, start [, end]])

  S.expandtabs([tabsize])        S.replace(old, new [, count])

  S.find(sub [, start [, end]])  S.rfind(sub [,start [,end]])

  S.format(fmtstr, *args,        S.rindex(sub [, start [, end]])
  **kwargs)

  S.index(sub [, start [, end]]) S.rjust(width [, fill])

  S.isalnum()                    S.rpartition(sep)

  S.isalpha()                    S.rsplit([sep[, maxsplit]])

  S.isdecimal()                  S.rstrip([chars])

  S.isdigit()                    S.split([sep [,maxsplit]])

  S.isidentifier()               S.splitlines([keepends])

  S.islower()                    S.startswith(prefix [, start [, end]])

  S.isnumeric()                  S.strip([chars])

  S.isprintable()                S.swapcase()

  S.isspace()                    S.title()

  S.istitle()                    S.translate(map)

  S.isupper()                    S.upper()

  S.join(iterable)               S.zfill(width)


 Примеры использования строковых методов: изменение строк

 Как уже говорилось ранее, строки являются неизменяемыми объектами,
поэтому их невозможно изменить непосредственно. Чтобы из существующей
строки сконструировать новое текстовое значение, необходимо создать
новую строку с помощью таких операций, как извлечение подстроки
и конкатенация. Например, чтобы изменить два символа в середине строки,
можно использовать такой способ:

\>>> S = ‘spammy’
\>>> S = S[:3] + ‘xx’ + S[5:]
\>>> S
‘spaxxy’

 При этом, если требуется только заменить подстроку, можно
воспользоваться методом replace:

\>>> S = ‘spammy’
\>>> S = S.replace(‘mm’, ‘xx’)
\>>> S
‘spaxxy’

 Метод replace является более универсальным, чем предполагает этот
программный код. Он принимает в качестве аргумента оригинальную
подстроку (любой длины) и строку (любой длины) замены, и выполняет
глобальный поиск с заменой:

\>>> ‘aa$bb$cc$dd’.replace(‘$’, ‘SPAM’)
‘aaSPAMbbSPAMccSPAMdd’

 В этой роли метод replace может использоваться как инструмент
реализации поиска с заменой по шаблону (например, замены символов
формата). Обратите внимание, что на этот раз мы просто выводим результат
на экран, а не присваиваем его переменной – присваивать результат
переменной необходимо только в том случае, если потребуется сохранить
результат дальнейшего использования.

 Если необходимо заменить одну подстроку фиксированного размера,
которая может появиться в любом месте, можно также выполнить операцию
замены или отыскать подстроку с помощью метода find и затем
воспользоваться операциями извлечения подстроки:

\>>> S = ‘xxxxSPAMxxxxSPAMxxxx’
\>>> where = S.find(‘SPAM’) # Поиск позиции
\>>> where # Подстрока найдена со смещением 4
4
\>>> S = S[:where] + ‘EGGS’ + S[(where+4):]
\>>> S
‘xxxxEGGSxxxxSPAMxxxx’

 Метод find возвращает смещение, по которому найдена подстрока
(по умолчанию поиск начинается с начала строки), или значение -1,
если искомая подстрока не найдена. Другой вариант использования метода
replace заключается в передаче третьего аргумента, который определяет
число производимых замен:

\>>> S = ‘xxxxSPAMxxxxSPAMxxxx’
\>>> S.replace(‘SPAM’, ‘EGGS’)  # Заменить все найденные подстроки
‘xxxxEGGSxxxxEGGSxxxx’
\>>> S.replace(‘SPAM’, ‘EGGS’, 1)  # Заменить одну подстроку
‘xxxxEGGSxxxxSPAMxxxx’

 Обратите внимание: метод replace возвращает новую строку.
Так как строки являются неизменяемыми, методы никогда в действительности
не изменяют оригинальную строку, даже если они называются «replace»
(заменить)!

 Тот факт, что операция конкатенации и метод replace всякий раз создают
новые строковые объекты, может оказаться недостатком их использования
для изменения строк. Если в сценарии производится множество изменений
длинных строк, вы можете повысить производительность сценария,
преобразовав строку в объект, который допускает внесение изменений:

\>>> S = ‘spammy’
\>>> L = list(S)
\>>> L
[‘s’, ‘p’, ‘a’, ‘m’, ‘m’, ‘y’]

 Встроенная функция list (или функция-конструктор объекта) создает новый
список из элементов любой последовательности – в данном случае
«разрывая» строку на символы и формируя из них список. Обладая строкой
в таком представлении, можно производить необходимые изменения,
не вызывая создание новой копии строки при каждом изменении:

\>>> L[3] = ‘x’  # Этот прием допустим для списков, но не для строк
\>>> L[4] = ‘x’
\>>> L
[‘s’, ‘p’, ‘a’, ‘x’, ‘x’, ‘y’]

 Если после внесения изменений необходимо выполнить обратное
преобразование (чтобы, например, записать результат в файл),
можно использовать метод join, который «собирает» список обратно
в строку:

\>>> S = ‘’.join(L)
\>>> S
‘spaxxy’

 Метод join на первый взгляд может показаться немного странным.
Так как он является строковым методом (а не методом списка),
он вызывается через указание желаемой строки-разделителя. Метод join
объединяет строки из списка, вставляя строку-разделитель между
элементами списка. В данном случае при получении строки из списка
используется пустая строка-разделитель. В более общем случае можно
использовать произвольную строку-разделитель:

\>>> ‘SPAM’.join([‘eggs’, ‘sausage’, ‘ham’, ‘toast’])
‘eggsSPAMsausageSPAMhamSPAMtoast’

 На практике объединение подстрок в одну строку часто выполняется
намного быстрее, чем последовательность операций конкатенации отдельных
элементов списка. Обратите также внимание на упоминавшийся выше
строковый тип bytearray, появившийся в версиях Python 3.0 и 2.6,
который полностью описывается в главе 36, – благодаря тому,
что объекты этого типа могут изменяться непосредственно, в некоторых
случаях он представляет отличную альтернативу комбинации функций
list/join, особенно когда текст приходится изменять достаточно часто.


 Примеры методов строк: разбор текста

 Еще одна распространенная роль, которую играют методы строк, –
это простейший разбор текста, то есть анализ структуры и извлечение
подстрок. Для извлечения подстрок из фиксированных смещений можно
использовать прием извлечения срезов:

\>>> line = ‘aaa bbb ccc’
\>>> col1 = line[0:3]
\>>> col3 = line[8:]
\>>> col1
‘aaa’
\>>> col3
‘ccc’

 В этом примере поля данных располагаются в фиксированных позициях
и потому могут быть легко извлечены из оригинальной строки. Этот прием
может использоваться, только если анализируемые компоненты располагаются
в известных фиксированных позициях. Если поля отделяются друг от друга
некоторым разделителем, можно воспользоваться методом разбиения строки
на компоненты. Этот прием используется, когда искомые данные могут
располагаться в произвольных позициях внутри строки:

\>>> line = ‘aaa bbb ccc’
\>>> cols = line.split()
\>>> cols
[‘aaa’, ‘bbb’, ‘ccc’]

 Строковый метод split преобразует строку в список подстрок,
окружающих строки-разделители. В предыдущем примере мы не указали
строку-разделитель, поэтому по умолчанию в качестве разделителей
используются пробельные символы – строка разбивается на группы
по символам пробела, табуляции или перевода строки, и в результате
мы получили список подстрок. В других случаях данные могут отделяться
другими разделителями. В следующем примере производится разбиение
(и, следовательно, разбор) строки по символу запятой, который обычно
используется для отделения данных, извлеченных из баз данных:

\>>> line = ‘bob,hacker,40’
\>>> line.split(‘,’)
[‘bob’, ‘hacker’, ‘40’]

 Разделители могут содержать более одного символа:

\>>> line = “i’mSPAMaSPAMlumberjack”
\>>> line.split(“SPAM”)
[“i’m”, ‘a’, ‘lumberjack’]


 Другие часто используемые методы строк в действии

 Другие строковые методы имеют более специфическое предназначение,
например удаляют пробельные символы в конце текстовой строки,
выполняют преобразование регистра символов, проверяют характер
содержимого строки и проверяют наличие подстроки в конце строки
или в начале:

\>>> line = “The knights who say Ni!\n”
\>>> line.rstrip()
‘The knights who say Ni!’

\>>> line.upper()
‘THE KNIGHTS WHO SAY NI!\n’

\>>> line.isalpha()
False

\>>> line.endswith(‘Ni!\n’)
True

\>>> line.startswith(‘The’)
True

 Для достижения тех же результатов в некоторых случаях могут
использоваться альтернативные приемы – с использованием оператора
проверки вхождения in можно проверить присутствие подстроки,
а функция получения длины строки и операция извлечения подстроки могут
использоваться для имитации действия функции endswith:

\>>> line
‘The knights who say Ni!\n’
\>>> line.find(‘Ni’) != -1  # Поиск с использованием вызова метода
True                        # или выражения

\>>> ‘Ni’ in line
True

\>>> sub = ‘Ni!\n’
\>>> line.endswith(sub)  # Проверка наличия подстроки в конце строки
True            # с помощью метода или операции извлечения подстроки

\>>> line[-len(sub):] == sub
True

 Обратите также внимание на строковый метод format, который описывается
ниже в этой главе, – он позволяет реализовать более сложные способы
подстановки в одной инструкции, чем комбинирование нескольких операций.

 Обратите внимание, что ни один из строковых методов не поддерживает
шаблоны, – для обработки текста с использованием шаблонов необходимо
использовать модуль re, входящий в состав стандартной библиотеки языка
Python, – дополнительный инструмент, начальные сведения о котором
приводились в главе 4, а полное его обсуждение выходит далеко за рамки
этой книги (один пример приводится в конце главы 36). Тем не менее,
несмотря на это ограничение, строковые методы иногда оказываются
эффективнее, чем функции модуля re.


 Выражения форматирования строк

 Уже с помощью представленных к этому моменту строковых методов
и операций над последовательностями можно сделать немало, но,
кроме того, в арсенале языка Python имеются дополнительные возможности
обработки строк - операции форматирования строк позволяют выполнять
подстановку в строки значений различных типов за одно действие.
Про операции форматирования нельзя сказать, что они в каких-то случаях
предоставляют единственно возможный способ решения каких-либо задач,
но их удобно использовать, например когда необходимо отформатировать
текст для вывода на экран. Благодаря богатству новых идей, появляющихся
в мире языка Python, операции форматирования строк могут выполняться
двумя способами:


 Выражения форматирования строк

  Первоначально существовавший способ – он основан на модели функции
 printf из языка C и широко используется в существующих программах.


 Метод форматирования строк

  Более новый способ, появившийся в версиях Python 2.6 и 3.0, –
 более уникальный для языка Python, возможности которого в значительной
 степени пересекаются с возможностями выражений форматирования.

 Из-за новизны метода форматирования существует вероятность,
что некоторые из его особенностей со временем будут переведены
в разряд нерекомендуемых. Выражения форматирования, скорее всего,
станут нерекомендуемыми в более поздних выпусках Python, хотя это
во многом будет зависеть от предпочтений активных программистов
на языке Python. Но так как оба способа являются лишь вариациями
на одну и ту же тему, то в настоящее время можно смело использовать
любой из них. Выражения форматирования строк появились в языке
значительно раньше, поэтому мы начнем с них.

 В языке Python имеется двухместный оператор %, предназначенный для
работы со строками (вы можете вспомнить, что для чисел он является
оператором деления по модулю, или получения остатка от деления).
Когда этот оператор применяется к строкам, он обеспечивает простой
способ форматирования значений, согласно заданной строке формата.
Проще говоря, оператор % обеспечивает возможность компактной записи
программного кода, выполняющего множественную подстановку строк,
позволяя избавиться от необходимости конструирования отдельных
фрагментов строки по отдельности с последующим их объединением.

 Чтобы отформатировать строку, требуется:

  1. Слева от оператора % указать строку формата, содержащую один
 или более спецификаторов формата, каждый из которых начинается
 с символа % (например, %d).

  2. Справа от оператора % указать объект (или объекты, в виде кортежа),
 значение которого должно быть подставлено на место спецификатора
 (или спецификаторов) в левой части выражения.

 Например, в примере форматирования строки, который приводился ранее
в этой главе, мы видели, что целое число 1 замещает спецификатор %d
в строке формата, расположенной в левой части выражения, а строка “dead”
замещает спецификатор %s. В результате получается новая строка,
которая содержит эти две подстановки.

\>>> ‘That is %d %s bird!’ % (1, ‘dead’)  # Выражение форматирования
That is 1 dead bird!

 Строго говоря, выражения форматирования строк не являются абсолютно
необходимыми – все, что можно сделать с их помощью, точно так же можно
сделать с помощью серии преобразований и операций конкатенации. Однако
операция форматирования позволяет объединить множество шагов в одной
инструкции. Мощные возможности этой операции заслуживают того, чтобы
рассмотреть еще несколько примеров:

\>>> exclamation = “Ni”
\>>> “The knights who say %s!” % exclamation
‘The knights who say Ni!’
\>>> “%d %s %d you” % (1, ‘spam’, 4)
‘1 spam 4 you’
\>>> “%s -- %s -- %s” % (42, 3.14159, [1, 2, 3])
‘42 -- 3.14159 -- [1, 2, 3]’

 В первом примере строка “Ni” внедряется в целевую строку слева, замещая
спецификатор %s. Во втором примере в целевую строку вставляются три
значения. Обратите внимание: когда вставляется более одного значения,
в правой части выражения их необходимо сгруппировать с помощью круглых
скобок (то есть создать из них кортеж). Оператор форматирования %
ожидает получить справа либо один объект, либо кортеж объектов.

 В третьем примере также вставляются три значения – целое число,
вещественное число и объект списка, но обратите внимание, что в левой
части выражения всем значениям соответствует спецификатор %s, который
соответствует операции преобразования в строку. Объекты любого типа
могут быть преобразованы в строку (это происходит, например, при выводе
на экран), поэтому для любого объекта может быть указан спецификатор %s.
Вследствие этого вам не придется выполнять специальное форматирование,
в большинстве случаев вам достаточно будет знать только о существовании
спецификатора %s.

 Имейте в виду, что выражение форматирования всегда создает
новую строку, а не изменяет строку, расположенную в левой части.
Поскольку строки являются неизменяемыми, этот оператор вынужден работать
именно таким способом. Как уже говорилось ранее, если вам требуется
сохранить полученный результат, присвойте его переменной.


 Дополнительные возможности форматирования строки

 Для реализации более сложного форматирования в выражениях
форматирования можно использовать любые спецификаторы формата,
представленные в табл. Большинство из них окажутся знакомы
программистам, использовавшим язык C, потому что операция форматирования
строк в языке Python поддерживает все наиболее типичные спецификаторы
формата, которые допускается использовать в функции printf языка C
(в отличие от которой выражение в языке Python возвращает результат,
а не выводит его на экран). Некоторые спецификаторы из табл.
предоставляют альтернативные способы форматирования данных одного
и того же типа, например %e, %f и %g обеспечивают альтернативные способы
форматирования вещественных чисел.

  Спецификатор    Назначение
  s               Строка (для объекта любого другого типа будет выполнен
                  вызов функции str(X), чтобы получить строковое
                  представление объекта)

  r               s, но использует функцию repr, а не str

  c               Символ

  d               Десятичное (целое) число

  i               Целое число

  u               То же, что и d (устарел: больше не является
                  представлением целого без знака)

  o               Восьмеричное целое число

  x               Шестнадцатеричное целое число

  X               x, но шестнадцатеричные цифры возвращаются в верхнем
                  регистре

  e               Вещественное число в экспоненциальной форме

  E               e, но алфавитные символы возвращаются в верхнем
                  регистре

  f               Вещественное число в десятичном представлении

  F               Вещественное число в десятичном представлении

  g               Вещественное число e или f

  G               Вещественное число E или а

  %               Символ %

 Фактически спецификаторы формата в левой части выражения поддерживают
целый набор операций преобразования с достаточно сложным собственным
синтаксисом. В общем виде синтаксис использования спецификатора формата
выглядит следующим образом:

%[(name)][flags][width][.precision]code

 Символ спецификатора формата (code) из табл. 7.4 располагается в самом
конце. Между символом % и символом спецификатора можно добавлять
следующую информацию: ключ в словаре (name); список флагов (flags),
которые могут определять, например, признак выравнивания (-), знак числа
(+), наличие ведущих нулей (0); общую ширину поля и число знаков после
десятичной точки и многое другое. Параметры формата width и precision
могут также принимать значение *, чтобы показать, что фактические
значения этих параметров должны извлекаться из следующего элемента
в списке входных значений.

 Полное описание синтаксиса спецификаторов формата вы найдете
в стандартном руководстве по языку Python, а сейчас для демонстрации
наиболее типичных случаев их использования приведем несколько примеров.
В первом примере сначала применяется форматирование целого числа
с параметрами по умолчанию, а затем целое число выводится в поле шириной
в шесть символов, с выравниванием по левому краю
и с дополнением ведущими нулями:

\>>> x = 1234
\>>> res = “integers: ...%d...%-6d...%06d” % (x, x, x)
\>>> res
‘integers: ...1234...1234 ...001234’

 Спецификаторы %e, %f и %g отображают вещественные числа разными
способами, как демонстрируется в следующем примере:

\>>> x = 1.23456789
\>>> x
1.2345678899999999

\>>> ‘%e | %f | %g’ % (x, x, x)
‘1.234568e+00 | 1.234568 | 1.23457’

\>>> ‘%E’ % x
‘1.234568E+00’

 Для вещественных чисел можно реализовать дополнительные эффекты
форматирования, указав необходимость выравнивания по левому краю,
дополнение ведущими нулями, знак числа, ширину поля и число знаков после
десятичной точки. Для простых задач можно было бы использовать простые
функции преобразования чисел в строки с применением выражения
форматирования или встроенной функции str, продемонстрированной ранее:

\>>> ‘%-6.2f | %05.2f | %+06.1f’ % (x, x, x)
‘1.23 | 01.23 | +001.2’

\>>> “%s” % x, str(x)
(‘1.23456789’, ‘1.23456789’)

 Если ширина поля и количество знаков после десятичной точки заранее
не известны, их можно вычислять во время выполнения, а в строке формата
вместо фактических значений использовать символ *, чтобы указать
интерпретатору, что эти значения должны извлекаться из очередного
элемента в списке входных значений, справа от оператора %. Число 4
в кортеже определяет количество знаков после десятичной точки:

\>>> ‘%f, %.2f, %.*f’ % (1/3.0, 1/3.0, 4, 1/3.0)
‘0.333333, 0.33, 0.3333’


 Форматирование строк из словаря

 Операция форматирования позволяет также использовать в спецификаторах
формата ссылки на ключи словаря, который указывается в правой части
выражения, для извлечения соответствующих значений. Мы пока немного
говорили о словарях, поэтому следующий пример демонстрирует самый
простой случай:

\>>> “%(n)d %(x)s” % {“n”:1, “x”:”spam”}
‘1 spam’

 В данном случае (n) и (x) в строке формата ссылаются на ключи в словаре
в правой части выражения и служат для извлечения соответствующих
им значений. Этот прием часто используется в программах, создающих код
разметки HTML или XML, – вы можете построить словарь значений
и затем подставить их все одним выражением форматирования,
которое использует ключи:

\>>> reply = “””  # Шаблон с замещаемыми спецификаторами формата
Greetings...
Hello %(name)s!
Your age squared is %(age)s
“””
\>>> values = {‘name’: ‘Bob’, ‘age’: 40}  # Подготовка фактических
                                          # значений
\>>> print reply % values  # Подстановка значений
Greetings...
Hello Bob!
Your age squared is 40

 Этот способ также часто используется в комбинации со встроенной
функцией vars, которая возвращает словарь, содержащий все переменные,
существующие на момент ее вызова:

\>>> food = ‘spam’
\>>> age = 40
\>>> vars()
{‘food’: ‘spam’, ‘age’: 40, ...и еще множество других... }

 Если задействовать эту функцию в правой части оператора форматирования,
можно отформатировать значения, обращаясь к ним по именам переменных
(то есть по ключам словаря):

\>>> “%(age)d %(food)s” % vars()
‘40 spam’
"""
