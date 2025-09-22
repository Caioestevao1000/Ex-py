print("união, interseção, diferença (A−B e B−A) e diferença simétrica")
a = input("Digite os números do conjunto A (separados por espaços):").split()
b = input("Digite os números do conjunto B (separados por espaços):").split()

conjunto_a = set(map(int, a))
conjunto_b = set(map(int, b))

uniao = conjunto_a | conjunto_b
intersecao = conjunto_a & conjunto_b
dif_a = conjunto_a - conjunto_b
dif_b = conjunto_b - conjunto_a
dif_sime = conjunto_a ^ conjunto_b

print("\nUnião:", uniao)
print("Interseção:", intersecao)
print("Diferença A:", dif_a)
print("Diferença B:", dif_b)
print("Diferença Simétrica:", dif_sime)

