print("\n## Alunos que Cursam as Duas Máterias ##")

lc = []
lp = []

comum = []

alunos_lp = 0
alunos_lc = 0

print("\nLógica Computacional - LC \nLinguagem de Programação - LP \n")

for i in range(25):
    matricula = int(input("\nDigite o Número da Matrícula do Aluno:"))
    materia = str(input("Digite o que o Aluno Estuda:"))
    if materia == "LP" or materia == "lp":
        lp.append(matricula)
        alunos_lp += 1
        if alunos_lp > 10:
            print("Linguagem de Programação não pode ter mais de 10 Alunos")
            break
    elif materia == "LC" or materia == "lc":
        lc.append(matricula)
        alunos_lc += 1
        if alunos_lc > 15:
            print("Lógica Computacional não pode ter mais de 15 Alunos")
            break
else:
    for i in range(len(lc)):
        for j in range(len(lp)):
            if lc [i] == lp[j]:
                comum.append(lc[i])
                break
    if len(comum) == 0:
        print("Não há Aluno Cursando as Duas Máterias")
    else:    
        print(f"Essas são as matrículas dos Alunos que Cursam os Dois Cursos {comum}")

# print("\n## Alunos que Cursam as Duas Máterias ##")

# lp = [] 
# lc = [] 
# comum = []

# print ("Preencha com os RAs do alunos de Linguagem de Programação...")
# for p in range(3):
#     ra = int(input(f"Digite o RA do {p+1}° Aluno:"))
#     lp.append(ra)
# else:
#     print ("Preencha com os RAs do alunos de Lógica Computacional...")
#     for c in range(2):
#         ra = int(input(f"Digite o RA do {c+1}° Aluno:"))
#         lc.append(ra)

# for x in range(len(lc)):
#     for j in range(len(lp)):
#         if lc[x] == lp[j]:
#             comum.append(lc[x])
#             break
# if len(comum) == 0:
#     print("Não há alunos cursando as duas máterias")
# else: 
#     print(f"Esses são os RAs dos alunos que cursam os dois cursos {comum}")
