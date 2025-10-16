#Função hanoi2 (regra obrigatória: O -> A -> D)
def hanoi2(n, origem, destino, auxiliar):
   
    movimentos = 0  #Inicializa o contador de movimentos
   
    if n == 1:
        #Caso base: um disco deve ser movido em dois passos (O -> A e A -> D)
        print(f"Mova disco 1 de {origem} para {auxiliar}")
        print(f"Mova disco 1 de {auxiliar} para {destino}")
       
        movimentos += 2  #Incrementa no contador (M(1) = 2)
        return movimentos
   
    else:
        #Passo 1: Mover n-1 discos de O para D (usando A)
        #Soma os movimentos da chamada recursiva
        movimentos += hanoi2(n - 1, origem, destino, auxiliar)
       
        #Passo 2: Mover o disco n de O para A
        print(f"Mova disco {n} de {origem} para {auxiliar}")
       
        movimentos += 1 #Incrementa
       
        #Passo 3: Mover n-1 discos de D para O (usando A)
        movimentos += hanoi2(n - 1, destino, origem, auxiliar)
       
        #Passo 4: Mover o disco n de A para D
        print(f"Mova disco {n} de {auxiliar} para {destino}")
       
        movimentos += 1 #Incrementa
        #Passo 5: Mover n-1 discos de O para D (usando A)

        movimentos += hanoi2(n - 1, origem, destino, auxiliar)
    return movimentos  #Retorna o total de movimentos mínimos realizados


def nDiscos():  #Função para ler e validar a entrada do usuário
    while True:
        try:
            n = int(input("Digite o número de discos (inteiro >= 1): "))
            if n < 1:   #Número inválido
                print("Erro: o número de discos deve ser pelo menos 1. Tente novamente.")
                continue
            return n  
        except ValueError:  #Entrada não é um número inteiro
            print("Erro: entrada inválida. Por favor, digite um número inteiro.")


def main(): #Função principal
    print("======== Torres de Hanoi - Movimento Obrigatório ========")
   
    n = nDiscos()   #Lê o número de discos do usuário
    print(f"\nMovendo {n} discos da torre A para a torre C (usando B como auxiliar):\n")
   
    movimentos_minimos = hanoi2(n, "A", "C", "B")    #Chama a função e armazena o retorno
    #Exibe a quantidade mínima de movimentos
    print(f"\nNúmero mínimo de movimentos necessários: {movimentos_minimos}")
if __name__ == "__main__":  #Executa o programa
    main()
