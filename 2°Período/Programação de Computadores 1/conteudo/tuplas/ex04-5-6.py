animais = ('cachorro', 'gato', 'peixe', 'rato')

for i in range(len(animais)):
    print(f" Sem enumerate- Posição {i} animal: {animais[i]}")

print()

for i in animais:
    print(animais[i])

print()

for i, valor in enumerate(animais):
    print(f" Com enumerate- Posição {i} animal: {animais[i]}")
