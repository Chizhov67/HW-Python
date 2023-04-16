while True:
    try:
        number = int(input("Введите номер билета: "))
        summ1=0
        summ2=0
        number_list = [int(x) for x in str(number)]
        if len(number_list) != 6 or number < 0: continue
        summ1 = number_list[0]+number_list[1]+number_list[2]
        summ2 = number_list[3] + number_list[4] + number_list[5]
        if summ1==summ2: print('yes')
        else: print('no')
        break
    except:
        print("Вы ввели некорректный номер билета")
