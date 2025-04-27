print("\n## Investimento ##")

print("\tTipo\t\tDescrição\t\t\tRendimento mensal")
print("\t 1\t\t Poupança\t\t\t\t3%")
print("\t 2\t\t Fundos de renda fixa\t\t\t4%")
print("\t 3\t\t Fundos de renda variável\t\t5%")

invest = int(input("\nQual o Tipo de investimento desejado?: "))
valor = float(input("A quantidade de dinheiro que deseja investir: R$"))

if invest == 1:
    tipo = 'Poupança'
    valor = valor + valor * 0.03
    print(f"\nO Investimento de {tipo} mais o valor de aplicação fica no Total de: R${valor:.2f}")
elif invest == 2:
    tipo = 'Fundos de renda fixa'
    valor = valor + valor * 0.04
    print(f"\nO Investimento de {tipo} mais o valor de aplicação fica no Total de: R${valor:.2f}")
elif invest == 3:
    tipo = 'Fundos de renda variável'
    valor = valor + valor * 0.05
    print(f"\nO Investimento de {tipo} mais o valor de aplicação fica no Total de: R${valor:.2f}")
else:
    print("\n#### Número Inválido: Digite de acordo com as opções de 1 a 3. ####")

input("\nPressione Enter para sair...")
