lista = []
pares = []
impares = []

for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))
    lista.append(num)

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print("Pares:", pares, "- Quantidade:", len(pares))
print("Ímpares:", impares, "- Quantidade:", len(impares))
