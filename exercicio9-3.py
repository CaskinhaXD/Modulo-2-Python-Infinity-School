def numeros_impares(lista):
    impares = []
    for num in lista:
        if num % 2 != 0:  # Verifica se o número é ímpar (resto da divisão por 2 é diferente de 0)
            impares.append(num)
    return impares

# Teste usando range()
lista_numeros = list(range(1, 11))  # Lista de 1 a 10
print("Lista original:", lista_numeros)
lista_impares = numeros_impares(lista_numeros)
print("Números ímpares:", lista_impares)

# Teste inserindo valores manualmente
outra_lista = [3, 9, 12, 17, 22, 30, 4]
print("Outra lista:", outra_lista)
outra_lista_impares = numeros_impares(outra_lista)
print("Números ímpares na outra lista:", outra_lista_impares)
