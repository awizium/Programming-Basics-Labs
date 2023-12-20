# Вариант 3
# Вычисление биномиальных коэффициентов / Ввод с клавиатуры
def C(m, n):
    if n == 0 or m == n:
        return 1
    else:
        return C(m - 1, n) + C(m - 1, n - 1)

nums = input('Введите два числа через пробел\n').split(' ')
m = int(nums[0])
n = int(nums[1])
print(C(m, n))