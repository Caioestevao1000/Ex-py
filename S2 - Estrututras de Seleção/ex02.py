print("\n## Média de Notas para Prova ##")

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
md = (nota1 + nota2) / 2

if md >= 0.0 and md < 4.0:
    print("Reprovado")
elif md >= 4.0 and md < 7.0:
    print("Exame")
elif md >= 7.0 and md >= 10.0:
    print("Aprovado")
input("\nPressione Enter para sair...")