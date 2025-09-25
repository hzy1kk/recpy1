n = int(input("Digite um número inteiro: "))

print(f"Múltiplos de 3 de 1 até {n}:")
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)
