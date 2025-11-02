class No: 
  def __init__(self, valor):
    self.nome = valor
    self.filhos = []

  def dfs(self, nivel=0, nome_buscado=0, callback=0):

    print("   " * nivel + str(self.nome)) #podemos apagar o callback, se tiver esse print
    #callback(self.valor) #callback, o que é?

    if self.nome == nome_buscado:
      return self

    for filho in self.filhos:
      resultado = filho.dfs(nivel + 1, nome_buscado)
      if resultado:
        return resultado
      
