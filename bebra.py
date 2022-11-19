import sys
fname = sys.argv[1]
if len(sys.argv)<3:
    task="python"
else: task = sys.argv[2]
assert task in ["python","fast","build"]
newfname=fname.replace("bebra","py")
f=open(fname,"r", encoding='utf-8').read()

syntax_reg={
    "подключить":"import",
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
    "плюс":"+",
    "минус":"-",
    "остаток":"%",

    "в":"in",
    "не":"not",
    "и":"and",
    "или":"or",

    "я":"self"
}
ru_a="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
en_a="ABvgDEfGZIJKLMNOPRSTUFWCXscQ_qEyY"

import re
art_str=re.split('("[^\"]*\")', f)[1::2]

for i in range(len(art_str)):
    f=f"bebra_string{i} = {art_str[i]}"+"\n#Bebra savetag\n"+f

f_unsaved="".join(f.split("#Bebra savetag")[-1])
f_saved="".join(f.split("#Bebra savetag")[:-1])

for i in range(len(art_str)):
    f_unsaved=f_unsaved.replace(art_str[i],f"bebra_string{i}")
for i in syntax_reg.items():
    f_unsaved=f_unsaved.replace(i[0],i[1])
for ru,en in zip(ru_a,en_a):
    f_unsaved=f_unsaved.replace(ru,en)

f=f_saved+f_unsaved

import os

with open(newfname,"w", encoding='utf-8') as nf:
    nf.write(f)

if os.system("pyflakes script.py"):
    print("BebraScript syntax error!!!")
    exit(1)
if task=="python":
    os.system("python "+newfname)

if task=="fast":
    exe=os.path.dirname(os.path.realpath(__file__))+"\pypy\pypy.exe"
    os.system(exe+" "+newfname)

elif task=="build":
    os.system("python -m nuitka "+newfname)
    os.remove(fname.replace("bebra","cmd"))
    __import__("shutil").rmtree(fname.replace("bebra","build"))
    print("Bebra compiling completed!")
