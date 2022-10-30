"""
 ООП и делегирование: объекты-обертки

 Кроме терминов «наследование» и «композиция» в ООП также часто
используется термин делегирование, под которым обычно подразумевается
наличие объекта-контроллера, куда встраиваются другие объекты,
получающие запросы на выполнение операций. Контроллеры могут решать
административные задачи, такие как слежение за попытками доступа
и так далее. В языке Python делегирование часто реализуется с помощью
метода __getattr__, потому что он перехватывает попытки доступа
к несуществующим атрибутам. Класс-обертка (иногда называется
прокси-классом) может использовать метод __getattr__ для перенаправления
обращений к обернутому объекту. Класс-обертка повторяет интерфейс
обернутого объекта и может добавлять дополнительные операции.

 В качестве примера рассмотрим файл trace.py:
"""


class wrapper:
    def __init__(self, object):
        self.wrapped = object  # Сохранить объект

    def __getattr__(self, attrname):
        print('Trace:', attrname)  # Отметить факт извлечения
        return getattr(self.wrapped, attrname)
        # Делегировать извлечение


"""
 В главе 29 говорилось, что метод __getattr__ получает имя атрибута 
в виде строки. В этом примере для извлечения из обернутого объекта
атрибута, имя которого представлено в виде строки, используется 
встроенная функция getattr – вызов getattr(X, N) аналогичен 
выражению X.N за исключением того, что N – это выражение, которое 
во время выполнения представлено строкой, а не именем переменной. 
Фактически вызов getattr(X, N) по его действию можно сравнить 
с выражением X.__dict__[N], только в первом случае дополнительно 
выполняется поиск в дереве наследования, как в выражении X.N, 
а во втором – нет (подробнее об атрибуте __dict__ рассказывается
в разделе «Словари пространств имен» в главе 29).

 Такой прием, реализованный в этом классе-обертке, можно использовать 
для управления доступом к любому объекту с атрибутами – спискам,
словарям и даже к классам и экземплярам. Ниже приводится класс wrapper,
который просто выводит сообщение при каждом обращении к атрибуту
и делегирует этот запрос обернутому объекту wrapped:
"""


x = wrapper([1, 2, 3])  # Обернуть список
x.append(4)  # Делегировать операцию методу списка

print(x.wrapped)  # Вывести обернутый объект

x = wrapper({'a': 1, 'b': 2})  # Обернуть словарь
print(list(x.keys()))

"""
 В результате интерфейс обернутого объекта расширяется за счет методов
класса-обертки. Этот подход может использоваться для регистрации вызовов
методов, перенаправления вызовов методов дополнительному 
или адаптированному программному коду и так далее.

 В главе 31 мы еще вернемся к обернутым объектам и делегированию 
операций, как к одному из способов расширения встроенных типов. 
Если шаблон проектирования с делегированием заинтересовал вас, тогда 
смотрите обсуждение декораторов функций в главах 31 и 38, очень близкой 
концепции расширения отдельных функций и методов, а не всего интерфейса 
объекта, и декораторов классов, которые обеспечивают возможность
автоматического добавления оберток, реализующих прием делегирования, 
ко всем экземплярам классов.


 Псевдочастные атрибуты класса
 
 Помимо основной задачи, связанной со структурированием программного 
кода, в классах часто приходится решать проблемы использования имен. 
В пятой части книги мы узнали, что все имена, для которых выполняется 
присваивание на верхнем уровне модуля, становятся глобальными 
для этого модуля. То же по умолчанию относится и к классам – сокрытие 
данных регулируется соглашениями, и клиенты могут получать и изменять
любые атрибуты класса или экземпляра по своему усмотрению. Фактически 
все атрибуты являются «общедоступными» (public) и «виртуальными» 
(virtual), если говорить в терминах языка C++, – они доступны отовсюду 
и динамически отыскиваются во время выполнения.
 
 Тем не менее Python поддерживает такое понятие, как «искажение» 
(«mangling») имен (то есть расширение) с целью придать им черты
локальных имен для класса. Искаженные имена иногда ошибочно называют 
«частными атрибутами», но в действительности это всего лишь способ 
ограничить доступ к именам в классе – искажение имен не предотвращает
доступ из программного кода, находящегося за пределами класса. 
Эта особенность в основном предназначена, чтобы избежать конфликтов имен 
в экземплярах, а не для ограничения доступа к именам, – поэтому 
искаженные имена лучше называть «псевдочастными», чем «частными».

 Псевдочастные имена – это дополнительная и совершенно не обязательная
возможность, и вы, скорее всего, не сочтете ее полезной, 
пока не столкнетесь с необходимостью создания инструментов общего
назначения и многоуровневых иерархий классов в проектах, создаваемых
командами программистов. Фактически псевдочастные имена не всегда 
используются даже тогда, когда их следовало бы использовать. 
Гораздо чаще программисты дают внутренним атрибутам имена, начинающиеся
с одного символа подчеркивания (например, _X), – согласно неофициальным 
соглашениям, атрибуты с такими именами не должны изменяться за пределами 
класса (для самого интерпретатора такие имена не имеют специального 
значения).

 Так как использование этой возможности может встретиться в программном
коде других программистов, вам следует знать о ней, даже если вы сами 
ее не используете.


 Об искажении имен в общих чертах
 
 Здесь описывается, как действует механизм искажения имен: имена внутри
инструкции class, которые начинаются с двух символов подчеркивания, 
но не заканчиваются двумя символами подчеркивания, автоматически 
расширяются за счет включения имени вмещающего класса. Например, 
такое имя, как __X, в классе с именем Spam автоматически изменится 
на _Spam__X: к оригинальному имени будет добавлен префикс, состоящий 
из символа подчеркивания и имени вмещающего класса, и в результате будет
получено достаточно уникальное имя, которое не будет вступать в конфликт
с именами в других классах иерархии.

 Искажение имен происходит только внутри инструкций class и только 
для имен, которые начинаются двумя символами подчеркивания. Однако 
это происходит со всеми именами, которые начинаются двумя символами 
подчеркивания, включая имена методов и имена атрибутов экземпляров 
(например, в нашем примере с классом Spam ссылка на атрибут экземпляра 
self.__X будет преобразована в self._Spam__X). Поскольку экземпляр может 
получать атрибуты более чем из одного класса, такое искажение позволяет
избежать конфликтов, но чтобы понять, как это происходит, нам нужно 
рассмотреть пример.


 Для чего нужны псевдочастные атрибуты?
 
 Задача, которую призваны решить псевдочастные атрибуты, состоит в том,
чтобы обеспечить способ сохранности атрибутов экземпляра. В языке Python
все атрибуты экземпляра принадлежат единственному объекту экземпляра,
расположенному внизу дерева наследования. Это существенно отличается
от модели языка C++, где каждый класс обладает своим собственным набором
членов данных, которые он определяет.

 В языке Python всякий раз, когда в пределах метода класса выполняется
присваивание атрибуту аргумента self (например, self.attr = value),
создается или изменяется атрибут экземпляра (поиск в дереве наследования
выполняется только при попытке получить ссылку,
а не присвоить значение). Это верно, даже когда несколько классов 
в иерархии выполняют присваивание одному и тому же атрибуту, поэтому
конфликты имен вполне возможны.

 Например, предположим, что, когда программист писал класс, 
он предполагал, что экземпляры этого класса будут владеть атрибутом X. 
В методах класса выполняется присваивание этому атрибуту и позднее 
извлекается его значение:



class C1:
    def meth1(self):
        self.X = 88  # Предполагается, что X - это мой атрибут

     def meth2(self):
        print(self.X)


 Далее предположим, что другой программист, работающий отдельно, исходил
из того же предположения, когда писал свой класс:



class C2:
    def metha(self):
        self.X = 99  # И мой тоже

    def methb(self):
        print(self.X)



 Каждый класс по отдельности работает нормально. Проблема возникает, 
когда оба класса оказываются в одном дереве наследования:



class C3(C1, C2):
    pass


I = C3()  # У меня только один атрибут X!


 Теперь значение, которое получит каждый класс из выражения self.X, 
будет зависеть от того, кто из них последним присвоил значение.
Все операции присваивания атрибуту self.X будут воздействовать на один
и тот же экземпляр, у которого может быть только один атрибут X – I.X, – 
независимо от того, сколько классов используют это имя.

 Чтобы гарантировать принадлежность атрибута тому классу, который 
его использует, достаточно в начале имени атрибута поставить два символа
подчеркивания везде, где оно используется классом, как в следующем файле
private.py:
"""


class C1:
    def meth1(self):
        self.__X = 88  # Теперь X - мой атрибут

    def meth2(self):
        print(self.__X)  # Превратится в _C1__X


class C2:
    def metha(self):
        self.__X = 99  # И мой тоже

    def methb(self):
        print(self.__X)  # Превратится в _C2__X


class C3(C1, C2):
    pass


I = C3()  # В I два имени X
I.meth1()
I.metha()

print(I.__dict__)
I.meth2()
I.methb()

"""
 их классов, прежде чем будут добавлены в экземпляр. Если вызвать 
функцию dir, чтобы просмотреть перечень атрибутов экземпляра I, 
или просмотреть содержимое его словаря пространства имен после того,
как атрибутам будут присвоены значения, вы увидите измененные имена 
_C1__X и _C2__X, но не X. Такое дополнение придаст именам уникальность
внутри экземпляра, поэтому разработчики классов могут рассчитывать 
на то, что все имена, начинающиеся с двух символов подчеркивания, 
действительно принадлежат их классам:

% python private.py
{‘_C2__X’: 99, ‘_C1__X’: 88}
88
99

 Этот прием помогает избежать конфликтов имен в экземплярах, 
но заметьте, что он не обеспечивает настоящего сокрытия данных. Если вы
знаете имя вмещающего класса, вы сможете обратиться к их атрибутам
из любой точки программы, где имеется ссылка на экземпляр, используя 
для этого расширенное имя (например, I._C1__X = 77). С другой стороны,
эта особенность делает менее вероятными случайные конфликты 
с существующими именами в классе.

 Псевдочастные атрибуты также удобно использовать в крупных проектах, 
так как они позволяют избежать необходимости выдумывать новые имена
методов, которые по ошибке могут переопределить методы, уже существующие
выше в дереве классов, и помогают снизить вероятность, что внутренние
методы окажутся переопределенными где-то ниже в дереве классов.
Если метод предназначен для использования только внутри класса, 
и этот класс может наследовать или наследоваться другими классами,
приставка из двух символов подчеркивания гарантирует, 
что имя этого метода не будет конфликтовать с другими именами в дереве, 
особенно, когда используется прием множественного наследования:


class Super:
    def method(self): ...  # Фактический прикладной метод
    
    
class Tool:
    def __method(self): ...  # Получит имя _Tool__method
    
    def other(self): self.__method()  # Используется внутренний метод
    
    
class Sub1(Tool, Super): ...
    def actions(self): self.method()  # Вызовет метод Super.method
    
    
class Sub2(Tool):
    def __init__(self): 
        self.method = 99  # Не уничтожит метод Tool.__method
        
        
 Мы коротко познакомились с механизмом множественного наследования 
в главе 25 и более подробно будем исследовать его ниже, в этой главе.
Напомню, что в случае множественного наследования поиск атрибутов 
в этих классах производится слева направо, в порядке их следования 
в заголовке инструкции class. Для данного примера это означает,
что при обращении к атрибутам в классе Sub1 поиск унаследованных 
атрибутов сначала будет производиться в классе Tool, и только потом 
в классе Super. Мы могли бы в этом примере вынудить интерпретатор
сначала пытаться выбирать методы класса Super, поменяв порядок 
следования супер-классов в заголовке определения класса Sub1,
но это никак не повлияло бы на порядок разрешения имен псевдочастных 
атрибутов. Кроме того, псевдочастные имена предотвращают возможность 
переопределения внутренних методов в подклассах, как показано
в классе Sub2.

 Еще раз отмечу, что эта особенность более полезна для крупных проектов,
в которых участвует несколько программистов, и только для отдельных 
имен. Не торопитесь загромождать свой программный код лишними символами
без нужды – используйте эту особенность, только когда действительно 
необходимо обеспечить принадлежность атрибута единственному классу.
Для простых программ этот прием будет излишеством.

 Дополнительные примеры использования имен вида __X вы найдете в файле
lister.py, в примесных классах, которые будут представлены ниже 
в этой главе, в разделе, посвященном множественному наследованию,
а также в главе 38, в обсуждении декоратора классов Private. 
Если проблема частных атрибутов представляет для вас интерес,
вернитесь к главе 29, где в разделе «Обращения к атрибутам: __getattr__ 
и __setattr__» коротко описывается прием имитации частных атрибутов, 
и посмотрите на реализацию декоратора классов Private, основанную 
на этом приеме, которая приводится в главе 38. В действительности 
в языке Python имеется возможность по-настоящему управлять доступом 
к атрибутам классов, однако она редко используется на практике, 
даже в крупных системах.


 Методы – это объекты: связанные и несвязанные методы
 
 Методы вообще и связанные методы в частности, упрощают решение многих
задач в языке Python. Мы уже сталкивались со связанными методами 
в главе 29, когда изучали специальный метод __call__ . Однако, как мы 
узнаем в этом разделе, связанные методы обладают большей гибкостью, 
чем вы могли бы ожидать.

 В главе 19 мы узнали, что функции могут обрабатываться как обычные
объекты. Методы – это разновидность объектов, напоминающая функции, – 
они могут присваиваться переменным, передаваться функциям, сохраняться
в структурах данных и так далее. Доступ к методам класса осуществляется
через экземпляр класса или через сам класс и, фактически, в языке Python
имеется две разновидности методов:

 Несвязанные методы класса: без аргумента self
 
  Попытка обращения к функциональному атрибуту класса через имя класса 
 возвращает объект несвязанного метода. Чтобы вызвать этот метод, 
 необходимо явно передать ему объект экземпляра в виде первого 
 аргумента. В Python 3.0 несвязанные методы напоминают простые функции
 и могут вызываться через имя класса. В версии 2.6 несвязанные методы – 
 это совершенно иной тип данных, и они не могут вызываться без передачи 
 им ссылки на экземпляр.

 Связанные методы экземпляра: пара self + функция
 
  Попытка обращения к функциональному атрибуту класса через имя
 экземпляра возвращает объект связанного метода. Интерпретатор
 автоматически упаковывает экземпляр с функцией в объект связанного 
 метода, поэтому вам не требуется передавать экземпляр в вызов 
 такого метода.

 Обе разновидности методов – это полноценные объекты. Они могут 
передаваться между программными компонентами как обычные строки
или числа. При запуске оба требуют наличия экземпляра в первом аргументе 
(то есть значения для аргумента self). Именно по этой причине
в предыдущей главе было необходимо явно передавать экземпляр при вызове
методов супер-класса из методов подкласса – с технической точки зрения
такие вызовы порождают объекты несвязанных методов.

 Вызывая объект связанного метода, интерпретатор автоматически
подставляет экземпляр, который использовался при создании объекта 
связанного метода. Это означает, что объекты связанных методов обычно 
взаимозаменяемы с объектами простых функций и создание их особенно
полезно в случае интерфейсов, изначально ориентированных 
на использование функций (реалистичный пример приводится во врезке 
«Придется держать в уме: связанные методы и функции обратного 
вызова» ниже). Чтобы проиллюстрировать вышесказанное, предположим, 
что имеется следующее определение класса:

class Spam:
    def doit(self, message):
        print(message)

 В обычной ситуации мы создаем экземпляр и сразу же вызываем его метод 
для вывода содержимого аргумента:

object1 = Spam()
object1.doit(‘hello world’)

 Однако в действительности попутно создается объект связанного метода –
как раз перед круглыми скобками в вызове метода. Т.е. мы можем получить
связанный метод и без его вызова. Квалифицированное имя object.name – 
это выражение, которое возвращает объект. В следующем примере 
это выражение возвращает объект связанного метода, в котором упакованы
вместе экземпляр (object1) и метод (Spam.doit). Мы можем присвоить этот 
связанный метод другому имени и затем использовать это имя для вызова, 
как простую функцию:

object1 = Spam()
x = object1.doit  # Объект связанного метода: экземпляр+функция
x(‘hello world’)  # То же, что и object1.doit(‘...’)

 С другой стороны, если для получения метода doit использовать имя
класса, мы получим объект несвязанного метода, который просто ссылается
на объект функции. Чтобы вызвать метод этого типа, необходимо явно 
передавать экземпляр класса в первом аргументе:

object1 = Spam()
t = Spam.doit # Объект несвязанного метода
t(object1, ‘howdy’) # Передать экземпляр

 Те же самые правила действуют внутри методов класса, когда используются
атрибуты аргумента self, которые ссылаются на функции в классе.
Выражение self.method возвращает объект связанного метода, 
потому что self – это объект экземпляра:


class Eggs:
    def m1(self, n):
        print(n)
    def m2(self):
        x = self.m1  # Еще один объект связанного метода
        x(42)  # Выглядит как обычная функция
        
        
Eggs().m2()  # Выведет 42

 В большинстве случаев вы будете вызывать методы немедленно, сразу же 
после указания квалифицированного имени, поэтому вы не всегда будете 
замечать, что попутно создается объект метода. Но как только вы начнете 
писать программный код, который вызывает объекты единообразным способом,
вам потребуется проявить внимание к несвязанным методам, потому что
обычно они требуют явной передачи экземпляра в первом аргументе.


 В Python 3.0 несвязанные методы являются функциями
 
 В Python 3.0 было ликвидировано понятие несвязанных методов. Методы,
которые в этом разделе описываются как несвязанные методы, в версии 3.0 
обрабатываются как обычные функции. В большинстве ситуаций это никак 
не влияет на программный код – в любом случае при вызове метода 
относительно экземпляра в первом аргументе ему будет передан 
сам экземпляр.

 Однако для программ, где выполняется явная проверка типа, это изменение
может оказаться существенным – если вывести тип метода, не получающего
ссылку на экземпляр, в версии 2.6 будет выведено «unbound method» 
(несвязанный метод), а в версии 3.0 – «function» (функция).

 Кроме того, в версии 3.0 метод может вызываться без передачи ему 
ссылки на экземпляр при условии, что сам метод не ожидает ее получить 
и вызывается исключительно через обращение к имени класса. То есть 
в Python 3.0 ссылка на экземпляр передается методу, только когда он
вызывается относительно экземпляра. При вызове метода через имя класса 
передавать ему экземпляр требуется, только если он ожидает получить его:

C:\misc> c:\python30\python
>>> class Selfless:
...     def __init__(self, data):
...         self.data = data
...     def selfless(arg1, arg2):  # Простая функция в 3.0
...         return arg1 + arg2
...     def normal(self, arg1, arg2): 
            # Ожидает получить экземпляр при вызове
...         return self.data + arg1 + arg2
...
>>> X = Selfless(2)
>>> X.normal(3, 4)  # Экземпляр передается автоматически
9
>>> Selfless.normal(X, 3, 4)  # Метод ожидает получить self:
9                             # передается вручную
>>> Selfless.selfless(3, 4)  # Вызов без экземпляра: работает в 3.0,
7                            # но завершается ошибкой в 2.6!

 В Python 2.6 последний вызов в этом примере завершится ошибкой, 
потому что по умолчанию несвязанные методы требуют, чтобы им
передавалась ссылка на экземпляр, а в Python 3.0 ошибки не возникнет, 
потому что в этой версии такие методы интерпретируются,
как простые функции, не требующие передачи экземпляра. Эта особенность
версии 3.0 повышает вероятность появления случайных ошибок (что если 
программист просто забудет передать экземпляр по невнимательности?), 
но, с другой стороны, она позволяет использовать методы как простые
функции, при условии, что им не передается, и они не ожидают получить
аргумент «self» со ссылкой на экземпляр.

 Следующие два вызова завершатся ошибкой в обеих версиях Python, 
2.6 и 3.0, – в первом случае (вызов относительно экземпляра) методу 
автоматически будет передан экземпляр, которого он не ожидает, 
а во втором (вызов через обращение к имени класса) метод не получит 
ожидаемый экземпляр:

>>> X.selfless(3, 4)
TypeError: selfless() takes exactly 2 positional arguments (3 given)
>>> Selfless.normal(3, 4)
TypeError: normal() takes exactly 3 positional arguments (2 given)

 Благодаря этому изменению в версии 3.0 отпала необходимость 
использовать декоратор staticmethod, описываемый в следующей главе, 
для оформления методов, которые не принимают аргумент self, вызываются
только через имя класса и никогда не вызываются относительно экземпляра, 
– такие методы действуют как обычные функции, не получая аргумент 
с экземпляром. В версии 2.6 вызовы таких методов будут приводить 
к ошибкам, если экземпляр не будет передаваться им вручную (подробнее 
о статических методах рассказывается в следующей главе).

 Важно помнить об этих различиях в поведении несвязанных методов 
в версии 3.0, но с практической точки зрения связанные методы важнее.
Связанные методы представляют собой объекты, объединяющие в себе 
экземпляры и функции, поэтому их можно интерпретировать, как обычные 
вызываемые объекты. Что это означает с точки зрения программирования, 
демонстрируется в следующем разделе.


 Связанные методы и другие вызываемые объекты
 
 Как упоминалось выше, связанные методы могут интерпретироваться как
обычные вызываемые объекты, то есть как обычные функции, – они могут
произвольно передаваться между компонентами программы. Кроме того, так
как связанные методы объединяют в себе функцию и экземпляр, они могут 
использоваться как любые другие вызываемые объекты и не требуют 
применения специальных синтаксических конструкций для вызова. Ниже 
демонстрируется возможность сохранения четырех объектов связанных 
методов в списке и их вызов как обычных функций:
"""


class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3


x = Number(2)  # Объекты экземпляров класса
y = Number(3)  # Атрибуты + методы
z = Number(4)
x.double()  # Обычный непосредственный вызов

acts = [x.double, y.double, y.triple, z.double]
# Список связанных методов

for act in acts:  # Вызовы откладываются
    print(act())  # Вызов как функции


"""
 Как и простые функции, объекты связанных методов обладают информацией,
позволяющей провести интроспекцию, включая атрибуты, обеспечивающие
доступ к объекту экземпляра и к методу. Вызов связанного метода просто 
задействует эту пару:
"""

bound = x.double
print(bound.__self__, bound.__func__)

print(bound.__self__.base)

print(bound())  # Вызовет bound.__func__(bound.__self__, ...)


"""
 Фактически связанные методы – это лишь одна из разновидностей 
вызываемых  объектов в языке Python. Как демонстрирует следующий пример,
простые функции, определенные с помощью инструкции def или lambda, 
экземпляры, наследующие метод __call__, и связанные методы экземпляров 
могут обрабатываться и вызываться одинаковыми способами:
"""


def square(arg):
    return arg ** 2  # Простые функции (def или lambda)


class Sum:
    def __init__(self, val):  # Вызываемые экземпляры
        self.val = val

    def __call__(self, arg):
        return self.val + arg


class Product:
    def __init__(self, val):  # Связанные методы
        self.val = val

    def method(self, arg):
        return self.val * arg


sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method]  # Функция, экземпляр, метод

for act in actions:  # Все 3 вызываются одинаково
    print(act(5))  # Вызов любого вызываемого объекта с 1 аргументом

print(actions[-1](5))  # Индексы, генераторы, отображения

print([act(5) for act in actions])

print(list(map(lambda act: act(5), actions)))

"""
 Технически классы также принадлежат к категории вызываемых объектов,
но обычно они вызываются для создания экземпляров, а не для выполнения
какой-либо фактической работы, как показано ниже:

>>> class Negate:
...     def __init__(self, val):  # Классы - тоже вызываемые объекты
...         self.val = -val  # Но вызываются для создания объектов
...     def __repr__(self):  # Реализует вывод экземпляра
...         return str(self.val)
...
>>> actions = [square, sobject, pobject.method, Negate] 
    # Вызвать класс тоже
>>> for act in actions:
...     print(act(5))
...
25
7
15
-5
>>> [act(5) for act in actions]  # Вызовет __repr__, а не __str__!
[25, 7, 15, -5]
>>> table = {act(5): act for act in actions} 
    # генератор словарей в 2.6/3.0
>>> for (key, value) in table.items():
...     print(‘{0:2} => {1}’.format(key, value)) 
        # метод str.format в 2.6/3.0
...
-5 => <class ‘__main__.Negate’>
25 => <function square at 0x025D4978>
15 => <bound method Product.method of 
      <__main__.Product object at 0x025D0F90>>
7 => <__main__.Sum object at 0x025D0F70>

 Как видите, связанные методы и модель вызываемых объектов вообще – это
лишь некоторые из множества особенностей, обеспечивающие языку Python
невероятную гибкость.

 Теперь, когда вы понимаете суть объектной модели методов, ознакомьтесь
с примерами применения связанных методов во врезке «Придется держать
в уме: связанные методы и функции обратного вызова» и еще раз прочитайте
раздел предыдущей главы «__call__ обрабатывает вызовы», где обсуждаются
функции обратного вызова.

 
 Придется держать в уме: связанные методы и функции обратного вызова

 В объектах связанных методов вместе с функцией автоматически
сохраняется экземпляр класса, поэтому они могут использоваться везде,
где используются обычные функции. Одно из обычных мест, где можно
увидеть эту идею в действии, – это программный код, регистрирующий 
методы как обработчики событий в интерфейсе tkinter GUI (В Python 2.6
он называется Tkinter). Ниже приводится простейший случай:

def handler():
    ...сохраняет информацию о состоянии в глобальных переменных...
...
widget = Button(text=’spam’, command=handler)

 Чтобы зарегистрировать обработчик события щелчка на кнопке, мы обычно 
передаем в аргументе с именем command вызываемый объект, который
не имеет входных аргументов. Здесь часто используются имена простых
функций (и lambda-выражения), но можно также передавать и методы классов
 – при условии, что они будут связанными методами:
 
 
class MyWidget:
    def handler(self):
        ...сохраняет информацию о состоянии в self.attr...
    def makewidgets(self):
        b = Button(text=’spam’, command=self.handler)
        
        
 Здесь обработчик события self.handler – это объект связанного метода,
в котором сохраняются self и MyWidget.handler. Так как аргумент self
ссылается на оригинальный экземпляр, позднее, когда метод handle будет 
вызван для обработки события, он получит доступ к атрибутам экземпляра,
где может сохраняться информация о состоянии между событиями.
"""
