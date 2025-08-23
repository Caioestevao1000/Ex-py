print("\n## 10 Números + Vetor ##")

numeros = []
negativo = 0
num=0
positivo=0

print("Digite 10 Números")
for x in range (10):
    num = float(input(f"Digite o {x+1}° Número:"))
    numeros.append(num)
    if num > 0:
        positivo += num
    elif num < 0:
        negativo += 1
    else: print("0 é um número neutro")
else: 
    print(f"Quantidade de Números Negativos: {negativo}")
    print(f"Soma dos Números Positivos: {positivo}")

input("Aperte Enter Para Sair...")