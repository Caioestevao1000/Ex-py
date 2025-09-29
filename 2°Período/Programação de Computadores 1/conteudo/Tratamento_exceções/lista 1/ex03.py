import os
print("Diretório atual:", os.getcwd())

try:
    nome_arquivo = input("Digite o Nome do Arquivo com sua Extensão:")
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read().strip
        num = int(conteudo)
        print(num)
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
except ValueError:
    print("Erro: conteúdo do arquivo não é um número inteiro.")