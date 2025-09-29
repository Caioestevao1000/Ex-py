dic = {}

for i in range(2):
    nome = input(f"Nome do aluno {i+1}: ")
    qtd = int(input(f"Quantas disciplinas {nome} cursa? "))
    
    disciplinas = []
    for j in range(qtd):
        disc = input(f"Digite a disciplina {j+1} de {nome}: ")
        disciplinas.append(disc)
    
    dic[nome] = disciplinas

# Transforma listas em conjuntos para comparar
nomes = list(dic.keys())
aluno1, aluno2 = nomes[0], nomes[1]
disc1 = set(dic[aluno1])
disc2 = set(dic[aluno2])

print("\nDisciplinas em comum:")
for d in disc1 & disc2:
    print(d)

print(f"\nSomente {aluno1}:")
for d in disc1 - disc2:
    print(d)

print(f"\nSomente {aluno2}:")
for d in disc2 - disc1:
    print(d)
