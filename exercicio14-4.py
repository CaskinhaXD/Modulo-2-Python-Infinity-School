from statistics import median

def mediana_numeros(lista):
    return median(lista)

entrada = input("Digite os números separados por espaço: ")

lista_numeros = [float(num) for num in entrada.split()]

resultado = mediana_numeros(lista_numeros)
print("Mediana dos números:", resultado)
