print("## Conta Linhas de um Arquivo ##")
arquivo = open("frases.txt", "r")

linhas = arquivo.readlines()

quantidade_linhas = len(linhas)

print(f"O arquivo contém {quantidade_linhas} linha(s).")

arquivo.close()
