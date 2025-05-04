print("\n## Quadrante de Acordo com os Graus ##")

grau = float(input("Digite um Ângulo em Graus: "))

voltas = int(abs(grau) // 360)

resto = grau % 360
if resto < 0:
    resto += 360  

if grau > 0:
    sentido = "Anti-Horário"
else:
    sentido = "Horário"

if resto == 0 or resto == 360:
    quadrante = "Sobre o eixo positivo X (entre quadrantes 1 e 4)"
elif resto > 0 and resto < 90:
    quadrante = "1º Quadrante"
elif resto == 90:
    quadrante = "Sobre o eixo Y (entre quadrantes 1 e 2)"
elif resto > 90 and resto < 180:
    quadrante = "2º Quadrante"
elif resto == 180:
    quadrante = "Sobre o eixo X negativo (entre quadrantes 2 e 3)"
elif resto > 180 and resto < 270:
    quadrante = "3º Quadrante"
elif resto == 270:
    quadrante = "Sobre o eixo Y negativo (entre quadrantes 3 e 4)"
elif resto > 270 and resto < 360:
    quadrante = "4º Quadrante"


print(f"\nSentido: {sentido}")
print(f"Ângulo Reduzido: {resto:.2f}°")
print(f"Quadrante: {quadrante}")
print(f"Número de Voltas Completas: {voltas}")

input("\nPressione Enter para sair...")
