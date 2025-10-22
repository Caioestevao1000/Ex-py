# Enunciado

# Vamos organizar cursos e suas “tags” usando dicionários e conjuntos.
# Primeiro, você informa quantos cursos vai cadastrar (n). Depois, para cada curso, digite, um por linha: o nome do curso (sem espaços), a carga horária (maior que zero), o preço (maior ou igual a 0), o número de tags desse curso (t) e, em seguida, t linhas com uma tag por linha (pode já digitar em minúsculas).

# Com esses dados em mãos, faça:

#     Mostre todas as tags distintas encontradas (a união das tags de todos os cursos).
#     Monte e exiba o mapa tag → quantidade de cursos em que a tag aparece.
#     Mostre o curso mais caro e o curso mais barato nos formatos:
#     Mais caro: <nome> (R$ x.xx)
#     Mais barato: <nome> (R$ x.xx)

# Observação:
# • Não precisa validar a entrada (assuma que vem tudo no formato certo).

# Execução simulada

# Quantos cursos serão cadastrados? 3

# --- Curso #1 ---
# Nome do curso: PythonBasico
# Carga horária: 40
# Preço: 299.9
# Quantas tags este curso terá? 3
# Tag #1: python
# Tag #2: iniciante
# Tag #3: dados

# --- Curso #2 ---
# Nome do curso: JavaPOO
# Carga horária: 60
# Preço: 450.0
# Quantas tags este curso terá? 2
# Tag #1: java
# Tag #2: poo

# --- Curso #3 ---
# Nome do curso: AnaliseDados
# Carga horária: 30
# Preço: 350.0
# Quantas tags este curso terá? 2
# Tag #1: dados
# Tag #2: pandas

# Tags distintas:
# python
# iniciante
# dados
# java
# poo
# pandas

# Tag -> quantidade de cursos:
# python -> 1
# iniciante -> 1
# dados -> 2
# java -> 1
# poo -> 1
# pandas -> 1

# Mais caro: JavaPOO (R$ 450.00)
# Mais barato: PythonBasico (R$ 299.90)


class ProdutoInexistenteError(Exception):
    pass

class QuantidadeInvalidaError(Exception):
    pass

class EstoqueInsuficienteError(Exception):
    pass


def validar_item(nome, qtd, catalogo):
    if nome not in catalogo:
        raise ProdutoInexistenteError("Produto ineixstente")
    if qtd <= 0:
        raise QuantidadeInvalidaError("Quantidade inválida")
    if qtd > catalogo[nome]["estoque"]:
        raise EstoqueInsuficienteError("Estoque insuficiente")


def registrar_pedido(itens, catalogo):
    total = 0.0

    for nome, qtd in itens:
        validar_item(nome, qtd, catalogo)

    for nome, qtd in itens:
        catalogo[nome]["estoque"] -= qtd
        total += catalogo[nome]["preco"] * qtd

    return total


def sistema():
    p = int(input("Quantos produtos no catálogo (p ≥ 2)? "))

    catalogo = {}
    for i in range(p):
        print(f"\n-- Produto #{i + 1} --")
        nome = input("Nome do produto (sem espaços): ")
        preco = float(input("Preço (float ≥ 0): "))
        estoque = int(input("Estoque inicial (int ≥ 0): "))
        catalogo[nome] = {"preco": preco, "estoque": estoque}

    print("\nDigite os itens do pedido. Para encerar, digite 'fim' no nome.")

    itens = []
    while True:
        nome = input("Nome do produto: ")
        if nome.lower() == "fim":
            break
        qtd = int(input("Quantidade: "))
        itens.append((nome, qtd))

    try:
        total = registrar_pedido(itens, catalogo)
        print(f"\nTotal: R${total:.2f}")
        print("Estoque atualizado")
        for nome, dados in catalogo.items():
            print(f"{nome} -> {dados['estoque']}")
    except (ProdutoInexistenteError, QuantidadeInvalidaError, EstoqueInsuficienteError) as e:
        print(e)


print(sistema())
