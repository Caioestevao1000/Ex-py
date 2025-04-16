print("## Tabuada em FOR e PRINT ##")

n1 = int(input("Tabuada em FOR...Digite o número da tabuada que você quer:"))

for i in range(1,11):
    r = i * n1
    print(n1, "x", i, "=", r)

n2 = int(input("Tabuada em PRINT, digite o número para a tabuada:"))
print(n2, "x", 1 ,"=", n2*1)
print(n2, "x", 2 ,"=", n2*2)
print(n2, "x", 3 ,"=", n2*3)
print(n2, "x", 4 ,"=", n2*4)
print(n2, "x", 5 ,"=", n2*5)
print(n2, "x", 6 ,"=", n2*6)
print(n2, "x", 7 ,"=", n2*7)
print(n2, "x", 8 ,"=", n2*8)
print(n2, "x", 9 ,"=", n2*9)
print(n2, "x", 10 ,"=", n2*10)

input("\nPressione Enter para sair...")
