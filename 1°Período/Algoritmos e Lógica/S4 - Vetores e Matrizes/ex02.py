print("\n## 7 Elementos Inteiros - Vetor ##")

multiplos_dois = []
multiplos_tres = []
multiplos_dos_dois = []


print("Digite 7 Números Inteiros")
for x in range (7):
    num = int(input("Digite um Número Inteiro:"))
    if num % 2 == 0 and num % 3 == 0:
        multiplos_dos_dois.append(num)
    elif num % 2 == 0:
        multiplos_dois.append(num)
    elif num % 3 == 0:
        multiplos_tres.append(num)
print("Multiplos de 2", multiplos_dois)
print("Multiplos de 3", multiplos_tres)
print("Multiplos de 2 e 3", multiplos_dos_dois)
print("Pressione Enter para sair...")