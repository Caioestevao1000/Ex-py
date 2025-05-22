print("\n## Transações ##")

preco = 0
prazo = 0 
vista = 0

for i in range(15):
    print("\nCódigo V para transação à Vista e P para Transação a Prazo.")
    codigo = str(input("Digite o Código:"))
    preco = float(input("Digite o valor total a ser pago: R$"))#erro aqui
    if codigo == "v" or codigo == "V" :
        vista += preco
        print(f" Valor total das compras feito a vista é R${vista}")
    elif codigo == "p" or codigo == "P":
         prazo += preco
         parcelamento = preco / 3
         print(f" Valor total da compras feito a prazo é R${prazo}")
         print(f" Valor da primeira parcela da compra R${parcelamento}")
else:
    total=vista+prazo
    parcelamento = prazo / 3
    print(f"O Valor Total das Transações é: R${total}")
    print(f"Primeira parcela a ser paga é de: R${parcelamento}3x")


input("Pressione Enter para Sair...")