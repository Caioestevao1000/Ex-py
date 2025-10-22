class Fila:
    def __init__(self):
        self._elementos = []  # Cria uma lista vazia para armazenar os clientes

    def enqueue(self, item):
        self._elementos.append(item)  # Adiciona um cliente no final da fila

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("A fila está vazia.")  # Levanta um erro se a fila estiver vazia
        return self._elementos.pop(0)  # Remove e retorna o cliente que está no início da fila

    def isEmpty(self):
        return len(self._elementos) == 0  # Verifica se a fila está vazia

# Criando uma fila para o call center
fila_atendimento = Fila()

# Clientes chegam na fila
fila_atendimento.enqueue("Cliente 1")
fila_atendimento.enqueue("Cliente 2")
fila_atendimento.enqueue("Cliente 3")

# Atendimento aos clientes
print(fila_atendimento.dequeue())  # Saída: Cliente 1
print(fila_atendimento.dequeue())  # Saída: Cliente 2