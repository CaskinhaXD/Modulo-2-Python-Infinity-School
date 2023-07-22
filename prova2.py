# O user envia 2 listas
# Gera uma terceira com o que tem em ambas e a soma desses números
primeira = []
segunda = []

while True:
    e = int(input("Digite um valor para a primeira lista (0 para terminar):"))
    
    if e == 0:
        break
    
    primeira.append(e)

primeira.sort()
# print(f"Primeira lista: {primeira}")

while True:
    e = int(input("Digite um valor para a segunda lista (0 para terminar):"))
    
    if e == 0:
        break

    segunda.append(e)

segunda.sort()
# print(f"Segunda lista: {segunda}")

primeiraSet = set(primeira)
segundaSet = set(segunda)

# print(primeiraSet)
# print(segundaSet)
print(list(primeiraSet.intersection(segundaSet)), sum(primeiraSet.intersection(segundaSet)))