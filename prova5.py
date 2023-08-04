def calcular_media(notas):
    total_notas = len(notas)
    soma_notas = sum(notas)
    media = soma_notas / total_notas
    return media

def verificar_situacao(media):
    if media == 10:
        return "Parabéns, sua média é 10"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

notas = []

while True:
    nota_str = input("Digite uma nota (ou 'fim' para calcular a média): ")
    if nota_str.lower() == "fim":
        break
    try:
        nota = float(nota_str)
        notas.append(nota)
    except ValueError:
        print("Valor inválido. Digite um número válido ou 'fim' para encerrar a entrada de notas.")

if not notas:
    print("Nenhuma nota foi digitada.")
else:
    media = calcular_media(notas)
    print(f"Média: {media:.2f}")
    situacao = verificar_situacao(media)
    print(situacao)