def adicionar_aluno(dicionario_alunos):
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número de matrícula do aluno: ")
    dicionario_alunos[matricula] = nome
    print("Aluno adicionado com sucesso!")


def remover_aluno(dicionario_alunos):
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in dicionario_alunos:
        del dicionario_alunos[matricula]
        print("Aluno removido com sucesso!")
    else:
        print("Matrícula não encontrada. Nenhum aluno foi removido.")


def visualizar_alunos(dicionario_alunos):
    if not dicionario_alunos:
        print("Nenhum aluno registrado.")
    else:
        print("Alunos registrados:")
        for matricula, nome in dicionario_alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")


dicionario_alunos = {}
while True:
    print("\n===== MENU =====")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Visualizar alunos")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        adicionar_aluno(dicionario_alunos)
    elif opcao == "2":
        remover_aluno(dicionario_alunos)
    elif opcao == "3":
        visualizar_alunos(dicionario_alunos)
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")