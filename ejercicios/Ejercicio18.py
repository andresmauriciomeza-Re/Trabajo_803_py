def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False  # encontró un divisor, no es primo
        i += 1
    return True

# 18. Pedir N y mostrar los números primos entre 2 y N
def ejercicio_18(n=None):
    # si no llega un valor desde el menú, lo pide por consola
    if n is None:
        n = input("Ingrese un valor N: ")
    try:
        N = int(n)
    except ValueError:
        print("Eso no es un número entero. Vuelva al menú.")
        return
    if N < 1:
        print("N debe ser mayor o igual a 1. Vuelva al menú.")
        return

    primos = []
    for numero in range(2, N + 1):
        if es_primo(numero):
            primos.append(numero)

    print(f"Números primos entre 1 y {N}:")
    print(primos)
    print(f"Se encontraron {len(primos)} números primos.")
