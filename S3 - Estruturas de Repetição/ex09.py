print("\n## Idade, Altura, Peso ##")

mcinquentao = 0
pessoas_dv = 0
pessoal_leve = 0
altura_dv = 0

for i in range(25):
    idade = int(input("Digite a sua Idade:"))
    if idade > 50:
        mcinquentao += 1
        altura = float(input("Digite sua Altura:"))
        peso = float(input("Digite seu Peso:"))
        if peso < 40 :
            pessoal_leve += 1 

    elif idade >= 10 and idade <= 20:
        pessoas_dv += 1
        altura_dv += float(input("Digite sua Altura:"))
        peso = float(input("Digite seu Peso:"))
        if peso < 40:
            pessoal_leve += 1 
    else: 
        altura = float(input("Digite sua Altura:"))
        peso= float(input("Digite seu Peso:"))
        if peso < 40:
            pessoal_leve += 1
else:
    if pessoas_dv == 0: 
        med_altura = 0
    else: 
        med_altura = altura_dv/pessoas_dv
percentagem_peso = (pessoal_leve / 25) * 100
print(f"Pessoas com mais de 50 anos {mcinquentao}")
print(f"Média da Altura de pessoas entre 10 e 20 anos: {med_altura}")
print(f"A porcentagem de pessoas com o peso inferior a 40 quilo é de:{percentagem_peso}%")

input("Pressione Enter para Sair...")