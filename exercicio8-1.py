n1 = int(input("Digite um ano: "))

if (n1 % 4 == 0):
    if (n1 % 100 != 0):
        print("Ano bissexto")
    else:
        print("Ano não bissexto")
else:
    if (n1 % 400 == 0):
        print("Ano bissexto")
    else:
        print("Ano não bissexto")