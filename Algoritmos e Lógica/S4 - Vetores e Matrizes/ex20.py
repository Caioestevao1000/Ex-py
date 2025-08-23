from random import uniform

matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(uniform(1.0, 50.0))
    matriz.append(linha)


# PRINT DA MATRIZ ARRUMADA
print('Matriz principal: ')
for i in range(5):
    for j in range(5):
        print(f'{matriz[i][j]:8.2f}', end = '')
    print()

print()

# PRINT DOS ELEMENTOS DA DIAGONAL PRINCIPAL
print('Diagonais principais: ')
for i in range(len(matriz)):
    print(f'{matriz[i][i]:.2f}')

print()

print(' Matriz após a multiplicação pela diagonal da linha: ')
for i in range(5):
    for j in range(5):
        multiplicacao = matriz[i][j] * matriz[i][i]
        print(f'{multiplicacao:10.2f}', end = '')
    print()