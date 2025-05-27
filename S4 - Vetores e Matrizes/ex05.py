print("\n## Total de Vendas ##")

nome=[]
total=[]
percentual=[]
comissao=[]

totalvendas = 0

for i in range(10):
    nome.append(str(input("\nDigite Seu Nome:")))
    total.append(float(input("Digite o Total de VendasR$:")))
    percentual.append(float(input("Digite o Percentual da Sua Comissão:")))
    comissao.append((total[i]/100) * percentual[i])

#colocando em ordem crescente a comissao o nome segue também
for i in range(9):
    for j in range(9 - i):
        if comissao[j] > comissao[j + 1]:
            comissao[j], comissao[j + 1] = comissao[j + 1], comissao[j]
            nome[j], nome[j + 1] = nome[j + 1], nome[j]
else:
    print(f"\nO Menor Valor de Comissão Será de {nome[0]} Receberá R${comissao[0]}")
    print(f"O Maior Valor de Comissão Será de {nome[9]} Receberá R${comissao[9]}")

#Total das Vendas
for i in range(len(total)):
    totalvendas += total[i]
    print('-' * 60)
    print(f" O Vendedor:{nome[i]} Receberá R${comissao[i]:.2f}")
print(f"Total de Vendas: {totalvendas:.2f}")