def contar_palavras_com_mais_de_5_caracteres(lista):
    return sum(1 for palavra in lista if len(palavra) > 5)

entrada = input("Digite as palavras separadas por espaço: ")

lista_palavras = entrada.split()

quantidade_palavras = contar_palavras_com_mais_de_5_caracteres(lista_palavras)
print("Quantidade de palavras com mais de 5 caracteres:", quantidade_palavras)
