import datetime

def req_factorial(n): #Рекурсивный факториал
    if n == 1:
        return 1
    return n * req_factorial(n - 1)

def iter_factorial(n): #Итеративный факториал
    n = int(input())
    factorial = 1
    for i in range(1, n):
        factorial *= i
    return factorial


def req_lagr(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return (2 * n + 1) / (n + 1) * x * req_lagr(n - 1, x) - n / (n + 1) * req_lagr(n - 2, x)

def iter_lagr(n, x):
    val = [0] * (n + 1)
    val[0] = 1
    if n >= 1:
        val[1] = x

    for i in range(2, n + 1):
        val[i] = (2 * i + 1) / (i + 1) * x * val[i -1] - i / (i + 1) * val[i - 2]

    return val[-1]

val1, val2 = 10, 20

start = datetime.datetime.now()
req_lagr(val1, val2)
print(f"\n[{val1}, {val2}] Рекурсивная функция справилась с задачей за: {datetime.datetime.now() - start} секунд")

start = datetime.datetime.now()
iter_lagr(val1, val2)
print(f"[{val1}, {val2}] Итеративная функция справилась с задачей за: {datetime.datetime.now() - start} секунд")


val1, val2 = 30, 50

start = datetime.datetime.now()
req_lagr(val1, val2)
print(f"\n[{val1}, {val2}] Рекурсивная функция справилась с задачей за: {datetime.datetime.now() - start} секунд")

start = datetime.datetime.now()
iter_lagr(val1, val2)
print(f"[{val1}, {val2}] Итеративная функция справилась с задачей за: {datetime.datetime.now() - start} секунд")

val1, val2 = 35, 55

start = datetime.datetime.now()
req_lagr(val1, val2)
print(f"\n[{val1}, {val2}] Рекурсивная функция справилась с задачей за: {datetime.datetime.now() - start} секунд")

start = datetime.datetime.now()
iter_lagr(val1, val2)
print(f"[{val1}, {val2}] Итеративная функция справилась с задачей за: {datetime.datetime.now() - start} секунд")

''' Рекурсия эффективнее по количеству операторов присваивания.
    По скорости работы, при малых значениях итерация эффективнее '''