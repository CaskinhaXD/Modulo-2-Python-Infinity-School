def menor_numero(lista):
    if len(lista) == 0:
        return None  # Retorna None se a lista estiver vazia

    menor = lista[0]  # Inicializa o maior número como o primeiro elemento da lista
    for num in lista:
        if num < menor:
            menor = num
    return menor

# Teste usando range()
lista_numeros = list(range(1, 11))  # Lista de 1 a 10
print("Lista original:", lista_numeros)
resultado = menor_numero(lista_numeros)
print("Menor número:", resultado)

# Teste inserindo valores manualmente
outra_lista = [3, 9, 12, 17, 22, 30, 4]
print("Outra lista:", outra_lista)
resultado_outra_lista = menor_numero(outra_lista)
print("Menor número na outra lista:", resultado_outra_lista)
