class Fila:
    def __init__(self):
        self._elementos = []

    def enqueue(self, item):
        self._elementos.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("A fila está vazia.")
        return self._elementos.pop(0)

    def front(self):
        if self.isEmpty():
            raise IndexError("A fila está vazia.")
        return self._elementos[0]

    def isEmpty(self):
        return len(self._elementos) == 0

    def size(self):
        return len(self._elementos)
        
if __name__ == '__main__':
    fila = Fila()

    while True:
      entrada = input().strip()
      if entrada.upper() == "FIM":
        break
      nome, itens = entrada.split(":")
      nome = nome.strip()
      itens = [item.strip() for item in itens.split(",")]
      fila.enqueue((nome, itens))

    while not fila.isEmpty():
      comando = input().strip()
      if comando.upper() == "PRONTO":
          nome, itens = fila.dequeue()
          print(f"Entregar para {nome}: {', '.join(itens)}")