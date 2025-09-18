Distancia = {}

quantidade = int(input("Quantas cidades deseja cadastrar? "))

for i in range(quantidade):
    cidade = str(input(f"Digite o nome da cidade de origem {i+1}: ")).lower()
    cidade2 = str(input(f"Digite o nome da cidade de destino {i+2}: ")).lower()
    distancia = float(input(f"Digite a distância entre {cidade} e {cidade2} (em km): "))
    Distancia[(cidade, cidade2)] = distancia
    Distancia[(cidade2, cidade)] = distancia  # Distância é a mesma em ambos os sentidos

print("\nConsulta de distâncias entre cidades")

origem = input("Digite a cidade de origem: ").lower()
destino = input("Digite a cidade de destino: ").lower()
print(f"A distância entre {origem}-{destino}:", Distancia.get((origem, destino), "Distância não encontrada ou Cidades não cadastradas"))