def mayor (x, y):
    if x > y:
        return x
    return y

a = 20
b = 2222
c = 2222
d = 11111111

maximo = mayor (a, b)
maximo = mayor (mayor (a, b), mayor(c, d))
print(maximo)