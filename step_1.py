def print_number_division(number_1, number_2):
    try:
        result = number_1 / number_2
    except ZeroDivisionError:
        return 'Не дели на 0'
    result = number_1 / number_2
    return result


first = int(input('Введите число:'))
second = int(input('Введите число:'))
print(print_number_division(first, second))
