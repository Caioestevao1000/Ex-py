from random import randint

matriz = []

qntd_pares = 0
qntd_impares = 0
soma_par = 0
soma_impar = 0

for i in range(3):
    linha = []
    for j in range(4):
        linha.append(randint(1,50))
    matriz.append(linha)

for i in range(3):
    for j in range(4):
        n = matriz[i][j]
        if n % 2 == 0:
            qntd_pares += 1
            soma_par += n
            media_par = soma_par / qntd_pares
        if n % 2 == 1:
            qntd_impares += 1
            soma_impar += n
            media_impar = soma_impar / qntd_impares


for i in range(3):
    for j in range(4):
        print(f'{matriz[i][j]:7}', end = '')
    print()

print(f'Quantidade de pares: {qntd_pares}\nSoma de todos os pares: {soma_par}\nMédia de todos os pares: {media_par:.2f}')
print(f'\nQuantidade de ímpares: {qntd_impares}\nSoma de todos os ímpares: {soma_impar}\nMédia de todos os ímpares: {media_impar:.2f}')