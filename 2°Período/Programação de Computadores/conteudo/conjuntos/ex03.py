print("Digite alguma frases nas duas linha, ambas as frases devem conter palavras iguais")
Linha1 = str(input("Digite uma frase:"))
Linha2 = str(input("Digite uma frase:"))

a = set(Linha1.split())
b = set(Linha2.split())

palavras_iguais = a & b

print("Palavras iguais nas duas frases ",", ".join(palavras_iguais))
