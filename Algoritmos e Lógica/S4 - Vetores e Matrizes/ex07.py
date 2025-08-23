print("## Alunos de Recuperação e Aprovados! ##")

nomes = []
medias = []
exame = []
nome_exam = []
maior_media = 0

for i in range(7):
    nome = input(f'\nDigite o Nome do {i+1}°Aluno:')
    media = float(input('Digite a Média final do Aluno:'))
    nomes.append(nome)
    medias.append(media)

for i in range(7):
    if medias[i] > maior_media:
        maior_media = medias[i]
        nome_maior = i
    if medias[i] < 7:
        exame_aprov = 10 - medias[i]
        exame.append(exame_aprov)
        nome_exam.append(nomes[i]) 
        

print(f'\nO Aluno {nomes[nome_maior]} Tem a Maior Média: {maior_media:.2f}')

print('\nAlunos com Média Menor que 7.0:')
for i in range(len(nome_exam)):
    print(f'O aluno {nome_exam[i]} precisa tirar {exame[i]:.2f} no exame para ser aprovado.')

input('\nPressione Enter para fechar o programa...')
