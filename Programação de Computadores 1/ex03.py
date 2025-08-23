lista = []
lista_inversa = []
media = 0
numeros_maior_media = 0

for i in range(4):
    n = int(input(f"Digite o Número {i+1}°:"))
    lista.append(n)
    media += n
media = media / 4

for i in range(len(lista) -1, -1, -1):
    lista_inversa.append(lista[i])

for x in lista:
    if x > media:
        numeros_maior_media += 1

print(f"Lista original: {lista}")
print(f"Lista inversa: {lista_inversa}")
print(f"Média dos números: {media}")
print(f"Quantidade de números acima da média: {numeros_maior_media}")