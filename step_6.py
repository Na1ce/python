product = [(1, {'Название': 'Компьютер', 'Цена': 20000, 'Количество': 5, 'ед.': 'шт'}),
           (2, {'Название': 'Принтер', 'Цена': 6000, 'Количество': 2, 'ед.': 'шт'}),
           (3, {'Название': 'Сканер', 'Цена': 2000, 'Количество': 7, 'ед.': 'шт'}),
          ]
for el in product:
    print(el[0], el[1])

analytics = {}
analytics_key = product[1][1].keys()

for key in analytics_key:
    analytics_values = []
    for el in product:
        if not el[1][key] in analytics_values:
            analytics_values.append(el[1][key])
    analytics[key] = analytics_values

for key, value in analytics.items():
    print(key, value)
