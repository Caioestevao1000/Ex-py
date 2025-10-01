def ler_dicionario():
    entrada = input("Digite os pares (ex: a:1, b:2): ")
    dicionario = {}
    pares = entrada.split(",")

    for par in pares:
        chave, valor = par.split(":")
        chave = chave.strip()
        valor = valor.strip()

        if valor.isdigit():
            valor = int(valor)

        dicionario[chave] = valor

    return dicionario


print("Primeiro dicionário")
d1 = ler_dicionario()

print("Segundo dicionário")
d2 = ler_dicionario()

d1.update(d2)

print("Resultado final:")
print(d1)
