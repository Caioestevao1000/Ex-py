Linha1 = str(input("Códigos Cadastrados(separdos por espaço):"))
Linha2 = str(input("Códigos Presentes(separdos por espaço):"))

cad = set(Linha1.split())
pres = set(Linha2.split())

diferenca = cad - pres
print("Falta:", diferenca)
