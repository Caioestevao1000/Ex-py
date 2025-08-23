
produtos = []
matriz = []
soma_produtos = 0

for i in range(5):
    preco_produto = float(input(f'Informe o preço do {i + 1}° produto: '))
    produtos.append(preco_produto)


for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input(f'Informe a quantidade do {i + 1}° produto no {j + 1}° armazém: ')))
    matriz.append(linha)


# Print da matriz arrumada
print(f'{'Preço':<15} {'1° Armazém':<15} {'2° Armazém':<14} {'3° Armazém':<14} {'4° Armazém':<14} {'5° Armazém':<15}')
print('-'*90)
for i in range(5):
    print(f'R${produtos[i]:.2f}', end = '')
    for j in range(5):
        print(f'{matriz[i][j]:15}', end = '')
    print()


for j in range(5):  
    soma_cada_armazem = 0      # QNTD DE PRODUTO EM CADA ARMAZÉM
    for i in range(5):    
        soma_cada_armazem += matriz[i][j] 
    print(f'Qntd de produto do {j + 1}° armazém: {soma_cada_armazem}')


print()

for i in range(5):
    soma_cada_produto = 0       # QNTD DE CADA PRODUTO EM TODOS OS ARMAZÉNS
    for j in range(5):
        soma_cada_produto += matriz[i][j]
    print(f'Qntd do {i + 1}° produto em todos os armazéns: {soma_cada_produto}')

print()
menor_estoque = matriz[0][0]
maior_estoq = 0
for i in range(5):
    for j in range(5):
        if matriz[i][j] > maior_estoq:
            maior_estoq = matriz[i][j]              # PREÇO DO PRODUTO COM MAIOR ESTOQUE 
            preco_maior_estoq = produtos[i]         # MENOR ESTOQUE
        if matriz[i][j] < menor_estoque:
            menor_estoque = matriz[i][j]
print(f'O preço do produto que possui maior estoque em um único armazém é: R${preco_maior_estoq:.2f}\nO menor estoque armazenado é: {menor_estoque}')

print()

for j in range(5):
    custo_armazem = 0
    for i in range(5):
        custo_armazem += matriz[i][j] * produtos[i]
    print(f'Custo total do {j + 1}° armazém: R${custo_armazem:.2f}')      # CUSTO TOTAL DO ARMAZÉM

print()
input('Pression Enter para fechar o programa...')