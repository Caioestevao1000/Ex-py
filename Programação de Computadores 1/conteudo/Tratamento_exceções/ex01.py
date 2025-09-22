try:
    total_compra = float(input("Digite o valor total (R$):"))
    itens = int(input("Digite a quantidade de itens:"))
    preço_unitario = total_compra // itens
    if itens < 0 or total_compra < 0:
        print("Erro: Valores não podem ser negativos ou zero")
    else: 
        print(f"Preço unitário: R$ {preço_unitario}")
except ZeroDivisionError:
    print("Erro: divisor não pode ser zero")
except ValueError:
    print("Erro: digite números inteiro eválidos")


