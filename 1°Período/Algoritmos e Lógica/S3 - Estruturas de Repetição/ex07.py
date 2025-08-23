print("\n## Tabuada do 1 ao 15 ##")

for i in range(1, 16):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")

input("Pressione Enter para Sair...")