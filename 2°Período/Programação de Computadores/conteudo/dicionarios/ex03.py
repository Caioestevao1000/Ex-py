funcionario = {}

nome = str(input("Digite o seu nome:"))
cargo = str(input("Digite que cargo você está:"))
salario = float(input("Digite o seu salário:"))

funcionario["nome"] = nome.lower()
funcionario["cargo"] = cargo.lower()
funcionario["salario"] = salario

print(funcionario)

resposta = str(input(f"{nome}, Seu salário atual é de {salario}, deseja atualizar o salário S/N?"))
resposta = resposta.lower()

if "s" == resposta:
    salario_novo = float(input("Digite o novo salário:")) 
    funcionario.update({"salario":salario_novo})
    print("Salário atualizado")
else:
    print("Salário mantido"),

print(funcionario)
