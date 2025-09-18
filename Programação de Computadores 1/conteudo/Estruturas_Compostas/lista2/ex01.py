# Exercício 1 - Alunos e Cursos
alunos = []
qnt_alunos = int(input("Quantos alunos? "))

for i in range(qnt_alunos):
    dic = {}
    dic['nome'] = input(f"Nome do aluno {i+1}: ")
    dic['curso'] = input(f"Curso do aluno {i+1}: ")
    alunos.append(dic)

print("\nAlunos cadastrados:")
for a in alunos:
    print(f"- {a['nome']} ({a['curso']})")

# Cursos sem repetição
cursos = set()
for a in alunos:
    cursos.add(a['curso'])

print("\nCursos (sem repetição):")
for c in cursos:
    print("-", c)

# Contagem por curso
print("\nQuantidade de alunos por curso:")
for c in cursos:
    qtd = 0
    for a in alunos:
        if a['curso'] == c:
            qtd += 1
    print(f"- {c}: {qtd}")
