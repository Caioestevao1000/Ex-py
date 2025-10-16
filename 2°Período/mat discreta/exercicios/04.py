print("\n===== 4. PROGRESSÕES ARITMÉTICAS E GEOMÉTRICAS =====")

# 4.1 PA
a1 = int(input("4.1 -> Primeiro termo da PA: "))
r = int(input("Razão da PA: "))
n = int(input("Número de termos (dias): "))
soma_pa = n/2 * (2*a1 + (n-1)*r)
print(f"Soma total da PA: {int(soma_pa)}")

# 4.2 PG
a1 = float(input("\n4.2 -> Primeiro termo da PG: "))
q = float(input("Razão (ex: 2 para dobrar): "))
n = int(input("Número de termos (meses): "))
a_n = a1 * q**(n-1)
print(f"Último termo da PG após {n} meses: {a_n}")

# 4.3 Funções genéricas
def termo_pa(a1, r, n):
    return a1 + (n-1)*r

def soma_pa_func(a1, r, n):
    return n/2 * (2*a1 + (n-1)*r)

def termo_pg(a1, q, n):
    return a1 * q**(n-1)

def soma_pg_func(a1, q, n):
    return a1 * ((q**n - 1) / (q - 1))

print("\n4.3 -> Teste funções PA e PG")
a1 = float(input("Primeiro termo: "))
r = float(input("Razão (para PA) ou razão de crescimento (para PG): "))
n = int(input("Número de termos: "))

print(f"PA -> n-ésimo termo: {termo_pa(a1, r, n)} | Soma dos n primeiros termos: {soma_pa_func(a1, r, n)}")
print(f"PG -> n-ésimo termo: {termo_pg(a1, r, n)} | Soma dos n primeiros termos: {soma_pg_func(a1, r, n)}")
