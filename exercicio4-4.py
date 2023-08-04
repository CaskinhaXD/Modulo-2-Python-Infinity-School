def concatenar_strings(lista):
    return ''.join(lista)

entrada = input("Digite as strings separadas por espaço: ")

lista_strings = entrada.split()

resultado = concatenar_strings(lista_strings)
print("Concatenação das strings:", resultado)