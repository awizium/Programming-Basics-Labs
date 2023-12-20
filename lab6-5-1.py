# Прямоугольники и квадраты / число (2 числа) / имя файла
import os
from moduls import printrectangle as rec
from moduls import printsquare as sq

a = list(os.listdir(r'C:\Users\rusik\PycharmProjects\pythonProject'))
b = []
for i in range(len(a)):
    if a[i][-4:] == '.txt':
        b.append(a[i])
if 'input.txt' not in b:
    print('Файл с входными данными не обнаружен')
if 'output.txt' not in b:
    print('Файл с выходными данными не обнаружен')
else:
    f_inp = open('input.txt')
    f = f_inp.readlines()
    size = f[0].split(' ')
    if len(size) == 2:
        a = int(size[0])
        b = int(size[1])
        filename = f[1]
        rec(a, b, filename)
    elif len(size) == 1:
        a = int(size[0])
        filename = f[1]
        sq(a, filename)