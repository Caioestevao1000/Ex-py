class Banco:

    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def exibir_correntistas(self):
        for correntista in self.contas:
            print(f"{correntista.titular.getNome()} - CPF: {correntista.titular.getCPF()} - R${correntista.saldo}")

    def fechar_conta(self, agencia, numero):
        encontrei = False
        
        for c in self.contas:
            if c.agencia == agencia and c.numero == numero:
                self.contas.remove(c)
                encontrei = True
        
        if encontrei == True:
            print("Conta fechada com sucesso.")
        else:
            print("Não encontrei a conta.")
                