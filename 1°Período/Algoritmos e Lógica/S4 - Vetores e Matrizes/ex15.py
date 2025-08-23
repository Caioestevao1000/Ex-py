matriz = []

meses_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

soma_total = 0

for i in range(12):
    print(f'\nNo mês de {meses_ano[i]}')
    linha = []
    for j in range(4):
        linha.append(float(input(f'Digite o valor da venda da {j+1}ª semana: R$'))) 
    matriz.append(linha)


print(f'\nRelatório de vendas anual:\n' + '-'*80)
print(f'{"Meses:":<16}{"1ª Semana":<17}{"2ª Semana":<17}{"3ª Semana":<17}{"4ª Semana":<17}')
print('-'*80)


for i in range(12):
    print(f'{meses_ano[i]:<16}', end='')
    for j in range(4):
        print(f'R${matriz[i][j]:<16.2f}', end='')
    print()

print('-'*80)

for i in range(12):
    total_mes = sum(matriz[i])
    print(f'O Total vendido no mês de {meses_ano[i]} é: R${total_mes:.2f}')
    soma_total += total_mes 

print(f'\nO Total vendido no ano todo foi: R${soma_total:.2f}')

input('\nPressione Enter para fechar o programa...')
