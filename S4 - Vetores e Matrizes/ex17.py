from random import randint

matriz = []
primo = []
maior_primo = 0
multiplicados = []

for i in range(5):
    linha = []
    for j in range(7):                      #Matriz 
        linha.append(randint(1, 100 ))
    matriz.append(linha)

posicao = []
for i in range(5):
    for j in range(7):
        cont = 0
        for k in range(1, matriz[i][j] + 1):    # Cálculo de primo
            if matriz[i][j] % k == 0:
                cont += 1
        if cont == 2:
            primo.append(matriz[i][j])
            if matriz[i][j] > maior_primo:
                maior_primo = matriz[i][j]
                posicao = (i,j)


if primo == []:
    print('Não há nenhum primo na lista.')
else:
    for i in range(5):                          # Multiplicação de todos pelo primo e condição caso nao tenha primo
        for j in range(7):
            multiplicados.append(matriz[i][j] * maior_primo) 


for i in range(5):
    for j in range(7):
        print(f'{matriz[i][j]:4}', end = '')        # Matriz apresentada arrumada
    print()


print(f'O maior primo encontrado é: {maior_primo} na posição {posicao}')
print(f'O resutlado de todos os elementos multiplicado pelo maior primo encontrado ({maior_primo}) é: \n{multiplicados}')

    
        