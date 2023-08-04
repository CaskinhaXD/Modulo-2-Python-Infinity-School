def fibonacci_ate(numero):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= numero:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

numero = int(input("Digite um número: "))

resultado = fibonacci_ate(numero)
print("Sequência de Fibonacci até o número:", resultado)
