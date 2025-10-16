# Atividade 1 – Torre de Hanói (3 hastes)
# Disciplina: Matemática Discreta
# Alunos: Victor Hugo M. Fernandes e Caio Estevão

#Função hanoi
def hanoi(n, origem, destino, auxiliar):
   
    movimentos = 0  #Inicializa o contador de movimentos
   
    if n == 1:
        #Caso base: mover um único disco diretamente
        print(f"Mova disco 1 de {origem} para {destino}")
       
        movimentos += 1     #Incrementa no contador
    else:
        #Passo 1: mover n-1 discos da origem para o auxiliar
        #Soma os movimentos da chamada recursiva
        movimentos += hanoi(n - 1, origem, auxiliar, destino)
       
        #Passo 2: mover o disco restante para o destino
        print(f"Mova disco {n} de {origem} para {destino}")
       
        movimentos += 1 #Incrementa
       
        #Passo 3: mover os n-1 discos do auxiliar para o destino
        #Soma os movimentos da chamada recursiva
        movimentos += hanoi(n - 1, auxiliar, destino, origem)
       
    return movimentos   #Retorna o total de movimentos mínimos realizados

def nDiscos():  #Função para ler e validar a entrada do usuário
    while True:
        try:
            n = int(input("Digite o número de discos (inteiro >= 1): "))
            if n < 1:   #Número inválido
                print("Erro: o número de discos deve ser pelo menos 1. Tente novamente.")
                continue
            return n  
        except ValueError:  #Entrada inválida
            print("Erro: entrada inválida. Por favor, digite um número inteiro.")


def main(): #Função principal
    print("======== Torres de Hanoi ========")
   
    n = nDiscos()   #Lê o número de discos do usuário
    print(f"\nMovendo {n} discos da torre A para a torre C (usando B como auxiliar):\n")
   
    movimentos_minimos = hanoi(n, "A", "C", "B")    #Chama a função e armazena o retorno


    #Exibe a quantidade mínima de movimentos
    print(f"\nNúmero mínimo de movimentos necessários: {movimentos_minimos}")


if __name__ == "__main__":  #Executa o programa
    main()
