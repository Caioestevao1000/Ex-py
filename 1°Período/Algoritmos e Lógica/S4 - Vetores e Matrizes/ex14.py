print("##  ##")
matriz = []
nomes = []

medias = []
soma_geral = 0

for i in range(15):
    nome = input(f'\nDigite o Nome do {i+1}° Aluno:')
    nomes.append(nome)
    linha = []
    for j in range(5):
        linha.append(float(input(f'Digite a Nota da {j+1}° Prova:')))
    matriz.append(linha)


for i in range(15):
    soma = 0
    for j in range(5):
        soma += matriz[i][j]
    medias.append(soma / 5)


for i in range(15):
    if medias[i] >= 6:
        print(f'{nomes[i]} media: {medias[i]:.2f} situação: Aprovado')
    
    if 4 <= medias[i] < 6:
        print(f'{nomes[i]} media: {medias[i]:.2f} situação: Exame')
        
    if  medias[i] < 4:
        print(f'{nomes[i]} media: {medias[i]:.2f} situação: Reprovado')


for i in range(15):
    soma_geral += medias[i]
media_geral = soma_geral / 15

print()
print(f'A média da classe é de: {media_geral:.2f}') 
print()

for i in range(len(nomes)):
    print(f'{nomes[i]:7}', end= '')
    for j in range(len(matriz[i])):
        print(f'{matriz[i][j]:7.2f}', end= '')
    print()

input('\nAperte Enter Para Sair...')