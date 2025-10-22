# Enunciado

# Implemente um sistema de vendas com exceções personalizadas para erros de negócio.

# Exceções personalizadas (mínimo)

#     ProdutoInexistenteError
#     QuantidadeInvalidaError
#     EstoqueInsuficienteError

# O que o sistema deve fazer

#     Manter um catálogo com preço e estoque por produto.
#     Ler um pedido com itens (cada item tem nome do produto e quantidade).
#     Validar e lançar exceções apropriadas quando ocorrer:
#         produto inexistente;
#         quantidade não positiva;
#         quantidade acima do estoque disponível.
#     Atomicidade: se qualquer item for inválido, nenhum estoque é alterado.
#     Sem erros: debitar estoques e exibir o total (2 casas) + o estoque final por produto (ordem livre).
#     Mensagens de erro: uma linha, claras e específicas.

# Funções obrigatórias (contrato)

# validar_item(nome, qtd, catalogo) -> None: lança as exceções conforme o caso; não altera o catálogo.

# registrar_pedido(itens, catalogo) -> float: valida todos os itens (propaga exceção se falhar), debita estoques apenas se tudo válido e retorna o total.

# Entrada (formato)

#     Um inteiro p (≥ 2).
#     Para cada produto: nome (sem espaços), preco (float ≥ 0), estoque_inicial (int ≥ 0).
#     Depois, itens do pedido até o usuário digitar fim no nome: para cada item, nome e qtd.

# Saída (comportamento esperado)

#     Com erro: apenas a mensagem da exceção correspondente; estoque inalterado.
#     Sem erro:

#     Total: R$ x.xx
#     Estoque atualizado
#     <nome> → <estoque>
#     <nome> → <estoque>
#     ...

# Execução simulada

# Caso A — Sucesso

# Quantos produtos no catálogo (p ≥ 2)? 3

# --- Produto #1 ---
# Nome do produto (sem espaços): arroz
# Preço (float ≥ 0): 20
# Estoque inicial (int ≥ 0): 10

# --- Produto #2 ---
# Nome do produto (sem espaços): feijao
# Preço (float ≥ 0): 8.5
# Estoque inicial (int ≥ 0): 5

# --- Produto #3 ---
# Nome do produto (sem espaços): macarrao
# Preço (float ≥ 0): 6
# Estoque inicial (int ≥ 0): 12

# Digite os itens do pedido. Para encerrar, digite 'fim' no nome.
# Nome do produto: arroz
# Quantidade: 2
# Nome do produto: feijao
# Quantidade: 3
# Nome do produto: fim

# Total: R$ 65.50
# Estoque atualizado
# arroz → 8
# feijao → 2
# macarrao → 12

# Caso B — Erro (estoque insuficiente, nada é alterado)

# Quantos produtos no catálogo (p ≥ 2)? 2

# --- Produto #1 ---
# Nome do produto (sem espaços): notebook
# Preço (float ≥ 0): 2500
# Estoque inicial (int ≥ 0): 1

# --- Produto #2 ---
# Nome do produto (sem espaços): mouse
# Preço (float ≥ 0): 80
# Estoque inicial (int ≥ 0): 10

# Digite os itens do pedido. Para encerrar, digite 'fim' no nome.
# Nome do produto: notebook
# Quantidade: 2
# Nome do produto: fim

# Estoque insuficiente


class ProdutoInexistenteError(Exception):
    pass

class QuantidadeInvalidaError(Exception):
    pass

class EstoqueInsuficienteError(Exception):
    pass


def validar_item(nome, qtd, catalogo):
    if nome not in catalogo:
        raise ProdutoInexistenteError("Produto inexistente")
    if qtd <= 0:
        raise QuantidadeInvalidaError("Quantidade inválida")
    if qtd > catalogo[nome]["estoque"]:
        raise EstoqueInsuficienteError("Estoque insuficeinte")


def registrar_pedido(itens, catalogo):
    total = 0.0

    for item in itens:
        nome = item[0]
        qtd = item[1]
        validar_item(nome, qtd, catalogo)

    for item in itens:
        nome = item[0]
        qtd = item[1]
        preco = catalogo[nome]["preco"]
        catalogo[nome]["estoque"] = catalogo[nome]["estoque"] - qtd
        total = total + (preco * qtd)

    return total


def sistemas():
    p = int(input("Quantos produtos no catalogo (p ≥ 2)? "))

    catalogo = {}

    for i in range(p):
        print(f"\n-- Produto {i + 1} --")
        nome = input("Nome do produto (sem espaços): ")
        preco = float(input("Preço (float ≥ 0): "))
        estoque = int(input("Estoque inicial (int ≥ 0): "))
        catalogo[nome] = {"preco": preco, "estoque": estoque}

    print("\nDigite os itens do pedido. Para encerrar, digite 'fim' no nome.")
    itens = []

    while True:
        nome = input("Nome do produto: ")
        if nome.lower() == "fim":
            break
        qtd = int(input("Quantidade: "))
        itens.append((nome, qtd))

    try:
        total = registrar_pedido(itens, catalogo)
        print(f"\nTotal: R$ {total:.2f}")
        print("Estoque atualizado")
        for nome in catalogo:
            estoque_atual = catalogo[nome]["estoque"]
            print(f"{nome} → {estoque_atual}")
    except (ProdutoInexistenteError, QuantidadeInvalidaError, EstoqueInsuficienteError) as e:
        print(e)

print(sistemas())
