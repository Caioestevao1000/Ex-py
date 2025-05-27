from random import randint

print("## Matriz 2x4 - Números Entre 12 e 20 ##")

matriz = []
num = 0
pares

for i in range(2):
    linha = []
    for j in range(4):
        linha.append(randint(1,50))
    matriz.append(linha)

for i in range(2):
    for j in range(5):
        if 12 <= matriz[i][j] <= 20:
            num += 1
        if i / 2 == 0 and j /2 == 0:



for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'{matriz[i][j]:3}', end= '')
    print()

print(f'A Quantidade de Números Entre 15 e 20 é:{num}')
input("Aperte Enter Para Sair...")
