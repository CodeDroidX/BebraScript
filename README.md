# <img src="https://img.shields.io/badge/Bebra-Скрипт-%20orange" height="100" />
Язык программирования на **русском** в ***100*** строк, полностью совместимый с <img src="https://img.shields.io/badge/Python-darkgreen" />

<details>
<summary>В чём челлендж?</summary>
Вы когда нибуть задумывались?

```
Почему КуМир такой популярный? что в нём такого, что его форсит сама система образования в россии?
```

Для справки это "Алгоритмический язык" т.е. программы на нём выглядят примерно так:
```kumir
нач
цел f1,f2,b,i,n
ввод n
f1 := 1
f2 := 2
если n >= 2 то вывод f1,» «,f2,» » все
нц для i от 3 до n
вывод f1+f2, » »
b := f1
f1 := f2
f2 := f2+b
кц
кон 10
```
лол, его подсветку синтаксиса даже github не потдерживает(

**В общем код на кумире полнейший нечитаемый pascal-подобный шлак <3.**
## Но это же госпроект, да?
В общем всё и так ясно.

Денежки на разработку выделели, переводчик на устаревший паскаль русских букв написали, и подали как конфетку)
## Я попытался написать что то подобное, но уже основанное на python.
И вот что вышло.

На "разработку" сия чуда у меня ушло от силы пол часа моей жизни

И оно идеально работает 😌
</details>

<details>
<summary>Синтаксис и фичи</summary>

Я не буду ничего объяснять и просто приложу этот кусок кода 😘
```
    "из":"from",
    "подключить":"import",
    "всё":"*",

    "вернуть":"return",
    "фун":"def",
    "класс":"class",
    "конец":"exit()",
    "выход":"exit()",
    "ошибка":"raise ValueError(\"Artificial bebra error\")",

    "пока":"while",
    "для":"for",
    "если":"if",

    "вывод":"print",
    "ввод":"input",

    "ряду":"range",
    "ряд":"range",

    "цел":"int",
    "вещ":"float",
    "лит":"str",
    "лог":"bool",

    "список":"list",
    "спис":"list",

    "больше или равно":">=",
    "меньше или равно":"<=",

    "больше":">",
    "меньше":"<",

    "не равно":"!=",
    "равно":"==",
    "присвоить":"=",

    "делить":"/",
    "умножить":"*",
    "в степень":"**",
    "взять корень":"**0.5",
    "плюс":"+",
    "минус":"-",
    "остаток":"%",

    "в":"in",
    "не":"not",
    "и":"and",
    "или":"or",

    "я":"self"
```
думаю, всё и так понятно. Вот он ваш пресловутый кумир.

Только bebra потдерживает весь инструментарий python, классы и ООП, библиотеки и т.д.

Так же Bebra позволяет использовать русские заглавные буквы в качестве имён переменных!

Добавлен тип данных для точной математики с дробями
```
вывод(вещ(0.1)+вещ(0.2)) #Обычные float
вывод(дрб(0.1)+дрб(0.2)) #bebra дрб
```
```
Out> 0.30000000000000004 #Обычные float
Out> 3/10                #bebra дрб
```

</details>

<details>
<summary>Что получилось?</summary>

итого код выглядит примерно так:
```
для ЦВЫФРА в ряду(0,5):
	если ЦВЫФРА остаток 2 не равно 0: 
		вывод(ЦВЫФРА+1)
вывод("завершение работы")
конец
```
## просто перевод на Python
Переведённый код отправляется в файлик .py рядом с .bebra
```python
bebra_string0 = "завершение работы"

for Cv_FRA in range(0,5):
	if Cv_FRA % 2 != 0: 
		print(Cv_FRA+1)
print(bebra_string0)
exit()
```
Поскольку перевод осуществляет замены, то такой код тоже легален (к слову об интеграции с питоном):
```
вывод("Это один")
print("И тот же код")
```

## Ещё пара примеров кода:
```
из math подключить sqrt как КОРЕНЬ
вывод(КОРЕНЬ(123))
конец
```

```
класс ПЕЧАТАТЕЛЬ:
	фун создать(я,ИМЯ):
		я.ИМЯ=ИМЯ
	фун ПЕЧАТЬ(я):
		вывод(я.ИМЯ," - супер-пупер полезный класс")
Ы=ПЕЧАТАТЕЛЬ("Вася")
Ы.ПЕЧАТЬ()

Out> Вася  - супер-пупер полезный класс
```
Ну и конечно, если не хватает функционала, можно хоть всё писать на чистом Python
```
подключить numpy как np
МАТРИЦА присвоить np.array=([[1,2],[3,4]])
вывод(np.transpose(МАТРИЦА))

Out> [[1 3]
      [2 4]]
```
</details>
