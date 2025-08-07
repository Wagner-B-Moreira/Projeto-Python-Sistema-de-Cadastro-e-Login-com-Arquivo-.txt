# Função para cadastrar um novo usuário
def cadastrar():
    print("\n..Cadastrar..")
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite sua senha: ")

    # Verificar se o usuário já existe
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")  # Divide a linha em nome e senha
                if dados[0] == usuario:
                    print("Esse usuário já existe.")
                    return
    except FileNotFoundError:
        pass  # Arquivo ainda não existe? Tudo bem. Vamos criar.

    # Salvar o usuário no arquivo
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(usuario + ";" + senha + "\n")
    print("Usuário cadastrado com sucesso!")

# Função para fazer login
def login():
    print("\n..Login..")
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite sua senha: ")

    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if dados[0] == usuario and dados[1] == senha:
                    print("Logado com sucesso!")
                    return
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
        return

    print("Usuário ou senha incorretos.")

# Função para criar o arquivo se ele não existir
def iniciar_arquivo():
    try:
        with open("usuarios.txt", "x") as arquivo:
            pass  # Apenas cria o arquivo vazio
    except FileExistsError:
        pass  # Já existe, então nada a fazer

# Menu principal
def menu():
    iniciar_arquivo()
    while True:
        print("\n==== MENU ====")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()

        elif opcao == "2":
            login()

        elif opcao == "3":
            print("Encerrando o programa. Até mais!")
            break  # Sai do while

        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
menu()
