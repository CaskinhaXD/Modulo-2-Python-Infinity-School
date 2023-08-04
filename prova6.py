def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
maior = maior_numero(num1, num2)
print(f"O maior número é: {maior}")

def maior_numero(num1, num2):
    return max(num1, num2)

maior = maior_numero(num1, num2)
print(f"O maior número é: {maior}")
