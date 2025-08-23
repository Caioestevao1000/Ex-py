from random import randint

matriz = []
soma_linha_4 = 0
soma_coluna = 0

soma_dg_princial = 0
soma_dg_secundaria = 0 

for i in range(5):         # Matriz 5x5
    linha= []
    for j in range(5):
        linha.append(randint(1, 50))
    matriz.append(linha)


for i in range(5):
    for j in range(5):
        print(f'{matriz[i][j]:4}', end = '')
    print()


i = 3   # linha da soma(é 3 por conta que é o indice, começa do 0)
for j in range(len(matriz[i])):
        soma_linha_4 += matriz[i][j]
print(f'\nSoma da linha 4: {soma_linha_4}')

coluna = 1
for i in range(len(matriz)):        # coluna é a coluna desejada, len(matriz) vai percorrer todas as linhas, += matriz[i][coluna] coluna = coluna desejada, e i = valor da coluna
     soma_coluna += matriz[i][coluna]
print(f'Soma da coluna 2: {soma_coluna}')


# Aqui é soma da diagonal principal, fiz manualmente, dpois descobri que se eu simplesmente rodar dentro de um for em range da matriz toda, a variavel soma += matriz[i][i] funciona
# Pois a linha e coluna da diagonal principal é a mesma pra todas as situações, [0][0], [1][1], [2][2]...
soma_dg_princial += matriz[0][0]
soma_dg_princial += matriz[1][1]
soma_dg_princial += matriz[2][2]
soma_dg_princial += matriz[3][3]
soma_dg_princial += matriz[4][4]


# que no caso seria, matriz[i][n - 1 - i] sendo que n = len(matriz) ou seja, o tanto de linhas dela que no caso é 5
# seria no primeiro caso i = 0 j = 5 - 1 - 0 = 4 entao [0][4] primeira da diagonal secundaria e assim por diante no percorrendo no for
soma_dg_secundaria += matriz[0][4] 
soma_dg_secundaria += matriz[1][3]
soma_dg_secundaria += matriz[2][2]
soma_dg_secundaria += matriz[3][1]
soma_dg_secundaria += matriz[4][0]


print(f'Soma da diagonal principal: {soma_dg_princial}')
print(f'Soma da diagonal secundária: {soma_dg_secundaria}')
