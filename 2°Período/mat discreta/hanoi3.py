# Atividade 3 – Torre de Hanói com 4 hastes
# Disciplina: Matemática Discreta
# Alunos: Victor Hugo M. Fernandes e Caio Estevão

# Função auxiliar para resolver o caso clássico (3 hastes)
def hanoi_3(n, origem, destino, auxiliar, movimentos):
    if n == 1:
        movimentos.append((origem, destino))
    else:
        hanoi_3(n - 1, origem, auxiliar, destino, movimentos)
        movimentos.append((origem, destino))
        hanoi_3(n - 1, auxiliar, destino, origem, movimentos)

# Função principal para o caso de 4 hastes (algoritmo Frame-Stewart)
def hanoi_4(n, origem, destino, aux1, aux2, movimentos):
    if n == 0:
        return
    elif n == 1:
        movimentos.append((origem, destino))
    else:
        # Escolhe k de forma aproximada (ótimo prático)
        k = n - int((2 * n + 1) ** 0.5) + 1

        # Etapa 1: mover k discos para a primeira haste auxiliar (usando 4 hastes)
        hanoi_4(k, origem, aux1, aux2, destino, movimentos)

        # Etapa 2: mover os n−k discos restantes para o destino (usando 3 hastes)
        hanoi_3(n - k, origem, destino, aux2, movimentos)

        # Etapa 3: mover os k discos da auxiliar para o destino (usando 4 hastes)
        hanoi_4(k, aux1, destino, origem, aux2, movimentos)

def nDiscos():  # Função para ler e validar a entrada do usuário
    while True:
        try:
            n = int(input("Digite o número de discos (inteiro >= 1): "))
            if n < 1:
                print("Erro: o número de discos deve ser pelo menos 1. Tente novamente.")
                continue
            return n
        except ValueError:
            print("Erro: entrada inválida. Por favor, digite um número inteiro.")

def main():  # Função principal
    print("======== Torre de Hanói com 4 Hastes ========")
    n = nDiscos()
    movimentos = []
    print(f"\nMovendo {n} discos da torre A para a torre D (usando B e C como auxiliares):\n")

    hanoi_4(n, "A", "D", "B", "C", movimentos)

    for i, (origem, destino) in enumerate(movimentos, start=1):
        print(f"Movimento {i}: {origem} → {destino}")

    print(f"\nNúmero mínimo de movimentos necessários: {len(movimentos)}")

if __name__ == "__main__":
    main()
