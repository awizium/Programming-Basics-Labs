# Особые точки / число / 2 числа
import datetime
import os
from moduls import amount_of_points as aop

start = datetime.datetime.now()

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
    r = float(f[0])
    coord = f[1].split(' ')
    f_out = open('output.txt', 'w')
    f_out.write('Сегодняшняя дата: ' + str(datetime.datetime.now()) + '\n')
    f_out.write('Время начала работы программы: ' + str(start) + '\n')
    f_out.write('Количество точек с целочисленными координатами = ' + str(aop(r, coord)) + '\n')
    f_out.write('Время выполнения программы = ' + str(datetime.datetime.now() - start))
    f_inp.close()
    f_out.close()