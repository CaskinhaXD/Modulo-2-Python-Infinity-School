cont = 0
n = int(input("Insira um número para saber se ele é primo: "))
contador = n

while contador > 0:
    if n % contador == 0:
        cont += 1

    contador -= 1

if cont >= 3:
    print('O número escolhido não é primo!')
else: 
    print('O número escolhido é primo!')