from random import randint
n = int(input('Informe o tamanho(N) da matriz quadrada(NxN): '))

matriz = []

if n <= 0:
    print('Número inválido')
else:
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(randint(1, 100))
        matriz.append(linha)

for i in range(n):
    for j in range(n):
        print(f'{matriz[i][j]:7}', end = '')
    print()

print()

# CÁLCULO DE DIAGONAL MAIOR QUE A SOMA ABSOLUTA DAS LINHAS, O CONTADOR_DOMINANTE SERVE PARA A CADA NÚMERO IGUAL A DIAGONAL ELE SOMA, SE FOR IGUAL AO 'N' É MATRIZ DOMINANTE
contador_dominante = 0     
for i in range(n):
    soma = 0
    for j in range(n):      
        if j != i:
            soma += matriz[i][j]
    if matriz[i][i] >= soma:
        contador_dominante += 1

if contador_dominante == n:
    print('É uma matriz diagonal dominante.')
else: print('Não é uma matriz diagonal dominante.')       

print()

soma_cima = 0
soma_baixo = 0
for i in range(n):
    for j in range(n):
        if j > i:
            soma_cima += matriz[i][j]  # SE A COLUNA FOR MAIOR QUE A LINHA, ENTAO ESTÁ ACIMA, (0,1) (1,1), (2,1), O (0,1) COLUNA MAIOR QUE LINHA, ESTÁ ACIMA
        elif i > j:
            soma_baixo += matriz[i][j]  # MESMA COISA DE CIMA, SO QUE AO CONTRARIO
print(f'Soma dos elementos acima da diagonal principal: {soma_cima}')
print(f'Soma dos elementos abaixo da diagonal principal: {soma_baixo}')

print()

# MAIOR ELEMENTO E MENOR ELEMENTO
maior_elemento = 0
menor_elemento = matriz[0][0]
for i in range(n):
    for j in range(n):
        if matriz[i][j] > maior_elemento:
            maior_elemento = matriz[i][j]
            posicao_maior = (i, j)
        if matriz[i][j] < menor_elemento:
            menor_elemento = matriz[i][j]
            posicao_menor = (i, j)
print(f'O maior elemento da matriz é: {maior_elemento} e sua posição: {posicao_maior}')
print(f'O menor elemento da matriz é: {menor_elemento} e sua posição é: {posicao_menor}')


input('\nPressione Enter para fechar o programa...')