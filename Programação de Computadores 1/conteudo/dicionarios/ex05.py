dicionario = {"a": 5, "b": 7, "c": 3}
soma = 0

for i in dicionario.items():
    soma = soma + i

print(f"A soma do dicionário {dicionario} é {soma}")