def sum_max(first, second, third):
    if first >= second <= third:
        return first + third
    elif second >= first <= third:
        return second + third
    elif first >= third <= second:
        return first + second


first = int(input('Введите первое число: '))
second = int(input('Введите первое число: '))
third = int(input('Введите первое число: '))

print(sum_max(first, second, third))
