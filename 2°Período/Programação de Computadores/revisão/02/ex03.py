def soma_entre(x, y):
    soma = 0
    if x <= y:
        for i in range(x, y+1):
            soma += i
    else:
        for i in range(y, x+1):
            soma += i
    return soma

# Programa principal
x = int(input("Digite o primeiro limite: "))
y = int(input("Digite o segundo limite: "))

print(f"Soma entre {x} e {y}: {soma_entre(x, y)}")
