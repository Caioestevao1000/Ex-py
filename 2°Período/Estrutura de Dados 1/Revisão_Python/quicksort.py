def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    pivo = lista[meio]
    print(pivo)

    restante = lista[:meio] + lista[meio+1:]

    menores = [x for x in restante if x <= pivo]
    maiores = [x for x in restante if x > pivo]
    
    return quicksort(menores) + [pivo] + quicksort(maiores)
                                                              
print(quicksort([9, 7, 5, 10, 22, 22, 10, 11, 2, 3]))

