print("## Convertendo Horas, minutos em Segundos ##")

def conversor():
    hr = int(input("Digite o tempo em horas:"))
    min = int(input("Digite o tempo em minutos:"))
    seg = int(input("Digite o tempo em segundos:"))

    seg_hora = hr * 3600
    seg_min = min * 60
    soma_segundos = seg_hora + seg_min + seg
    
    print(f"A soma total em segundos é {soma_segundos}")

conversor()