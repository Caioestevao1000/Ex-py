def carregarLista():
    lista = []
    while True:
        nums = int(input())
        if nums == 0:
            break
        else:
            lista.append(nums)
    print(f"Os elementos da lista são: {lista}")
    return lista


def soma_lista(lista):
    soma_todos = 0
    for i in lista:
        soma_todos += i
    print(f"A soma desses elementos é: {soma_todos}")
    

soma = carregarLista()
soma_lista(soma)
