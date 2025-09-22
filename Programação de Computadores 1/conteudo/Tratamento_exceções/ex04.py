try:
    numero = int(input("Digite o Numerador:"))
    divisor = int(input("Digite o Denominador:"))
    resultado = numero / divisor
except ZeroDivisionError:
    print("Erro: divisor não pode ser zero")
except ValueError:
    print("Erro: digite números inteiro eválidos")
else: print("Resultado:", resultado)