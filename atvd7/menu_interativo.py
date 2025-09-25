while True:
    print("\nMenu:")
    print("[1] Olá")
    print("[2] Ajuda")
    print("[3] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá! Seja bem-vindo(a)!")
    elif opcao == "2":
        print("Ajuda: Escolha uma opção do menu digitando 1, 2 ou 3.")
    elif opcao == "3":
        print("Saindo do programa... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")