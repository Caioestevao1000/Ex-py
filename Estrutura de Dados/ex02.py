tentativa =0

while True:
    senha = input()
    if senha == '0':
        print("Encerrando")
        break
    elif senha == 'abc1234':
        print("Acesso permitido")
        break
    else: 
        tentativa += 1
        print("Senha incorreta, tente novamente")
        if tentativa == 3:
            break