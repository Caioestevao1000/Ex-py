print("\n## Média de Notas ##")
print("Notas de 1 a 10")

nota1= float(input("Digite a Primeira Nota:"))
nota2= float(input("Digite a Segunda Nota:"))
nota3= float(input("Digite a Terceira Nota:"))
nota4= float(input("Digite a Quarta Nota:"))

med = (nota1 + nota2 + nota3 + nota4) /2  

if med >= 6.0:
    print("\nVocê está APROVADO")
elif med < 6.0:
    print("\nVocê está REPROVADO")

input("\nPressione Enter para sair...")