def ler_primeira_linha(nome_arquivo):
    print(f"Abrindo '{nome_arquivo}'...")
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            primeira = arquivo.readline()
            if not primeira:  # arquivo vazio
                raise IOError
    except FileNotFoundError:
        print(f"Erro: arquivo '{nome_arquivo}' não encontrado.")
    except IOError:
        print("Erro: falha ao ler o arquivo.")
    else:
        print("Primeira linha:", primeira.strip())
    finally:
        print("Fechando arquivo... (sempre executado)")


ler_primeira_linha("notas.txt")
