numeros = 1 ,2 ,2 ,2 ,2 ,2 ,2 ,3 ,4 ,5 ,5 ,8 ,8 ,9 ,9 ,9 ,9 ,10
qtd = 0
n = int(input("Escolha um Número de 1 a 10:"))

for i in range(len(numeros)):
    if numeros[i] == n:
        qtd += 1
    else:
        print("ERRO")
    
print("A Tupla há esses elementos:", numeros)
print(f"O número {n} aparece {qtd} vez")