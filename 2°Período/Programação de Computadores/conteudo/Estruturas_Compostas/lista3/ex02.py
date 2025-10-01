Distancia = {}

quantidade = int(input("Quantos registros de distância? "))

for i in range(quantidade):
    cidade = str(input(f"Registro {i+1} - Cidade 1:  : ")).lower()
    cidade2 = str(input(f"Registro {i+2} - Cidade 2:  : ")).lower()
    distancia_km = float(input(f"Digite a distância entre {cidade} e {cidade2} (em km): "))
    Distancia[(cidade, cidade2)] = distancia_km
    Distancia[(cidade2, cidade)] = distancia_km  # Distância é a mesma em ambos os sentidos

print(Distancia)
print("\nConsulta de distâncias entre cidades")

origem = input("Digite a cidade de origem: ").lower()
destino = input("Digite a cidade de destino: ").lower()
print(f"A distância entre {origem}-{destino}:", Distancia.get((origem, destino), "Distância não encontrada ou Cidades não cadastradas"))