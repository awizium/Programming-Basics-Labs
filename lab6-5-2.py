# Все о цифрах в числе / число (числа)
import os
import math

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
    num = f_inp.readline().split(' ')
    num = num[0].split('\n')
    n2 = str(len(num[0]))
    n3 = sum(int(i) for i in num[0] if i != '\n')
    n4 = math.prod(int(i) for i in num[0] if i != '\n')
    f_out.write('Число: ' + num[0] + '\n')
    f_out.write('Количество цифр: ' + n2 + '\n')
    f_out.write('Сумма цифр: ' + str(n3) + '\n')
    f_out.write('Произведение цифр: ' + str(n4))
    f_inp.close()
    f_out.close()