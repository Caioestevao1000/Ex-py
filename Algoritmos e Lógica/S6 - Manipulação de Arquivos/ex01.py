print("## Criar Arquivo com Frases ##")
arquivo = open("frases.txt", "w")

for i in range(3):
    frase = input(f"Digite a {i+1}°frase: ")
    arquivo.write(frase + "\n")  

arquivo.close()
