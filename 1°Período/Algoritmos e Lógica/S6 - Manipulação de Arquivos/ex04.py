print("## Verificação de Palavras no Arquivo ##")
palavra = input("Digite a palavra que deseja procurar: ")

arquivo = open("frases.txt", "r")

encontrada = False
for linha in arquivo:
    if palavra in linha:
        encontrada = True
        break

arquivo.close()

if encontrada:
    print(f"A palavra '{palavra}' foi encontrada no arquivo.")
else:
    print(f"A palavra '{palavra}' NÃO foi encontrada no arquivo.")
