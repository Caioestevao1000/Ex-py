lista_emails = set(str(input("Digite a lista de emails com acessa autorizados(separe cada email com espaço entre eles):")).split())
entrada = set(str(input("Digite o email para acessar:")).split())

if entrada in lista_emails:
    print("Acesso liberado")
else:
    print("Acesso negado")