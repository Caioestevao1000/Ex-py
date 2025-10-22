class ContaBancaria:

    def __init__(self, titular, agencia, numero, saldo):
        self.titular = titular
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
    
    def getTitular(self):
        return self.titular
    
    def getAgencia(self):
        return self.agencia
    
    def getNumero(self):
        return self.numero
    
    def getSaldo(self):
        return self.saldo

    def setAgencia(self, agencia):
        self.agencia = agencia
    
    def setNumero(self, numero):
        self.numero = numero
    
    def setSaldo(self, saldo):
        self.saldo = saldo

    def __str__(self):
        return f"Titular: {self.titular} - Saldo: {self.saldo}"


    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
        else:
            print(f"Não foi possível sacar. Você quis sacar ${valor}, mas só tem ${self.saldo} de saldo")