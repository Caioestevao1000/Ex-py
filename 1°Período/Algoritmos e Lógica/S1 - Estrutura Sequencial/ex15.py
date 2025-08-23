print("## Conversor de Moedas ##")
print("## Real para Dólar, Marco Alemão e Libra Esterlina ##")

real = float(input("Digite a quantia em real que você deseja converter: "))

dolar = real / 5.70  
libra = real / 7.35
marco = real / 3.16

print(f"\nVocê receberá em Dólar: US$ {dolar:.2f}")
print(f"Você receberá em Marco Alemão: DM {marco:.2f}")
print(f"Você receberá em Libra Esterlina: £ {libra:.2f}")

input("\nPressione Enter para sair...")