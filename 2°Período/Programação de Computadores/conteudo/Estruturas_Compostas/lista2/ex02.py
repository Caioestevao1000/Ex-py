# Exercício 2 - Funcionários
funcionarios = []
qnt = int(input("Quantos funcionários? "))

for i in range(qnt):
    dic = {}
    dic['nome'] = input(f"Funcionário {i+1} - Nome: ")
    dic['cargo'] = input(f"Funcionário {i+1} - Cargo: ")
    dic['salario'] = float(input(f"Funcionário {i+1} - Salário: "))
    funcionarios.append(dic)

# Total
total = 0
for f in funcionarios:
    total += f['salario']

# Média
media = total / qnt

# Maior e menor
maior = funcionarios[0]
menor = funcionarios[0]
for f in funcionarios:
    if f['salario'] > maior['salario']:
        maior = f
    if f['salario'] < menor['salario']:
        menor = f

# Cargos
cargos = set()
for f in funcionarios:
    cargos.add(f['cargo'])

print(f"\nTotal de salários: R$ {total:.2f}")
print(f"Salário médio: R$ {media:.2f}")
print(f"Maior salário: R$ {maior['salario']:.2f} ({maior['nome']})")
print(f"Menor salário: R$ {menor['salario']:.2f} ({menor['nome']})")

print("\nCargos (sem repetição):")
for c in cargos:
    print("-", c)
