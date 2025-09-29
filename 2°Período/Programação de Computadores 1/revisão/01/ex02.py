lista = []
lista_nova = []

for i in range(10):
    lista.append(int(input(f"Digite o Número {i+1}°:")))
for x in range(len(lista)):
    const = 0
    for i in range(len(lista)):
        if lista[i] == lista[x]:
            const += 1
    if const == 1:
        lista_nova.append(lista[x])
print(lista_nova)
