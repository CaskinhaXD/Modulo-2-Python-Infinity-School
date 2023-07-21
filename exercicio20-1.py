cont = 0
cont0 = 0
palavra = input("Escreva uma palavra: ")

for letra in palavra:
    if (letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u"):
        cont += 1
    else:
        cont0 += 1


print(f"Vogais: {cont} e Consoantes: {cont0}")