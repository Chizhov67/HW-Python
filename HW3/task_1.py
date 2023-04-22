import random
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
x_count = random_nums.count(x)
print(f'Число вхождений числа X в списке: {x_count}')