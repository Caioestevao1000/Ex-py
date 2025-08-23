print("## Cálculo da idade ##")

idade = int(input("Digite seu ano de nascimento:"))
ano_atual = int(input("Digite o ano atual:"))

ano = ano_atual - idade

print("\nSua idade é igual", ano)
print("\nSua idade em meses é igual:", ano * 12)
print("\nSua idade em dias é igual:", ano * 365, "considerado que todo os anos tem 365 dias")
print("\nSua idade em semans é igual:", ano * 52.18)

input("\nPressione Enter para sair...")
