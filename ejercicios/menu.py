# Menú principal del proyecto (interfaz gráfica con tkinter)
import contextlib
import io
import tkinter as tk
from tkinter import scrolledtext

from E28 import ejercicio_28
from Ejercicio18 import ejercicio_18
from epaso25 import ejercicio_25


# Guarda los print() de un ejercicio para mostrarlos en la ventana
def capturar_salida(funcion, *args):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        funcion(*args)
    return buffer.getvalue()


# Ventana modal para hacer un ejercicio (bloquea el menú hasta cerrarla)
def abrir_modal(root, titulo, etiqueta, funcion):
    modal = tk.Toplevel(root)
    modal.title(titulo)
    modal.transient(root)  # se queda encima de la ventana principal
    modal.grab_set()       # el menú no responde hasta cerrar el modal

    # Campo para escribir el dato (solo si el ejercicio lo necesita)
    entrada = None
    if etiqueta:
        tk.Label(modal, text=etiqueta).pack(padx=10, pady=(10, 0))
        entrada = tk.Entry(modal, width=40)
        entrada.pack(padx=10, pady=5)
        entrada.focus_set()

    # Área donde se muestra el resultado del ejercicio
    resultado = scrolledtext.ScrolledText(modal, width=55, height=12)
    resultado.pack(padx=10, pady=10, fill="both", expand=True)

    # Botón que ejecuta el ejercicio y muestra lo que imprime
    def ejecutar():
        resultado.delete("1.0", "end")
        try:
            if entrada is not None:
                texto = capturar_salida(funcion, entrada.get())
            else:
                texto = capturar_salida(funcion)
            resultado.insert("end", texto)
        except Exception as error:
            resultado.insert("end", f"Error inesperado: {error}")

    tk.Button(modal, text="Ejecutar", command=ejecutar).pack(pady=(0, 5))
    tk.Button(modal, text="Cerrar", command=modal.destroy).pack(pady=(0, 10))

    # Con Enter en el campo también se ejecuta
    if entrada is not None:
        modal.bind("<Return>", lambda event: ejecutar())

    return modal


# Mostrar las opciones del menú
def mostrar_menu(root):
    tk.Label(root, text="=== MENÚ DE EJERCICIOS ===",
             font=("Arial", 14, "bold")).pack(pady=12)
    tk.Button(root, text="1. Números primos (18)",
              command=lambda: abrir_modal(root, "Ejercicio 18",
                                          "Valor N:", ejercicio_18)
              ).pack(fill="x", padx=25, pady=5)
    tk.Button(root, text="2. Buscar nombres (25)",
              command=lambda: abrir_modal(root, "Ejercicio 25",
                                          "Nombre del aprendiz:", ejercicio_25)
              ).pack(fill="x", padx=25, pady=5)
    tk.Button(root, text="3. Clasificar positivos, negativos y ceros (28)",
              command=lambda: abrir_modal(root, "Ejercicio 28",
                                          None, ejercicio_28)
              ).pack(fill="x", padx=25, pady=5)
    tk.Button(root, text="0. Salir", command=root.destroy
              ).pack(fill="x", padx=25, pady=(5, 12))


# Ventana principal del programa
def main():
    root = tk.Tk()
    root.title("Menú de ejercicios")
    root.resizable(False, False)
    mostrar_menu(root)
    root.mainloop()


if __name__ == "__main__":
    main()
