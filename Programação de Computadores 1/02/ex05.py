def inverter(lista):
    nova_lista = [0] * len(lista)
    for i in range(len(lista)):
        nova_lista[i] = lista[len(lista)-1-i]
    return nova_lista

def media(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma / len(lista)

def contar_acima_da_media(lista, m):
    cont = 0
    for i in range(len(lista)):
        if lista[i] > m:
            cont += 1
    return cont

numeros = []
for i in range(8):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

print("Lista original:", numeros)
print("Lista invertida:", inverter(numeros))
m = media(numeros)
print("Média dos valores:", m)
print("Quantidade acima da média:", contar_acima_da_media(numeros, m))
