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

def decimal_para_base(numero, base):
    digitos = "0123456789ABCDEF"
    pilha = Pilha()

    while numero > 0:
        resto = numero % base
        pilha.push(digitos[resto])
        numero = numero // base

    resultado = ""
    while not pilha.isEmpty():
        resultado += pilha.pop()
    return resultado

# Exemplo de uso:
print(decimal_para_base(30, 16))  # Saída: "1E"