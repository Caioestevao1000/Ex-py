print("## Valor Máximo e Mínimo de uma Matriz ##")

def max_min(matriz):
    maior = matriz[0][0]
    menor = matriz[0][0]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valor = matriz[i][j]

            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor

    return [maior, menor]

matriz = []
linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

print("Digite os valores da matriz:")

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input("Valor para posição [" + str(i) + "][" + str(j) + "]: "))
        linha.append(valor)
    matriz.append(linha)

resultado = max_min(matriz)

print("Maior valor:", resultado[0])
print("Menor valor:", resultado[1])

input("Aperte Enter para sair...")
