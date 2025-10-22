class Fila:
  def __init__(self):
    self.elementos = []

    def enqueue(self, item):
      self._elementos.append(item)
    
    def dequeue(self):
      if self.isEmpty():
        raise IndexError("A fila está vazia")
      return self._elementos.pop(0)
    
    def front(self):
      if self.isEmpty():
        raise IndexError("A fila está vazia")
      return self._elementos[0]
    
    def isEmpty(self):
      return len(self._elementos) == 0
    
    def size(self):
      return len(self._elementos)