print("\n===== 2. INDUÇÃO MATEMÁTICA =====")

def soma_recursiva(n):
    if n == 1:
        return 1
    return n + soma_recursiva(n - 1)

def soma_fechada(n):
    return n * (n + 1) // 2

n = int(input("2.3 -> Informe um número natural n: "))
print(f"Soma recursiva = {soma_recursiva(n)}")
print(f"Soma pela fórmula fechada = {soma_fechada(n)}")