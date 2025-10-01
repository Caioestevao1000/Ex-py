lista_livro = []

qtn_livros = int(input("Quantos livros para cadastrar:"))

for i in range(qtn_livros):
    autores = {}
    autores['autor'] = input("Autor:")
    autores['titulo'] = input("Título:")
    lista_livro.append(autores)

print("\nAutores cadastrados:")
conjunto_autores = set()
for autores in lista_livro:
    conjunto_autores.add(autores['autor'])
print("Autores:\n", conjunto_autores)

print("\nDigite o nome do autor para consulta:")
nome = input("nome autor:").lower()
conjunto_livros = set()
for livros in lista_livro:
    if livros['autor'] == nome :
        conjunto_livros.add(livros['titulo'])
print("\nLivros do autor:\n", conjunto_livros)

