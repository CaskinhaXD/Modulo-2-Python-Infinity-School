def media_numeros(lista):
    if not lista:
        return None

    total = sum(lista)
    quantidade = len(lista)
    media = total / quantidade
    return media

entrada = input("Digite os números separados por espaço: ")

lista_numeros = [float(num) for num in entrada.split()]

resultado = media_numeros(lista_numeros)
print("Média dos números:", resultado)
