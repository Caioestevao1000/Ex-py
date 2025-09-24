def potencia(a,b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b-1)
a = int(input())
b = int(input())
soma = potencia(a,b)
print(soma)