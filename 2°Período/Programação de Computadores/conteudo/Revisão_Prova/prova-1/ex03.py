nomes_a = input("Nome A:")
nomes_b = input("Nome B:")

conj_a = set(nomes_a.split())
conj_b = set(nomes_b.split())

uniao = conj_a | conj_b

somente_a = conj_a - conj_b

somente_b = conj_b - conj_a

diferenca = conj_a ^ conj_b

print("União:",uniao, "\nTotal:", len(uniao))

print("Somente A:",somente_a)

print("Somente B:",somente_b)

print("Simetrica:",diferenca)


