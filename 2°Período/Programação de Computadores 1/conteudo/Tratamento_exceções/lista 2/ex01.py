def definir_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser menor que zero")
    return idade

try:
    idade = int(input("Idade"))
    print(definir_idade(idade))
except ValueError as e:
    print('Erro:', e)