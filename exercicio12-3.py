def is_palindromo(palavra):
    palavra = palavra.lower()  # Convertendo a palavra para minúsculas
    return palavra == palavra[::-1]

# Teste da função
palavra = input("Digite uma palavra: ")
resultado = is_palindromo(palavra)
print(f"A palavra '{palavra}' é um palíndromo: {'Sim' if resultado else 'Não'}")
