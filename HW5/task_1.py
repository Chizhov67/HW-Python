def GetPow(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    else:
        return a * GetPow(a, b - 1)

a = int(input("a="))
b = int(input("b="))
res = GetPow(a, b)
print(res)
