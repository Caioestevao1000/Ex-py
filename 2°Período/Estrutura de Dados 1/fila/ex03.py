class FilaImpressao:
    def __init__(self):
        self._documentos = []

    def adicionar_documento(self, documento):
        self._documentos.append(documento)

    def imprimir_documento(self):
        if self.isEmpty():
            raise IndexError("Não há documentos na fila.")
        return self._documentos.pop(0)

    def isEmpty(self):
        return len(self._documentos) == 0

# Criando a fila de impressão
fila_impressao = FilaImpressao()

# Adicionando documentos para impressão
fila_impressao.adicionar_documento("Relatório de Vendas")
fila_impressao.adicionar_documento("Planilha de Financeiro")

# Imprimindo os documentos
print(fila_impressao.imprimir_documento())  # Saída: Relatório de Vendas
print(fila_impressao.imprimir_documento())  # Saída: Planilha de Financeiro
  