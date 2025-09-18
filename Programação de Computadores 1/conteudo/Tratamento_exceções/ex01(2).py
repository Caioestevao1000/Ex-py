try:
    total_compra = float(input("Digite o valor total (R$):"))
    itens = int(input("Digite a quantidade de itens:"))
    preço_unitario = total_compra // itens
    print(f"Preço unitário: R$ {preço_unitario}")

except ZeroDivisionError:
    print("Erro: divisor não pode ser zero")
except ValueError:
    print("Erro: Não pode ser vazio")
except TypeError:
    print("Tipo errado de Dado")
