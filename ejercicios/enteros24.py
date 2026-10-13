def enteros24():
    Numeros = [5, 7, 8, 10, 12, 18, 20, 25, 30, 35, 40, 48, 5, 20, 40]

    Mayor = 0
    Smayor = 0

    for numero in Numeros:
        if numero > Mayor:
            Smayor = Mayor
            Mayor = numero
        elif numero < Mayor and numero > Smayor:
            Smayor = numero

    if Smayor == 0:
        print('No existe un segundo número mayor diferente.')
    else:
        print('El mayor es:', Mayor)
        print('El segundo mayor es:', Smayor)
        print('La diferencia de los números es:', Mayor - Smayor)