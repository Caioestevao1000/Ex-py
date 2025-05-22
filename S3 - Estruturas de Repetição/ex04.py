print("\n## Grupos ##")

print("Digite 4 Números para 5 Grupos")

for grupos in range(1, 6):
    print(f"\nGrupo {grupos}:")
    
    A = float(input("Digite o Número 1: "))
    B = float(input("Digite o Número 2: "))
    C = float(input("Digite o Número 3: "))
    D = float(input("Digite o Número 4: "))
    grupo_ordem = [A, B, C, D]

    print("\nOrdem Original:", grupo_ordem)


    crescente = grupo_ordem[:]
    for i in range(3):
        for j in range (3 - i):
            if crescente[j] > crescente[j + 1]:
                crescente[j], crescente[j + 1] = crescente[j + 1], crescente[j]

    print("\nOrdem Crescente:", crescente)
            

    decrescente = grupo_ordem[:]
    for i in range(3):
        for j in range (3 - i):
            if decrescente[j] < decrescente[j + 1]:
                decrescente[j], decrescente[j + 1] = decrescente[j + 1], decrescente[j]

    print("\nOrdem Decrescente:", decrescente)

input("\n Pressione Enter para Sair...")