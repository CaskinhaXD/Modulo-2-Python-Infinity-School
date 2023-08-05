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

def lista_numeros(lista: list):
    if (len(lista) == 0):
        return

    n = max(lista)

    print(n)

    lista.remove(n)

    return lista_numeros(lista)

lista = [1, 3, 4, 5, 6, 7]

lista_numeros(lista)