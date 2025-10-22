class Cliente:

    def __init__(self, nome, sobrenome, cpf, telefone, endereco, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

    def getNome(self):
        return self.nome
    
    def getCPF(self):
        return self.cpf