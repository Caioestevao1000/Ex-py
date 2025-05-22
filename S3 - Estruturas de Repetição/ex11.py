print("\n### Simulador de Pagamento de Carro ###")

valor_carro = float(input("Digite o Valor do Carro:"))

valor_vista = valor_carro * 0.8
print(f"\nValor do Carro à Vista com 20% de Desconto é: {valor_vista:.2f}")

parcelas_acrescimos = {
    6: 3,
    12: 6,
    18: 9,
    24: 12,
    30: 15,
    36: 18,
    42: 21,
    48: 24,
    54: 27,
    60: 30
}

# Cabeçalho da tabela
print(f"{'Parcelas':<10} {'% Acréscimo':<15} {'Preço Final (R$)':<20} {'Valor da Parcela (R$)'}")
print("-" * 65)

for parcelas, percentual in parcelas_acrescimos.items():
    preco_final = valor_carro * (1 + percentual / 100)
    valor_parcela = preco_final / parcelas
    print(f"{parcelas:<10} {percentual:<15}% {preco_final:<20.2f} {valor_parcela:.2f}")

