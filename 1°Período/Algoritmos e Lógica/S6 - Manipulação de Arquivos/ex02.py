print("## Lê e Exibi o Conteúdo do Arquivo ##")
arquivo = open("frases.txt", "r")

conteudo = arquivo.read()

print("Conteúdo do arquivo:")
print(conteudo)

arquivo.close()
