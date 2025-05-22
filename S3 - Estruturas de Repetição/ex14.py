print("## Cálculo de Fatorial ##")

num = int(input("Digite um número inteiro não negativo: "))

if num < 0:
    print("Fatorial não definido para números negativos.")
else:
    fatorial = 1
    contador = 1
    while contador <= num:
        fatorial *= contador
        contador += 1
    print(f"O fatorial de {num} é {fatorial:.2f}")

input("Aperte Enter Para Sair...")
