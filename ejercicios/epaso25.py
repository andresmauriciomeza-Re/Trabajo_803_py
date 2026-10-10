
# 25. Buscar nombres
# Crear una lista con 10 nombres de aprendices
def ejercicio_25(nombre=None):
    aprendices = [
        "Andres",
        "Juan",
        "Maria",
        "Pedro",
        "Ana",
        "Carlos",
        "Laura",
        "Sofia",
        "Daniel",
        "Camila"
    ]

    # Solicitar un nombre al usuario (o recibirlo desde el menú)
    if nombre is None:
        nombre = input("Ingrese el nombre del aprendiz que desea buscar: ")

    # Verificar si el nombre existe en la lista
    if nombre in aprendices:
        posicion = aprendices.index(nombre)
        print(f"El aprendiz {nombre} sí existe en la lista.")
        print(f"Su posición es: {posicion}")
    else:
        print(f"El aprendiz {nombre} no existe en la lista.")
