print("## Cálculo do Peso ##")
peso = float(input("Digite o seu Peso em Kg:"))

peso15 = peso * 15 / 100 + peso
peso20 = -peso * 20 / 100 +peso

print("\nCaso você engordar 15%, seu peso será:", peso15,"kg\nCaso você emagrecer 20%, seu peso será:", peso20,"kg")

input("\nPressione Enter para sair...")
