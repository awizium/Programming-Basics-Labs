def check_input_position(field, x, y):
    """ Проверяет данны пользователя.
    Если такая клеточка есть на доске, возвращает True,
    В противном случае False.
    """
    
    if not(1 <= x <= len(field[0])) or not(1 <= y <= len(field)):
        return False
    return True

def get_right_cords(x, y, field):
    """ На вход программе поступает значение 1 на 1.
    Но пользователь на самом деле хочет не клетку нашего поля field[1][1]
    А хочет клетку под номером 7,7 для доски 8x8 - field[7][7]
    Эта функция переводит координаты x и y в координаты для списка.
    """
    return (len(field)-y, x-1)

def print_field(field):
    """ Печатает заданное поле на экран.
    При этом корректная работа будет наблюдаться до значения 999.
    На каждую клеточку выделяется 4 символа.
    """

    for row in field:
        line = ""
        for el in row:
            l_el = len(str(el))
            line += str(el) + " " * (4-l_el)
        print(line)

def get_all_variants(x, y, field):
    """ Получает все доступные варианты хода из конкретной точки
    и возвращает их в виде списка кортежей (x, y)
    """
    variants = []
    for x_step, y_step in step:
        if (x + x_step < 0) or (x + x_step >= len(field)) or (y + y_step < 0) or (y + y_step >= len(field[0])):
            continue
        if field[x + x_step][y + y_step] != 0:
            continue
        variants.append((x + x_step, y + y_step))
    return variants

def move(field, n, x, y, visited=0):
    """ Рекурсивная функция для обхода всего поля доски.
    Возвращает True, если заданную доску возможно обойти и False, если нельзя.

    field - список, в котором хранится поле
    n - количество клеточек в поле (8x8) => 64
    x - куда должен пойти конь по координате x
    y - куда должен пойти конь по координате y
    visited - количество посещённых клеток, если оно равно n, значит мы обошли всё поле
    """

    # Проверяем, что мы можем сходить этим ходом
    if (x <= -1) or (x >= len(field)) or (y <= -1) or (y >= len(field[0])):
        return False

    # Если посещённых клеток столько же, сколько клеток всего - мы прошли доску
    if n-1 == visited:
        field[x][y] = visited+1
        return True
    
    # Если в какой-то из точек мы уже побывали, значит ходить туда нельзя
    if field[x][y] != 0:
        return False
    
    # Новый ход
    visited += 1
    field[x][y] = visited

    # Получаем все возможные варианты хода
    move_list = get_all_variants(x, y, field)

    if len(move_list) != 0:
        # Получаем количество ходов для каждого хода
        neighbours = [ (len(get_all_variants(newx, newy, field)), (newx, newy)) for newx, newy in move_list]
        # Отбираем только те ходы, у которых кол-во ходов минимально по правилу Варнсдорфа
        neighbours_min = min([neigh[0] for neigh in neighbours])
        candidates = [neigh[1] for neigh in neighbours if neigh[0] == neighbours_min]

        # Перебираем всех кандидатов, пока не решим задачу
        for newx, newy in candidates:
            if (move(field, n, newx, newy, visited)):
                return True

    # Ходов нет, так что возвращаем ложь
    visited -= 1
    field[x][y] = 0
    return False


try:
    # Получаем данные для работы программы
    config = []
    with open("input.txt", 'r', encoding='utf-8') as f:
        config = [i.rstrip() for i in f.readlines()]
        config = [config[0].replace("M = ", ""), config[1].replace("N = ", ""),
                  config[3].replace("X = ", ""), config[4].replace("Y = ", "")]
        config = [int(i) for i in config]
    m, n = config[0], config[1]
    x, y = config[2], config[3]

    if (m < 1) or (n < 1):
        print("Координат не существует!")
        raise ValueError

    # Формируем поле для обхода. 0 считается за непосещённую клетку
    field = [[0 for _ in range(0, n)] for _ in range(0, m)]

    # Проверка на ввод правильных параметров пользователем
    does_exist = check_input_position(field, x, y)
    if not does_exist:
        print("Координат не существует!")
        raise ValueError
    
    # Получаем правильные координаты для нашего списка
    x, y = get_right_cords(x, y, field)

    # Формируем все возможные ходы коня
    step = [ [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2] ]
    
    # Начинаем движение, предварительно считаем количество клеток
    cell_amount = m*n
    lines = []
    if move(field, cell_amount, x, y):
        for row in field:
            line = ""
            for el in row:
                l_el = len(str(el))
                line += str(el) + " " * (4-l_el)
            lines.append(line + "\n")
    else:
        lines.append("Маршрут не существует")

    # Записываем все строчки, которые у нас получились в файл
    with open("output.txt", 'w', encoding='utf-8') as f:
        f.write("".join(lines))

    print("Программа успешно завершена!")

except Exception as e:
    print("Произошла ошибка при работе программы!")
    print(e)