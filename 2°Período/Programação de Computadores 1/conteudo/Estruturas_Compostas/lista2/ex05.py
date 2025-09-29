# Exercício 5 - Contatos
contatos = []
qnt = int(input("Quantos contatos? "))

for i in range(qnt):
    dic = {}
    dic['nome'] = input(f"Contato {i+1} - Nome: ")
    dic['telefone'] = input(f"Contato {i+1} - Telefone: ")
    contatos.append(dic)

print("\nNomes cadastrados:")
for c in contatos:
    print("-", c['nome'])

# Nomes sem repetição
nomes = set()
for c in contatos:
    nomes.add(c['nome'])

print("\nNomes (sem repetição):")
for n in nomes:
    print("-", n)

# Buscar telefone
nome_busca = input("\nDigite um nome para buscar o telefone: ")
for c in contatos:
    if c['nome'] == nome_busca:
        print(f"Telefone de {nome_busca}: {c['telefone']}")
        break

# Alterar telefone
nome_alterar = input("\nDigite um nome para alterar o telefone (ou deixe vazio para pular): ")
if nome_alterar != "":
    novo_tel = input("Novo telefone: ")
    for c in contatos:
        if c['nome'] == nome_alterar:
            c['telefone'] = novo_tel
            print("Telefone alterado.")
            break

# Remover contato
nome_remover = input("\nDigite um nome para remover (ou deixe vazio para pular): ")
if nome_remover != "":
    for c in contatos:
        if c['nome'] == nome_remover:
            contatos.remove(c)
            print("Contato removido.")
            break

# Lista final
print("\nLista final de contatos:")
for c in contatos:
    print(f"- {c['nome']}: {c['telefone']}")
