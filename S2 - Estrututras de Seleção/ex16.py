print("\n## Concessão de Bolsa de Estudos ##")

med = float(input("Digite a Sua Média Final:"))
renda = float(input("Digite a Renda Mensal da Sua Família:"))
hr = int(input("Digite as horas de Serviço Comunitário Comprovadas:"))

if med >= 8.5 and renda <= 2500:
    print("Estudante Elegível para a Bolsa de Estudos!")
elif med < 8.5 and renda > 2500:
    print("Estudante Não Elegível para a Bolsa de Estudos.")
elif med >= 8 and med <= 8.4 and hr >= 30:
    print("Estudante Elegível para a Bolsa de Estudos!")
else:   
    print("Estudante Não Elegível para a Bolsa de Estudos.")

input("\nPressione Enter para sair...")
