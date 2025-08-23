print("\n## Sistema de Classificação de Risco de Investimento ##")

idade = int(input("Digite a Sua Idade:"))
renda = float(input("Digite a Renda Mensal:"))
dividas = float(input("Digite o Números de Dívidas nos Últimos 2 anos:"))

pagamento_dividas = 0

if dividas > 0:
    pagamento_dividas = float(input("Digite o valor total da(s) dívida(s) R$:"))

pontuação = (renda / 1000) - (pagamento_dividas / 2000) + (idade / 2)

if idade >= 30 and idade <= 50 and renda > 10000 and dividas == 0:
    risco = 'Categoria Inicial de Risco: Baixo Risco!'
elif idade >= 25 and idade <= 60 and renda >= 5000 and renda <= 10000 and pagamento_dividas < 5000:
    risco = 'Categoria Inicial de Risco: Médio Risco!'
else:   
    risco = 'Categoria Inicial de Risco: Alto Risco!'

print("\n",risco, "\nSua Pontuação é de:",pontuação )

if pontuação > 80 and risco == 'Categoria Inicial de Risco: Médio Risco!':
    print("Categoria de Risco Ajustada para Baixo Risco!")
elif pontuação > 80 and risco == 'Categoria Inicial de Risco: Alto Risco!':
    print("Categoria de Risco Ajustada para Médio Risco!")
else: 
    print("Sem Alteração na sua Classificação")

input("\nPressione Enter para sair...")
