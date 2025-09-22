idade = int(input())

if idade >= 18:
    print("Acesso completo")
elif 13 <= idade <= 17:
    print("Acesso parcial")
else:
    print("Acesso negado")