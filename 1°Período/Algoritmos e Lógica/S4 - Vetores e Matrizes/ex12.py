from random import randint

print("\n## Matriz 2x4 - Números Entre 12 e 20 e Média dos Pares ##")

matriz=[]
pares_soma = 0
pares_qtd = 0

for i in range (2):
    linha = []
    for j in range(4):
        valor = randint(1, 50)
        linha.append(valor)
    matriz.append(linha)

print("Matriz Gerada:")
for i in range(2):
    for j in range(4):
        print(f"{matriz[i][j]:4}", end='')
    print()

for i in range(2):
    cont = 0
    for j in range(4):
        if 12 <= matriz[i][j] <=20:
            cont += 1
            print(f"Linha {i+1} possui {cont} número(s) entre 12 e 20.")

for i in range(2):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            pares_soma += matriz[i][j]
            pares_qtd += 1
if pares_qtd > 0:
    media = pares_soma / pares_qtd
    print(f"\nA média dos elementos pares da matriz é:{media:.2f}")
else:
    print("\nNão há elemnetos pares na matriz")

input("\nPressione Enter para sair...")
