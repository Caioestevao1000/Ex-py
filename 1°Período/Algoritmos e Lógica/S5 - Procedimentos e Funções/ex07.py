print("## Diagonal Principal de uma Matriz Quadrada ##")

def diagonal_principal(matriz):
    linhas = len(matriz)
    for linha in matriz:
        if len(linha) != linhas:
            print("A matriz não é quadrada.")
            return []

    diagonal = []
    for i in range(linhas):
        diagonal.append(matriz[i][i])
    
    return diagonal

matriz = []
n = int(input("Digite o tamanho N da matriz NxN: "))

print(f"Digite os {n} elementos de cada uma das {n} linhas:")
for i in range(n):
    linha = input(f"Linha {i + 1} (separe os números por espaço): ").split()
    linha = [int(num) for num in linha]
    matriz.append(linha)
2
resultado = diagonal_principal(matriz)

if resultado:
    print("Elementos da diagonal principal:", resultado)

input("Aperte Enter para sair...")
