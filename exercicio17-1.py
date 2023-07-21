senha = input("Digite a senha: ")
senhaConfirm = ""
cadeado = bool

while True:
    senhaConfirm = input("Digite a senha para acessar o aplicativo: ")

    if (senhaConfirm == senha):
        print("Acesso liberado!")
        cadeado = True
        break
    else:
        print("Tente novamente.")
        cadeado = False