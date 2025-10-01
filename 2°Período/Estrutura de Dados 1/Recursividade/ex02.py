def contagem(n):
   if n < 10:
      return 1
   else:
    return 1 + contagem(n // 10)
n = int(input())
print(contagem(n))