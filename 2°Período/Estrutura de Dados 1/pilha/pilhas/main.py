from pilha import Pilha

def showMenu():
    print("1 - Visitar página")
    print("2 - Voltar")
    print("3 - Avançar")
    print("4 - Mostrar as pilhas")

def goToPage(undo, redo):
    url = input("Digite a URL: ")

    undo.push(url)
    print(f"Acessando o site: {url}")

    while not redo.isEmpty():
        redo.pop()

def showStack(undo, redo):
    print(undo)
    print(redo)

def goBack(undo, redo):
    if undo.size() > 1:
        pagina = undo.pop()
        redo.push(pagina)
        print(f"Voltando para a página {undo.top()}")
    else:
        print("Não há mais páginas para retornar")

def goForward(undo, redo):
    if redo.size() > 0:
        pagina = redo.pop()
        undo.push(pagina)
        print(f"Avançando para a página {pagina}")
    else:
        print("Não há página para avançar")

if __name__ == "__main__":
    
    undo = Pilha()
    redo = Pilha()

    while True:
        showMenu()
        opcao = int(input("Digite uma opção: "))

        match opcao:
            case 1:
                goToPage(undo, redo)
            case 2:
                goBack(undo, redo)
            case 3:
                goForward(undo, redo)
            case 4:
                showStack(undo, redo)