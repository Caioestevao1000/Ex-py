print("\n## Sistema de Classificação de Risco de Investimento ##")

idade = int(input("Digite a Sua Idade:"))
renda = float(input("Digite a Renda Mensal:"))
dividas = float(input("Digite o Números de Dívidas nos Últimos 2 anos:"))

if idade >= 25 and idade <= 60 and renda >= 3000 and dividas == 0:
    print("Baixo Risco!")
elif idade >= 25 and idade <= 60 and renda >= 3000 and dividas <= limite_divida and pagamentos >= 2:
    print("Crédito Aprovado.")
else:   
    print("## Crédito Não Aprovado ##")

input("\nPressione Enter para sair...")
