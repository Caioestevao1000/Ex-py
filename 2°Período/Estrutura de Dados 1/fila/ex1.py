# Importa a classe Fila (Fila.py) localizada no mesmo diretório deste arquivo
from ex01 import Fila

# Criando uma instância da fila
fila = Fila()

# Verificando se a fila está vazia
print(fila.isEmpty())  # Saída: True

# Adicionando elementos à fila
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)

# Verificando o tamanho da fila
print(fila.size())  # Saída: 3

# Consultando o primeiro elemento da fila
print(fila.front())  # Saída: 10

# Removendo elementos da fila
print(fila.dequeue())  # Saída: 10
print(fila.dequeue())  # Saída: 20

# Verificando novamente o primeiro elemento
print(fila.front())  # Saída: 30

# Verificando se a fila está vazia
print(fila.isEmpty())  # Saída: False

# Esvaziando a fila
fila.dequeue()
print(fila.isEmpty())  # Saída: True