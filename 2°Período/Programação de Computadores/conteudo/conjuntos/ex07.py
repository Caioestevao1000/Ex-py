emails = input("Digite a lista de emails (separe cada email com espaço): ").split()

dominios = set()
for email in emails:
    dominios.add(email.lower().split('@')[1])

print("Domínios:", dominios)
print("Total:", len(dominios))


# emails = input("Digite a lista de emails (separe cada email com espaço): ").split()

# # extrair domínios em minúsculo
# dominios = {email.lower().split('@')[1] for email in emails}

# print("Domínios:", dominios)
# print("Total:", len(dominios))
