ponto = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lista = []

for i in ponto:
    if i % 2 == 0:
        lista.append(i)

print(ponto[0:3])
print("Números pares ",lista)