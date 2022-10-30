"""
 Условная инструкция if и синтаксические правила


 Условные инструкции if

 Если говорить простым языком, в Python инструкция if выбирает, какое
действие следует выполнить. Это основной инструмент выбора в Python,
который отражает большую часть логики программы на языке Python. Кроме
того, это наша первая составная инструкция. Как и все составные
инструкции языка Python, инструкция if может содержать другие
инструкции, в том числе другие условные инструкции if. Фактически
инструкции в программные последовательности (чтобы они выполнялись одна
за другой) и в произвольно вложенные конструкции (которые выполняются
только при соблюдении определенных условий).


 Общая форма

 Условная инструкция if в языке Python – это типичная условная
инструкция, которая присутствует в большинстве процедурных языков
программирования. Синтаксически сначала записывается часть if с условным
выражением, далее могут следовать одна или более необязательных частей
elif («else if») с условными выражениями и, наконец, необязательная
часть else. Условные выражения и часть else имеют ассоциированные
с ними блоки вложенных инструкций, с отступом относительно основной
инструкции. Во время выполнения условной инструкции if интерпретатор
выполняет блок инструкций, ассоциированный с первым условным выражением,
только если оно возвращает истину, в противном случае выполняется блок
инструкций else. Общая форма записи условной инструкции if выглядит
следующим образом:

if <test1>:  # Инструкция if с условным выражением test1
<statements1>  # Ассоциированный блок
elif <test2>:  # Необязательные части elif
<statements2>
else:  # Необязательный блок else
<statements3>


 Простые примеры

 C целью демонстрации инструкции if в действии рассмотрим несколько
простых примеров. Все части этой инструкции, за исключением основной
части if с условным выражением и связанных с ней инструкций, являются
необязательными. В простейшем случае остальные части инструкции опущены:

\>>> if 1:
... print ‘true’
...
true

 Обратите внимание, что приглашение к вводу изменяется на ... для строк
продолжения в базовом интерфейсе командной строки, используемом здесь
(в IDLE текстовый курсор просто перемещается на следующую строку уже
с отступом, а нажатие на клавишу Backspace возвращает на строку вверх).
Ввод пустой строки (двойным нажатием клавиши Enter) завершает инструкцию
и приводит к ее выполнению. Вспомните, что число 1 является логической
истиной, поэтому данная проверка всегда будет успешной. Чтобы обработать
ложный результат, добавьте часть else:

\>>> if not 1:
... print ‘true’
... else:
... print ‘false’
...
false


 Множественное ветвление

 Теперь рассмотрим пример более сложной условной инструкции if,
в которой присутствуют все необязательные части:

\>>> x = ‘killer rabbit’
\>>> if x == ‘roger’:
... print “how’s jessica?”
... elif x == ‘bugs’:
... print “what’s up doc?”
... else:
... print ‘Run away! Run away!’
...
Run away! Run away!

 Эта многострочная инструкция простирается от строки if до конца блока
else. При выполнении этой инструкции интерпретатор выполнит вложенные
инструкции после той проверки, которая даст в результате истину,
или блок else, если все проверки дадут ложный результат (в этом примере
так и происходит). На практике обе части elif и else могут быть опущены,
и в каждой части может иметься более одной вложенной инструкции.
Обратите внимание, что связь слов if, elif и else определена тем,
что они находятся на одной вертикальной линии, с одним и тем же
отступом.

 Если вы знакомы с такими языками, как C или Pascal, вам будет интересно
узнать, что в языке Python отсутствует инструкция switch или case,
которая позволяет выбирать производимое действие на основе значения
переменной. Вместо этого множественное ветвление оформляется либо в виде
последовательности проверок if/elif, как в предыдущем примере, либо
индексированием словарей, либо поиском в списках. Поскольку словари
и списки могут создаваться во время выполнения, они иногда способны
обеспечить более высокую гибкость, чем жестко заданная логика
инструкции if:

\>>> choice = ‘ham’
\>>> print {‘spam’: 1.25,  # Инструкция ‘switch’ на базе словаря
... ‘ham’: 1.99,  # Используйте has_key или get для
... ‘eggs’: 0.99,  # значения по умолчанию
... ‘bacon’: 1.10}[choice]
1.99

 Тем, кто такой прием видит впервые, может потребоваться некоторое
время, чтобы осознать его; тем не менее данный словарь обеспечивает
множественное ветвление через индексирование по ключу choice для выбора
одного из нескольких значений, почти так же, как это делает инструкция
switch в языке C. Эквивалентная, но менее компактная инструкция if
в языке Python выглядит, как показано ниже:

\>>> if choice == ‘spam’:
... print 1.25
... elif choice == ‘ham’:
... print 1.99
... elif choice == ‘eggs’:
... print 0.99
... elif choice == ‘bacon’:
... print 1.10
... else:
... print ‘Bad choice’
...
1.99

 Обратите внимание на часть else, которая предназначена для обработки
ситуации, когда не найдено ни одного совпадения. Как было показано
в главе 8, значение по умолчанию при использовании словарей может быть
получено с помощью оператора in, метода get или при перехвате
исключения. Те же самые приемы могут использоваться и здесь –
для определения действия по умолчанию в случае реализации множественного
ветвления на базе словаря. Ниже приводится пример
с использованием метода get для получения значения по умолчанию:

\>>> branch = {‘spam’: 1.25,
... ‘ham’: 1.99,
... ‘eggs’: 0.99}
\>>> print branch.get(‘spam’, ‘Bad choice’)
1.25
\>>> print branch.get(‘bacon’, ‘Bad choice’)
Bad choice

 Применение оператора in проверки на вхождение в инструкции if может
обеспечить получение того же результата по умолчанию:

\>>> choice = ‘bacon’
\>>> if choice in branch:
... print(branch[choice])
... else:
... print(‘Bad choice’)
...
Bad choice

 Словари хорошо подходят для выбора значений, ассоциированных
с ключами, но как быть в случае более сложных действий, которые можно
запрограммировать в инструкциях if? В четвертой части книги вы узнаете,
что словари также могут содержать функции, выполняющие сложные действия
при ветвлении, реализуя обычные таблицы переходов. В этом случае
функции, играющие роль значений в словаре, часто создаются как
лямбда-функции и вызываются добавлением круглых скобок. Подробнее
об этом вы прочитаете в главе 19.

 Множественное ветвление на базе словаря довольно удобно использовать
в программах, которые имеют дело с динамическими данными, однако
большинство программистов согласятся, что использование инструкции if
является наиболее простым способом организации множественного ветвления.
Обычно при колебаниях при выборе того или иного подхода предпочтение
следует отдавать более простому и более удобочитаемому способу.


 Синтаксические правила языка Python

 Первое знакомство с синтаксической моделью языка Python состоялось
в главе 10. Теперь, когда мы подошли к таким крупным инструкциям,
как if, настало время пересмотреть и дополнить сведения о синтаксисе,
введенные ранее. Вообще язык программирования Python обладает простым
синтаксисом, основанным на применении инструкций. Однако он обладает
некоторыми особенностями, о которых вам необходимо знать:

  Инструкции выполняются последовательно, одна за другой, пока не будет
 предусмотрено что-то другое. Обычно интерпретатор выполняет инструкции
 в файле или в блоке от начала до конца, но такие инструкции, как if
 (и, как будет показано далее, циклы), заставляют интерпретатор
 выполнять переходы внутри программного кода. Так как путь
 интерпретатора Python через текст программы называется потоком
 управления, такие инструкции, как if, часто называются инструкциями
 управления потоком выполнения.

  Границы блоков и инструкций определяются автоматически. Как мы уже
 видели, в языке Python отсутствуют фигурные скобки или разделители
 «begin/end», окружающие блоки программного кода. Вместо этого
 принадлежность инструкций к вложенному блоку определяется по величине
 отступов. Точно так же инструкции в языке Python обычно не завершаются
 точкой с запятой; обычно признаком конца инструкции служит конец строки
 с этой инструкцией.

  Составные инструкции = “заголовок + «:» + инструкции с отступами”. Все
 составные инструкции в языке Python оформляются одинаково: строка
 с заголовком завершается двоеточием, далее следуют одна или более
 вложенных инструкций, обычно с отступом относительно заголовка. Эти
 инструкции с отступами называются блоком (или иногда набором).
 В инструкции if предложения elif и else являются не только частями
 инструкции if, но и заголовками с собственными вложенными блоками.

  Пустые строки, пробелы и комментарии обычно игнорируются. Пустые
 строки игнорируются в файлах (но не в интерактивной оболочке, когда они
 завершают составные инструкции). Пробелы внутри инструкций и выражений
 игнорируются практически всегда (за исключением строковых литералов,
 а также когда они используются для оформления отступов). Комментарии
 игнорируются всегда: они начинаются с символа # (не внутри строковых
 литералов) и простираются до конца строки.

  Строки документирования игнорируются, но сохраняются и отображаются
 специализированными инструментами. В языке Python поддерживается
 дополнительная форма комментариев, которая называется строками
 документирования, которые, в отличие от комментариев, начинающихся с #,
 сохраняются и доступны для просмотра во время выполнения. Строки
 документирования – это обычные строки, которые располагаются в начале
 файлов с программами и в некоторых инструкциях. Интерпретатор
 игнорирует их содержимое, но они автоматически присоединяются
 к объектам во время выполнения и могут отображаться инструментами
 доступа к документации. Строки документирования являются частью
 стратегии документирования в языке Python и будут рассматриваться
 в последней главе этой части книги.

 Как уже говорилось ранее, в языке Python отсутствует необходимость
объявлять типы переменных – только один этот факт упрощает синтаксис
языка больше, чем любые другие особенности. Но для большинства новых
пользователей самой необычной особенностью синтаксиса языка Python
кажется отсутствие фигурных скобок и точек с запятой, используемых
в качестве разделителей блоков и инструкций во многих других языках,
поэтому давайте рассмотрим их поближе.


 Разделители блоков: правила оформления отступов

 Интерпретатор автоматически определяет границы блоков по величине
отступов – то есть по ширине пустого пространства слева от программного
кода. Все инструкции, смещенные вправо на одинаковое расстояние,
принадлежат к одному и тому же блоку кода. Другими словами, инструкции
в блоке выстроены по вертикальной линии. Блок заканчивается либо
с концом файла, либо как только встретится строка с меньшим отступом;
более глубоко вложенные блоки имеют более широкие отступы,
чем инструкции в объемлющем блоке. Например, на рис. 12.1 показана
структура блоков следующего фрагмента программного кода:

x = 1
if x:
    y = 2
    if y:
        print ‘block2’
    print ‘block1’
print ‘block0’

 Данный фрагмент содержит три блока: первый (программный код верхнего
уровня) вообще не имеет отступов, второй (внутри внешней инструкции if)
имеет отступ из четырех пробелов и третий (инструкция print внутри
вложенной инструкции if) имеет отступ из восьми пробелов.

 Вообще программный код верхнего уровня (не вложенный) должен начинаться
в строках с позиции 1. Вложенные блоки могут начинаться
с любой позиции – отступ может состоять из любого числа пробелов
и символов табуляции, главное, чтобы все инструкции в одном блоке имели
одинаковые отступы. То есть для интерпретатора не важно, как будут
оформляться отступы, главное, чтобы оформление было непротиворечивым.
Наиболее часто для смещения на один уровень используются четыре пробела
или один символ табуляции, но в этом отношении не существует никаких
стандартов.

 Правила оформления отступов в программном коде являются вполне
естественными. Например, в следующем фрагменте демонстрируются типичные
ошибки, связанные с оформлением отступов:

  x = ‘SPAM’  # Ошибка: отступ в первой строке
if ‘rubbery’ in ‘shrubbery’:
    print(x * 8)
        x += ‘NI’  # Ошибка: неуместный отступ
        if x.endswith(‘NI’):
                x *= 2
            print(x)  # Ошибка: непоследовательное оформление отступов

 Правильно оформленная версия этого фрагмента приводится ниже – даже
в таком простом примере, как этот, правильное оформление отступов делает
программный код намного более удобочитаемым:

x = ‘SPAM’
if ‘rubbery’ in ‘shrubbery’:
    print(x * 8)
    x += ‘NI’
    if x.endswith(‘NI’):
        x *= 2
        print(x) # Выведет “SPAMNISPAMNI”

 Единственное, где в языке Python пробелы имеют большое значение, –
это когда они находятся левее программного кода; в большей части других
случаев неважно, есть пробелы или нет. При этом отступы
в действительности являются частью синтаксиса языка, а не просто
предложением по оформлению: все инструкции внутри любого заданного блока
должны иметь одинаковые отступы, в противном случае интерпретатор
сообщит о синтаксической ошибке. Т.к. вам не требуется явно отмечать
начало и конец вложенного блока, различные синтаксические элементы,
которые можно найти в других языках, в языке Python не нужны.

 Как уже отмечалось в главе 10, отступы, как часть синтаксической
модели, стали важным компонентом обеспечения удобочитаемости в языках
структурного программирования, таких как Python. Иногда синтаксис языка
Python описывают фразой «what you see is what you get» (что видишь,
то и получаешь) – отступ каждой строки однозначно говорит, к какому
блоку она принадлежит. Такой непротиворечивый внешний вид программного
кода на языке Python обеспечивает простоту его сопровождения
и многократного использования.

 Не смешивайте пробелы и символы табуляции: новый механизм проверки
ошибок в версии 3.0

 Для оформления отступов допускается использовать пробелы и символы
табуляции, но обычно не принято смешивать их внутри блока – используйте
что-то одно – или пробелы, или символы табуляции. С технической точки
зрения считается, что символ табуляции смещает текущую позицию в строке
до ближайшей позиции с номером, кратным 8, и программный код будет
интерпретироваться безошибочно, если пробелы и символы табуляции
смешиваются непротиворечивым способом. Однако такой программный код
будет достаточно сложно изменять. Хуже того, смешивание пробелов
и символов табуляции ухудшают удобочитаемость программного кода –
символы табуляции могут отображаться в текстовом редакторе другого
программиста совсем не так, как у вас.

 В действительности по только что описанным причинам, интерпретатор
Python 3.0 считает ошибкой непоследовательное смешивание пробелов
и символов табуляции в пределах блока (то есть, когда величина отступов
из смешанных символов в пределах блока может отличаться в зависимости
от интерпретации ширины символов табуляции). В Python 2.6 допускается
подобное смешивание. Однако эта версия интерпретатора имеет ключ -t
командной строки, при использовании которого интерпретатор будет
предупреждать о непоследовательном использовании символов табуляции,
а при запуске с ключом -tt он будет считать ошибкой такое оформление
программного кода (вы можете указывать эти ключи в командной строке
при запуске своего сценария, например: python –t main.py). Режим работы
интерпретатора Python 3.0 эквивалентен запуску интерпретатора
версии 2.6 с ключом -tt.


 Разделители инструкций: строки и многострочные инструкции

 В языке Python инструкция обычно заканчивается в конце строки. Однако
если инструкция слишком велика, чтобы уместиться в одной строке, можно
использовать следующие специальные правила размещения инструкции
в нескольких строках:

  Инструкции могут располагаться в нескольких строках, если они окружены
 синтаксической парой скобок. Язык Python позволяет продолжить ввод
 инструкции в следующей строке, когда содержимое инструкции заключено
 в пару скобок (), {} или []. Примерами инструкций, которые могут
 располагаться в нескольких строках, могут служить выражения в круглых
 скобках, литералы словарей и списков – инструкция не считается
 законченной, пока интерпретатор Python не встретит строку с закрывающей
 скобкой (), } или ]). Промежуточные строки (вторая и последующие строки
 инструкции) могут иметь любые отступы, но желательно, чтобы вы
 обеспечили одинаковое выравнивание по вертикали для повышения
 удобочитаемости, если это возможно. Это правило относится также
 к генераторам словарей и множеств в Python 3.0.

  Инструкции могут располагаться в нескольких строках, если они
 завершаются символом обратного слэша. Это несколько устаревшая
 особенность, но если необходимо разместить инструкцию в нескольких
 строках, можно в конец каждой предшествующей строки вставить символ
 обратного слэша, который будет служить признаком, что инструкция
 продолжается на следующей строке. Так как существует возможность
 использовать круглые скобки для заключения длинных конструкций, символы
 обратного слэша практически никогда не используются. При использовании
 такого подхода легко допустить ошибку: обычно интерпретатор замечает
 отсутствие символа \ и выводит сообщение об ошибке, но если текущая
 и следующая строки могут интерпретироваться, как самостоятельные
 и независимые инструкции, ошибка не будет замечена, а результат может
 оказаться непредсказуемым.

  Литералы строк в тройных кавычках могут располагаться в нескольких
 строках. Очень длинные строковые литералы можно разместить в нескольких
 строках – блоки строк в тройных кавычках, с которыми мы встретились
 в главе 7, предназначены именно для этих целей. Там же, в главе 7,
 мы узнали, что к строковым литералам применяется неявная операция
 конкатенации – в соответствии с правилом скобок, упоминавшимся выше,
 использование круглых скобок позволит расположить несколько строковых
 литералов в разных строках.

  Другие правила. Существует еще несколько моментов, которые хотелось бы
 упомянуть. Хотя это и используется редко, инструкции можно завершать
 точкой с запятой – иногда это соглашение применяется, чтобы компактно
 разместить несколько инструкций в одной строке. Кроме того, в любом
 месте в файле могут присутствовать пустые строки и комментарии.
 Комментарии (которые начинаются с символа #) простираются до конца
 строки.


 Несколько специальных случаев

 Ниже показано, как выглядит инструкция при использовании правила
использования скобок. Конструкции, заключенные в скобки, могут занимать
произвольное число строк:

L = [“Good”,
     “Bad”,
     “Ugly”]  # Пара скобок может охватывать несколько строк

 Этот прием также можно использовать с круглыми скобками (выражения,
аргументы функций, заголовки функций, кортежи и выражения-генераторы)
и с фигурными скобками (словари, литералы множеств в версии 3.0, а также
генераторы множеств и словарей). С некоторыми из этих инструментов мы
познакомимся в следующих главах, однако это правило охватывает
большинство конструкций, которые могут располагаться в нескольких
строках. При желании можно использовать символы обратного слеша, но этот
прием редко используется на практике:

if a == b and c == d and \
   d == e and f == g:
    print(‘olde’)  # Символы обратного слэша позволяют продолжить...

 Поскольку любое выражение можно заключить в круглые скобки, то лучше
использовать их, когда возникает необходимость расположить инструкцию
в нескольких строках:

if (a == b and c == d and
    d == e and e == f):
    print(‘new’) # Но круглые скобки позволяют то же самое

 На практике символы обратного слэша к использованию не рекомендуются,
потому что они малозаметны и их легко пропустить по случайности.
В следующем примере задача состояла в присваивании переменной x
значения 10, если учесть наличие символа обратного слэша. Однако если
обратный слэш случайно опустить, переменной x будет присвоено
значение 6; при этом никаких сообщений об ошибке не появится
(+4 – это допустимая инструкция выражения). В действующих программах
подобная случайность в более сложных инструкциях присваивания могла бы
привести к весьма неприятным проблемам:

x = 1 + 2 + 3 \  # Отсутствие \ существенно изменяет смысл выражения
+4

 Еще один специальный случай: в языке Python допускается записывать
в одной строке несколько несоставных инструкций (то есть инструкций,
которые не имеют вложенных инструкций), разделяя их точками с запятой.
Некоторые программисты используют эту возможность для экономии
пространства в файле, однако удобочитаемость будет выше, если в каждой
строке размещать только одну инструкцию:

x = 1; y = 2; print(x)  # Несколько простых инструкций в одной строке

 Как мы узнали в главе 7, строковые литералы в тройных кавычках также
могут занимать несколько строк. Кроме того, если два строковых литерала
следуют друг за другом, они объединяются, как если бы между ними стоял
оператор конкатенации +. Согласно правилу скобок, если несколько
строковых литералов окружить круглыми скобками, их можно будет
расположить в разных строках. В первом примере ниже между строками будет
вставлен символ конца строки и переменной S будет присвоен результат
‘\naaaa\nbbbb \ncccc’, а во втором примере будет выполнена неявная
операция конкатенации и переменной S будет присвоена строка
‘aaaabbbbcccc’. Во втором случае комментарии будут игнорироваться,
а в первом они станут частью строки S:

S = “””
aaaa
bbbb
cccc”””

S = (‘aaaa’
     ‘bbbb’  # Этот комментарий игнорируется
     ‘cccc’)

 И наконец, Python позволяет располагать тело составной инструкции
в одной строке с заголовком при условии, что тело образует простая
(несоставная) инструкция. Вам часто придется видеть следующий вариант
использования простых инструкций с единственным условием и действием:

if 1: print(‘hello’)  # Простая инструкция в строке заголовка

 Эти специальные случаи можно комбинировать между собой, чтобы писать
программный код, который будет сложно читать, но я не рекомендую
поступать так – старайтесь записывать по одной инструкции в строке
и выравнивайте все блоки; исключение могут составлять только простейшие
случаи. Когда вам придется вернуться к своей программе спустя полгода,
вы будете рады, что поступали именно так.


 Проверка истинности

 Понятия сравнения, равенства и значений истинности были введены
в главе 9. Инструкция if – это первая инструкция на нашем пути, которая
использует результаты проверки, поэтому здесь мы подробнее поговорим
о некоторых из этих идей. В частности, о том, что логические операторы
в языке Python несколько отличаются от аналогичных операторов в таких
языках, как C. В языке Python:

  Любое число, не равное нулю, или непустой объект интерпретируется
 как истина.

  Числа, равные нулю, пустые объекты и специальный объект None
 интерпретируются как ложь.

  Операции сравнения и проверки на равенство применяются к структурам
 данных рекурсивно.
 
  Операции сравнения и проверки на равенство возвращают значение True
 или False (которые представляют собой версии чисел 1 и 0).

  Логические операторы and и or возвращают истинный или ложный
 объект-операнд.

 В двух словах, логические операторы используются для объединения
результатов других проверок. В языке Python существует три логических
оператора:

X and Y

 Истина, если оба значения X и Y истинны.

 X or Y

 Истина, если любое из значений X или Y истинно.

not X

 Истина, значение X ложно (выражение возвращает значение True или False)

 Здесь X и Y могут быть любыми значениями истинности или выражениями,
которые возвращают значения истинности (например, выражение проверки
на равенство, сравнение с диапазоном значений и так далее). В языке
Python логические операторы имеют вид слов (вместо обозначений &&, ||
и !, как это реализовано в языке C). Кроме того, логические операторы
and и or возвращают истинный или ложный объект, а не значение True
или False. Рассмотрим несколько примеров, чтобы понять, как они
работают:

\>>> 2 < 3, 3 < 2  # Меньше чем: возвращает True или False (1 или 0)
(True, False)

 Операция сравнения величин, как в данном случае, возвращает в качестве
результата значение True или False, которые, как мы узнали
в главах 5 и 9, в действительности являются особыми версиями целых чисел
1 и 0 (выводятся они особым образом, а во всем остальном являются
обычными числами).

 С другой стороны, операторы and и or всегда возвращают объект – объект
либо слева от оператора, либо справа. Если действие этих операторов
проверяется инструкцией if или другими инструкциями, они будут иметь
ожидаемый результат (не забывайте, что каждый объект может
интерпретироваться как истина или как ложь), но это не будут простые
значения True или False.

 В случае оператора or интерпретатор начинает вычислять значения
объектов-операндов слева направо и возвращает первый, имеющий истинное
значение. Кроме того, интерпретатор прекратит дальнейшие вычисления,
как только будет найден первый объект, имеющий истинное значение.
Это обычно называют вычислением по короткой схеме, так как конечный
результат становится известен еще до вычисления остальной части
выражения:

\>>> 2 or 3, 3 or 2  # Вернет левый операнд, если он имеет истинное
(2, 3)  # Иначе вернет правый операнд (истинный или ложный)     значение
\>>> [] or 3
3
\>>> [] or {}
{}

 В первой строке предыдущего примера оба операнда (2 и 3) имеют истинные
(то есть ненулевые) значения, поэтому интерпретатор всегда будет
останавливать вычисления и возвращать операнд слева. В других двух
операциях левый операнд имеет ложное значение (пустой объект), поэтому
интерпретатор просто вычисляет и возвращает объект справа (который может
иметь как истинное, так и ложное значение).

 Вычисление оператора and также останавливается, как только результат
станет известен, однако в этом случае интерпретатор вычисляет операнды
слева направо и возвращает первый объект, имеющий ложное значение:

\>>> 2 and 3, 3 and 2  # Вернет левый операнд, если он имеет ложное
(3, 2)  # Иначе вернет правый операнд (истинный или ложный)     значение
\>>> [] and {}
[]
\>>> 3 and []
[]

 Здесь в первой строке оба операнда имеют истинные значения, поэтому
интерпретатор вычислит оба операнда и вернет объект справа. Во второй
проверке левый операнд имеет ложное значение ([]), поэтому интерпретатор
останавливает вычисления и возвращает его в качестве результата
проверки. В последней проверке левый операнд имеет истинное
значение (3), поэтому интерпретатор вычисляет и возвращает объект справа
(который имеет ложное значение []). Конечный результат будет тот же,
что и в языке C и во многих других языках, – вы получаете значение,
которое логически интерпретируется как истина или ложь при использовании
в инструкции if или while. Однако в языке Python логические операторы
возвращают либо левый, либо правый объект, а не простое целочисленное
значение.

 Такое поведение операторов and и or может показаться странным на первый
взгляд, поэтому загляните во врезку «Придется держать в уме: логические
значения», где вы найдете примеры, как иногда эта особенность может
использоваться программистами на языке Python. Кроме того, в следующем
разделе демонстрируются часто встречающиеся способы использования такого
поведения операторов и их замена в более свежих версиях Python.


 Трехместное выражение if/else

 Одна из основных ролей логических операторов в языке Python заключается
в образовании выражений, которые выполняются так же, как условная
инструкция if. Рассмотрим следующую инструкцию, которая записывает
в A значение Y или Z, в зависимости от истинности значения X:

if X:
    A = Y
else:
    A = Z

 Иногда, как в данном примере, элементы инструкции настолько просты, что
кажется излишеством тратить на них четыре строки. В некоторых случаях
у нас может появиться желание вложить такую конструкцию внутрь другой
инструкции вместо того, чтобы выполнять присваивание переменной. По этим
причинам (и, откровенно говоря, потому что в языке C имеется похожая
возможность)1 в версии Python 2.5 появилась новая конструкция,
позволяющая записать те же действия в виде единственного выражения:

A = Y if X else Z

 Данное выражение дает тот же результат, что и предыдущая
четырех строчная инструкция if, но выглядит она проще.
Как и в предыдущей инструкции, интерпретатор выполняет выражение Y,
только если объект X имеет истинное значение, а выражение Z выполняется,
только если объект X имеет ложное значение. То есть вычисления здесь
также выполняются по сокращенной схеме. Ниже приводятся
несколько примеров выражения в действии:

\>>> A = ‘t’ if ‘spam’ else ‘f’  # Непустая строка – это истина
\>>> A
‘t’
\>>> A = ‘t’ if ‘’ else ‘f’
\>>> A
‘f’

 До версии Python 2.5 (да и после) тот же эффект можно было получить
за счет комбинирования операторов and и or благодаря тому, что они
возвращают объект слева или справа:

A = ((X and Y) or Z)

 Этот прием работает, но он скрывает в себе ловушку – он предполагает,
что Y будет иметь истинное значение. В этом случае эффект будет тот же
самый: оператор and выполнится первым и вернет Y, если X имеет истинное
значение. В противном случае оператор or просто вернет Z. Другими
словами, мы получаем: «if X then Y else Z».

 Эта комбинация операторов and/or требует некоторого времени, чтобы
осознать ее при первом знакомстве, но, начиная с версии 2.5, надобность
в таком приеме отпала, так как существует более наглядная конструкция
Y if X else Z, которую можно использовать в качестве выражения. Если же
составляющие достаточно сложны, лучше использовать полноценную
инструкцию if.

 В качестве дополнительного примечания: в языке Python следующее
выражение дает похожий эффект – благодаря тому, что функция bool
преобразует X в соответствующее целое число 1 или 0, которое затем
используется для выбора требуемого значения из списка:

A = [Z, Y][bool(X)]

 Например:

\>>> [‘f’, ‘t’][bool(‘’)]
‘f’
\>>> [‘f’, ‘t’][bool(‘spam’)]
‘t’

 Однако это далеко не то же самое, потому что в данном случае
интерпретатор не использует сокращенную схему вычисления – он всегда
будет вычислять оба значения Z и Y, независимо от значения X. Из-за всех
этих сложностей лучше использовать более простое и более понятное
выражение if/else, появившееся в версии Python 2.5. Кроме того, этим
выражением не следует злоупотреблять и следует использовать его, только
если части выражения достаточно просты, в противном случае лучше
использовать обычную инструкцию if, что облегчит модификацию
программного кода в будущем. Ваши коллеги будут благодарны вам за это.

 Однако вы по-прежнему можете встретить конструкцию на основе комбинации
and/or в программном коде, написанном до появления версии Python 2.5
(и в программном коде, написанном программистами, использовавшими
язык C, и не сумевшими избавиться от прошлых привычек).


 Придется держать в уме: логические значения

 В языке Python часто используется прием выбора одного объекта
из множества, основанный на необычном поведении логических операторов.
Следующая инструкция:

X = A or B or C or None

 - присвоит переменной X первый непустой (имеющий истинное значение)
объект из множества объектов A, B и C или None, если все эти объекты
окажутся пустыми. Этот прием стал возможен благодаря тому, что оператор
or возвращает один из двух объектов и, как оказывается, это весьма
распространенная парадигма программирования на языке Python: чтобы
выбрать непустой объект из фиксированного множества, достаточно просто
объединить их в выражение с помощью оператора or. В простейшем случае
эту особенность можно использовать для назначения значения
по умолчанию – следующая инструкция присвоит переменной X значение
переменной A, если оно истинно (или непустое), и default –
в противном случае:

X = A or default

 Также важно осознать, как выполняются вычисления по сокращенной схеме,
потому что справа от логического оператора может находиться функция,
выполняющая важную работу или оказывающая побочное влияние, вызов
которой не произойдет из-за действия правила вычисления
по сокращенной схеме:

if f1() or f2(): ...

 В данном случае, если функция f1 вернет истинное (или непустое)
значение, интерпретатор никогда не вызовет функцию f2. Чтобы
гарантировать вызов обеих функций, можно вызвать их до применения
оператора or:

tmp1, tmp2 = f1(), f2()
if tmp1 or tmp2: ...

 Вы уже видели другой вариант использования такого поведения: благодаря
особенностям работы логических операторов выражение ((A and B) or C)
может использоваться для достаточно близкой (смотрите обсуждение этой
инструкции выше) имитации инструкции if/else.

 Другие случаи логических значений мы уже видели в предыдущих главах.
Как мы видели в главе 9, вследствие того, что все объекты могут
расцениваться как истинные или ложные значения, в языке Python легко
и просто выполнить проверку объекта напрямую (if X:) вместо того, чтобы
сравнивать его с пустым значением (if X != ‘’:). В случае строк эти
две проверки равнозначны. Мы также узнали в главе 5, что логические
значения True и False являются обычными целыми числами 1 и 0 и могут
использоваться для инициализации переменных (X = False), в условных
выражениях циклов (while True:) и для отображения результатов
в интерактивном сеансе.

 Кроме того, в шестой части, при обсуждении темы перегрузки операторов
мы увидим, что в определениях новых типов объектов с помощью классов
имеется возможность определять их логическую природу с помощью методов
__bool__ и __len__ (метод __bool__ в версии 2.6 носит имя __nonzero__).
Если первый метод отсутствует в определении класса, для проверки
истинности объекта используется второй метод – если возвращаемая длина
равна нулю, объект считается ложным, так как пустые объекты всегда
считаются ложными.
"""
