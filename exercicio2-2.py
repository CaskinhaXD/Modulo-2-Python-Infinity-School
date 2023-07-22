primeira = []

while True:
    e = input("Digite itens para a lista de compras' (FIM para terminar): ")
    
    if e.upper() == "FIM":
        break
    
    primeira.append(e)
    print(primeira)

while True:
    e = input("Digite itens para remover da lista de compras (FIM para terminar): ")
    
    if (e.upper() == "FIM"):
        break
    
    primeira.remove(e)
    print(primeira)
    
print(f"Lista final: {primeira}")