print("## Compressão de Matrizes - Compactação de Caracteres ##")

def compactar_matriz(matriz):
    vetor_compactado = []
    atual = ''
    contador = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            caractere = matriz[i][j]

            if atual == '':
                atual = caractere
                contador = 1
            elif caractere == atual:
                contador = contador + 1
            else:
                vetor_compactado.append((atual, contador))
                atual = caractere
                contador = 1

    if contador > 0:
        vetor_compactado.append((atual, contador))

    return vetor_compactado

matriz = []

linhas = int(input("Digite a quantidade de linhas da matriz: "))
colunas = int(input("Digite a quantidade de colunas da matriz: "))

print("Digite os caracteres da matriz (um por um):")

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = input("Digite o caractere da posição [" + str(i) + "][" + str(j) + "]: ")
        linha.append(valor)
    matriz.append(linha)

resultado = compactar_matriz(matriz)

print("Vetor Compactado:")
for i in range(len(resultado)):
    print("(", resultado[i][0], ",", resultado[i][1], ")", sep='')

input("Aperte Enter para sair...")
