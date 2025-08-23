print("\n## 6 Elementos Pares e Ímpares - Vetor ##")

pares = []
impares = []

par = 0
impar = 0

print("Digite 6 Números Inteiros")
for x in range (6):
    num = int(input("Digite um Número Inteiro:"))
    if num % 2 == 0:
        par += 1
        pares.append(num)
    else:
        impares.append(num)
        impar += 1
print(f"A Quatidade de Números Pares é : {par} que são esses:{pares}")
print(f"A Quatidade de Números Ímpares é : {impar} que são esses:{impares}")

print("Pressione Enter para sair...")