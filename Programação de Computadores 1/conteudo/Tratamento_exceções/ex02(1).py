try:
    list = ["arroz", "feijão", "macarrão", "óleo"]
    indice = int(input("Digite o índice do item:"))

    print("Item selecionado;", list[indice])
except ValueError:
    print("Erro: Não pode ser vazio")
except TypeError:
    print("Tipo errado de entrada deve ser um número") #não está funcionando
except IndexError:
    print("índice da Lista não existe")