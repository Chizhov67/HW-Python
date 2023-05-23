def ritm_maker(s: str) -> str:
    # Вспомогательные константы
    vowels = ("а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е")
    ok = "Парам пам-пам"
    not_ok = "Пам парам"
    # Разбиваем строку по пробелам
    arr = s.lower().split(" ")
    # Если строка из одного слова, то возвращаем не ритм
    if len(arr) == 1:
        return not_ok
    # Убираем все символы кроме гластных
    arr = list(map(lambda str: list(filter(lambda letter: letter in vowels, str)), arr))
    # Считаем гластные в первой строке
    cnt = len(arr[0])
    # Смотрим, чтобы в остальных строках было столько же гластных
    result = all(map(lambda str: len(str) == cnt, arr))
    return ok if result else not_ok

s = input("Введите фразу: ")
print(ritm_maker(s))   