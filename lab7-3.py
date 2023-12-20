import os
# Вариант 3
# Нахождение наибольшего общего делителя / Ввод с клавиатуры
def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)

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
    f_out = open('output.txt', 'w')
    a = int(input('Введите первое число\n'))
    b = int(input('Введите второе число\n'))
    f_out.write(f'НОД({a}, {b}) = ' + str(nod(a, b)))