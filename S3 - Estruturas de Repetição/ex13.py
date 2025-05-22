import random

print("## Jogo de Adivinhação ##")
print("Tente adivinhar o número entre 1 e 50.")
print("Você tem 7 tentativas!\n")

numero_secreto = random.randint(1, 50)

for tentativa in range(1, 8): 
    try:
        palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite (1 a 50): "))
        
        if palpite < 1 or palpite > 50:
            print("Por favor, digite um número entre 1 e 50.\n")
            continue

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} na tentativa {tentativa}!")
            break
        elif palpite < numero_secreto:
            print("Dica: O número secreto é **MAIOR**.\n")
        else:
            print("Dica: O número secreto é **MENOR**.\n")

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.\n")
        continue

else:
    print(f"\n Suas tentativas acabaram! O número secreto era: {numero_secreto}")
