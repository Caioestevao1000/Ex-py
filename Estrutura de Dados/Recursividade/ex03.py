def operacao(n):
    if n < 10:
        return n
    else: return n % 10 + operacao(n // 10)
num = int(input())
print(operacao(num))