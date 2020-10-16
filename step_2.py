def print_data(**kwargs):
    for position, argument in kwargs.items():
        print(f"{position}: {argument}")


a = dict(name='Валентин', surname='Стрыкало', birth_data='02.10.1988', living_city='Киев', email='str@kiev.ua',
         phone_number='800 507 001')
print_data(**a)
