alunos1 = []
alunos2 = []

while True:
    try:
        num = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida. Tente novamente!")

for n in range(num):
    alunos1.append(str(input(f"Digite os nomes dos alunos:")))

num2 = int(input("\nQuantos alunos na turma 2? "))
for u in range(num2):
    alunos2.append(str(input(f"Digite os nomes dos alunos:")))

conjunto_alunos1 = set(alunos1)
conjunto_alunos2 = set(alunos2)

print(f"Turma 1: {conjunto_alunos1}")
print(f"Turma 2: {conjunto_alunos2}")

print(f"Alunos nas duas turmas: {conjunto_alunos1 & conjunto_alunos2}")

print(f"Alunos na apenas na turma 1: {conjunto_alunos1 - conjunto_alunos2}")

print(f"Alunos na apenas na turma 2: {conjunto_alunos2 - conjunto_alunos1}")
