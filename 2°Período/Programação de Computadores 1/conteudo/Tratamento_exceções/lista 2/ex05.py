class FilaVaziaError(Exception):
    pass

def entrar(fila, nome):
    if nome == '':
        raise ValueError("Nome não pode ser Vazio")
    else: 
        fila.append(nome)

def chamar(fila):
    if not fila:
        raise FilaVaziaError("Lista não pode ser vazia")
    return fila.pop(0)

try:
    lista_fila = []

    nome = input("Digite um nome:")
    entrar(lista_fila, nome)

    print(chamar(lista_fila))

except FilaVaziaError as e:
    print("Erro:", e)

except ValueError as e:
    print("Erro:", e)