import math

print("===== 1. NÚMEROS NATURAIS =====")

# 1.1 Número mínimo de bits
registros = int(input("1.1 -> Quantos registros o sistema precisa armazenar? "))
bits = math.ceil(math.log2(registros))
print(f"Número mínimo de bits necessários: {bits}")

# 1.2 Número total de arquivos
n = int(input("\n1.2 -> Informe o número de pastas (n): "))
total_arquivos = sum(range(1, n+1)) * n
print(f"Número total de arquivos possíveis: {total_arquivos}")

# 1.3 Senhas de 4 dígitos
print("\n1.3 -> Senhas de 4 dígitos (0 a 9)")
senhas_com_repeticao = 10**4
senhas_sem_repeticao = math.perm(10, 4)
print(f"Com repetição: {senhas_com_repeticao} | Sem repetição: {senhas_sem_repeticao}")