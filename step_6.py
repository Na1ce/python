current_result = 2
required_result = 3
day = 1

while current_result <= required_result:
    current_result = current_result + current_result * 0.1
    day += 1

print(f'На {day}-й день спортсмен достиг результата')
