def mover_zeros_fim(lista):
    nova_lista = [0] * len(lista) 
    pos = 0
    for i in range(len(lista)):
        if lista[i] != 0:
            nova_lista[pos] = lista[i]
            pos += 1
    return nova_lista

numeros = []
for i in range(12):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

resultado = mover_zeros_fim(numeros)
print("Lista com zeros movidos para o fim:", resultado)
