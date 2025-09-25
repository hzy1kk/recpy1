numeros = []

for i in range(3):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

numeros_dobro = [x * 2 for x in numeros]


print(f"Números originais: {numeros}")
print(f"Números multiplicados por 2: {numeros_dobro}")

soma_original = sum(numeros)
soma_dobro = sum(numeros_dobro)

print(f"Soma dos números originais: {soma_original}")
print(f"Soma dos números multiplicados por 2: {soma_dobro}")