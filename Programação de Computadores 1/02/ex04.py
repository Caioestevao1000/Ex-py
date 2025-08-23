def somente_unicos(lista):
    nova_lista = []
    for i in range(len(lista)):
        cont = 0
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                cont += 1
        if cont == 1:
            nova_lista.append(lista[i])
    return nova_lista

numeros = []
for i in range(10):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

resultado = somente_unicos(numeros)
print("Lista apenas com elementos únicos:", resultado)
