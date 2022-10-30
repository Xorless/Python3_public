"""
 Дополнительные возможности модулей


 Сокрытие данных в модулях

 Как мы уже видели, модули в языке Python экспортируют все имена,
которым были присвоены значения на верхнем уровне файлов. В языке нет
никаких объявлений, которые позволили бы сделать одни имена видимыми,
а другие – невидимыми за пределами модуля. Фактически нет никакого
способа предотвратить возможность изменения имен в модуле извне,
если у кого-то появится такое желание.

 Сокрытие данных модуля в языке Python регулируется соглашениями,
а не синтаксическими конструкциями. Если задаться целью повредить
модуль, изменяя имена в нем, вам ничто не сможет помешать, но,
к счастью, я еще не встречал программистов, кто стремился бы
это сделать. Некоторые пуристы возражают против такого либерального
отношения к сокрытию данных, утверждая в связи с этим, что в языке
Python отсутствует возможность инкапсуляции. Однако инкапсуляция в языке
Python имеется, просто она, скорее, относится к организации пакетов,
чем к возможности накладывать ограничения.


 Минимизация повреждений, причиняемых инструкцией from *: _X и __all__

 Как особый случай, существует возможность начинать имена переменных
с одного символа подчеркивания (например, _X), чтобы предотвратить их
перезаписывание, когда клиент выполняет импортирование модуля
инструкцией from *. Этот прием на самом деле предназначен только
для минимизации загрязнения пространства имен – так как инструкция
from * копирует все имена, импортирующий модуль может получить больше,
чем предполагал (включая имена, которые перезапишут имена импортирующего
модуля). Символы подчеркивания не являются объявлением «частных» данных:
вы по-прежнему можете видеть эти имена и изменять их с помощью других
форм импортирования, таких как инструкция import.

 Альтернативный способ достижения эффекта сокрытия данных, напоминающий
соглашение об именовании _X, заключается в присвоении на верхнем уровне
модуля переменной __all__ списка строк с именами переменных. Например:

__all__ = [“Error”, “encode”, “decode”]
# Экспортируются только эти имена

 При использовании этого приема инструкция from * будет копировать
только имена, перечисленные в списке __all__. В действительности
это соглашение, обратное соглашению _X: переменная __all__
идентифицирует имена, доступные для копирования, тогда как соглашение _X
идентифицирует имена, недоступные для копирования. Интерпретатор Python
сначала отыскивает список __all__ в модуле, и если он отсутствует,
инструкция from * копирует все имена, которые не начинаются
с единственного символа подчеркивания.

 Подобно соглашению _X, список __all__ имеет смысл только для инструкции
from * и не является объявлением частных данных. Программисты могут
использовать при реализации модулей любой из этих приемов,
которые хорошо работают с инструкцией from *. (Смотрите также обсуждение
списков __all__ в файлах пакетов __init__.py в главе 23 – там эти списки
объявляют подмодули, которые могут быть загружены инструкцией from *.)


 Включение будущих возможностей языка

 В языке периодически появляются изменения, которые могут повлиять
на работоспособность существующего программного кода. Сначала они
появляются в виде расширений, которые по умолчанию отключены. Чтобы
включить такие расширения, используется инструкция импорта специального
вида:

from __future__ import имя_функциональной_особенности

 Эта инструкция вообще должна появляться в самом начале файла модуля
(возможно, сразу же вслед за строкой документирования), потому что
она включает специальный режим компиляции программного кода для каждого
отдельно взятого модуля. Возможно также выполнить эту инструкцию
в интерактивной оболочке, что позволит поэкспериментировать с грядущими
изменениями в языке – включенная особенность будет после этого доступна
в течение всего интерактивного сеанса.

 Например, в предыдущих изданиях этой книги мы использовали эту форму
инструкции для демонстрации функций-генераторов, в которых используется
ключевое слово, еще недоступное по умолчанию в то время (в качестве
имя_функциональной_особенности указывалось имя generators). Мы уже
использовали эту инструкцию для включения операции истинного деления
чисел в главе 5, функции print в главе 11 и импорта в пакетах
по абсолютному пути в главе 23. Все эти изменения могут отрицательно
сказаться на работоспособности существующего программного кода
для Python 2.6, и поэтому они так постепенно вводятся в язык – сначала
в виде дополнительных возможностей, включаемых с помощью этой
специальной формы инструкции импорта.


 Смешанные режимы использования: __name__ и __main__

 Ниже демонстрируется специальный прием, позволяющий импортировать
файлы как модули и запускать их как самостоятельные программы. Каждый
модуль обладает встроенным атрибутом __name__, который устанавливается
интерпретатором следующим образом:

  Если файл запускается как главный файл программы, атрибуту __name__
 на запуске присваивается значение “__main__”.

  Если файл импортируется, атрибуту __name__ присваивается имя модуля,
 под которым он будет известен клиенту.

 Благодаря этому модуль может проверить собственный атрибут __name__
и определить, был ли он запущен как самостоятельная программа
или импортирован другим модулем. Например, предположим, что мы создаем
файл модуля с именем runme.py, который экспортирует единственную функцию
с именем tester:

def tester():
    print(“It’s Christmas in Heaven...”)
if __name__ == ‘__main__’:          # Только когда запускается,
tester()                            # а не импортируется

 Этот модуль определяет функцию для клиентов и может импортироваться как
обычный модуль:

% python
\>>> import runme
\>>> runme.tester()
It’s Christmas in Heaven...

 Но в самом конце модуля имеется программный код, который вызывает
функцию, когда этот файл запускается как самостоятельная программа:

% python runme.py
It’s Christmas in Heaven...

 Таким образом, переменная __name__ может играть роль флага,
определяющего режим использования, позволяя программному коду выполнять
разные действия, когда он используется как импортируемая библиотека
или как самостоятельный сценарий. Вы будете встречать этот прием
практически во всех действующих программах на языке Python, с которыми
вам предстоит столкнуться.

 Пожалуй, чаще всего проверка атрибута __name__ выполняется
в программном коде для самопроверки модуля. Проще говоря, вы можете
добавить в конец модуля программный код, который будет выполнять
проверку экспортируемых элементов внутри самого модуля, заключив этот
код в условную инструкцию, проверяющую атрибут __name__. При таком
подходе вы можете использовать файл в других модулях, импортируя его,
и тестировать логику работы, запуская его из командной строки
или каким-либо другим способом. На практике программный код самопроверки
в конце файла, заключенный в условную инструкцию, проверяющую атрибут
__name__, является, пожалуй, самым распространенным и удобным способом
модульного тестирования в языке Python. (В главе 35 обсуждаются другие
часто используемые способы тестирования программного кода на языке
Python – как будет показано, в стандартной библиотеке существуют модули
unittest и doctest, которые реализуют более совершенные средства
тестирования.)

 Прием, основанный на проверке атрибута __name__, также часто
используется при создании файлов, которые могут использоваться
и как утилиты командной строки, и как библиотеки инструментов. Например,
предположим, что вы пишете на языке Python сценарий поиска файлов. Код
принесет больше пользы, если реализовать его в виде функций и добавить
проверку атрибута __name__ для организации вызова этих функций, когда
файл запускается как самостоятельная программа. При таком подходе
сценарий может повторно использоваться в составе других программ.


 Тестирование модулей с помощью __name__

 Мы уже видели в этой книге один хороший пример, когда проверка атрибута
__name__ могла бы быть полезной. В разделе, рассказывающем
об аргументах, в главе 18, мы написали сценарий, который находит
минимальное значение среди множества предложенных аргументов:

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

print(minmax(lessthan, 4, 2, 1, 5, 6, 3))  # Код самопроверки
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))

 В самом конце этого сценария присутствует программный код самопроверки,
благодаря которому мы можем проверить правильность работы модуля
без необходимости вводить его в интерактивной оболочке всякий раз,
когда нам потребуется проверить модуль. Однако при такой реализации
имеется одна проблема – результаты самопроверки будут выводиться
на экран всякий раз, когда этот файл будет импортироваться
для использования другим файлом, но тогда это становится невежливым
по отношению к пользователю! Чтобы исправить положение, можно обернуть
проверочные вызовы функции в условную инструкцию, проверяющую атрибут
__name__ так, чтобы они выполнялись, только когда файл запускается
как самостоятельная программа, а не во время импорта:

print ‘I am:’, __name__
def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

if __name__ == ‘__main__’:
    print(minmax(lessthan, 4, 2, 1, 5, 6, 3))   # Код самопроверки
    print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))

 Тут в самом начале добавлена инструкция вывода значения атрибута
__name__, чтобы проверить его визуально. Интерпретатор Python создает
эту переменную и присваивает ей значение во время загрузки файла. Когда
файл запускается как самостоятельная программа, этому имени
присваивается значение ‘__main__’, поэтому в данном случае происходит
автоматическое выполнение кода самопроверки:

% python min.py
I am: __main__
1
6

 Однако, когда файл импортируется, значение атрибута __name__ уже
не равно ‘__main__’, поэтому необходимо явно вызвать функцию, чтобы
запустить ее:

\>>> import min
I am: min
\>>> min.minmax(min.lessthan, ‚s‘, ‚p‘, ‚a‘, ‚m‘)
‚a‘

 Неважно, будет ли использоваться этот прием для нужд тестирования,
главный результат – что наш программный код может использоваться
и как библиотека инструментов, и как самостоятельная программа.


 Обработка аргументов командной строки с помощью __name__

 Теперь представим более практичный пример, демонстрирующий еще один
распространенный способ использования переменной __name__. Следующий
модуль, formats.py, определяет вспомогательные функции форматирования
строк. Кроме того, он проверяет имя модуля, чтобы узнать, был ли он
запущен как самостоятельная программа. Если это так, он проверяет
и использует аргументы командной строки для запуска встроенного
или конкретного теста. Список sys.argv в языке Python содержит аргументы
командной строки – список строк со словами, введенными в командной
строке, где первый элемент списка всегда содержит имя файла сценария:
"""

"""
Различные специализированные функции форматирования строк.
Модуль можно протестировать с помощью встроенных тестов или посредством 
передачи аргументов командной строки.
"""


def commas(N):
    """
    Форматирует целое положительное число N, добавляя запятые,
    разделяющие группы разрядов: xxx,yyy,zzz
    """
    digits = str(N)
    assert(digits.isdigit())
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
        
    return result


def money(N, width=0):
    """
    Форматирует число N, добавляя запятые, оставляя 2 десятичных знака
    в дробной части, добавляя в начало символ $ и знак числа, и,
    при необходимости, – отступ: $ -xxx,yyy.zz
    """
    sign = '-' if N < 0 else ''
    N = abs(N)
    whole = commas(int(N))
    fract = ('%.2f' % N)[-2:]
    format = '%s%s.%s' % (sign, whole, fract)
    return '$%*s' % (width, format)


if __name__ == '__main__':
    def selftest():
        tests = 0, 1                    # ошибка при значениях: -1, 1.23
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))
            print('')

        tests = 0, 1, -1, 1.23, 1., 1.2, 3.14159
        tests += 12.34, 12.344, 12.345, 12.346
        tests += 2 ** 32, (2 ** 32 + .2345)
        tests += 1.2345, 1.2, 0.2345
        tests += -1.2345, -1.2, -0.2345
        tests += -(2 ** 32), -(2**32 + .2345)
        tests += (2 ** 100), -(2 ** 100)
        for test in tests:
            print('%s [%s]' % (money(test, 17), test))

    import sys
    if len(sys.argv) == 1:
        selftest()
    else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))

"""
 Этот модуль работает одинаково в версиях Python 2.6 и 3.0.
Когда он запускается как самостоятельная программа, он тестирует себя,
как было описано выше, но при этом для управления тестированием
он использует аргументы командной строки. Чтобы увидеть,
что будет выведено в результате тестирования, запустите у себя этот файл
как самостоятельную программу. Чтобы протестировать определенные строки,
передайте их в командной строке вместе со значением минимальной ширины
поля вывода:
C:\misc> python formats.py 999999999 0
$999,999,999.00
C:\misc> python formats.py -999999999 0
$-999,999,999.00
C:\misc> python formats.py 123456789012345 0
$123,456,789,012,345.00
C:\misc> python formats.py -123456789012345 25
$ -123,456,789,012,345.00
C:\misc> python formats.py 123.456 0
$123.46
C:\misc> python formats.py -123.454 0
$-123.45
C:\misc> python formats.py
...чтобы увидеть результаты встроенных тестов –
запустите сценарий сами...

 Этот модуль может запускаться как самостоятельная программа
и импортироваться другими модулями, поэтому мы можем импортировать
его функции как обычные библиотечные компоненты:

>>> from formats import money, commas
>>> money(123.456)
‘$123.46’
>>> money(-9999999.99, 15)
‘$ -9,999,999.99’
>>> X = 99999999999999999999
>>> ‘%s (%s)’ % (commas(X), X)
‘99,999,999,999,999,999,999 (99999999999999999999)’

 В этом файле также присутствуют строки документирования, с которыми мы
познакомились в главе 15, поэтому мы можем использовать функцию help 
для исследования инструментов, входящих в него:

>>> import formats
>>> help(formats)
Help on module formats:

NAME
    formats
FILE
    c:\misc\formats.py
    
DESCRIPTION
Различные специализированные функции форматирования строк.
Модуль можно протестировать с помощью встроенных тестов или посредством 
передачи аргументов командной строки.

FUNCTIONS
    commas(N)
        Форматирует целое положительное число N, добавляя запятые,
        разделяющие группы разрядов: xxx,yyy,zzz
        
    money(N, width=0)
        Форматирует число N, добавляя запятые, оставляя 2 десятичных 
        знака в дробной части, добавляя в начало символ $ и знак числа,
        и, при необходимости, отступ: $ -xxx,yyy.zz
        
 
"""

import ExtraAbilities24_1

help(ExtraAbilities24_1)

"""
 Вы можете использовать аргументы командной строки похожими способами,
чтобы обеспечить передачу в свои сценарии входных данных, которые также
могут быть встроены в программный код как функции или классы и доступны 
импортирующим модулям. Если вам потребуются более широкие возможности 
обработки аргументов командной строки, обратите внимание на модули 
getopt и optparse – они входят в состав стандартной библиотеки Python 
и описываются в руководствах. В некоторых случаях можно также 
использовать встроенную функцию input, представленную в главе 3,
которой мы пользовались в главе 10, чтобы реализовать возможность 
запрашивать данные у пользователя, вместо того чтобы заставлять его 
вводить эти данные в командной строке.

 Загляните также в главу 7, где обсуждается новый синтаксис 
спецификаторов формата {,d}, который будет доступен в версии Python 3.1 
и выше, – он позволяет вставлять запятые между группами разрядов,
подобно функциям в этом модуле. Кроме того, модуль, представленный 
здесь, позволяет также форматировать денежные суммы и может служить 
альтернативным способом добавления запятых для тех, кто пользуется 
версиями Python ниже 3.1.


 Изменение пути поиска модулей
 
 В главе 21 мы узнали, что путь поиска модулей – это список каталогов, 
и что этот список можно дополнить с помощью переменной окружения 
PYTHONPATH и файлов .pth. Но я пока еще не показывал, как сами программы
на языке Python могут изменять путь поиска, изменяя встроенный список
с именем sys.path (атрибут path встроенного модуля sys). Список sys.path 
инициализируется во время запуска программы, однако и после этого 
допускается удалять, добавлять и изменять компоненты списка по своему
усмотрению:

>>> import sys
>>> sys.path
[‘’, ‘C:\\users’, ‘C:\\Windows\\system32\\python30.zip’, 
 ...далее опущено...]
>>> sys.path.append(‘C:\\sourcedir’)   # Дополнение пути поиска модулей
>>> import string                      # Новый каталог будет участвовать
                                       # в поиске

 Как только будут внесены изменения, они будут воздействовать на все 
последующие инструкции импорта, выполняемые в программе, так как все 
инструкции во всех файлах программы используют один и тот же общий 
список sys.path. Этот список может изменяться произвольным образом:

>>> sys.path = [r’d:\temp’]               # Изменяет путь поиска модулей
>>> sys.path.append(‘c:\\lp4e\\examples’)    # Только для этой программы
>>> sys.path
[‘d:\\temp’, ‘c:\\lp4e\\examples’]
>>> import string
Traceback (most recent call last):
  File “<stdin>”, line 1, in ?
ImportError: No module named string

 Таким образом, этот прием может использоваться для динамической
настройки пути поиска внутри программ на языке Python. Однако будьте 
внимательны: если убрать из пути критически важный каталог, можно
потерять доступ к критически важным утилитам. Так в предыдущем примере
был потерян доступ к модулю string, потому что из пути был удален 
исходный каталог библиотеки.

 Кроме того, не забывайте, что такие изменения списка sys.path действуют
только в рамках интерактивного сеанса или внутри программы (технически –
в рамках процесса), где были выполнены эти изменения, – они 
не сохраняются после завершения работы интерпретатора. Настройки 
в переменной окружения PYTHONPATH и в файлах .pth располагаются в самой 
операционной системе, а не в работающей программе, и потому они имеют 
более глобальный характер: они воспринимаются всеми программами, которые
запускаются на вашей машине, и продолжают существовать по завершении 
программы.
"""

import sys

print(sys.path)

"""
 Расширение as для инструкций import и from
 
 Обе инструкции, import и from, были расширены так, чтобы позволить 
давать модулям в вашем сценарии другие имена. Следующая инструкция 
import:

import longmodulename as name

 эквивалентна инструкциям:
 
import longmodulename
name = longmodulename
del longmodulename       # Не сохранять оригинальное имя

 После выполнения такой инструкции import для ссылки на модуль можно 
(и фактически необходимо) использовать имя, указанное после ключевого
слова as. Точно такое же расширение имеется и у инструкции from, 
где оно позволяет изменять имена, импортируемые из файла:

from module import longname as name

 Это расширение обычно используется с целью создать короткие синонимы 
для длинных имен и избежать конфликтов с именами, уже используемыми
в сценарии, которые в противном случае были бы просто перезаписаны 
инструкцией импортирования:

import reallylongmodulename as name    # Использовать короткий псевдоним
name.func()
from module1 import utility as util1   # Допускается только одно имя 
from module2 import utility as util2   # “utility”
util1(); util2()

 Кроме того, это расширение может пригодиться с целью создания коротких
и простых имен для длинных путей, состоящих из цепочки каталогов, 
при импортировании пакетов, которое описывалось в главе 23:

import dir1.dir2.mod as mod  # Полный путь достаточно указать 
mod.func()                   # всего один раз


 Модули – это объекты: метапрограммы
 
 Поскольку модули экспортируют большую часть своих свойств в виде 
встроенных атрибутов, это позволяет легко создавать программы, которые
управляют другими программами. Такие менеджеры программ мы обычно 
называем метапрограммами, потому что они работают поверх других 
программ. Этот прием также называется интроспекцией, потому что 
программы могут просматривать внутреннее устройство объектов 
и действовать исходя из этого. Интроспекция – это дополнительная
особенность, которая может быть полезна при создании инструментальных 
средств программирования.

 Например, чтобы получить значение атрибута с именем name в модуле 
с именем M, мы можем использовать полное имя атрибута или обратиться 
к нему с помощью словаря атрибутов модуля (экспортируется в виде 
встроенного атрибута __dict__, с которым мы уже встречались в главе 22). 
Кроме того, интерпретатор экспортирует список всех загруженных модулей
в виде словаря sys.modules (то есть в виде атрибута modules модуля sys)
и предоставляет встроенную функцию getattr, которая позволяет получать 
доступ к атрибутам по строкам с их именами (напоминает выражение 
object.attr, только attr – это строка времени выполнения). Благодаря 
этому все следующие выражения представляют один и тот же атрибут 
и объект:

M.name    # Полное имя объекта
M.__dict__[‘name’]   # Доступ с использованием словаря пространства имен
sys.modules[‘M’].name   # Доступ через таблицу загруженных модулей
getattr(M, ‘name’)   # Доступ с помощью встроенной функции

 Обеспечивая доступ к внутреннему устройству модулей, интерпретатор
помогает создавать программы, управляющие другими программами. 

 Как мы видели в главе 17, функция может получить доступ к вмещающему
модулю с помощью таблицы sys.modules, что позволяет имитировать действие
инструкции global. Например, эффект действия инструкций global X; X=0 
внутри функции можно реализовать (хотя для этого придется ввести
с клавиатуры значительно больше символов!) так: import sys; 
glob=sys.modules[__name__]; glob.X=0. Не забывайте, что каждый модуль
имеет атрибут __name__; внутри функции, принадлежащей модулю, 
он выглядит как глобальное имя. Этот прием обеспечивает еще один способ 
изменения одноименных локальных и глобальных переменных внутри функции.

 Например, ниже приводится модуль с именем mydir.py, в котором 
использованы эти идеи для реализации измененной версии встроенной 
функции dir. Этот модуль определяет и экспортирует функцию с именем
listing, которая принимает объект модуля в качестве аргумента и выводит 
отформатированный листинг пространства имен модуля:
"""

"""
mydir.py: выводит содержимое пространства имен других модулей
"""

seplen = 60
sepchr = '-'


def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__, 'file:', module.__file__)
        print(sepline)

    count = 0

    for attr in module.__dict__:         # Сканировать пространство имен
        print('%02d) %s' % (count, attr), end=' ')
        if attr.startswith('__'):
            print('<built-in name>')         # Пропустить __file__ и др.
        else:
            print(getattr(module, attr))  # То же, что и .__dict__[attr]
            
        count = count+1

    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)
        print(sepline)

    if __name__ == "__main__":
        listing(ExtraAbilities24_1)  # Код самопроверки: вывести своё
        #                              пространство имен


r"""
 Обратите внимание на строку документирования в начале модуля – как 
и в предыдущем примере formats.py, мы можем получить доступ к ней 
с помощью универсальных инструментов. Строки документирования создаются 
с целью предоставить функциональное описание, которое можно получить 
через атрибут __doc__ или с помощью функции help (подробности приводятся 
в главе 15):

>>> import mydir
>>> help(mydir)
Help on module mydir:

NAME
    mydir - mydir.py: выводит содержимое пространства имен других
    модулей
FILE
    c:\users\veramark\mark\mydir.py
FUNCTIONS
    listing(module, verbose=True)
DATA
    sepchr = ‘-’
    seplen = 60
    
 В модуле, в самом конце, реализована логика самопроверки, которая 
заставляет модуль импортировать самого себя и вывести содержимое своего
пространства имен. Ниже показан результат работы этого модуля 
под управлением Python 3.0 (чтобы использовать его в Python 2.6,
включите возможность использования функции print как в версии 3.0, 
импортировав модуль __future__, как описывается в главе 11, потому что 
ключевое слово end допустимо только в версии 3.0):

C:\Users\veramark\Mark> c:\Python30\python mydir.py
------------------------------------------------------------
name: mydir file: C:\Users\veramark\Mark\mydir.py
------------------------------------------------------------
00) seplen 60
01) __builtins__ <built-in name>
02) __file__ <built-in name>
03) __package__ <built-in name>
04) listing <function listing at 0x026D3B70>
05) __name__ <built-in name>
06) sepchr -
07) __doc__ <built-in name>
------------------------------------------------------------
mydir has 8 names
------------------------------------------------------------

 Чтобы использовать его как инструмент интроспекции других модулей, 
просто передайте функции listing объект требуемого модуля. 
Ниже приводится список атрибутов модуля tkinter из стандартной 
библиотеки (он же Tkinter в Python 2.6):

>>> import mydir
>>> import tkinter
>>> mydir.listing(tkinter)
------------------------------------------------------------
name: tkinter file: c:\PYTHON30\lib\tkinter\__init__.py
------------------------------------------------------------
00) getdouble <class ‘float’>
01) MULTIPLE multiple
02) mainloop <function mainloop at 0x02913B70>
03) Canvas <class ‘tkinter.Canvas’>
04) AtSelLast <function AtSelLast at 0x028FA7C8>
...many more name omitted...
151) StringVar <class ‘tkinter.StringVar’>
152) ARC arc
153) At <function At at 0x028FA738>
154) NSEW nsew
155) SCROLL scroll
------------------------------------------------------------
tkinter has 156 names
------------------------------------------------------------

 С функцией getattr и родственными ей мы встретимся еще раз позднее. 
Самое важное здесь, что mydir – это программа, которая позволяет 
исследовать другие программы. Так как интерпретатор не скрывает
внутреннее устройство модулей, вы можете реализовать обработку любых 
объектов единообразно.

 Инструменты, такие как mydir.listing, могут быть предварительно 
загружены в пространство имен интерактивной оболочки импортированием 
их в файле, указанном в переменной окружения PYTHONSTARTUP. Так как
программный код этого файла выполняется в интерактивном пространстве
имен (модуль __main__), такой способ импортирования часто используемых 
инструментов позволит вам сэкономить время на вводе инструкций вручную.
"""
