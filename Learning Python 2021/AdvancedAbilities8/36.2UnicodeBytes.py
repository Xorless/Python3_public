r"""
 Кодирование строк Юникода

 Операции кодирования и декодирования приобретут для вас большую
значимость, когда вы начнете применять их к строкам Юникода, содержащим
символы, не являющиеся символами ASCII. Чтобы добавить в строковый
литерал символы Юникода, которые порой даже невозможно ввести
с клавиатуры, в языке Python поддерживается возможность указывать
экранированные значения байтов “\xNN” в шестнадцатеричном виде
и экранированные значения символов Юникода “\uNNNN” и “\UNNNNNNNN”.
Экранированные значения символов Юникода первого вида состоят
из четырех шестнадцатеричных цифр и представляют 2-байтовые (16-битные)
коды символов, а значения второго вида состоят из восьми
шестнадцатеричных цифр и представляют 4-байтовые (32-битные)
коды символов.


 Кодирование строк символов ASCII

 Рассмотрим несколько примеров, демонстрирующих основы кодирования
строк. Как мы уже знаем, строки символов ASCII являются простейшей
разновидностью строк символов Юникода, которые хранятся
как последовательности байтов, представляющих символы:
"""

print(ord('X'))  # В кодировке по умолчанию ‘X’ имеет значение 88

print(chr(88))   # Код 88 соответствует символу ‘X’

S = 'XYZ'        # Строка Юникода из символов ASCII
print(S)

print(len(S))    # 3 символа

print([ord(c) for c in S])  # 3 байта с целочисленными значениями

"""
 Обычный текст, состоящий только из 7-битных символов ASCII, 
как в данном примере, представляется как последовательность байтов 
в любых схемах кодирования Юникода, о чем уже говорилось выше:
"""

print(S.encode('ascii'))    # Значения 0..127 в 1 байте (7 битов) каждое

print(S.encode('latin-1'))  # Значения 0..255 в 1 байте (8 битов) каждое

print(S.encode('utf-8'))    # Значения 0..127 в 1 байте,
# 128..2047 – в 2, другие – в 3 или 4

"""
 Фактически объекты типа bytes, возвращаемые данной операцией 
кодирования строки символов ASCII, в действительности являются 
последовательностью коротких целых чисел, которые просто выводятся
как символы ASCII, когда это возможно:
"""

print(S.encode('latin-1')[0])

print(list(S.encode('latin-1')))

"""
 Кодирование строк символов не-ASCII
 
 Для представления символов, не входящих в диапазон ASCII, можно 
использовать шестнадцатеричные экранированные последовательности 
значений байтов и символов Юникода – шестнадцатеричные экранированные 
последовательности значений байтов могут представлять только значения 
отдельных байтов, а экранированные последовательности значений символов 
Юникода могут определять символы, состоящие из двух или четырех байтов. 
Шестнадцатеричные значения 0xCD и 0xE8, например, представляют коды двух 
специальных символов с диакритическими знаками, не входящими 
в диапазон 7-битных символов ASCII, но мы можем вставлять их 
в объекты str, потому что тип str в Python 3.0 поддерживает символы
Юникода:
"""

print(chr(0xc4))  # 0xC4, 0xE8: символы, не входящие в диапазон ASCII

print(chr(0xe8))

S = '\xc4\xe8'  # Экранированные последовательности шестнадцатеричных
print(S)        # значений байтов

S = '\u00c4\u00e8'  # 16-битные экранированные последовательности
print(S)            # шестнадцатеричных значений символов Юникода

print(len(S))   # 2 символа (это не число байтов!)

"""
 Кодирование и декодирование строк символов не-ASCII
 
 Если теперь попробовать закодировать строки символов не-ASCII 
в последовательности простых байтов, используя кодировку ASCII, 
мы получим сообщение об ошибке. Однако, если указать кодировку Latin-1, 
ошибки не будет и каждому символу в строке будет поставлен
в соответствие отдельный байт. При использовании кодировки UTF-8 
для каждого символа будет выделено по 2 байта. Если записать 
такую строку в файл, в нем фактически будет сохранена последовательность
байтов с учетом использовавшейся кодировки, как показано ниже:

>>> S.encode(‘ascii’)
UnicodeEncodeError: ‘ascii’ codec can’t encode characters 
in position 0-1:
ordinal not in range(128)
"""

print(S.encode('latin-1'))  # По одному байту на символ

print(S.encode('utf-8'))    # Два байта на символ

print(len(S.encode('latin-1')))  # 2 байта – в latin-1, 4 – в utf-8

print(len(S.encode('utf-8')))

"""
 Обратите внимание, что можно пойти обратным путем – прочитать 
последовательность байтов из файла и декодировать их в строку символов 
Юникода. Однако, как будет показано ниже, если в вызове функции open 
указать название кодировки, то операции чтения автоматически будут 
выполнять декодирование прочитанных данных (и помогут избежать ошибок, 
которые могут явиться результатом чтения неполных последовательностей 
символов, когда чтение выполняется блоками байтов):
"""

B = b'\xc4\xe8'
print(B)

print(len(B))               # 2 байта, 2 символа

print(B.decode('latin-1'))  # Декодировать в текст latin-1

B = b'\xc3\x84\xc3\xa8'
print(len(B))               # 4 байта

print(B.decode('utf-8'))

print(len(B.decode('utf-8')))  # 2 символа Юникода

r"""
 Другие способы кодирования строк Юникода
 
 Некоторые кодировки используют еще более длинные последовательности
байтов для представления символов. В случае необходимости вы можете 
указывать 16- и 32-битные значения Юникода для символов в строках –
в первом случае используется форма “\u...” с четырьмя шестнадцатеричными 
цифрами, а во втором – форма “\U...” с восемью шестнадцатеричными
цифрами:
"""

S = 'A\u00c4B\U000000e8C'
print(S)          # A, B, C и 2 не-ASCII символа

print(len(S))     # 5 символов

print(S.encode('latin-1'))

print(len(S.encode('latin-1')))  # 5 байтов в кодировке latin-1

print(S.encode('utf-8'))

print(len(S.encode('utf-8')))    # 7 байтов в кодировке utf-8

"""
 Интересно, что некоторые кодировки могут иметь существенные различия
в кодах символов. Например, кодировка cp500 EBCDIC даже символы ASCII
кодирует совсем не так, как кодировки, с которыми мы уже познакомились
выше (поскольку интерпретатор автоматически выполняет кодирование 
и декодирование, нам остается только позаботиться о том, чтобы указать 
нужное имя кодировки):
"""

print(S.encode('cp500'))    # Две другие западноевропейские кодировки

print(S.encode('cp850'))    # 5 байтов в каждой

S = 'spam'                  # В большинстве кодировок символы ASCII
print(S.encode('latin-1'))  # кодируются одинаково

print(S.encode('utf-8'))

print(S.encode('cp500'))    # Но не в кодировке cp500: IBM EBCDIC!

print(S.encode('cp850'))

"""
 С технической точки зрения, вы можете составлять строки Юникода 
по частям, используя функцию chr вместо экранированных шестнадцатеричных
значений, но это может оказаться весьма утомительным в случае длинных
строк:

>>> S = ‘A’ + chr(0xC4) + ‘B’ + chr(0xE8) + ‘C’
>>> S
‘AÄBèC’

 Здесь следует сделать два замечания. Во-первых, в Python 3.0 
допускается в строках типа str кодировать специальные символы 
с использованием шестнадцатеричных экранированных последовательностей 
значений байтов и символов Юникода, но в строках типа bytes могут
применяться только шестнадцатеричные экранированные последовательности 
значений байтов – экранированные последовательности значений символов
Юникода в строках типа bytes будут интерпретироваться буквально, 
а не как экранированные последовательности. Фактически строки bytes 
должны декодироваться в строки str, чтобы корректно вывести символы,
не являющиеся символами ASCII:
"""

S = 'A\xC4B\xE8C'  # str распознает экранированные
print(S)           # значения символов Юникода

S = 'A\u00C4B\U000000E8C'
print(S)

B = b'A\xC4B\xE8C'  # bytes распознает экранированные
print(B)            # последовательности байтов, но не символов Юникода

B = b'A\u00C4B\U000000E8C'  # Экранированные последовательности
print(B)                    # интерпретируются буквально!
B = b'A\xC4B\xE8C'  # В строках bytes используйте экранированные
#                     последовательности байтов
print(repr(B))      # Выведет не-ASCII символы в шестнадцатеричном виде
print(B)

print(B.decode('latin-1'))  # Декодировать в кодировку latin-1,
#                             чтобы вывести как текст

"""
 Во-вторых, при определении литералов bytes допускается использовать 
символы ASCII, а для байтов со значениями выше 127 – экранированные 
последовательности шестнадцатеричных значений. С другой стороны, 
в литералах str допускается использовать любые символы, имеющиеся 
в исходной кодировке (в качестве которой, как будет рассказываться ниже, 
по умолчанию используется UTF-8, если в исходном файле явно не была
объявлена другая кодировка):
"""

S = 'AÄBèC'  # Символы из UTF-8, если кодировка не была объявлена
print(S)

# B = b'AÄBèC'

B = b'A\xC4B\xE8C'  # Допускаются символы ASCII или
print(B)            # экранированные последовательности

print(B.decode('latin-1'))

print(S.encode())  # Исходная строка закодирована в кодировке UTF-8
# Если кодировка не указана, используется системная кодировка

print(S.encode('utf-8'))

# B.decode()  # Простые байты не соответствуют кодировке utf-8

"""
 Преобразования между кодировками
 
 До сих пор мы использовали операции кодирования и декодирования строк,
только чтобы исследовать их структуру. В более общем случае мы можем 
использовать эти операции для преобразования строк в другие кодировки, 
отличающиеся от исходной кодировки по умолчанию, но при этом мы должны
явно указывать название кодировки в операциях кодирования 
и декодирования:
"""

T = S.encode('cp500')  # Преобразовать в кодировку EBCDIC
print(T)

U = T.decode('cp500')  # Преобразовать обратно в Юникод
print(U)
print(U.encode())  # По умолчанию снова используется кодировка utf-8

"""
 Имейте в виду, что специальные экранированные последовательности 
необходимы только для представления символов, не входящих в набор ASCII,
в литералах строк. На практике такой текст вам часто придется загружать
из файлов. Как будет показано ниже в этой главе, объект файла 
в Python 3.0 (созданный с помощью встроенной функции open) автоматически
декодирует текстовые строки в процессе их чтения и кодирует в процессе
записи – благодаря этому в своих сценариях вы сможете работать 
со строками обычным способом, не нуждаясь в использовании специальных 
форм представления символов.


 Объявление кодировки по умолчанию в файлах
 
 Экранированные последовательности значений Юникода отлично подходят
для определения символов Юникода в литералах строк, но их использование
может стать достаточно утомительным при частом употреблении
для внедрения символов не-ASCII в строки. Для представления строк 
в исходных текстах сценариев Python по умолчанию использует кодировку
UTF-8, однако имеется возможность указать любую другую кодировку, 
включив комментарий с названием требуемой кодировки. В сценариях 
для Python 2.6 и 3.0 данный комментарий должен находиться в первой 
или во второй строке и должен иметь следующий вид:

# -*- coding: latin-1 -*-

 Если в сценарии присутствует подобный комментарий, интерпретатор будет
распознавать строки, представленные в указанной кодировке. Это означает,
что вы можете редактировать файл сценария в текстовом редакторе, 
способном принимать и корректно отображать национальные символы,
не входящие в набор ASCII, а интерпретатор будет корректно 
декодировать их в строковые литералы. Например, обратите внимание, 
как комментарий в начале следующего файла text.py обеспечивает
возможность употребления символов Latin-1 в литералах строк:
"""

# -*- coding: latin-1 -*-
# Все следующие литералы строк содержат символы latin-1.
# Если изменить название кодировки в комментарии выше на ascii
# или utf-8, это приведет к появлению ошибок, так как значения 0xc4
# и 0xe8 в строке myStr1 не являются допустимыми ни в одной из них.

myStr1 = 'aÄBèC'

myStr2 = 'A\u00c4B\U000000e8C'

myStr3 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'

import sys


print('Default encoding:', sys.getdefaultencoding())

for aStr in myStr1, myStr2, myStr3:
    print('{0}, strlen={1}, '.format(aStr, len(aStr)), end='')

    bytes1 = aStr.encode()  # В utf-8 по умолчанию:
    # 2 байта на каждый символ не-ASCII
    bytes2 = aStr.encode('latin-1')  # По одному байту на символ
    # bytes3 = aStr.encode(‘ascii’) # Кодирование в ASCII
    # приведет к ошибке: за пределами диапазона 0..127

    print('byteslen1={0}, byteslen2={1}'.format(len(bytes1),
                                                len(bytes2)))

"""
 Если запустить этот сценарий, он выведет следующее:
 
C:\misc> c:\python30\python text.py
Default encoding: utf-8
aÄBèC, strlen=5, byteslen1=7, byteslen2=5
AÄBèC, strlen=5, byteslen1=7, byteslen2=5
AÄBèC, strlen=5, byteslen1=7, byteslen2=5

 Большинство программистов вероятнее всего будут использовать 
стандартную кодировку UTF-8, поэтому я оставлю описание подробностей, 
касающихся этой и других особенностей поддержки Юникода, таких как 
свойства и названия символов, за стандартным набором руководств
по языку Python.


 Использование объектов bytes в Python 3.0
 
 В главе 7 мы изучили большое разнообразие операций, поддерживаемых 
типом str в Python 3.0, – в основе своей строковый тип действует 
одинаково в версиях 2.6 и 3.0, поэтому мы не будем вновь возвращаться 
к этой теме. Вместо этого мы поближе познакомимся с операциями,
которые поддерживаются новым типом bytes Python 3.0.

 Как уже упоминалось ранее, объекты типа bytes являются 
последовательностями коротких целых чисел, каждое из которых имеет 
значение в диапазоне от 0 до 255, которые могут выводиться как символы 
ASCII. Этот тип поддерживает обычные операции над последовательностями
и большинство строковых методов, доступных для объектов типа str 
(и для объектов типа str в версии 2.X). Однако тип bytes не поддерживает
метод format и оператор % форматирования, и вы не сможете смешивать 
и сопоставлять объекты типов bytes и str, не выполняя 
явное преобразование, – для представления тестовых данных вы 
в подавляющем большинстве случаев будете использовать объекты типа str
и текстовые файлы, а для представления двоичных данных – объекты типа
bytes и двоичные файлы.


 Методы
 
 Если вы действительно желаете увидеть, какие атрибуты имеют объекты 
типа str, которые отсутствуют в объектах типа bytes, вы всегда можете
воспользоваться встроенной функцией dir. Результаты вызова этой функции
сообщат также дополнительную информацию об операторах, поддерживаемых 
этими типами (например, методы __mod__ и __rmod__ реализуют оператор 
деления по модулю %):
"""

# Атрибуты, уникальные для типа str

print(set(dir(str)) - set(dir(bytes)))

# Атрибуты, уникальные для типа bytes
print(set(dir(bytes)) - set(dir(str)))

"""
 Как видите, типы str и bytes обладают практически идентичной 
функциональностью. Атрибуты, отличающие их друг от друга, являются 
методами, которые не могут применяться к объектам другого типа; 
например, метод decode преобразует последовательность простых байтов 
в объект типа str, а метод encode преобразует строку 
в последовательность байтов типа bytes. Оба типа поддерживают множество
одних и тех же методов, только методы объектов bytes принимают аргументы
типа bytes (напомню, что в версии 3.0 объекты строкового типа не могут
смешиваться с объектами типа bytes). Кроме того, объекты типа bytes 
относятся к категории неизменяемых, как и объекты типа str в Python 2.6 
и 3.0 (сообщения об ошибках в следующем примере были урезаны 
для краткости):
"""

B = b'spam'                     # b’...’ – литерал типа bytes
print(B.find(b'pa'))

print(B.replace(b'pa', b'XY'))  # Методы объектов bytes принимают
#                                 аргументы типа bytes
print(B.split(b'pa'))

print(B)

# B[0] = 'x' - TypeError

"""
 Одно важное отличие заключается в том, что операции форматирования
строк в версии 3.0 могут применяться только к объектам типа str
и не поддерживаются объектами типа bytes (подробнее о форматировании
строк рассказывается в главе 7):

>>> b’%s’ % 99
TypeError: unsupported operand type(s) for %: ‘bytes’ and ‘int’
>>> ‘%s’ % 99
‘99’
>>> b’{0}’.format(99)
AttributeError: ‘bytes’ object has no attribute ‘format’
>>> ‘{0}’.format(99)
‘99’


 Операции над последовательностями

 Кроме методов, объекты типов str и bytes в версии 3.0 поддерживают
все обычные операции над последовательностями, известные
(и, возможно, полюбившиеся) вам по строкам и спискам
в версии Python 2.X, – включая индексирование, извлечение срезов,
конкатенацию и так далее. Обратите внимание, что операция индексирования
в следующем примере для объекта типа bytes возвращает целое число,
представляющее значение байта, – объекты bytes в действительности
являются последовательностями 8-битных целых чисел, но для удобства
они выводятся как строки символов ASCII, когда это возможно.
Чтобы узнать, какому символу соответствует значение
того или иного байта, используйте встроенную функцию chr,
как показано ниже:
>>> 
"""

B = b'spam'     # Последовательность коротких целых чисел
print(B)        # Выводится как последовательность символов ASCII

print(B[0])     # Операция индексирования возвращает целое число

print(B[-1])

chr(B[0])       # Выведет символ, соответствующий целому числу

print(list(B))  # Выведет целочисленные значения всех байтов

print(B[1:], B[:-1])

print(len(B))

print(B + b'lmn')

print(B * 4)

"""
 Другие способы создания объектов bytes
 
 До сих пор мы создавали объекты типа bytes с использованием синтаксиса
литералов b’...’ – однако они точно так же могут создаваться вызовом 
конструктора bytes с объектом типа str и названием кодировки, вызовом 
конструктора bytes с итерируемым объектом, возвращающим целые числа, 
или с помощью метода encoding объекта str с явно указанным 
(или подразумеваемым по умолчанию) названием кодировки. Как мы 
уже видели, операция кодирования принимает объект str и возвращает
последовательность байтов со значениями, в зависимости от указанной 
кодировки, – операция декодирования, напротив, принимает 
последовательность простых байтов и декодирует ее в строку – 
последовательность символов, возможно многобайтовых. Обе операции
создают новые строковые объекты:
"""

B = b'abc'
print(B)

B = bytes('abc', 'ascii')
print(B)

print(ord('a'))

B = bytes([97, 98, 99])
print(B)

B = 'spam'.encode()  # Или bytes()
print(B)

S = B.decode()       # Или str()
print(S)

"""
 Смешивание строковых типов в выражениях
 
 Методу replace в примере, приводившемся в разделе «Методы» выше,
мы передавали два объекта типа bytes – он не принимает объекты типа str. 
В Python 2.X объекты типа str автоматически преобразуются в объекты 
типа unicode и обратно, если это возможно (то есть, когда объекты str
содержат только 7-битные символы ASCII), однако в Python 3.0 
в некоторых случаях допускается использовать строковые объекты 
определенного типа, а все необходимые преобразования должны 
выполняться явно:
"""

# Функциям и методам должны передаваться объекты допустимых типов
B = b'spam'
# B.replace('pa', 'XY')  # TypeError:
#                        expected an object with the buffer interface
print(B.replace(b'pa', b'XY'))

B = B'spam'
# B.replace(bytes('pa'), bytes('xy')) # TypeError:
#                                    string argument without an encoding
print(B.replace(bytes('pa', 'ascii'), bytes('xy', 'utf-8')))

# При необходимости преобразования типов должны выполняться явно
# print(b'ab' + 'cd')  # TypeError: can’t concat bytes to str
print(b'ab'.decode() + 'cd')  # bytes в str

print(b'ab' + 'cd'.encode())  # str в bytes

print(b'ab' + bytes('cd', 'ascii'))  # str в bytes

"""
 Использование объектов bytearray в 3.0 (и 2.6)
  
 До сих пор мы рассматривали типы str и bytes, поскольку они 
соответствуют типам unicode и str в Python 2. Однако в Python 3.0 
имеется третий строковый тип – bytearray, представляющий изменяемые 
последовательности целых чисел со значениями в диапазоне от 0 до 255. 
По сути это изменяемая версия типа bytes. Он поддерживает те же самые 
методы строк и операции над последовательностями, что и тип bytes, 
а также множество операций, изменяющих объекты в памяти, которые 
поддерживаются списками. Кроме того, тип bytearray доступен также 
в Python 2.6 как результат переноса из версии 3.0, но он не так строго
разграничивает текстовые и двоичные данные, как в версии 3.0.

 Давайте совершим короткий ознакомительный тур. Объекты типа bytearray
могут создаваться вызовом встроенной функции bytearray. В Python 2.6 
для инициализации могут использоваться любые строки:


"""

# Создание в 2.6: изменяемая последовательность коротких (0..255)
# целых чисел
S = 'spam'
C = bytearray(S, 'latin-1')  # Результат переноса из 3.0 в 2.6
print(C)          # b’..’ == ‘..’ в 2.6 (str)

"""
 В Python 3.0 требуется использовать строку байтов или указывать 
название кодировки, потому что в этой версии не допускается смешивать 
текстовые строки и строки байтов, даже при том, что строки байтов могут 
являться отражением строк Юникода:
"""

B = b'spam'       # b’..’ != ‘..’ в 3.0 (bytes/str)
C = bytearray(B)
print(C)

"""
 В результате мы получаем объекты bytearray, которые являются 
последовательностями коротких целых чисел, как bytes, и изменяемыми,
как списки. В операциях присваивания по индексу требуется указывать 
целые числа, а не строки (все следующие ниже фрагменты являются 
продолжением данного сеанса в Python 3.0, если явно не оговаривается 
иное, – смотрите примечания к использованию в версии 2.6 
в комментариях):
"""

# Изменяемый, присваиваться должны целые числа, а не строки
print(C[0])

# C[0] = b'x'  # TypeError: an integer is required
C[0] = ord('x')
print(C)

C[1] = b'Y'[0]
print(C)

"""
 Для обработки объектов типа bytearray допускается использовать 
операции, которые обычно применяются к строкам и спискам, поскольку 
они являются изменяемыми строками байтов. Помимо обычных методов 
тип bytearray реализует также методы __iadd__ и __setitem__ поддержки 
оператора += конкатенации в памяти и присваивания по индексу
соответственно:
"""

# Методы, свойственные типам str и bytes, а также методы,
# свойственные спискам
print(set(dir(b'abc')) - set(dir(bytearray(b'abc'))))

print(set(dir(bytearray(b'abc'))) - set(dir(b'abc')))

"""
 Вы можете изменять объекты типа bytearray непосредственно в памяти 
с помощью операции присваивания по индексу, как только что было 
показано, и с помощью методов, похожих на методы списков, как показано
ниже (чтобы в версии 2.6 изменить текст непосредственно в памяти, 
вам пришлось бы преобразовать его в список и обратно с помощью list(str)
и ‘’.join(list)):
"""

# Методы изменяемых объектов

# C.append(b'LMN')  # В 2.6 требуется строка с длиной 1
# # TypeError: an integer is required
C.append(ord('L'))
print(C)

C.extend(b'MNO')
print(C)

"""
 К объектам типа bytearray могут применяться все обычные операции 
над последовательностями и строковые методы, как и можно было бы 
предполагать (обратите внимание, что как и в случае с объектами 
типа bytes, операторы и методы ожидают получить аргументы типа bytes,
а не str):
"""

# Операции над последовательностями и строковые методы
print(C + b'!#')

print(C[0])

print(C[1:])

print(len(C))

C = C.replace(b'xY', b'sp')

print(C)

print(C * 4)

"""
 Наконец, следующие примеры демонстрируют, что объекты типов bytes 
и bytearray являются последовательностями целых чисел, а объекты
типа str – последовательностями символов:
"""

# Двоичные и текстовые данные

print(list(B))

print(list(C))

print(list(S))

"""
 Несмотря на то, что все три строковых типа в Python 3.0 могут содержать 
значения символов и поддерживают почти те же самые операции, 
тем не менее, вы всегда должны:

  Для представления текстовых данных использовать тип str.
  
  Для представления двоичных данных использовать тип bytes.
  
  Для представления двоичных данных с возможностью непосредственного
 изменения использовать тип bytearray.
 
 Другие похожие инструменты, такие как файлы, которые рассматриваются
в следующем разделе, часто делают этот выбор типа объектов за вас.
"""