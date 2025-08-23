vogais = ('a', 'e', 'i', 'o', 'u')
n = str(input("Digite uma Vogal:")).lower()

for i in range(len(vogais)):
    if vogais[i] == n:
        ind = i
    
print(f"A letra '{n}' aparece no índice {ind}")