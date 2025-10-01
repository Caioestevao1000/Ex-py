def ler_disciplinas(nome):
    qtd = int(input(f"Quantas disciplinas {nome} cursa? "))
    disciplinas = []
    for i in range(1, qtd + 1):
        disc = input(f"Digite a disciplina {i} de {nome}: ")
        disciplinas.append(disc)
    return set(disciplinas) 

aluno1 = input("Nome do aluno 1: ")
disciplinas1 = ler_disciplinas(aluno1)

aluno2 = input("Nome do aluno 2: ")
disciplinas2 = ler_disciplinas(aluno2)

comum = disciplinas1 & disciplinas2
so_aluno1 = disciplinas1 - disciplinas2
so_aluno2 = disciplinas2 - disciplinas1

print("Disciplinas em comum:")
for d in comum:
    print("-", d)

print(f"Somente {aluno1}:")
for d in so_aluno1:
    print("-", d)

print(f"Somente {aluno2}:")
for d in so_aluno2:
    print("-", d)

print("Quantidades:")
print("- Em comum:", len(comum))
print(f"- Exclusivas de {aluno1}:", len(so_aluno1))
print(f"- Exclusivas de {aluno2}:", len(so_aluno2))
