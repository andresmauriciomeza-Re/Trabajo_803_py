Lista = [1,-20,53,6,75,-9,-494,100,0,7,-4, 0,53,74,-193,12,-9,-500,-21, 3]
positivos = []
negativos = []
ceros = []
for numero in Lista:
    if numero > 0:
        positivos.append(numero)
    elif numero < 0:
            negativos.append(numero)
    else:
            ceros.append(numero)
print(f"Los numeros positivos son:{positivos}")
print(f"Los numeros negativos son: {negativos}")
print(f"Los numeros ceros son: {ceros}")