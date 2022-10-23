"""
 Пользовательский интерфейс IDLE

 До сих пор мы рассматривали запуск программного кода Python с помощью
интерактивной оболочки интерпретатора, системной командной строки,
с помощью щелчка мышью на ярлыке, с использованием операции импорта
и функции exec. Если вам требуется более наглядный подход,
программа IDLE может предложить вам графический интерфейс пользователя
(ГИП) для разработки программ на языке Python; IDLE является стандартной
и свободно распространяемой частью системы Python. Обычно она называется
интегрированной средой разработки (integrated development environment,
IDE), потому что позволяет решать разнообразные задачи
в единой оболочке.

 Проще говоря, IDLE – это набор инструментальных средств с графическим
интерфейсом, который способен работать на самых разных платформах,
включая Microsoft Windows, X Windows (в Linux, UNIX и других
UNIX-подобных операционных системах) и Mac OS (включая версии Classic
и OS X). Для многих IDLE представляет собой удобную альтернативу
командной строке, а также альтернативу способу запуска щелчком мыши.


 Использование IDLE

 Программа IDLE проста в использовании, переносима и доступна в
большинстве платформ. Я обычно рекомендую ее тем, кто только начинает
программировать на языке Python, потому что она упрощает некоторые
аспекты и не предполагает наличие опыта работы с системной командной
строкой. Но, по сравнению с некоторыми коммерческими интегрированными
средами разработки, она имеет некоторые ограничения. Ниже приводится
список особенностей, которые должны приниматься во внимание
начинающими пользователями IDLE:

  При сохранении файлов необходимо явно добавлять расширение «.py».

  Запускайте сценарии, выбирая пункт меню Run (Запустить) → Run Module
 (Запустить модуль) в окне редактирования, а не за счет их
 импортирования или перезагрузки в окне интерактивного сеанса.

  Вам по-прежнему может потребоваться выполнять перезагрузку
 импортируемых модулей.

  Вы можете настроить IDLE.

  В настоящее время в IDLE отсутствует возможность очистки экрана.

  Многопоточные программы и программы с графическим интерфейсом
 на базе tkinter могут не работать со средой IDLE. Из-за того, что IDLE
 сама является программой Python/tkinter, она может зависать при запуске
 некоторых типов программ на языке Python, использующих библиотеку
 tkinter.

  Если возникают ошибки соединения, попробуйте запустить IDLE в виде
 единого процесса.

  Остерегайтесь использования некоторых особенностей IDLE. Кроме того,
 IDLE автоматически переходит в каталог, где находится запускаемый файл
 и добавляет свой каталог в путь поиска модулей, что позволяет
 импортировать файлы без дополнительной настройки пути поиска.
 Эта особенность будет недоступна при запуске сценариев
 за пределами IDLE. Нет ничего предосудительного, если вы будете
 пользоваться этой возможностью, но не забывайте, что она доступна
 только в IDLE.


 Другие способы запуска

 К настоящему моменту мы рассмотрели, как выполнять программный код
в интерактивной командной оболочке интерпретатора и как запускать
программный код, сохраненный в файлах, из системной командной строки,
из исполняемых сценариев в системе UNIX, щелчком мыши, с помощью
операции импортирования модулей, с помощью функции exec и
в интегрированной среде разработки, такой как IDLE. Это подавляющее
большинство способов, которые встретятся вам в этой книге. Однако
существует еще ряд способов запуска программного кода на языке Python,
большая часть которых имеет узкоспециализированное назначение.
В следующих нескольких разделах мы коротко познакомимся
с некоторыми из них.


 Встраивание вызовов

 В некоторых особых случаях программный код на языке Python может
запускаться из других программ. В таких ситуациях мы говорим,
что программы на языке Python встроены в другие программы (то есть
запускаются другими программами). Сам программный код Python может
храниться в текстовом файле, в базе данных, извлекаться из страницы HTML
или из документа XML интерпретатору выполнить программный код,
созданный вами. Такой способ запуска программного кода
обычно используется для обеспечения поддержки возможности настройки
у конечного пользователя. Например, игровая программа может позволять
изменять ход игры, запуская в ключевые моменты
внедренный программный код на языке Python, доступный пользователю.
Поскольку программный код на языке Python интерпретируется,
внесение изменений в этот программный код
не требует перекомпилировать всю систему.

 В подобных случаях программа, вызывающая программный код
на языке Python, может быть написана на языке C, C++ и даже Java,
когда используется интерпретатор Jython. Например, вполне возможно
создавать и выполнять строки программного кода Python из программ
на языке C, вызывая функции API времени выполнения интерпретатора Python
(набор служб, экспортируемых библиотеками, созданными при компиляции
Python на вашей машине):

#include <Python.h>
...
Py_Initialize();           // Это язык C, а не Python
PyRun_SimpleString(“x = ‘brave ‘ + ‘sir robin’”);
                           // Но он запускает код на языке Python

 В этом фрагменте программа на языке C, скомпонованная с библиотеками
Python, инициализирует интерпретатор и передает ему для выполнения
строку с инструкцией присваивания. Программы на языке C могут также
получать доступ к объектам Python и взаимодействовать с ними,
используя другие функции API языка Python.


 Фиксированные исполняемые двоичные файлы

 Фиксированные исполняемые двоичные файлы, описанные в главе 2,
представляют собой комбинацию байт-кода программы и интерпретатора
Python, объединенных в одном исполняемом файле. Благодаря этому такие
программы могут запускаться точно так же, как любые другие программы
(щелчком на ярлыке, из командной строки и другими способами).
Такая возможность замечательно подходит для случая распространения
готовых программных продуктов, но она не предназначена для использования
в процессе разработки программ. Обычно фиксирование файлов производится
непосредственно перед отправкой (когда разработка уже завершена)
программы заказчику.


 Возможность запуска программ из текстового редактора

 Как упоминалось ранее, большинство текстовых редакторов
для программистов, хотя и не являются полноценными интегрированными
средами разработки, тем не менее поддерживают возможность редактирования
и запуска программ на языке Python. Такая поддержка может быть
изначально встроена в редактор или доступна в виде расширений,
которые можно загрузить из Сети. Например, если вы знакомы с текстовым
редактором Emacs, вы сможете редактировать программный код на языке
Python и запускать его, не покидая текстовый редактор.


 Прочие возможности запуска

 В зависимости от используемой платформы могут существовать и другие
способы запуска программ Python. Например, в некоторых системах
Macintosh выполнить программу на языке Python можно, перетащив мышью
ярлык файла программы на ярлык интерпретатора Python. В Windows
сценарии можно запускать с помощью пункта Выполнить... (Run…)
меню кнопки Пуск (Start). Наконец в состав стандартной библиотеки Python
входят вспомогательные функции, позволяющие запускать программы
на языке Python из других программ на языке Python (такие, как os.popen,
os.system), однако обсуждение этих функций выходит за рамки этой главы.


 Отладка программ на языке Python

 Разумеется, ни один из моих читателей и студентов никогда
не допускает ошибок в программном коде (здесь можно улыбнуться),
но ошибки могут допускать ваши менее удачливые друзья, поэтому здесь мы
рассмотрим краткий список стратегий, которые часто используются
программистами при отладке программ на языке Python:

  Ничего не делать. Здесь я не имею в виду, что программисты не должны
 отлаживать программный код, но, когда вы допускаете ошибку в программе,
 вы обычно получаете весьма информативное сообщение об ошибке.

  Добавление инструкций print. Пожалуй, самый основной способ отладки,
 которым пользуются программисты (и я тоже пользуюсь им) заключается
 в том, чтобы вставить инструкции print и выполнить программу еще раз.
 Так как интерпретатор позволяет запустить программу сразу после
 внесения изменений, этот прием обычно является самым быстрым способом
 получить дополнительную информацию сверх той, что содержится
 в сообщении об ошибке. Инструкции print не должны быть
 слишком сложными – вывода простой строки «Я здесь» или отображения
 значений переменных обычно вполне достаточно, чтобы понять
 причины ошибки.

  Использование отладчиков в интегрированных средах разработки.

  Использование pdb – отладчика командной строки. В составе Python
 поставляется отладчик исходного программного кода pdb, доступный
 в виде модуля в стандартной библиотеке языка Python. При использовании
 pdb вы сможете выполнять программный код построчно, отображать значения
 переменных, устанавливать и сбрасывать точки останова, возобновлять
 выполнение программы после остановки в контрольной точке и после ошибки
 и так далее.

  Другие возможности. Для удовлетворения более специфических требований,
 включая отладку многопоточных программ, внедряемого программного кода
 и уже запущенных процессов, можно поискать инструменты среди проектов,
 распространяемых с открытыми исходными текстами. Например,
 система Winpdb – автономный и платформонезависимый отладчик
 с расширенными возможностями, обладающий как графическим интерфейсом,
 так и интерфейсом командной строки.


 Упражнения к первой части

 1. Взаимодействие. Используя системную командную строку, IDLE
или другой инструмент, запустите интерактивный сеанс интерпретатора
Python (приглашение к вводу >>>) и введите выражение “Hello World!”
(включая кавычки). Строка должна быть повторно выведена на экран.
Цель этого упражнения состоит в том, чтобы помочь вам настроить
окружение для запуска интерпретатора Python. В некоторых случаях
вам может потребоваться сначала выполнить команду cd, ввести полный путь
к каталогу, куда был установлен выполняемый файл интерпретатора Python,
или добавить путь к этому каталогу в переменную окружения PATH.
При желании значение переменной PATH в системах UNIX можно установить
в файле .cshrc или .kshrc; в Windows для этой цели можно использовать
файл setup.bat, autoexec.bat или выполнить настройку переменной
окружения с использованием инструмента с графическим интерфейсом.
Справку по настройкам переменных окружения см. в приложении А.
"""

print('"Hello World!"')

"""
2. Программы. В текстовом редакторе, который вы предпочитаете, создайте
простой файл модуля, содержащий единственную инструкцию 
print(‘Hello module world!’), и сохраните его под именем module1.py. 
Теперь запустите этот файл каким-либо способом: из среды разработки 
IDLE, щелчком на ярлыке, вызовом интерпретатора Python из командной 
строки, передав ему имя файла в виде аргумента (например, 
python module1.py), и так далее. Попробуйте поэкспериментировать 
с разными способами запуска, которые обсуждались в этой главе.
Какие способы запуска показались вам проще? (На этот вопрос 
не может быть единственно правильного ответа.)
"""

exec(open('module1.py').read())

"""
3. Модули. Запустите интерактивный сеанс работы с интерпретатором Python
(приглашение к вводу >>>) и импортируйте модуль, который был создан
в упражнении 2. Попробуйте переместить файл в другой каталог 
и импортировать его снова из первоначального каталога (то есть запустите
Python в каталоге, где производился импорт в первый раз). Что произошло?
(Подсказка: посмотрите, остался ли в первоначальном каталоге файл с 
байт-кодом module1.pyc?)

4. Сценарии. Если ваша платформа поддерживает такую возможность, 
добавьте комбинацию символов #! в начало файла модуля module1.py, дайте
файлу право на выполнение и попробуйте запустить его как обычный 
исполняемый файл. Что должна содержать первая строка? Обычно комбинация 
символов #! имеет особое значение только на платформе UNIX, Linux
и других UNIX-подобных системах, таких как MAC OS X. Если вы работаете 
в Windows, попробуйте просто запустить файл, введя его имя 
без предшествующего ему слова «python» (этот способ работает 
в последних версиях Windows) или с помощью диалога Пуск (Start) 
→ Выполнить… (Run…).

5. Ошибки и отладка. Поэкспериментируйте с математическими выражениями 
и операциями присваивания в интерактивной командной оболочке Python.
Для начала введите выражения 2 ** 500 и 1/0. Что произошло? 
Потом попробуйте ввести имя переменной, которой еще не было присвоено
значение. Что произошло на этот раз?

 Вы еще можете не знать этого, но вы столкнулись с исключениями 
(эту тему мы подробно будем рассматривать в седьмой части книги).
Там вы узнаете, что, с технической точки зрения, ваши действия привели 
к вызову того, что известно под названием обработчик исключений 
по умолчанию, – программного кода, который выводит стандартные сообщения
об ошибках. Если вы не выполняете перехват ошибок в своих программах,
это за вас сделает обработчик по умолчанию, который выведет сообщение
об ошибке. Исключения неразрывно связаны с понятием отладки в языке 
Python. Для начала вам вполне будет достаточно стандартного механизма
обработки ошибок – он позволит узнать причину ошибки, а также покажет, 
какие строки кода выполнялись в момент ее появления. 

6. Прерывание программы. В командной строке интерпретатора Python 
введите следующие инструкции:

L = [1, 2] # Создать список с двумя элементами
L.append(L) # Добавить в конец списка
L

 Что произошло? Во всех современных версиях Python вы увидите кажущийся
странным результат, который описывается в приложении с решениями, 
а также в следующей части книги. При использовании версий Python 
старее 1.5.1 остановить работу этого программного кода на большинстве 
платформ вам поможет комбинация клавиш Ctrl-C. Как вы думаете, 
в чем причина происходящего? Что вывел интерпретатор после нажатия 
комбинации клавиш Ctrl-C?
"""

L = [1, 2]   # Создать список с двумя элементами
L.append(L)  # Добавить в конец списка
print(L)

"""
7. Документация. Потратьте хотя бы 17 минут на исследование библиотеки
Python и руководства по языку программирования, чтобы получить 
представление о стандартной библиотеке и о структуре комплекта 
документации. Вам нужно понять, по крайней мере, где в руководстве 
находятся описания основных тем. После этого вы легко сможете отыскать
интересующую вас информацию. В системе Windows это руководство находится
в разделе Python меню кнопки Пуск (Start), а также в виде пункта Python 
Docs (Документация Python) в меню Help (Справка) в среде разработки IDLE
или в Интернете по адресу: http://www.python.org/doc. Кроме того, 
хотелось бы также сказать несколько слов о других руководствах 
и источниках документации, описываемых (включая PyDoc и функцию help) 
в главе 15. Если у вас есть свободное время, займитесь исследованием 
веб-сайтов Python, а также веб-сайта расширений сторонних разработчиков 
PyPy. В частности, ознакомьтесь со страницами документации и поиска 
на сайте Python.org – они могут оказаться для вас 
весьма значимыми ресурсами.
"""
