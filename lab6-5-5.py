# Матрицы / 2 числа
import os
import random
from moduls import matrix_gen
from moduls import matrix_prod

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
    f = f_inp.readlines()
    f1 = f[0].split(' ')
    n = int(f1[0])
    m = int(f1[1])
    a = matrix_gen(n, m)
    output_lines = ["Матрица A:\n"]
    for row in a:
        output_lines.append(" ".join([str(i) for i in row]) + "\n")
    k = random.randint(5, 15) # k = int(f[1])
    b = matrix_gen(m, k)
    output_lines.append('\n' + "Матрица B:\n")
    for row in b:
        output_lines.append(" ".join([str(i) for i in row]) + "\n")
    output_lines.append('\n' + "Матрица A * B:\n")
    for row in matrix_prod(a, b):
        output_lines.append(" ".join([str(i) for i in row]) + "\n")
    for line in output_lines:
        f_out.write(line)
    f_inp.close()
    f_out.close()