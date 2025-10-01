def quantos_maiores(lista, limite):
    cont = 0
    for i in range(len(lista)):
        if lista[i] > limite:
            cont += 1
    return cont

numeros = []
for i in range(8):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

limite = int(input("Digite o valor limite: "))
resultado = quantos_maiores(numeros, limite)
print(f"Quantidade de números maiores que {limite}: {resultado}")
