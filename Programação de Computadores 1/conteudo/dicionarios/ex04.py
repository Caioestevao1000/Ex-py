paises = {
    'Brasil': 'Brasília',
    'Alemanha': 'Berlim',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago'
}

pais = input("Digite um nome de um país: ")

if pais in paises:
    print(f"A capital de {pais} é {paises[pais]}")
else:
    print("País não encontrado")
