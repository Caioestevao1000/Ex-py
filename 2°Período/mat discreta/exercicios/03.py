print("\n===== 3. FUNÇÕES =====")

def gerar_mapeamento(usuarios):
    return {usuario: i+1 for i, usuario in enumerate(usuarios)}

qtd = int(input("3.3 -> Quantos usuários deseja cadastrar? "))
usuarios = []
for i in range(qtd):
    nome = input(f"Nome do usuário {i+1}: ")
    usuarios.append(nome)

mapeamento = gerar_mapeamento(usuarios)
print("Mapeamento de usuários para IDs únicos:")
for nome, id_ in mapeamento.items():
    print(f"{nome} -> {id_}")