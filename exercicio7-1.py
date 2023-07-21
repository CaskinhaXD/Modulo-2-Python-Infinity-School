n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

calc = (n1 + n2 + n3) / 3

if (calc >= 7):
    print("Aluno aprovado")
else:
    print("Aluno reprovado")