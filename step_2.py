input_time = int(input('Введите время в секундах:'))
hours = (input_time // 3600) % 24
minutes = (input_time // 60) % 60
seconds = input_time % 60
print('Время равно %02d-%02d-%02d' % (hours, minutes, seconds))
