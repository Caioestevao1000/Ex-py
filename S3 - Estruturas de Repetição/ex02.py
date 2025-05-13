print("\n## Soma das Frações ##")

n = int(input("Digite um número inteiro positivo:"))
soma = 1 

for i in range(2, n + 1):
    soma += 1 / i
    print(f"Soma até 1/{i}: {soma:.2f}")

print(f"\nSoma total S = {soma:.3f}")
input("Pressione Enter para sair...")
