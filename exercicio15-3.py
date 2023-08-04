def media(lista):
    if len(lista) == 0:
        return None  # Retorna None se a lista estiver vazia

    media = lista[0]  # Inicializa o maior número como o primeiro elemento da lista
    for num in lista:
        media += num

    return media / len(lista)

# Teste usando range()
lista_numeros = list(range(1, 11))  # Lista de 1 a 10
print("Lista original:", lista_numeros)
resultado = media(lista_numeros)
print("Média número:", resultado)

# Teste inserindo valores manualmente
outra_lista = [3, 9, 12, 17, 22, 30, 4]
print("Outra lista:", outra_lista)
resultado_outra_lista = media(outra_lista)
print("Média número na outra lista:", resultado_outra_lista)
