search_month = int(input('Введите месяц в виде целого числа:'))
if search_month <= 12:
    year_list = ['Зима', 'Весна', 'Лето', 'Осень', 'Зима']
    year_dict = {
        0: 'Зима',
        1: 'Весна',
        2: 'Лето',
        3: 'Осень',
        4: 'Зима'
    }
    season = search_month // 3
    print(year_list[season])
    print(year_dict[season])
else:
    print('МЕСЯЦЕВ ВСЕГО 12!')
