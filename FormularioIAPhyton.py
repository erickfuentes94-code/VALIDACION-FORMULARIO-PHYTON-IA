
import tkinter as tk
from tkinter import messagebox
import re


# VALIDACIONES

def EnteroValido(valor):
    try:
        return int(valor) >= 0
    except ValueError:
        return False


def DecimalValido(valor):
    try:
        numero = float(valor.replace(",", "."))
        return numero > 0
    except ValueError:
        return False


def TelefonoValido(valor):
    return valor.isdigit() and len(valor) == 10


def TextoValido(valor):
    valor = valor.strip()
    return (
        bool(valor)
        and any(letra.isalpha() for letra in valor)
        and all(letra.isalpha() or letra.isspace()
                for letra in valor)
    )


# LIMPIAR FORMULARIO

def borrar():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    rbSeleccionGenero.set(0)
    tbNombre.focus_set()


# GUARDAR INFORMACION

def guardar():
    nombres = tbNombre.get().strip()
    apellidos = tbApellidos.get().strip()
    edad = tbEdad.get().strip()
    tel = tbTelefono.get().strip()
    estatura = tbEstatura.get().strip()

    opciones_genero = {
        1: "Masculino",
        2: "Femenino",
        3: "No definido"
    }
    genero = opciones_genero.get(rbSeleccionGenero.get(), "")

    # Verificar campos vacios
    if not all([nombres, apellidos, edad, tel, estatura]):
        messagebox.showerror(
            "Campos incompletos",
            "Completa todos los campos antes de guardar."
        )
        return

    # Validar nombres y apellidos
    if not TextoValido(nombres):
        messagebox.showerror(
            "Nombre incorrecto",
            "El nombre debe contener solamente letras y espacios."
        )
        tbNombre.focus_set()
        return

    if not TextoValido(apellidos):
        messagebox.showerror(
            "Apellidos incorrectos",
            "Los apellidos deben contener solamente letras y espacios."
        )
        tbApellidos.focus_set()
        return

    # Validar edad
    if not edad.isdigit() or not EnteroValido(edad):
        messagebox.showerror(
            "Edad incorrecta",
            "Ingresa una edad entera igual o mayor que cero."
        )
        tbEdad.focus_set()
        return

    # Validar estatura
    if not DecimalValido(estatura):
        messagebox.showerror(
            "Estatura incorrecta",
            "Ingresa una estatura positiva, por ejemplo 1.70."
        )
        tbEstatura.focus_set()
        return

    # Validar telefono
    if not TelefonoValido(tel):
        messagebox.showerror(
            "Telefono incorrecto",
            "El telefono debe contener exactamente 10 digitos."
        )
        tbTelefono.focus_set()
        return

    # Validar seleccion de genero
    if not genero:
        messagebox.showerror(
            "Genero no seleccionado",
            "Selecciona una opcion de genero."
        )
        return

    # Preparar registro
    datos = (
        f"Nombre: {nombres}\n"
        f"Apellidos: {apellidos}\n"
        f"Edad: {edad}\n"
        f"Telefono: {tel}\n"
        f"Estatura: {estatura.replace(',', '.')}\n"
        f"Genero: {genero}\n"
        "------------------------------\n"
    )

    # Guardar en el archivo TXT
    try:
        with open("DatosN3_13Feb26.txt", "a", encoding="utf-8") as archivo:
            archivo.write(datos)

        messagebox.showinfo(
            "Registro exitoso",
            "Los datos se guardaron correctamente.\n\n" + datos
        )
        borrar()

    except OSError as error:
        messagebox.showerror(
            "Error al guardar",
            f"No fue posible guardar los datos.\nDetalle: {error}"
        )


# CREAR VENTANA

ventana = tk.Tk()
ventana.configure(bg="pink")
ventana.geometry("380x570")
ventana.title("Actividad 04 - Formulario de Registro Vr. 002")

rbSeleccionGenero = tk.IntVar(value=0)


# CAMPOS DEL FORMULARIO

tk.Label(
    ventana, text="Nombre:",
    font=("Segoe UI", 14, "bold"), bg="pink"
).pack(padx=10, pady=8)

tbNombre = tk.Entry(ventana, width=35, justify="center")
tbNombre.pack()

tk.Label(
    ventana, text="Apellidos:",
    font=("Segoe UI", 14, "bold"), bg="pink"
).pack(padx=10, pady=8)

tbApellidos = tk.Entry(ventana, width=35, justify="center")
tbApellidos.pack()

tk.Label(
    ventana, text="Edad:",
    font=("Segoe UI", 14, "bold"), bg="pink"
).pack(padx=10, pady=8)

tbEdad = tk.Entry(ventana, width=10, justify="center")
tbEdad.pack()

tk.Label(
    ventana, text="Estatura:",
    font=("Segoe UI", 14, "bold"), bg="pink"
).pack(padx=10, pady=8)

tbEstatura = tk.Entry(ventana, width=15, justify="center")
tbEstatura.pack()

tk.Label(
    ventana, text="Telefono:",
    font=("Segoe UI", 14, "bold"), bg="pink"
).pack(padx=10, pady=8)

tbTelefono = tk.Entry(ventana, width=35, justify="center")
tbTelefono.pack()


# OPCIONES DE GENERO

gb = tk.LabelFrame(
    ventana, text="Seleccione un genero:",
    padx=10, pady=8, bg="pink"
)
gb.pack(padx=10, pady=8)

rbMasculino = tk.Radiobutton(
    gb, text="Masculino", value=1,
    variable=rbSeleccionGenero, bg="pink"
)
rbMasculino.grid(column=0, row=0)

rbFemenino = tk.Radiobutton(
    gb, text="Femenino", value=2,
    variable=rbSeleccionGenero, bg="pink"
)
rbFemenino.grid(column=1, row=0)

rbNoDefinido = tk.Radiobutton(
    gb, text="No definido", value=3,
    variable=rbSeleccionGenero, bg="pink"
)
rbNoDefinido.grid(column=2, row=0)


# BOTONES

gb2 = tk.LabelFrame(ventana, text="", bg="pink")
gb2.pack(padx=10, pady=8)

btnBorrar = tk.Button(
    gb2, text="Borrar", width=10,
    padx=10, pady=8, command=borrar
)
btnBorrar.grid(column=0, row=0, padx=5)

btnGuardar = tk.Button(
    gb2, text="Guardar", width=10,
    padx=10, pady=8, command=guardar
)
btnGuardar.grid(column=1, row=0, padx=5)

ventana.mainloop()

