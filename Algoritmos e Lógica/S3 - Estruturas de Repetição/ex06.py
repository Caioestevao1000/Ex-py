print("\n## Faixa Etária ##")

um = 0
dois = 0
tres = 0
quatro = 0
cinco = 0

for i in range(2):
    idade = int(input("\nDigite Sua Idade:"))
    if idade <= 15:
        um += 1
    elif idade >= 16 and idade <= 30:
        dois += 1
    elif idade >= 31 and idade <= 45:
        tres += 1
    elif idade >= 46 and idade <= 60:
        quatro += 1
    else:
        cinco += 1
else: 
    total = um + dois + tres + quatro + cinco
    porcent_um= (um/total) * 100
    porcent_cinco= (cinco/total) * 100
    print("FAIXA ETÁRIA\t\t\tIDADE")
    print("-----------------------------------------------------")
    print("\t1ª\t\taté 15 anos ", um, "Pessoas nessa Faixa Etária")
    print("\t2ª\t\tde 16 a 30 anos ", dois, "Pessoas nessa Faixa Etária")
    print("\t3ª\t\tde 31 a 45 anos ", tres, "Pessoas nessa Faixa Etária")
    print("\t4ª\t\tde 46 a 60 anos ", quatro, "Pessoas nessa Faixa Etária")
    print("\t5ª\t\tAcima de 61 anos ", cinco, "Pessoas nessa Faixa Etária")

    print(f"\nPercentual da 1°Faixa (até 15 anos): {porcent_um:.2f}%")
    print(f"Percentual da 5°Faixa (acima de 61 anos): {porcent_cinco:.2f}%")


input("Pressione Enter para Sair...")