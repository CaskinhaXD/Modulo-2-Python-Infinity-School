cont = 0
palavra = input("Escreva uma palavra: ")

for letra in palavra:
    if (letra.lower() == "a"):
        cont += 1

print(cont)