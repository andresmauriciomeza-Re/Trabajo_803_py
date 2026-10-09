def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False  # encontró un divisor, no es primo
        i += 1
    return True

N = int(input("Ingrese un valor N: "))

primos = []
for numero in range(2, N + 1):
    if es_primo(numero):
        primos.append(numero)

print(f"Números primos entre 1 y {N}:")
print(primos)
print(f"Se encontraron {len(primos)} números primos.")