class Pilha: 
  def __init__(self): #o que é esse self?
    self.elementos = []

  def push(self, item):
    self.elementos.append(item)

  def pop(self):
    if self.isEmpty():
      raise IndexError("A pilha está vazia.")
    return self.elementos.pop()
  
  def top(self):
    if self.isEmpty():
      raise IndexError("A pilha está vazia.")
    return self.elementos[-1]
  
  def isEmpty(self):
    return len(self.elementos) == 0 # pq == a zero?
  
  def size(self):
    return len(self.elementos)