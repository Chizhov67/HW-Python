import random
import sys
try:
 list_length = int(input('Введите число элементов в массиве: '))
except ValueError:
print('[ОШИБКА]: Введено не число.')
exit(1)
random_nums = []
for i in range(list_length):
 random_number = random.randint(0, 10)
 random_nums.append(random_number)
 print(random_nums)
 try:
 x = int(input('Введите искомое число X (от 0 до 10): '))
except ValueError:
print('[ОШИБКА]: Введено не число.')
exit(1)
nearest_value_to_x = None
difference_to_x = sys.maxsize
for random_number in random_nums:
    new_difference = abs(random_number - x)
    if new_difference < difference_to_x:
        nearest_value_to_x = random_number
        difference_to_x = new_difference
        print(f'Ближайшее число к X ({x}): {nearest_value_to_x}')
     
