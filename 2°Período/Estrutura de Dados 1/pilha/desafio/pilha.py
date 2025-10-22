class Pilha:

    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)
    
    def pop(self):
        if len(self.elementos) > 0:
            return self.elementos.pop()
        else:
            print("Não há elemento a ser removido.")

    def top(self):
        if len(self.elementos) > 0:
            return self.elementos[-1]
        else:
            return None
        
    def size(self):
        return len(self.elementos)
    
    def isEmpty(self):
        if len(self.elementos) > 0:
            return False
        else:
            return True
                
    def __str__(self):
        return f"({len(self.elementos)}) {self.elementos}"
    
