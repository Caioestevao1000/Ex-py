def atribuir_nota(nota):
    if 0 >= nota > 10:
        raise ValueError("Nota deve estar entre 0 e 10")
    return nota
try:
    nota = float(input("Digite sua nota:"))
    print(atribuir_nota(nota))
except ValueError as e:
    print("Erro:", e)