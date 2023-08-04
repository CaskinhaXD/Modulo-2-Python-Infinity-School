def vogais(palavra):
    vogais = "aeiouAEIOU"  # Lista de vogais
    num_vogais = 0  # Variável para contar o número de vogais

    for letra in palavra:
        if letra in vogais:
            num_vogais += 1

    return num_vogais
            
palavra = input("Digite uma palavra: ")
print(f"A {palavra} tem {vogais(palavra)} vogais.")