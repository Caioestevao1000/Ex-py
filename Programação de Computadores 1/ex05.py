palavras = []
vogais = ["a", "e", "i", "o", "u",
          "A", "E", "I", "O", "U"]
maior_qtd_vogais = 0
palavra_mais_vogais = ""

for i in range(5):
    p = input(f"Digite a palavra {i+1}: ")
    palavras.append(p)

for p in palavras:
    qtd = 0
    for letra in p:
        if letra in vogais:
            qtd += 1
    print(f"A palavra '{p}' tem {qtd} vogais.")

    if qtd > maior_qtd_vogais:
        maior_qtd_vogais = qtd
        palavra_mais_vogais = p

print("Palavra com mais vogais:", palavra_mais_vogais)
