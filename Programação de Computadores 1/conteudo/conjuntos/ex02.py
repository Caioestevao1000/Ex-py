conjunto1 = input("Digite o nome dos aluno da turma A, separados por espaços:")
conjunto2 = input("Digite o nome dos aluno da turma B, separados por espaços:")

a = set(conjunto1.split())
b = set(conjunto2.split())

unia1 = a | b
print("União:", ", ".join(sorted(unia1)))
print(f"Total:{len(unia1)}")

# O join serve para jnutar elementos de uma lista(/outro iterável de strings), em uma única string, usando um separador que você escolher.

# A sintaxe:
# separador.join(lista_de_strings)