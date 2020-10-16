def my_first_func(x, y):
    return x ** y


def my_second_func(x, y):
    a = 1
    for el in range(abs(y)):
        a *= x
    if y >= 0:
        return a
    else:
        return 1 / a


x = int(input('Введите первое значение: '))
y = int(input('Введите первое значение: '))

print(my_first_func(x, y))
print(my_second_func(x, y))
