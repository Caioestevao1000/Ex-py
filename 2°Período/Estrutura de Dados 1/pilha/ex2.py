class Pilha:
    def __init__(self):
        self._elementos = []

    def push(self, item):
        self._elementos.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("A pilha está vazia.")
        return self._elementos.pop()

    def isEmpty(self):
        return len(self._elementos) == 0

def inverte_string(texto):
    pilha = Pilha()
    for char in texto:
        pilha.push(char)

    invertida = ""
    while not pilha.isEmpty():
        invertida += pilha.pop()
    return invertida

if __name__ == '__main__':
    texto_original = "estrutura"
    texto_invertido = inverte_string(texto_original)
    print(f"Texto original: {texto_original}")
    print(f"Texto invertido: {texto_invertido}")