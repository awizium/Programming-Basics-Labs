import random
# Вариант  1
# Метод пузырька
def bubble_sort(a):
    for i in range(1, len(a) + 1):
        for j in range(1, len(a) - i + 1):
            if a[-j] < a[-j - 1]:
                a[-j], a[-j - 1] = a[-j - 1], a[-j]
    return a

# Сортировка простыми вставками
def insertion_sort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        while (j >= 0 and temp < a[j]):
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = temp
    return a

# Быстрая сортировка
def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        q = random.choice(a)
    l_nums = [n for n in a if n < q]

    e_nums = [q] * a.count(q)
    b_nums = [n for n in a if n > q]
    return quick_sort(l_nums) + e_nums + quick_sort(b_nums)
