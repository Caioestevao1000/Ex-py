alunos = {
    "Ana": 8.5,
    "João": 7.2,
    "Maria": 9.0
}

print("Dicionário:", alunos)

maior_aluno = None
maior_nota = -1

for nome, nota in alunos.items():
    if nota > maior_nota:
        maior_nota = nota
        maior_aluno = nome

print(f"O aluno com a maior nota é {maior_aluno} ({maior_nota})")
