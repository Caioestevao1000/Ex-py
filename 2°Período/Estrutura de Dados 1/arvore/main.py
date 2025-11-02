from arvore import Arvore
from NO import No

arvore = Arvore("Ormogenio")
no_ormisdo = No("Ormisdo")
no_benjamim = No("Benjamim")
no_jurema = No("Jurema")

arvore.add_filho(arvore.raiz, no_ormisdo)
arvore.add_filho(arvore.raiz, no_benjamim)
arvore.add_filho(arvore.raiz, no_jurema)

no_eliabe = No("Eliabe")
no_marciana = No("Marciana")

arvore.add_filho(no_ormisdo, no_eliabe)
arvore.add_filho(no_ormisdo, no_marciana)

no_eldienia = No("Eldienia")
arvore.add_filho(no_benjamim, no_eldienia)

elemento = arvore.raiz.dfs(0, "Eldienia")

if elemento:
  print(elemento.nome)