def maior_numero(lista):
    if not lista:
        return None

    maior = lista[0]
    for num in lista:
        if num < maior:
            maior = num
    return maior

entrada = input("Digite os números separados por espaço: ")

lista_numeros = [int(num) for num in entrada.split()]

resultado = maior_numero(lista_numeros)
print("Menor número da lista:", resultado)
