# 1.1 найти min число в листе
# l = [22, 3,5,2,8,2,-23, 8,23,5]
# print(min(l))

# 1.2 удалить все дубликаты в листе
# print(set(l))

# 1.3 заменить каждое четвертое значение на "Х"
# l[3] = "X"
# l[7] = "X"
# print(l)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# print('*','*','*','*','*','*','*','*','*','*')
# print('*',                                '*',sep='                 ')
# print('*',                                '*',sep='                 ')
# print('*',                                '*',sep='                 ')
# print('*',                                '*',sep='                 ')
# print('*',                                '*',sep='                 ')
# print('*',                                '*',sep='                 ')
# print('*',                                '*',sep='                 ')
# print('*','*','*','*','*','*','*','*','*','*')

#3) вывести табличку умножения с помощью цикла while
# a=1
# while a<=9:
#     b=1
#     while b<=9:
#         c=a*b
#         print(c, end=" ")
#         b+=1
#     print(" ")
#     a+=1

#4) переделать первое задание под меню с помощью цикла
l = [22, 3,5,2,8,2,-23, 8,23,5]
print(l)
while True:
    print('1. Найти min число в листе')
    print('2. Удалить все дубликаты в листе')
    print('3. Заменить каждое четвертое значение на "Х"')
    print('4. Выход')
    num = input('Введите номер: ')
    if num not in '12345':
        continue

    elif num == '1':
        print(min(l))

    elif num == '2':
        print(set(l))

    elif num == '3':
        l[3] = "X"
        l[7] = "X"
        print(l)
    elif num == '4':
        break
