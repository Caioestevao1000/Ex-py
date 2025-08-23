print("## Diagonal Secundária de uma Matriz Quadrada ##")

def diagonal_secundaria(matriz):
    diagonal = []
    linhas = len(matriz)

    for i in range(linhas):
        if len(matriz[i]) != linhas:
            print("A matriz não é quadrada.")
            return []

    for i in range(linhas):
        j = linhas - 1 - i
        diagonal.append(matriz[i][j])

    return diagonal

matriz = []
n = int(input("Digite o tamanho N da matriz quadrada (NxN): "))

print("Digite os elementos da matriz:")

for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input("Valor para posição [" + str(i) + "][" + str(j) + "]: "))
        linha.append(valor)
    matriz.append(linha)

resultado = diagonal_secundaria(matriz)

if len(resultado) > 0:
    print("Elementos da diagonal secundária:")
    for valor in resultado:
        print(valor, end=' ')

input("\nAperte Enter para sair...")
