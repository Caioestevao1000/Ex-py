class ValorInvalidoError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor < 0:
        raise ValorInvalidoError("Valor do saque não pode ser negativo")
    elif valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque")
    return saldo - valor

try:
    sal = float(input("Saldo da Conta: "))
    val = float(input("Valor para Saque: "))

    novo_saldo = sacar(sal, val)
    print("Saque realizado com sucesso! Novo saldo:", novo_saldo)

except ValorInvalidoError as e:
    print("Erro:", e)

except SaldoInsuficienteError as e:
    print("Erro:", e)
