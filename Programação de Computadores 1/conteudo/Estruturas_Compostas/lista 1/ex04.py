conjunto = set()

n = int(input("Informe a quantidade de matrículas: "))

for i in range(n):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    disciplina = input(f"Digite a disciplina do aluno {i+1}: ")

    conjunto.add((nome, disciplina))  # tupla (aluno, disciplina)

print("\nMatrículas únicas:")
for aluno, disciplina in conjunto:
    print(f"{aluno} -> {disciplina}")
