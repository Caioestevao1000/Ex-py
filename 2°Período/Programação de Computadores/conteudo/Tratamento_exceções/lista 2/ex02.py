def dividir(a,b):
    if b < 0:
        raise ZeroDivisionError("Não pode dividir por Zero")
    return a/b
try:
    valor = int(input("Valor:"))
    divisor = int(input("Divisor:"))
    print(dividir(valor,divisor))
except ZeroDivisionError as e:
    print("Erro", e)