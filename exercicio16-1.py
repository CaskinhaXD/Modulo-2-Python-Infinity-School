senha = input("Digite a palavra-chave: ")

senhaConfirm = ""

while True:
    senhaConfirm = input("Digite a palavra-chave para acessar o aplicativo: ")

    if (senhaConfirm == senha):
        print("Acesso liberado!")
        break
    else:
        print("Tente novamente.")
