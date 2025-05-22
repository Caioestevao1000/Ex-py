print("\n## Idade, Altura, Peso, Olhos, Cabelo ##")

requisito1 = 0
somaidade = 0
pessoas = 0
pessoa_olhos = 0
pessoas_ruivas_nolhos_azuis = 0

for i in range(20):
    idade = int(input("Digite a sua Idade: "))
    peso = float(input("Digite seu Peso: "))
    altura = float(input("Digite sua Altura: "))
    
    print("\nCor dos Olhos (A - Azul, P - Preto, V - Verde e C - Castanho)")
    olhos = input("Digite a Cor dos seus Olhos: ")
    
    print("Cor dos Cabelos (P - Preto, C - Castanho, L - Louro e R - Ruivo)")
    cabelo = input("Digite a Cor dos seus Cabelos: ")

    if idade > 50 and peso < 60:
        requisito1 += 1

    if altura < 1.5:
        somaidade += idade
        pessoas += 1

    if olhos.lower() == 'a':
        pessoa_olhos += 1

    if cabelo.lower() == 'r' and olhos.lower() != 'a':
        pessoas_ruivas_nolhos_azuis += 1

# Calcular a média de idades apenas se houver pessoas com altura < 1.5
if pessoas > 0:
    med = somaidade / pessoas
else:
    med = 0

percent = (pessoa_olhos / 20) * 100

print(f"\nQuantidade de pessoas com mais de 50 anos e peso < 60 kg: {requisito1}")
print(f"Média das idades das pessoas com altura < 1,50 m: {med:.2f}")
print(f"Percentagem de pessoas com olhos azuis: {percent:.2f}%")
print(f"Quantidade de pessoas ruivas sem olhos azuis: {pessoas_ruivas_nolhos_azuis}")

input("\nPressione Enter para Sair...")
