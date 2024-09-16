# Sequencia de Fibonacci

def pertence_fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return f"O número {n} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {n} não pertence à sequência de Fibonacci."

n = 21  # Número de exemplo
print(pertence_fibonacci(n))


