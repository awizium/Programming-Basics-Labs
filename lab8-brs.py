import random

# Случайное количество баллов
def random_n():
    i = random.randint(0, 34)
    if i in range(0, 5):
        return 0
    elif i in range(5, 10):
        return 1
    elif i in range(10, 20):
        return 2
    elif i in range(20, 30):
        return 3
    elif i in range(30, 35):
        return 4

# Вычисление КРМ
def krm(n):
    return (n/4) * 100

# Вычисление оценки
def score(n: float):
    if n >= 0 and n < 60:
        return 'Неудовлетворительно'
    elif n >= 60 and n < 75:
        return 'Удовлетворительно'
    elif n >= 75 and n < 85:
        return 'Хорошо'
    elif n >= 85 and n <= 100:
        return 'Отлично'

table = { "ФИО студента": {},
          "1. Среда программирования PyCharm (4 балла/вес 1)": {},
          "Рейтинг 1 КРМ": {},
          "2. Переменные. Типы (4 балла/вес 2)": {},
          "Рейтинг 2 КРМ": {},
          "3. Строки (4 балла/вес 3)": {},
          "Рейтинг 3 КРМ": {},
          "4. Структуры данных (4 балла/вес 4)": {},
          "Рейтинг 4 КРМ": {},
          "5. Условный оператор. Подпрограммы (4 балла/вес 5)": {},
          "Рейтинг 5 КРМ": {},
          "6. Циклы. Модули. Файлы (4 баллов/вес 6)": {},
          "Рейтинг 6 КРМ": {},
          "7. Рекурсия. (4 балла/вес 7)": {},
          "Рейтинг 7 КРМ": {},
          "8. Сортировки (4 балла/вес 8)": {},
          "Рейтинг 8 КРМ": {},
          "Рейтинг текущего контроля": {},
          "Рейтинг промежуточной аттестации": {},
          "Рейтинг по дисциплине": {},
          "Оценка за дисциплину": {} }



f_out = open('output.txt', 'w')

# Заполнение ФИО студентов
n = int(input('Введите количество студентов больше 5:\n'))
if n < 1:
    exit('Недостаточное количество студентов, введите число, большее 5')
fio_max = 12
for i in range(1, n + 1):
    table['ФИО студента'][i] = str(input('Введите ФИО студента:\n'))
    if len(table['ФИО студента'][i]) > fio_max:
        fio_max = len(table['ФИО студента'][i])



# Заполнение случайными баллами и вычисление КРМ
for i in range(1, n + 1):
    n1 = random_n()
    table['1. Среда программирования PyCharm (4 балла/вес 1)'][i] = n1
    table['Рейтинг 1 КРМ'][i] = krm(n1)

    n2 = random_n()
    table['2. Переменные. Типы (4 балла/вес 2)'][i] = random_n()
    table['Рейтинг 2 КРМ'][i] = krm(n2)

    n3 = random_n()
    table['3. Строки (4 балла/вес 3)'][i] = random_n()
    table['Рейтинг 3 КРМ'][i] = krm(n3)

    n4 = random_n()
    table['4. Структуры данных (4 балла/вес 4)'][i] = random_n()
    table['Рейтинг 4 КРМ'][i] = krm(n4)

    n5 = random_n()
    table['5. Условный оператор. Подпрограммы (4 балла/вес 5)'][i] = random_n()
    table['Рейтинг 5 КРМ'][i] = krm(n5)

    n6 = random_n()
    table['6. Циклы. Модули. Файлы (4 баллов/вес 6)'][i] = random_n()
    table['Рейтинг 6 КРМ'][i] = krm(n6)

    n7 = random_n()
    table['7. Рекурсия. (4 балла/вес 7)'][i] = random_n()
    table['Рейтинг 7 КРМ'][i] = krm(n7)

    n8 = random_n()
    table['8. Сортировки (4 балла/вес 8)'][i] = random_n()
    table['Рейтинг 8 КРМ'][i] = krm(n8)



# Заполнение Рейтинга текущего контроля
for i in range(1, n + 1):
    ''' summa1 = table['Рейтинг 1 КРМ'][i] + table['Рейтинг 2 КРМ'][i] \
        + table['Рейтинг 3 КРМ'][i] + table['Рейтинг 4 КРМ'][i] \
        + table['Рейтинг 5 КРМ'][i] + table['Рейтинг 6 КРМ'][i] \
        + table['Рейтинг 7 КРМ'][i] + table['Рейтинг 8 КРМ'][i]
        summa2 = sum([1 for n in range(1,9)]) ''' # Если вес КРМ по 1 баллу
    summa1 = table['Рейтинг 1 КРМ'][i] * 1 + table['Рейтинг 2 КРМ'][i] * 2 \
        + table['Рейтинг 3 КРМ'][i] * 3 + table['Рейтинг 4 КРМ'][i] * 4 \
        + table['Рейтинг 5 КРМ'][i] * 5 + table['Рейтинг 6 КРМ'][i] * 6 \
        + table['Рейтинг 7 КРМ'][i] * 7 + table['Рейтинг 8 КРМ'][i] * 8
    summa2 = sum([int(n) for n in range(1,9)])
    table['Рейтинг текущего контроля'][i] = f"{(summa1 / summa2):.6f}"



# Заполнение рейтинга промежуточной аттестации, рейтинга по дисциплине и оценки за дисциплину
for i in range(1, n + 1):
    n1 = random.randint(0, 100)
    table['Рейтинг промежуточной аттестации'][i] = n1
    rd1 = 0.6 * float(table['Рейтинг текущего контроля'][i]) + 0.4 * float(table['Рейтинг промежуточной аттестации'][i])
    rd2 = float(table['Рейтинг текущего контроля'][i])
    rd = max(rd1, rd2)
    table['Рейтинг по дисциплине'][i] = f"{rd:.6f}"
    table['Оценка за дисциплину'][i] = score(rd)



# Шапка таблицы
f_out.write(f"ФИО студента{' ' * (fio_max - len('ФИО студента'))} | 1. Среда программирования PyCharm (4 балла/вес 1) "
                f"| Рейтинг 1 КРМ | 2. Переменные. Типы (4 балла/вес 2) | Рейтинг 2 КРМ | 3. Строки (4 балла/вес 3) "
                f"| Рейтинг 3 КРМ | 4. Структуры данных (4 балла/вес 4) | Рейтинг 4 КРМ | 5. Условный оператор. Подпрограммы (4 балла/вес 5) "
                f"| Рейтинг 5 КРМ | 6. Циклы. Модули. Файлы (4 баллов/вес 6) | Рейтинг 6 КРМ | 7. Рекурсия. (4 балла/вес 7) "
                f"| Рейтинг 7 КРМ | 8. Сортировки (4 балла/вес 8) | Рейтинг 8 КРМ | Рейтинг текущего контроля | Рейтинг промежуточной аттестации "
                f"| Рейтинг по дисциплине | Оценка за дисциплину | \n")



# Итоговая таблица
for i in range(1, n + 1):
    f_out.write(f"{table['ФИО студента'][i]}{' ' * (fio_max - len(table['ФИО студента'][i]))} | {table['1. Среда программирования PyCharm (4 балла/вес 1)'][i]}"
                f"{' ' * (len('1. Среда программирования PyCharm (4 балла/вес 1)') - len(str(table['1. Среда программирования PyCharm (4 балла/вес 1)'][i])))} "
                f"| {table['Рейтинг 1 КРМ'][i]}{' ' * (len('Рейтинг 1 КРМ') - len(str(table['Рейтинг 1 КРМ'][i])))} "
                f"| {table['2. Переменные. Типы (4 балла/вес 2)'][i]}{' ' * (len('2. Переменные. Типы (4 балла/вес 2)') - len(str(table['2. Переменные. Типы (4 балла/вес 2)'][i])))} "
                f"| {table['Рейтинг 2 КРМ'][i]}{' ' * (len('Рейтинг 2 КРМ') - len(str(table['Рейтинг 2 КРМ'][i])))} "
                f"| {table['3. Строки (4 балла/вес 3)'][i]}{' ' * (len('3. Строки (4 балла/вес 3)') - len(str(table['3. Строки (4 балла/вес 3)'][i])))} "
                f"| {table['Рейтинг 3 КРМ'][i]}{' ' * (len('Рейтинг 3 КРМ') - len(str(table['Рейтинг 3 КРМ'][i])))} "
                f"| {table['4. Структуры данных (4 балла/вес 4)'][i]}{' ' * (len('4. Структуры данных (4 балла/вес 4)') - len(str(table['4. Структуры данных (4 балла/вес 4)'][i])))} "
                f"| {table['Рейтинг 4 КРМ'][i]}{' ' * (len('Рейтинг 4 КРМ') - len(str(table['Рейтинг 4 КРМ'][i])))} "
                f"| {table['5. Условный оператор. Подпрограммы (4 балла/вес 5)'][i]}{' ' * (len('5. Условный оператор. Подпрограммы (4 балла/вес 5)') - len(str(table['5. Условный оператор. Подпрограммы (4 балла/вес 5)'][i])))} "
                f"| {table['Рейтинг 5 КРМ'][i]}{' ' * (len('Рейтинг 5 КРМ') - len(str(table['Рейтинг 5 КРМ'][i])))} "
                f"| {table['6. Циклы. Модули. Файлы (4 баллов/вес 6)'][i]}{' ' * (len('6. Циклы. Модули. Файлы (4 баллов/вес 6)') - len(str(table['6. Циклы. Модули. Файлы (4 баллов/вес 6)'][i])))} "
                f"| {table['Рейтинг 6 КРМ'][i]}{' ' * (len('Рейтинг 6 КРМ') - len(str(table['Рейтинг 6 КРМ'][i])))} "
                f"| {table['7. Рекурсия. (4 балла/вес 7)'][i]}{' ' * (len('7. Рекурсия. (4 балла/вес 7)') - len(str(table['7. Рекурсия. (4 балла/вес 7)'][i])))} "
                f"| {table['Рейтинг 7 КРМ'][i]}{' ' * (len('Рейтинг 7 КРМ') - len(str(table['Рейтинг 7 КРМ'][i])))} "
                f"| {table['8. Сортировки (4 балла/вес 8)'][i]}{' ' * (len('8. Сортировки (4 балла/вес 8)') - len(str(table['8. Сортировки (4 балла/вес 8)'][i])))} "
                f"| {table['Рейтинг 8 КРМ'][i]}{' ' * (len('Рейтинг 8 КРМ') - len(str(table['Рейтинг 8 КРМ'][i])))} | {table['Рейтинг текущего контроля'][i]}{' ' * (len('Рейтинг текущего контроля') - len(table['Рейтинг текущего контроля'][i]))} "
                f"| {table['Рейтинг промежуточной аттестации'][i]}{' ' * (len('Рейтинг промежуточной аттестации') - len(str(table['Рейтинг промежуточной аттестации'][i])))} "
                f"| {table['Рейтинг по дисциплине'][i]}{' ' * (len('Рейтинг по дисциплине') - len(str(table['Рейтинг по дисциплине'][i])))} "
                f"| {table['Оценка за дисциплину'][i]}{' ' * (len('Оценка за дисциплину') - len(str(table['Оценка за дисциплину'][i])))}\n")