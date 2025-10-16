linha_1 = input("Linha 1:")
linha_2 = input("Linha 2:")

conjunto1 = set(linha_1.split())
conjunto2 = set(linha_2.split())

uniao = conjunto1 | conjunto2
print(uniao)

exclusiva1 = conjunto1 - conjunto2
print(exclusiva1)

exclusiva2 = conjunto2 - conjunto1
print(exclusiva2)