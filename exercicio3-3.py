def saudacao(nome):
    return f"Olá, {nome}. Seja bem vindo ao sistema."

nome = input("Digite o seu nome: ")
saudacao = saudacao(nome)
print(saudacao)
print(type(saudacao))