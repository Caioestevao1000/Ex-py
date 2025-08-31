antes_c = set(str(input("Digite os nomes presentes no momendo de Antes(nomes separados por espaço):")).split())
depois_c = set(str(input("Digite os nomes presentes no momendo de Depois(nomes separados por espaço):")).split())

diferenca = antes_c ^ depois_c

print("Mudanças:", diferenca)
