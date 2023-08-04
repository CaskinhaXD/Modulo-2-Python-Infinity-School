def numeros_pares(lista):
    return [num for num in lista if num % 2 == 1]

entrada = input("Digite os números separados por espaço: ")

lista_numeros = [int(num) for num in entrada.split()]

numeros_pares_lista = numeros_pares(lista_numeros)
print("Números pares:", numeros_pares_lista)
