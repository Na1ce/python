data_list = []
value = None
while True:
    value = input('Введите значение. Чтобы остановить цикл, введите q: ')
    if value == 'q':
        break
    data_list.append(value)
print(f'Вы заполнили список значениями: {data_list}')
idx = 0
while idx < (len(data_list) // 2) * 2:
    data_list[idx], data_list[idx + 1] = data_list[idx + 1], data_list[idx]
    idx += 2
print(f'Мы поменяли местами соседние элементы списка: {data_list}')
