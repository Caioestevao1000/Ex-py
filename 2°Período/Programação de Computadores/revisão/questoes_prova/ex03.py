# Enunciado

# Vamos gerenciar um cadastro de alunos usando lista de dicionários.
# Primeiro, informe quantos alunos serão cadastrados (m ≥ 1). Para cada aluno, digite, em linhas separadas: o nome e três notas (floats entre 0 e 10).

# Armazene os alunos em uma lista de dicionários, onde cada dicionário tem exatamente:

# {"nome": str, "notas": [float, float, float]}

# Com a lista pronta, faça:

#     Mostre a média da turma (1 casa decimal).
#     Mostre uma tabela nome → média (pode ser na ordem de cadastro).
#     Classifique por status e mostre as quantidades:
#         Aprovado (média ≥ 7.0)
#         Recuperação (5.0 ≤ média < 7.0)
#         Reprovado (média < 5.0)
#     Leia um nome para consulta e mostre Notas: [n1, n2, n3] | Média: x.x. Se não existir, mostre Aluno não encontrado.

# Observações:
# • Não precisa validar a entrada (assuma que vem tudo no formato certo);
# • Sugere-se implementar em duas etapas: (1) entrada e armazenamento dos dados; (2) processamento (cálculo da média da turma, tabela e contagens).
# Execução simulada

# Quantos alunos serão cadastrados? 4

# --- Aluno #1 ---
# Nome: Ana
# Nota 1: 8
# Nota 2: 7.5
# Nota 3: 9

# --- Aluno #2 ---
# Nome: Bruno
# Nota 1: 6
# Nota 2: 5
# Nota 3: 6.5

# --- Aluno #3 ---
# Nome: Carla
# Nota 1: 4
# Nota 2: 5
# Nota 3: 5

# --- Aluno #4 ---
# Nome: Daniel
# Nota 1: 8
# Nota 2: 7
# Nota 3: 8

# Média da turma: 6.8

# Tabela nome → média:
# Ana → 8.2
# Bruno → 5.8
# Carla → 4.7
# Daniel → 7.7

# Quantidade por status:
# Aprovado: 2
# Recuperação: 1
# Reprovado: 1

# Consulta - digite um nome: Carla
# Notas: [4.0, 5.0, 5.0] | Média: 4.7


def sistema():
    alunos = []

    m = int(input("Quantos alunos serão cadastrados? "))

    for i in range(m):
        print(f"\n Aluno {i + 1}")
        nome = input("Nome: ")
        notas = []
        for j in range(3):
            nota = float(input(f"Nota {j + 1}: "))
            notas.append(nota)
        aluno = {"nome": nome, "notas": notas}
        alunos.append(aluno)

    medias = []
    for aluno in alunos:
        notas = aluno["notas"]
        media = sum(notas) / 3
        medias.append(media)

    media_turma = sum(medias) / len(medias)
    print(f"\nMédia da turma: {media_turma:.1f}")

    print("\nTabela nome -> média:")
    for i in range(len(alunos)):
        nome = alunos[i]["nome"]
        media = medias[i]
        print(f"{nome} -> {media:.1f}")

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for media in medias:
        if media >= 7.0:
            aprovados += 1
        elif media >= 5.0:
            recuperacao += 1
        else:
            reprovados += 1

    print("\nQuantidade por status:")
    print(f"Aprovado: {aprovados}")
    print(f"Recuperação: {recuperacao}")
    print(f"Reprovado: {reprovados}")

    nome_busca = input("\nConsulta - digite nome de um aluno: ")

    encontrado = False
    for i in range(len(alunos)):
        if alunos[i]["nome"].lower() == nome_busca.lower():
            notas = alunos[i]["notas"]
            media = medias[i]
            print(f"Notas: {notas} | Média: {media:.1f}")
            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado.")

print(sistema())
