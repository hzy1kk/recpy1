nome = input("Digite seu nome: ")
contador = 0
for char in nome:
    if char.isalpha():
        contador += 1

print(f"Seu nome tem {contador} letras.")