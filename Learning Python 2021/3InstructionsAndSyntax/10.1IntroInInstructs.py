"""
 Введение в инструкции языка Python


 Структура программы на языке Python

 Другой способ понять роль инструкций состоит в том, чтобы вновь
вернуться к иерархии понятий, представленной в главе 4,
в которой рассказывалось о встроенных объектах и выражениях,
управляющих ими. Эта глава рассматривает следующую ступень иерархии:

  1. Программы делятся на модули.

  2. Модули содержат инструкции.

  3. Инструкции состоят из выражений.

  4. Выражения создают и обрабатывают объекты.

 Синтаксис языка Python по сути построен на инструкциях и выражениях.
Выражения обрабатывают объекты и встраиваются в инструкции. Инструкции
представляют собой более крупные логические блоки программы –
они напрямую используют выражения для обработки объектов,
которые мы рассматривали в предыдущих главах. Кроме того, инструкции –
это место, где создаются объекты (например, в инструкциях присваивания),
а в некоторых инструкциях создаются совершенно новые виды объектов
(функции, классы и так далее).

 
 Инструкции в языке Python

 В табл. 10.1 приводится набор инструкций языка Python. В этой
части книги рассматриваются инструкции, которые в таблице расположены
от начала и до инструкций break и continue. Ранее неофициально вам уже
были представлены некоторые из инструкций, присутствующих в табл.
В этой части книги будут описаны подробности, опущенные ранее; вашему
вниманию будут представлены остальные процедурные инструкции языка
Python, а также будет рассмотрена общая синтаксическая модель.
Инструкции, расположенные в табл. 10.1 ниже, имеют отношение к крупным
блокам программы – функциям, классам, модулям и исключениям,
и заключают в себе крупные понятия программирования, поэтому каждой
из них будет посвящен отдельный раздел. Более экзотические инструкции,
такие как del (которая удаляет различные компоненты), раскрываются далее
в книге или в стандартной документации по языку Python.

  Инструкция        Роль             Пример
  Присваивание      Создание ссылок  a, *b = ‘good’, ‘bad’, ‘ugly’

  Вызовы и другие   Запуск функций   log.write(“spam, ham”)
  выражения

  Вызов функции     Вывод объектов   print(‘The Killer’, joke)
  print

  if/elif/else      Операция выбора  if “python” in text:
                                        print(text)

  for/else          Обход            for x in mylist:
                последовательности      print(x)
                    в цикле

  while/else        Циклы общего     while X > Y:
                    назначения          print(‘hello’)

  pass              Пустая           while True:
            инструкция-заполнитель       pass

  break             Выход из цикла   while True:
                                        if exittest(): break

  continue          Переход          while True:
                    в начало цикла      if skiptest(): continue

  def               Создание функций def f(a, b, c=1, *d):
                    и методов           print(a+b+c+d[0])

  return            Возврат          def f(a, b, c=1, *d):
                    результата          return a+b+c+d[0]

  yield             Функции-         def gen(n):
                    генераторы       for i in n: yield i*2

  global            Пространства     x = ‘old’
                    имен             def function():
                                        global x, y; x = ‘new’

  nonlocal          Пространства     def outer():
                    имен (3.0+)          x = ‘old’
                                         def function():
                                            nonlocal x; x = ‘new’

  import           Доступ к модулям  import sys

  from             Доступ            from sys import stdin
                   к атрибутам
                   модуля

  class            Создание объектов class Subclass(Superclass):
                                        staticData = []
                                        def method(self): pass

  try/except       Обработка         try:
  /finally         исключений           action()
                                     except:
                                         print(‘action error’)

  raise            Возбуждение       raise endSearch(location)
                   исключений

  assert           Отладочные        assert X > Y, ‘X too small’
                   проверки

  with/as          Менеджеры         with open(‘data’) as myfile:
                   контекста            process(myfile)
                   (2.6+)

  del              Удаление ссылок   del data[k]
                                     del data[i:j]
                                     del obj.attr
                                     del variable

 В табл. перечислены разновидности инструкций в версии Python 3.0 –
элементы программного кода, каждый из которых имеет свой характерный
синтаксис и назначение. Ниже приводятся несколько замечаний к таблице:

  Инструкции присваивания могут принимать различные синтаксические
 формы, которые описываются в главе 11: простое, присваивание
 последовательностей, комбинированное присваивание и другие.

  В версии 3.0 print не является ни зарезервированным словом,
 ни инструкцией – это встроенная функция. Однако она практически всегда
 выполняется как инструкция (то есть занимает отдельную строку
 в программе), поэтому ее обычно воспринимают как инструкцию. Мы поближе
 познакомимся с функцией print в главе 11.

  Начиная с версии 2.5 yield в действительности является выражением,
а не инструкцией. Как и функция print, это выражение обычно занимает
отдельную строку, и потому оно было включено в табл. 10.1. Однако иногда
в сценариях выполняется присваивание этой инструкции или извлечение
результата из нее, как будет показано в главе 20. Кроме того, в отличие
от print, имя yield является зарезервированным словом.

 Большая часть инструкций, перечисленных в табл. 10.1, также имеется
в версии Python 2.6. Ниже приводятся несколько замечаний для тех,
кто пользуется Python 2.6 или более ранними версиями:

  В версии 2.6 инструкция nonlocal недоступна. Как мы увидим в главе 17,
 существуют другие способы добиться того же эффекта в отношении
 присваивания значений переменным.

  В версии 2.6 print является не функцией, а инструкцией со своим
 характерным синтаксисом, который описывается в главе 11.

  exec (в версии 3.0 – встроенная функция, позволяющая выполнять
 фрагменты программного кода) в версии 2.6 также является инструкцией
 со своим характерным синтаксисом. Так как она поддерживает возможность
 заключения аргументов в круглые скобки, в версии 2.6 ее можно
 использовать как функцию.

  В версии 2.5 инструкции try/except и try/finally были объединены:
 ранее это были две самостоятельные инструкции, но теперь мы можем
 использовать предложения except и finally одновременно,
 в одной инструкции try.

  В версии 2.5 инструкция with/as была необязательным расширением,
 и она была недоступна, если в программный код не включить инструкцию
 from __future__ import with_statement (глава 33).


 История о двух if

 Однако прежде чем углубиться в детали какой-либо конкретной инструкции
из табл. 10.1, я хочу обратить ваше внимание на синтаксис инструкций
в языке Python, показав, как не надо писать программный код,
чтобы у вас была возможность сравнить его с другими синтаксическими
моделями, которые, возможно, вы видели ранее.

 Рассмотрим следующую условную инструкцию на языке C:

if (x > y) {
    x = 1;
    y = 2;
}

 Это могла бы быть инструкция на языке C, C++, Java, JavaScript
или Perl. А теперь взгляните на эквивалентную инструкцию
на языке Python:

if x > y:
    x = 1
    y = 2

 Первое, что бросается в глаза, – инструкция на языке Python выглядит
компактнее, точнее, в ней меньше синтаксических элементов.
Это соответствует основным принципам языка; так как Python –
это язык сценариев, его основная цель состоит в том, чтобы облегчить
жизнь программистам за счет меньшего объема ввода с клавиатуры.

 Если быть более точным, то, сравнив две синтаксических модели,
можно заметить, что язык Python один новый элемент добавляет,
а три элемента, которые присутствуют в языках, подобных языку C,
ликвидирует.


 Что добавляет язык Python

 Один из новых синтаксических элементов в языке Python – это символ
двоеточия (:). Все составные инструкции в языке Python (то есть
инструкции, которые включают вложенные в них инструкции) записываются
в соответствии с одним и тем же общим шаблоном, когда основная
инструкция завершается двоеточием, вслед за которым располагается
вложенный блок кода, обычно с отступом под строкой основной инструкции,
как показано ниже:

Основная инструкция:
    Вложенный блок инструкций

 Двоеточие является обязательным, а его отсутствие является самой
распространенной ошибкой, которую допускают начинающие программисты, –
я встречал тысячи подтверждений этому в учебных классах. Фактически
если вы плохо знакомы с языком Python, то вы почти наверняка очень скоро
забудете о символе двоеточия. Большинство текстовых редакторов,
обладающих функцией подсветки синтаксиса, делают эту ошибку легко
заметной, а с опытом вырабатывается привычка вставлять двоеточие
бессознательно (да так, что вы начинаете вводить двоеточие в программный
код на языке C++, что приводит к большому числу весьма интересных
сообщений об ошибках от компилятора C++!).


 Что Python устраняет

 Хотя Python требует ввода дополнительного символа двоеточия, существуют
три элемента, обязательных для языков, подобных языку C, которые языку
Python не требуются.


 Круглые скобки не обязательны

 Первый элемент – это пара круглых скобок, окружающих условное выражение
в основной инструкции:

if (x < y)

 Круглые скобки здесь являются обязательными во многих
C-подобных языках. В языке Python это не так – мы просто можем
опустить скобки, и инструкция будет работать точно так же:

if x < y

 Точнее говоря, так как каждое выражение может быть заключено в скобки,
присутствие их не будет противоречить синтаксису языка Python, и они не
будут считаться ошибкой. Но не делайте этого: вы лишь понапрасну будете
изнашивать свою клавиатуру, а окружающим сразу будет видно, что вы
типичный программист на C, еще только изучающий Python (когда-то
и я был таким же). Стиль языка Python состоит в том, чтобы вообще
опускать скобки в подобных инструкциях.


 Конец строки является концом инструкции

 Второй, еще более важный синтаксический элемент, который вы
не найдете в программном коде на языке Python, – это точка с запятой.
В языке Python не требуется завершать инструкции точкой с запятой,
как это делается в C-подобных языках:

x = 1;

 Общее правило в языке Python гласит, что конец строки автоматически
считается концом инструкции, стоящей в этой строке. Другими словами,
вы можете отбросить точку с запятой, и инструкция будет работать
точно так же:

x = 1

 Существует несколько способов обойти это правило, как будет показано
чуть ниже. Но в общем случае большая часть программного кода на языке
Python пишется по одной инструкции в строке, и тогда точка с запятой
не требуется. В данном случае, если вы скучаете по тем временам,
когда программировали на языке C (если такое состояние вообще
возможно…), можете продолжать вставлять точки с запятой в конце каждой
инструкции – синтаксис языка допускает это. Но не делайте этого:
потому что если вы будете поступать так, окружающим сразу будет видно,
что вы остаетесь программистом на языке C, который никак не может
переключиться на использование языка Python. Стиль языка Python состоит
в том, чтобы вообще опускать точки с запятой.


 Конец отступа – это конец блока

 Теперь третий, и последний, синтаксический компонент, который удаляет
Python, и возможно, самый необычный для недавних экс-С-программеров
(пока они не поработают с Python десять минут и не поймут,
что в действительности это является достоинством языка), – вы не вводите
ничего специально в ваш код, чтобы синтаксически пометить начало
и конец вложенного блока кода. Вам не нужно вставлять begin/end,
then/endif или фигурные скобки вокруг вложенных блоков, как это делается
в C-подобных языках:

if (x > y) {
    x = 1;
    y = 2;
}
 Для этих целей в языке Python используются отступы, когда все
инструкции в одном и том же вложенном блоке оформляются с одинаковыми
отступами от левого края. По величине отступа интерпретатор определяет,
где находится начало блока и где – конец:

if x > y:
    x = 1
    y = 2

 Под отступами в данном примере я подразумеваю пустое пространство слева
от двух вложенных инструкций. Интерпретатор не накладывает ограничений
на то, как выполняются отступы (для этого можно использовать символы
пробела или символы табуляции), и на величину отступов (допускается
использовать любое число пробелов или символов табуляции). При этом
отступ для одного вложенного блока может существенно отличаться
от отступа для другого блока. Синтаксическое правило состоит лишь в том,
что все инструкции в пределах одного блока должны иметь один
и тот же отступ от левого края. Если это не так, будет получена
синтаксическая ошибка, и программный код не будет работать, пока вы
не исправите отступ.


 Почему отступы являются частью синтаксиса?

 Правило оформления отступов может показаться необычным на первый взгляд
для программистов, работавших с C-подобными языками программирования,
но это было сделано преднамеренно и является одним из основных способов,
которыми язык Python вынуждает программистов писать однородный
и удобочитаемый программный код. По существу это означает, что вы должны
выстраивать свой программный код вертикально, выравнивая его
в соответствии с логической структурой. В результате получается менее
противоречивый и более удобочитаемый программный код (в отличие
от большей части кода, написанного на C-подобных языках).

 Требования к выравниванию программного кода в соответствии с его
логической структурой – это главная составляющая, способствующая
созданию удобочитаемого кода, и, следовательно, кода, пригодного
к многократному использованию и простого в сопровождении как вами,
так и другими. Фактически даже если ранее вы никогда не использовали
Python, после прочтения этой книги у вас должна выработаться привычка
оформлять отступы в программном коде для удобочитаемости в любом языке
программирования. Язык Python вносит определенные ограничения, сделав
отступы частью синтаксиса, но они достаточно важны для любого языка
программирования и оказывают огромное влияние на применимость вашего
программного кода.

 Ваш опыт может отличаться от моего, но когда я занимался разработкой
полный рабочий день, мне платили зарплату за работу над крупными старыми
программами, написанными на языке C++, над которыми долгие годы
трудились множество программистов. Практически у каждого программиста
был свой стиль оформления программного кода. Например, мне часто
приходилось изменять циклы while, написанные на языке C++, которые
начинались примерно так:

while (x > 0) {

 Даже еще не дойдя до отступов, мы можем столкнуться с тремя
или четырьмя способами расстановки фигурных скобок в C-подобных языках.
В организациях часто ведутся жаркие споры и пишутся стандарты
по оформлению исходных текстов программ (обсуждение которых сильно
выходит за рамки проблем, которые решаются в процессе программирования).
Оставим этот вопрос в стороне, ниже приводится пример оформления,
с которым мне часто приходилось сталкиваться в программном коде
на языке C++. Первый программист, который поработал над этим циклом,
оформлял отступы четырьмя пробелами:

while (x > 0) {
    --------;
    --------;

 Со временем этот программист был переведен на руководящую должность,
и его место занял другой, который предпочитал использовать более широкие
отступы:

while (x > 0) {
    --------;
    --------;
        --------;
        --------;

 Позднее и он ушел на другую работу, а его место занял третий, которому
не нравилось делать отступы:

while (x > 0) {
    --------;
    --------;
        --------;
        --------;
--------;
--------;
}

 И так далее. В конце блок завершается закрывающей фигурной скобкой (}),
которая и делает этот фрагмент структурированным (о чем можно говорить
с определенной долей сарказма). В любом блочно-структурированном языке
программирования, будь то Python или другой язык, если вложенные блоки
не имеют непротиворечивых отступов, их очень сложно читать, изменять
и приспосабливать для многократного использования. Отступ – это важная
составляющая поддержки удобочитаемости.

 Ниже приводится другой пример, на котором, возможно, вам приходилось
обжечься, если вы достаточно много программировали на C-подобном языке.
Взгляните на следующие инструкции языка C:

if (x)
    if (y)
        statement1;
else
    statement2;

 К какому оператору if относится инструкция else? Это удивительно,
но инструкция else относится к вложенному оператору if (if(y)),
даже при том, что визуально она выглядит так, как если бы относилась
к внешнему оператору if (if(x)). Это классическая ловушка языка C
и она может привести к неправильному пониманию программного кода тем,
кто его изменяет, и к появлению ошибок при его изменении, которые будут
обнаружены, только когда марсоход врежется в скалу!

 Такого не может произойти в языке Python, потому что отступы для него
имеют важное значение и программный код работает именно так,
как выглядит. Взгляните на эквивалентный фрагмент на языке Python:

if x:
    if y:
        statement1
else:
    statement2

 В этом примере инструкции if и else, расположенные на одной
вертикальной линии, связаны логически (внешний оператор if x).
В некотором смысле Python – это язык типа WYSIWYG (What You See Is
What You Get – что видишь, то и получаешь) – что вы видите,
то и получаете, потому что порядок оформления программного кода
определяет порядок его выполнения, независимо от предпочтений того,
кто его пишет.

 По моему мнению, даже если язык программирования и не требует этого,
хороший программист должен понимать, какое важное значение имеет
выравнивание для удобочитаемости и высокого качества программного кода.
Тот факт, что в языке Python отступы были возведены в ранг синтаксиса,
по большей части выглядит как достоинство языка.

 Наконец, имейте в виду, что практически любой текстовый редактор
с дружественным (для программистов) интерфейсом обладает встроенной
поддержкой синтаксической модели языка Python. В Python-среде разработки
IDLE, например, отступы оформляются автоматически1, когда начинается
ввод вложенного блока; нажатие клавиши Backspace (забой) возвращает
на один уровень вложенности выше, а кроме того, IDLE позволяет настроить
величину отступов во вложенном блоке. Нет никаких стандартных требований
к оформлению отступов: чаще всего используются четыре пробела или один
символ табуляции на каждый уровень вложенности; вам самим решать,
какой ширины отступы вы будете использовать. Выполняйте отступ вправо,
чтобы открыть вложенный блок, и возвращайтесь на предыдущий уровень,
чтобы закрыть его.

 Вообще говоря, недопустимо смешивать символы табуляции и пробелы для
оформления отступов в одном и том же блоке, если делать это
неединообразно. Для оформления отступов в блоке используйте либо символы
табуляции, либо пробелы, но не одновременно те и другие
(в действительности Python 3.0 теперь считает ошибкой непоследовательное
использование символов табуляции и пробелов, как мы увидим в главе 12).
Точно так же нежелательно смешивать символы табуляции и пробелы
для оформления отступов в любом другом структурированном языке
программирования – такой программный код очень трудно будет читать
следующему программисту, если в его текстовом редакторе отображение
символов табуляции будет настроено иначе, чем у вас. C-подобные языки
позволяют программистам нарушать это правило, но делать этого
не следует, – в результате может получиться жуткая мешанина.


 Несколько специальных случаев

 Как уже упоминалось ранее, в синтаксической модели языка Python:

  Конец строки является концом инструкции, расположенной в этой строке
 (точка с запятой не требуется).
  Вложенные инструкции объединяются в блоки по величине отступов
 (без фигурных скобок).

 Эти правила охватывают большую часть программного кода на языке Python,
который вы будете писать или с которым придется столкнуться. Однако
существуют некоторые специальные правила, которые касаются оформления
как отдельных инструкций, так и вложенных блоков.


 Специальные случаи оформления инструкций

 Обычно на каждой строке располагается одна инструкция, но вполне
возможно для большей компактности записать несколько инструкций в одной
строке, разделив их точками с запятой:

a = 1; b = 2; print(a + b)  # Три инструкции на одной строке

 Это единственный случай, когда в языке Python необходимо использовать
точки с запятой: как разделители инструкций. Однако такой подход
не может применяться к составным инструкциям. Другими словами, в одной
строке можно размещать только простые инструкции, такие как
присваивание, print и вызовы функций. Составные инструкции по-прежнему
должны находиться в отдельной строке (иначе всю программу можно было бы
записать в одну строку, что, скорее всего, не нашло бы понимания
у ваших коллег!).

 Другое специальное правило, применяемое к инструкциям, по сути является
обратным к предыдущему: допускается записывать одну инструкцию
в нескольких строках. Для этого достаточно заключить часть инструкции
в пару скобок – круглых (()), квадратных ([]) или фигурных ({}).
Любой программный код, заключенный в одну из этих конструкций, может
располагаться на нескольких строках: инструкция не будет считаться
законченной, пока интерпретатор Python не достигнет строки с закрывающей
скобкой. Например, литерал списка можно записать так:

mlist = [111,
         222,
         333]

 Так как программный код заключен в пару квадратных скобок,
интерпретатор всякий раз переходит на следующую строку,
пока не обнаружит закрывающую скобку. Литералы словарей в фигурных
скобках (а также литералы множеств и генераторы словарей и множеств
в Python 3.0) тоже могут располагаться в нескольких строках,
а с помощью круглых скобок можно оформить многострочные кортежи, вызовы
функций и выражения. Отступы в строках, где продолжается инструкция,
в учет не принимаются, хотя здравый смысл диктует, что строки все-таки
должны иметь некоторые отступы для обеспечения удобочитаемости.

 Круглые скобки являются самым универсальным средством, потому что в них
можно заключить любое выражение. Добавьте левую скобку, и вы сможете
перейти на следующую строку и продолжить свою инструкцию:

X = (A + B +
     C + D)

 Между прочим, такой прием допускается применять и к составным
инструкциям. Если вам требуется записать длинное выражение, оберните
его круглыми скобками и продолжите на следующей строке:

if (A == 1 and
    B == 2 and
    C == 3):
    print(‘spam’ * 3)

 Еще одно старое правило также позволяет переносить инструкцию
на следующую строку: если предыдущая строка заканчивается символом о
братного слеша:

X = A + B + \  # Альтернативный способ, который может быть
      C + D    # источником ошибок

 Но это устаревшее правило, которое не рекомендовано к использованию
в новых программах, потому что символы обратного слеша малозаметны
и ненадежны – не допускается наличие каких-либо других символов после
символа обратного слеша, а случайное удаление символа обратного слеша
может приводить к неожиданным эффектам, если следующая строка может
интерпретироваться, как самостоятельная инструкция. Кроме того,
это рассматривается как пережиток языка C, где очень часто используются
макроопределения #define в Питонляндии нужно все делать так,
как это делают Питонисты, а не как программисты на языке C.


 Специальный случай оформления блока

 Как уже говорилось выше, инструкции во вложенном блоке обычно
объединяются по величине отступа. Специальный случай: тело составной
инструкции может располагаться в той же строке, что и основная
инструкция, после символа двоеточия:

if x > y: print(x)

 Это позволяет записывать в одной строке условные операторы, циклы
и так далее. Однако такой прием будет работать, только если тело
составной инструкции не содержит других составных инструкций.
То есть после двоеточия могут следовать только простые инструкции –
инструкции присваивания, инструкции print, вызовы функций и подобные им.
Крупные инструкции по-прежнему должны записываться в отдельных строках.
Дополнительные части составных инструкций (такие, как блоки else
в условных инструкциях if, с которыми мы встретимся ниже) также должны
располагаться в отдельных строках. Тело инструкции может состоять
из нескольких простых инструкций, разделенных точкой с запятой,
но такой стиль оформления не приветствуется.

 Вообще, хотя это не является обязательным требованием, но если вы
будете размещать инструкции в отдельных строках
и всегда будете оформлять отступы для вложенных блоков,
ваш программный код будет проще читать и вносить в него изменения.
Кроме того, некоторые инструменты профилирования
оказываются неспособными справиться с ситуациями,
когда несколько инструкций располагаются в одной строке или когда тело
составной инструкции оказывается на одной строке вместе с основной
инструкцией. Поэтому в ваших интересах всегда стремиться оформлять
программный код как можно проще. Чтобы увидеть одно из этих правил
в действии (когда однострочная инструкция if используется для прерывания
выполнения цикла), давайте перейдем к следующему разделу, где мы напишем
и опробуем настоящий программный код.
"""