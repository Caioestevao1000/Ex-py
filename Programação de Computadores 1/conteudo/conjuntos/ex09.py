conjunto_1 = set(str(input("Digite os Códigos dessa lista 1:")).split())
conjunto_2 = set(str(input("Digite os Códigos dessa lista 2:")).split())
conjunto_3 = set(str(input("Digite os Códigos dessa lista 3:")).split())


uniao = conjunto_1 | conjunto_2 | conjunto_3
inter_12 = conjunto_1 & conjunto_2 & conjunto_3

print("Pelo meons uma: ",uniao)
print("Todos: ",inter_12)