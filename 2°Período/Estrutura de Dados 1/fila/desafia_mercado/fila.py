class Fila:
    def __init__(self):
        self.elementos = []

    #adiciona elemento no final da fila
    def enqueue(self, elemento):
        self.elementos.append(elemento)

    # remove o primeito elemento da fila
    def dequeue(self):
        if len(self.elementos) > 0:
            return self.elementos.pop(0) #se vazio remove o ultimo
        else:
            return None
    
    # Vê o tamanho
    def size(self):
        return len(self.elementos)
    
    # verifica se elemento está vazio
    def is_empty(self):
        if len(self.elementos) == 0:
            return True
        else: 
            return False
        
    # pega o primeiro elemento e remove

    def front(self):
        if len(self.elementos) > 0:
            return self.elementos[0]
        else:
            return None
        
    def __str__(self):
        return str(self.elementos)