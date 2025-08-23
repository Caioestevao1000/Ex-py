print("\n## Aprovação de Crédito ##")

idade = float(input("Digite a Sua Idade:"))
renda = float(input("Digite a Renda Mensal:"))
dividas = float(input("Digite o Total de Suas Dívidas Pendentes em R$:"))
pagamentos = int(input("Digite o Total de Pagamentos Realizados nos Últimos 6 Meses:"))

limite_divida= renda * 0.2

if idade >= 25 and idade <= 60 and renda >= 3000 and dividas == 0:
    print("Crédito Aprovado!")
elif idade >= 25 and idade <= 60 and renda >= 3000 and dividas <= limite_divida and pagamentos >= 2:
    print("Crédito Aprovado.")
else:   
    print("## Crédito Não Aprovado ##")

input("\nPressione Enter para sair...")
