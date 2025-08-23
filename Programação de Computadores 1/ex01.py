lista = []
lista_nova = []
lista_zero = []

for i in range(12):
    num = int(input(f"Digite o número {i+1}: "))
    lista.append(num)

for x in lista:
    if x != 0:
        lista_nova.append(x)
    else:
        lista_zero.append(x)

print(lista_nova + lista_zero)
