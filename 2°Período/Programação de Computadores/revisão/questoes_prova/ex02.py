# Enunciado

# Vamos organizar eventos e seus participantes usando apenas listas e conjuntos.

#     Informe quantos eventos serão cadastrados (e ≥ 2). Para cada evento, digite:
#         o título (sem espaços),
#         o número de participantes p,
#         e p linhas com um participante por linha (minúsculas).

# Estruturas (somente listas e conjuntos):

#     titulos: lista com os títulos (uma string por evento);
#     participantes: lista de conjuntos, onde participantes[i] é o conjunto de nomes do evento titulos[i].

# Com os dados, faça apenas:

#     Mostre os participantes presentes em todos os eventos (interseção global).
#     Leia dois títulos (A e B) e compare os eventos, exibindo:
#         Em ambos,
#         Só em A,
#         Só em B,
#         Em exatamente um.

# Observações: não precisa validar a entrada; sem split() e sem ordenação; um nome por linha é suficiente.
# Execução simulada

# Quantos eventos serão cadastrados (e ≥ 2)? 3

# --- Evento #1 ---
# Título (sem espaços): SemanaBSI
# Quantos participantes (p ≥ 0)? 3
# Participante #1: ana
# Participante #2: bruno
# Participante #3: carla

# --- Evento #2 ---
# Título (sem espaços): WorkshopIA
# Quantos participantes (p ≥ 0)? 4
# Participante #1: ana
# Participante #2: daniel
# Participante #3: erika
# Participante #4: bruno

# --- Evento #3 ---
# Título (sem espaços): Hackathon
# Quantos participantes (p ≥ 0)? 3
# Participante #1: ana
# Participante #2: felipe
# Participante #3: bruno

# Participantes em todos os eventos:
# ana
# bruno

# Compare dois eventos
# Título A: SemanaBSI
# Título B: Hackathon

# Comparação entre SemanaBSI e Hackathon
# Em ambos:
# ana
# bruno

# Só em A:
# carla

# Só em B:
# felipe

# Em exatamente um:
# carla
# felipe


def sistema():
    e = int(input("Quantos eventos serão cadastrados (eventos maiores que 1)? "))

    titulos = []
    participantes = []

    for i in range(e):
        print(f"\n ## Evento {i + 1} ##")
        titulo = input("Título (sem espaços): ")
        titulos.append(titulo)

        p = int(input("Número de Participantes (maior que 0)? "))
        conjunto = set()

        for j in range(p):
            nome = input(f"Participante {j + 1}°: ")
            conjunto.add(nome)

        participantes.append(conjunto)

    inters_global = participantes[0]
    for i in range(1, len(participantes)):
        inters_global = inters_global & participantes[i]

    print("\nParticipantes em todos os eventos:")
    if len(inters_global) == 0:
        print("(Nenhum)")
    else:
        for nome in inters_global:
            print(nome)

    print("\nCompare dois eventos")
    tituloA = input("Título A: ")
    tituloB = input("Título B: ")

    indiceA = titulos.index(tituloA)
    indiceB = titulos.index(tituloB)

    conjuntoA = participantes[indiceA]
    conjuntoB = participantes[indiceB]

    print(f"\nComparação entre {tituloA} e {tituloB}")

    em_ambos = conjuntoA & conjuntoB
    so_A = conjuntoA - conjuntoB
    so_B = conjuntoB - conjuntoA
    em_exat_um = conjuntoA ^ conjuntoB

    print("Em ambos:")
    if len(em_ambos) == 0:
        print("(Nenhum)")
    else:
        for nome in em_ambos:
            print(nome)

    print("\nSó em A:")
    if len(so_A) == 0:
        print("(Nenhum)")
    else:
        for nome in so_A:
            print(nome)

    print("\nSó em B:")
    if len(so_B) == 0:
        print("(Nenhum)")
    else:
        for nome in so_B:
            print(nome)

    print("\nEm exatamente um:")
    if len(em_exat_um) == 0:
        print("(Nenhum)")
    else:
        for nome in em_exat_um:
            print(nome)

print(sistema())
