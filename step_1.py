data_list = [1, 3.14, 1 + 1j, 'This is string',
            ['1', '2', '3'], ('one', 'two', 'three'),
            {'a', 'b', 'c'}, dict(key_1='data_1', key_2='data_2', key_3='data_3'),
            True, b'byte', bytearray(b'bytearray'), None]

for el in data_list:
    print(type(el))

