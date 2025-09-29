# Exercício 4 - Livros e Autores
livros = []
qnt = int(input("Quantos livros? "))

for i in range(qnt):
    dic = {}
    dic['titulo'] = input(f"Livro {i+1} - Título: ")
    dic['autor'] = input(f"Livro {i+1} - Autor: ")
    livros.append(dic)

# Autores sem repetição
autores = set()
for l in livros:
    autores.add(l['autor'])

print("\nAutores (sem repetição):")
for a in autores:
    print("-", a)

# Livros por autor
print("\nLivros por autor:")
livros_por_autor = {}
for a in autores:
    titulos = []
    for l in livros:
        if l['autor'] == a:
            titulos.append(l['titulo'])
    livros_por_autor[a] = titulos
    print(f"- {a}: {', '.join(titulos)}")

# Listar livros de um autor específico
autor_busca = input("\nDigite um autor para listar títulos: ")
if autor_busca in livros_por_autor:
    print(f"\nLivros de {autor_busca}:")
    for t in livros_por_autor[autor_busca]:
        print("-", t)

# Autor com mais livros
mais_livros = ""
qtd_livros = 0
for a, titulos in livros_por_autor.items():
    if len(titulos) > qtd_livros:
        qtd_livros = len(titulos)
        mais_livros = a

print(f"\nAutor com mais livros cadastrados: {mais_livros} ({qtd_livros})")
