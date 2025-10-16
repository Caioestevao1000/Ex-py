quant_alunos = int(input("Quantos alunos:"))

dic = {}

for i in range(quant_alunos):
    aluno = input(f"Aluno {i+1} - nome:")
    nota1 = input(f"Nota {i+1} - Nota:")
    nota2 = input(f"Nota {i+2} - Nota:")
    nota3 = input(f"Nota {i+3} - Nota:")
    notas =[nota1,nota2,nota3]
    dic[aluno]=notas
print(dic)

print("Média")
soma = 0
for chave, valor in dic.items():
    soma += valor
    print(soma)