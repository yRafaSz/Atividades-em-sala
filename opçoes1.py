cadastros = []

while True:
    print("\n1 - Adicionar nome\n2 - Listar nomes\n3 - Sair")
    opcao = input("Escolha uma opção: ")  # Agora está correto.

    if opcao == "1":
       nome = input("Digite o nome: ") # Usuário digita o nome
       cadastros.append(nome) # Nome adicionado à lista
       print("Nome cadastrado!")

    elif opcao == "2":
       print("\nLista de nomes:")
       for nome in cadastros: # Exibe todos os nomes cadastrados
        print(nome)

    elif opcao == "3":
        print("Saindo do programa...")
        break
