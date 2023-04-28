def sum(a, b):
    if a == 0:
        return b;
    return sum(a-1, b+1)


a = int(input("a="))
b = int(input("b="))
res = sum(a, b)
print(res)
