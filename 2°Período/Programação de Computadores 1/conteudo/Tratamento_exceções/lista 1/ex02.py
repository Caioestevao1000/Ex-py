try:
    list = ["arroz", "feijão", "macarrão", "óleo"]
    indice = int(input("Digite o índice do item:"))

    print("Item selecionado:", list[indice])
except ValueError:
    print("Erro: você digitou um valor que não é número inteiro")
except IndexError:
    print("índice da Lista não existe")