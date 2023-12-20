import random
from sorts import bubble_sort as bub
from sorts import insertion_sort as ins
from sorts import quick_sort as qui
import datetime

def check(a): # Проверка на отсортированность
    if all(a[i] <= a[i + 1] for i in range(int(len(str(i))) - 1)):
        return True
    return False

n = int(input('Введите количество элементов N\n'))
a = []
for i in range(n):
    a.append(random.randint(1, 99)) # Генерация случайного списка

a2 = tuple(a) # Неотсортированная последовательность

a1 = tuple(qui(a)) # Отсортированная последовательность

a3 = tuple(qui(a)[::-1]) # Отсортированная в обратном порядке последовательность

f_out = open('output.txt', 'w')

start = datetime.datetime.now()
a1_bub = bub(list(a1))
time_a1_bub = datetime.datetime.now() - start

start = datetime.datetime.now()
a1_ins = ins(list(a1))
time_a1_ins = datetime.datetime.now() - start

start = datetime.datetime.now()
a1_qui = qui(list(a1))
time_a1_qui = datetime.datetime.now() - start



start = datetime.datetime.now()
a2_bub = bub(list(a2))
time_a2_bub = datetime.datetime.now() - start

start = datetime.datetime.now()
a2_ins = ins(list(a2))
time_a2_ins = datetime.datetime.now() - start

start = datetime.datetime.now()
a2_qui = qui(list(a2))
time_a2_qui = datetime.datetime.now() - start



start = datetime.datetime.now()
a3_bub = bub(list(a3))
time_a3_bub = datetime.datetime.now() - start

start = datetime.datetime.now()
a3_ins = ins(list(a3))
time_a3_ins = datetime.datetime.now() - start

start = datetime.datetime.now()
a3_qui = qui(list(a3))
time_a3_qui = datetime.datetime.now() - start



start = datetime.datetime.now()
a1_sort = (list(a1)).sort
time_a1_sort = datetime.datetime.now() - start

start = datetime.datetime.now()
a2_sort = (list(a2)).sort
time_a2_sort = datetime.datetime.now() - start

start = datetime.datetime.now()
a3_sort = (list(a3)).sort
time_a3_sort = datetime.datetime.now() - start



f_out.write('\n')
f_out.write(f' Метод{" " * 35} | Отсортированная{" " * 5} | Слуйчайная{" " * 10} | Отсортированная в обратном порядке \n')
f_out.write(f' Сортировка пузырьком{" " * 20} | {time_a1_bub} {check(a1_bub)}{" " * (19 - len(str(time_a1_bub)) - len(str(check(a1_bub))))} | {time_a2_bub} {check(a2_bub)}{" " * (19 - len(str(time_a2_bub)) - len(str(check(a2_bub))))} | {time_a3_bub} {check(a3_bub)}{" " * (33 - len(str(time_a3_bub)) - len(str(check(a3_bub))))}\n')
f_out.write(f' Сортировка вставками{" " * 20} | {time_a1_ins} {check(a1_ins)}{" " * (19 - len(str(time_a1_ins)) - len(str(check(a1_ins))))} | {time_a2_ins} {check(a2_ins)}{" " * (19 - len(str(time_a2_ins)) - len(str(check(a2_ins))))} | {time_a3_ins} {check(a3_ins)}{" " * (33 - len(str(time_a3_ins)) - len(str(check(a3_ins))))}\n')
f_out.write(f' Быстрая сортировка{" " * 22} | {time_a1_qui} {check(a1_qui)}{" " * (19 - len(str(time_a1_qui)) - len(str(check(a1_qui))))} | {time_a2_qui} {check(a2_qui)}{" " * (19 - len(str(time_a2_qui)) - len(str(check(a2_qui))))} | {time_a3_qui} {check(a3_qui)}{" " * (33 - len(str(time_a3_qui)) - len(str(check(a3_qui))))}\n')
f_out.write(f' Встроенная сортировка{" " * 19} | {time_a1_sort} {" " * (19 - len(str(time_a1_sort)))} | {time_a2_sort} {" " * (19 - len(str(time_a2_sort)))} | {time_a3_sort} {" " * (33 - len(str(time_a3_sort)))}\n')

''' Исходя из результатов сортировок, можно заметить, что встроенный метод .sort осуществляется быстрее всего,
    за ним по скорости стоит  "быстрая сортировка'''