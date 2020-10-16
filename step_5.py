el = 0

my_list = []
while el != 1:
    numbers = input('Введите числа без пробела и нажмите Enter ')
    s = numbers.split()
    for sym in s:
        if sym == '*':
            el += 1
            break
        my_list.append(int(sym))
    sum_num = sum(my_list)
    print(f'Сумма чисел равна {sum_num}')
