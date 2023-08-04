def consoantes(palavra):
    vogais = "aeiouAEIOU"  # Lista de vogais
    num_vogais = 0  # Variável para contar o número de vogais

    for letra in palavra:
        if letra not in vogais:
            num_vogais += 1

    return num_vogais
            
palavra = input("Digite uma palavra: ")
print(f"A {palavra} tem {consoantes(palavra)} consoantes.")