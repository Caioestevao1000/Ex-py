print("\n===== 5. RECORRÊNCIAS =====")

def cache(n):
    if n == 0:
        return 0
    return 2 * cache(n-1) + 1

n = int(input("5.2 -> Informe n para calcular Cn (C0 = 0): "))
print(f"C{n} = {cache(n)}")

def T(n):
    if n == 1:
        return 1
    return T(n-1) + 3*n

n = int(input("\n5.3 -> Informe n para calcular T(n): "))
print(f"T({n}) = {T(n)}")

print("\n=== FIM DOS EXERCÍCIOS ===")
