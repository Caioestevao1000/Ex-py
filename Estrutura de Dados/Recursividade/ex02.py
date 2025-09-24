def contagem(n):
   if n < 10:
      return 1
   else:
    return 1 + contagem(n // 10)

print(contagem(1234))