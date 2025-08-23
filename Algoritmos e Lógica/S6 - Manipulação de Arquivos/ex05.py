print("## Cria um Novo Arquivo sem Linhas em Branco ##")
entrada = open("frases.txt", "r")

saida = open("frases_limpo.txt", "w")

for linha in entrada:
    if linha.strip() != "":
        saida.write(linha)

# Fecha ambos os arquivos
entrada.close()
saida.close()

print("Linhas em branco removidas. Arquivo 'frases_limpo.txt' criado.")
