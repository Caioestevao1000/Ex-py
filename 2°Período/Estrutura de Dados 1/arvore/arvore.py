from NO import No

class Arvore:
  def __init__(self, valor_raiz):
    self.raiz = No(valor_raiz)

  def add_filho(self, no_pai, no_filho):
    no_pai.filhos.append(no_filho)