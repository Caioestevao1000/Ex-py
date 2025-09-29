contatos = []

n = int(input("Informe a quantidade de contatos: "))

for i in range(1, n + 1):
    nome = input(f"Contato {i} - Nome: ")
    telefone = input(f"Contato {i} - Telefone: ")
    contatos.append({"nome": nome, "telefone": telefone})

print("\nNomes cadastrados:")
for contato in contatos:
    print("-", contato["nome"])

print("\nNomes únicos:")
nomes_unicos = list(dict.fromkeys([c["nome"] for c in contatos]))
for nome in nomes_unicos:
    print("-", nome)

busca = input("\nDigite um nome para buscar o telefone: ")
encontrado = False
for contato in contatos:
    if contato["nome"].lower() == busca.lower():
        print(f"Telefone de {contato['nome']}: {contato['telefone']}")
        encontrado = True
        break

if not encontrado:
    print(f"{busca} não encontrado nos contatos.")
