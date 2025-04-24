print("\n## Crédito Especial ##")

saldo = float(input("Digite seu saldo médio do último ano:"))

if saldo > 400:
    credito = saldo * 0.30
elif saldo >= 400 and saldo > 300:
    credito = saldo * 0.25
elif saldo > 200 and saldo <= 300:
    credito = saldo * 0.20
elif saldo <= 200:
    credito = saldo * 0.10

print(f"\nO seu saldo médio anual é de R$ {saldo:.2f}")
print(f"Você receberá de crédito especial: R$ {credito:.2f}")

input("\nPressione Enter para sair...")