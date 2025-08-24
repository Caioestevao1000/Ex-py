lista_telefonica = {}

n = int(input("Digite a quantidadade de nomes e números que você deseja cadastrar:"))

for i in range(n):
    nome = str(input("Digite o nome da pessoa:"))
    numero = int(input("Digite o número da pessoa:"))
    lista_telefonica[nome] = numero

print(lista_telefonica)

procurar_nome = str(input("Digite o nome da pessoa que vc desseja procurar o número:"))

print(lista_telefonica.get(procurar_nome, 'Contato não encontrado'))