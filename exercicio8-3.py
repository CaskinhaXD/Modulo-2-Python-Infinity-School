def numeros_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

# Teste usando range()
lista_numeros = list(range(1, 11))  # Lista de 1 a 10
print("Lista original:", lista_numeros)
lista_pares = numeros_pares(lista_numeros)
print("Números pares:", lista_pares)

# Teste inserindo valores manualmente
outra_lista = [3, 9, 12, 17, 22, 30, 4]
print("Outra lista:", outra_lista)
outra_lista_pares = numeros_pares(outra_lista)
print("Números pares na outra lista:", outra_lista_pares)
