print("Введите n, m, k через пробел")
n, m, k = map(int, input().split())
print((k < n*m) and ((k % n == 0) or (k % m == 0)))