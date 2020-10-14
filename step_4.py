intro_str = input('Введите строку:')
intro_str.split()
for idx, el in enumerate(intro_str.split()):
    print(idx + 1, el[:10])
