print("\n## Números Primos e o Produto Deles ##")

produto = 1

for num in range(92, 1479):
    eh_primo = True
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(num)
        produto *= num

print("Produto dos primos:", produto)

input("Pressione Enter para sair...")
