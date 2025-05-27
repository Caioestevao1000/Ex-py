from random import randint

print("Matriz 6x3, Maior e Menor Elemento")

matriz = []
maior = 0
menor = 51

for i in range(6):
    linha=[]
    for j in range(3):
        valor = int(randint(1,50))
        linha.append(valor)
    matriz.append(linha)

for i in range(6):
    for j in range(3):
        print(f"{matriz[i][j]:4}", end = '')
    print()

for i in range(6):
    for j in range(3):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i+1
            coluna_maior = j+1
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            linha_menor = i+1
            coluna_menor = j+1
print(f"\nO Maior Número é: {maior} na linha {linha_maior}, coluna {coluna_maior}")
print(f"O Menor Número é: {menor} na linha {linha_menor}, coluna {coluna_menor}")

input("Aperte Enter Para Sair...")
