# Генератор простых чисел / число
import os
from moduls import prostak

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
    f_out = open('output.txt', 'w')
    n = f_inp.readline().strip().replace(' ', '')
    f_out.write(str(prostak(n)))
    f_inp.close()
    f_out.close()