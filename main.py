entrada = -1

while True:
    print("-------- BEM VINDO --------")
    print("1. Imprimir um nome com A.")
    print("2. Imprimir um nome com B.")
    print("3. Imprimir um nome com C.")
    print("4. Imprimir um nome com D.")
    print("0. Sair")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 0:
        print("\nObrigada e volte sempre!")
        print("^-^~\n")
        break
    elif opcao == 1:
        print("\nAline")
    elif opcao == 2:
        print("\nBruna")
    elif opcao == 3:
        print("\nCamila")
    elif opcao == 4:
        print("\nDiego")