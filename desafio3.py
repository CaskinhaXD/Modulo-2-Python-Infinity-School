# Reproduzir o seguinte código sem o for:
# def list_numeros(lista):
#     for valor in lista:
#         print(valor)
# lista = [1, 3, 4, 5, 6, 7]
# list_numeros(lista)
# def logica_codigo(n: int):
#     if (n == 1):
#         return 1
#     print(n)
#     return logica_codigo(n - 1)
# print(logica_codigo(10))

def lista_numeros(max: int, lista: list, count: int):
    if (len(lista) == count):
        return

    n = max

    if (n in lista):
        print(n)
        count = count + 1

    return lista_numeros(n - 1, lista, count)

lista = [1, 3, 4, 5, 6, 7]

count = 0

lista_numeros(max(lista), lista, count)
