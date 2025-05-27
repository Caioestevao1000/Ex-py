print("\n## 10 Elementos e Divisão em Dois Vetores ##")
vetor_origin = []
vetor_compac = []

print("Digite 10 valores (positivos, negativos ou zero):")
for i in range(10):
    valor = int(input(f"Valor {i + 1}: "))
    vetor_origin.append(valor)

# Compactação: adicionar apenas valores positivos e diferentes de zero
for i in range(10):
    if vetor_origin[i] > 0:
        vetor_compac.append(vetor_origin[i])

# Resultado
print("\nVetor original:")
print(vetor_origin)

print("\nVetor compactado (apenas valores positivos e diferentes de zero):")
print(vetor_compac)

input("Aperte Enter Para Sair...")