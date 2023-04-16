while True:
    try:
        number = int(input("Введите трехзначное число: "))
        summ=0
        number_list = [int(x) for x in str(number)]
        if len(number_list) != 3: continue
        summ = sum(number_list)
        print(f'Сумма цифр в указанном числе = {summ}')
    except:
        print("Вы ввели некорректное число")

        