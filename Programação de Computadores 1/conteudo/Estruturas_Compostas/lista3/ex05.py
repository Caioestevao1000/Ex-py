agenda = []

qtd = int(input("Quantos compromissos deseja cadastrar? "))
for i in range(1, qtd + 1):
    data = input(f"Compromisso {i} - Data (AAAA-MM-DD): ")
    hora = input(f"Compromisso {i} - Hora (HH:MM): ")
    desc = input(f"Compromisso {i} - Descrição: ")
    agenda.append({"data": data, "hora": hora, "desc": desc})

print("Todos os compromissos:")
for c in agenda:
    print(f"- {c['data']} {c['hora']} | {c['desc']}")

busca = input("Buscar por data (AAAA-MM-DD): ")
print(f"Compromissos em {busca}:")
for c in agenda:
    if c["data"] == busca:
        print(f"- {c['hora']} | {c['desc']}")

datas = {c["data"] for c in agenda}
print("Datas (sem repetição):")
for d in datas:
    print("-", d)

excluir = input("Excluir compromisso pela descrição (ou deixe vazio para pular): ")
if excluir:
    agenda = [c for c in agenda if c["desc"] != excluir]
    print("Compromisso removido.")

print("Agenda final:")
for c in agenda:
    print(f"- {c['data']} {c['hora']} | {c['desc']}")
