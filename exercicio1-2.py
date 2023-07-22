primeira = []

while True:
    e = input("Digite qualquer coisa para a lista (FIM para terminar):")
    
    if e.upper() == "FIM":
        break
    
    primeira.append(e)
    
print(primeira)