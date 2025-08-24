portugues = {'gato':'cat', 'livro':'book', 'casa':'house'}

palavra = str(input("Digite uma palavra:"))

print(portugues.get(palavra, 'Não Existe'))