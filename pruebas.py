import tkinter as tk

def abrir_ventana():
    # Acción que quieres ejecutar al hacer clic en la palabra
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nueva ventana")
    nueva_ventana.geometry("200x200")
    nueva_ventana.mainloop()

def cambiar_color(event):
    etiqueta.config(foreground="blue")

def restaurar_color(event):
    etiqueta.config(foreground="black")

def crear_etiqueta_click(root, texto, palabra):
    global etiqueta
    etiqueta = tk.Label(root, text=texto)

    def clic(event):
        if palabra in etiqueta.cget("text"):
            abrir_ventana()

    etiqueta.bind("<Button-1>", clic)
    etiqueta.bind("<Enter>", cambiar_color)
    etiqueta.bind("<Leave>", restaurar_color)
    etiqueta.pack()

# Crear la ventana principal
root = tk.Tk()

# Crear una etiqueta con la palabra clickeable
crear_etiqueta_click(root, "¡Haz clic en esta palabra!", "palabra")

# Ejecutar la aplicación
root.mainloop()
