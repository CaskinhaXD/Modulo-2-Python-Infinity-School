def par(num):
    if (num % 2 == 0):
        return True
    else:
        return False
    
num = int(input("Digite um número: "))
print(f"Par?: {par(num)}")