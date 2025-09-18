funcionarios = []

quantidade = int(input("Informe a quantidade de funcionários: "))

for i in range(quantidade):
    funcionario = {}
    funcionario['nome'] = input(f"\nFuncionário {i+1} - Nome: ")
    funcionario['cargo'] = input(f"Funcionário {i+1} - Cargo: ")
    funcionario['salario'] = float(input(f"Funcionário {i+1} - Salário: "))
    funcionarios.append(funcionario)

total = 0
for f in funcionarios:
    total += f['salario']
print(f"\nTotal gasto com salários: R$ {total:.2f}")

cargos = set()
for f in funcionarios:
    cargos.add(f['cargo'])

print("\nCargos cadastrados (sem repetição):")
for c in cargos:
    print("-", c)
