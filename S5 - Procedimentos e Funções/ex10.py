print("## Detecção de Cruz em Matrizes ##")

def encontrar_cruzes(matriz):
    posicoes_cruz = []
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            cima = matriz[i - 1][j]
            baixo = matriz[i + 1][j
            esquerda = matriz[i][j - 1]
            direita = matriz[i][j + 1]

            if cima == 1 and baixo == 1 and esquerda == 1 and direita == 1:
                posicoes_cruz.append((i, j))

    return posicoes_cruz

matriz = []

linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

print("Digite os valores da matriz (0 ou 1):")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = in(input("Valor para posição [" + str(i) + "][" + str(j + "]: "))
        linha.append(valor)
    matriz.append(linha

resultado = encontrar_cruzes(matriz)

print("Posições centrais das cruzes encontradas:")
for pos in resultado:
    print("[", pos[0], "][", pos[1], "]", sep='')

input("Aperte Enter para sair..."