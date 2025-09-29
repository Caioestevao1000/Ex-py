# conjunto = set()
# numeros = input("Digite um conjunto de números, ex:(1 2 3 4 5): ")
# numero = numeros.split()
# for n in numero:
#     conjunto.add(int(n))
# print("Quantidade de valores distintos:", len(conjunto))

numeros = input("Digite os números separados por espaço: ").split()
conjunto = set(map(int, numeros))
print("Quantidade de valores distintos:", len(conjunto))
