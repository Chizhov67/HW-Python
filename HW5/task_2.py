def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a, b)
    else:
        return a

a = int(input("a="))
b = int(input("b="))
res = sum(a, b)
print(res)