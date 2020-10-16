def int_func(input_string):
    first_letter = chr(ord(input_string[0]) - ord('a') + ord('A'))
    return first_letter + input_string[1:]


input_string = input('Введите текст:')
print(int_func(input_string))
