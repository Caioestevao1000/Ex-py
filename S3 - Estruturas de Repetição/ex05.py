print("\n## Correspondência de Bônus Especial ##")

for i in range(15):
    nome = str(input("\nDigite o Nome do Cliente:"))
    valor = float(input("Digite o Valor das Compras do Ano Passado:"))

    if valor < 1000:
        bonus = valor * 0.10
        print(f"\nSr(a). {nome}, você recebeu um bônus de 10%: R$ {bonus:.2f}")
    else: 
        bonus = valor * 0.15
        print(f"\nSr(a). {nome}, você recebeu um bônus de 15%: R$ {bonus:.2f}")

input("Pressione Enter para Sair...")