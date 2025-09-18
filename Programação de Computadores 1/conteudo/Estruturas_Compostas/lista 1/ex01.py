alunos = []

n = int(input("Informe a quantidade de alunos: "))

for i in range(n):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    curso = input(f"Digite o curso do aluno {i+1}: ")
    
    alunos.append({
        "nome": nome,
        "curso": curso
    })

    print(alunos)

cursos = {aluno["curso"] for aluno in alunos}  

print("\nCursos cadastrados (sem repetição):")
for curso in cursos:
    print(f"- {curso}")

