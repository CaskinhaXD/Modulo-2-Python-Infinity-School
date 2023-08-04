def soma_elementos(lista):
    return sum(lista)

entrada = input("Digite os números separados por espaço: ")

lista_numeros = [int(num) for num in entrada.split()]

resultado = soma_elementos(lista_numeros)
print("Soma dos elementos da lista:", resultado)
