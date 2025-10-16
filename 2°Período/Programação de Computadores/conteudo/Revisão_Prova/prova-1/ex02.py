quant_alunos = int(input("Quantos alunos:"))

dic_alunos = {}
soma_notas = 0

for i in range(quant_alunos):
    nome = str(input(f"Aluno {i+1} - nome:"))
    nota = float(input(f"Aluno {i+1} - nota:"))
    soma_notas += nota
    dic_alunos[nome] = nota

maior_nota = float('-inf')
menor_nota = float('inf')
aluno_maior = ""
aluno_menor = ""

for chave, valor in dic_alunos.items():
    if valor > maior_nota:
        maior_nota = valor
        aluno_maior = chave
    if valor < menor_nota:
        menor_nota = valor
        aluno_menor = chave

print(f"\nMaior nota é do(a) {aluno_maior}: {maior_nota}")
print(f"Menor nota é do(a) {aluno_menor}: {menor_nota}")

media = soma_notas / quant_alunos
print(f"Média da turma: {media:.2f}")

consultar_aluno = input("\nConsultar aluno: ")

if consultar_aluno in dic_alunos:
    print(f"Nota do(a) {consultar_aluno}: {dic_alunos[consultar_aluno]}")
else:
    print("Aluno não encontrado")