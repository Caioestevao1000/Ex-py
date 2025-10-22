from classes.Banco import Banco
from classes.ContaBancaria import ContaBancaria
from classes.Cliente import Cliente

libina_bank = Banco("Libina Natu Bank")

cliente1 = Cliente("John", "Drapper", "938.593.192-23", "99970-6070", "Rua das Flores, 292", "johndrapper@gmail.com")
c1 = ContaBancaria(cliente1, "0001", "9393", 0)

libina_bank.adicionar_conta(c1)

libina_bank.exibir_correntistas()