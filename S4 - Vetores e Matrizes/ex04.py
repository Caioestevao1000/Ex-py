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