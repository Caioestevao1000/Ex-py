class Semaforo:
    def __init__(self):
        self._carros = []

    def chegar_carro(self, carro):
        self._carros.append(carro)

    def liberar_carro(self):
        if self.isEmpty():
            raise IndexError("Não há carros na fila.")
        return self._carros.pop(0)

    def isEmpty(self):
        return len(self._carros) == 0

# Criando o semáforo
semaforo = Semaforo()

# Carros chegando ao semáforo
semaforo.chegar_carro("Carro 1")
semaforo.chegar_carro("Carro 2")
semaforo.chegar_carro("Carro 3")

# Liberando os carros
print(semaforo.liberar_carro())  # Saída: Carro 1
print(semaforo.liberar_carro())  # Saída: Carro 2  