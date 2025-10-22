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

fila = Fila()

if __name__ == '__main__':
  while True:
      nome = input("Digite seu nome (ou 'FIM' para encerrar): ")
      if nome == 'FIM':
          break
      fila.enqueue(nome)
  
  for i in range(fila.size()):
      print(f"Atendendo: {fila.dequeue()}")