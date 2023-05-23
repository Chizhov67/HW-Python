def print_operation_table(operation, num_rows=6, num_columns=6):
    # Проверка на то, что столбцов и строк больше 0
    if not (num_rows<=0 or num_columns<=0):
        # Цикл по строкам и столбцам, начиная с 1
        for i in range(1, num_columns+1):
            for j in range(1, num_rows+1):
                # Вычисляем очередной элемент с помощью переданной функции
                item = operation(i, j)
                # Выводим элемент на экран
                print(str(item), end=" ")
            # Переход на следующую строку
            print()

print_operation_table(lambda x,y: x*y, 6, 6)