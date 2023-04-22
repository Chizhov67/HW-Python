def GetPow(a, b):
    if b == 1:
        return a
    else:
        return a * GetPow(a, b - 1)

a = int(input("a="))
b = int(input("b="))
res = GetPow(a, b)
print(res)