the_list = [7, 5, 3, 3, 2]
number = int(input('Введите число:'))
idx = 0
if number < the_list[-1]:
    the_list.append(number)
    print(the_list)
else:
    while idx < len(the_list):
        if number >= the_list[idx]:
            the_list.insert(idx, number)
            print(the_list)
            break
        else:
            idx += 1
