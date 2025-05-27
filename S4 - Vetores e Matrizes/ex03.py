print("## Vetor com 15 Elementos Inteiros - Encontrar Número 30 ##")

trinta = False
nvetor = []
vetor = []

for i in range(15):
    vetor.append(int(input(f"Digite o {i+1}° Número:")))

for j in range(15):
    if vetor[j] == 30:
        trinta = True
        nvetor.append(j)
else:
    if trinta == True:
        print(f"O Número 30 se encontra no(s) vetor(es); {nvetor}")