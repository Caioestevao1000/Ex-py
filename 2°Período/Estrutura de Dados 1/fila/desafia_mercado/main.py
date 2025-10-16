from unittest import case
from fila import Fila

def showMenu():
    print("1 Adiciona pessoas na fila")
    print("2 Atender pessoas da fila")
    print("3 Verificar tamanho da fila")
    print("4 Mostrar fila")
    print("5 Finalizar atendimento do caixa normal")
    print("6 Finalizar atendimento do caixa prioritário")
    print("7 Sair")

def entrarNaFila(fila):
    nome = input("Digite o nome da pessoa: ")
    fila.enqueue(nome)
    print(f"{nome} entrou na fila.")

def showQtde(fila):
    print(f"Tamanho da fila: {fila.size()}")

def showFila(fila):
    print(f"Fila atual: {fila}")

def atenderFila(fila):
    if not fila.is_empty():
        print(f"{fila.dequeue()} foi atendido.")
    else:
        print("Fila vazia, ninguém para atender.")

if __name__ == "__main__":
    
    fila_convencional = Fila() #instancia da Fila e ele se torna um objeto
    fila_preferencial = Fila()
    while True:
        showMenu()
        opcao = int(input("Digite a opção desejada: "))
        
        match opcao:
            case 1:
                entrarNaFila(fila_convencional, fila_preferencial)
            case 2:
                atenderFila(fila)
            case 3:
                showQtde(fila)
            case 4:
                showFila(fila)
            case 5:
                break


# desafio implementar como se fosse dois caixas
# fila prioritária e normal
# se caixa normal estiver vazio, atender prioritária
# se caixa prioritária não tiver ninguém, atender normal
