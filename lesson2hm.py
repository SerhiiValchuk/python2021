# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка 2,3,5,4,4

st = 'asd 432grge43222ea'

answer = ''
for n in st:
    if n.isdecimal():
        answer += n
answer = ', '.join(answer)
print(answer)

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st = 'asd 432grge43222ea'

res = ''
for n in st:
    if n.isdigit():
        res += n
    else:
        res += ' '
res = ', '.join(res.split())
print(res)

# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
rezult = [x.upper() for x in greeting]
print(rezult)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
lest = [lest ** 2 for lest in range(50) if lest % 2 != 0]
print(lest)

# - створити функцію яка виводить ліст


fun = [1, 23, 44, 55, 4, 3, 'f']


def fun_2():
    print(fun)


fun_2()


# l = [1, 2, 3, 4, 5]
# def list_func(l):
#     for i in range(len(l)):
#         print(f'{i} -> {l[i]}')
#
#
# list_func(l)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.


def min_3(a, b, c):
    num = min(a, b, c)
    print(num)
    return num


min_3(6, 8, 9)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def max_3(a, b, c):
    num = max(a, b, c)
    return num


ris = max_3(78, -55, 777)
print(ris)


# -створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше


def inner(*args):
    num = max(*args)
    num2 = min(*args)
    print(num)
    return num2


inner(4, 6, 2, 45, 677, 2232, -4, 6, 2)

# створити функцію яка повертає найбільше число з ліста

mas = [22, 3231, -4, -453]


def l_1(mas):
    return max(mas)


print(l_1(mas))


# створити функцію яка повертає найменьше число з ліста


def l_2(mas):
    return min(mas)


print(l_2(mas))

# створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.


def list_sklad(mas):
    return sum(mas)


print(list_sklad(mas))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.


def avereg(mas):
    return sum(mas) // len(mas)


print(avereg(mas))

# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення


def decor(func):
    def wrap():
        return func().replace('_', ' ')

    return wrap


@decor
def pr():
    return 'Hello_boss_!!!'


print(pr())
