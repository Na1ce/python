proceed = int(input('Введите выручку фирмы:'))
costs = int(input('Введите издержки фирмы:'))

if proceed > costs:
    profit = proceed - costs
    staff = int(input(f'Прибыль составила {profit}, для расчета рентабельности введите кол-во сотрудников:'))
    profitability = profit / staff
    print(f'Рентабельность составила {profitability}')
else:
    print('Фирма работает в убыток')
