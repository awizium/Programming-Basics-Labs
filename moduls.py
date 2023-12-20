import math
import random

def printrectangle(a, b, file):
    f = open(file, 'w')
    f.write(a * '* ')
    if b == 1:
        f.close()
    elif b > 1:
        for i in range(1, b - 1):
            f.write('\n* ' + (a - 2) * '  ' + '* ')
    f.write('\n')
    f.write(a * '* ')
    f.write('\n')
    f.close()

def printsquare(a, file):
    f = open(file, 'w')
    f.write(a * '* ')
    if a == 1:
        f.close()
    elif a > 1:
        for i in range(1, a - 1):
            f.write('\n* ' + (a - 2) * '  ' + '* ')
    f.write('\n')
    f.write(a * '* ')
    f.write('\n')
    f.close()

def prostak(n):
    p = []
    for i in range(2, int(n) + 1):
        k = 0
        for j in range(2, round(i ** 0.5) + 1):
            if i % j == 0:
                k += 1
        if k == 0:
            p.append(i)
    return p

def amount_of_points(r, coord):
    count = 0
    x0 = float(coord[0])
    y0 = float(coord[1])
    for x in range(math.ceil(x0 - r), math.floor(x0 + r) + 1):
        for y in range(math.ceil(y0 - r), math.floor(y0 + r) + 1):
            if ((x - x0) ** 2 + (y - y0) ** 2 <= r ** 2):
                count += 1
    return count

def matrix_gen(n, m):
    matrix = []
    for i in range(0, n):
        row = []
        for j in range(0, m):
            row.append(str(random.randint(0, 9)))
        matrix.append(row)
    return matrix

def matrix_prod(a, b):
    mult_result = [[0 for i in range(len(b[0]))] for row in range(len(a))]
    for m in range(len(a)):
        for n in range(len(b[0])):
            for o in range(len(b)):
                mult_result[m][n] += int(a[m][o]) * int(b[o][n])
    return mult_result