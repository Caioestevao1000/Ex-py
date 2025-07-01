print("## Verificador de Número Positivo ou Negativo ##")

def verificar(num):
    if num >= 0:
        return "Número positivo"
    else:
        return "Número negativo"

numero = int(input("Digite um número inteiro: "))
resultado = verificar(numero)
print(resultado)

input("Aperte Enter para sair...")
