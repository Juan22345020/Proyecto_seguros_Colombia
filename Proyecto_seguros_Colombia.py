from tkinter import * 
from tkinter import messagebox
import random

ventana_principal=Tk()
ventana_principal.geometry("1200x600")
ventana_principal.title("Aseguradoras")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="white")

titulo = Label(ventana_principal, text="Comparador y Recomendador de aseguradoras de Colombia")
titulo.config(bg = "white",fg="black", font=("Helvetica", 20))
titulo.place(x=240,y=10)

lb_titulo1=Label(ventana_principal, text="Elige una opción")
lb_titulo1.config( bg="light blue" , fg="black", bd=5,relief="raised",  font=("new time roma",20))
lb_titulo1.place(x=500,y=250)

rb_k = Radiobutton(ventana_principal, text="comparar", value="comparar")
rb_k.config(bg="white", fg="blue", font=("Helvetica", 18))
rb_k.place(x=500, y=300)

# radiobutton para farenheit
rb_f = Radiobutton(ventana_principal, text="recomendar", value="recomendar")
rb_f.config(bg="white", fg="blue", font=("Helvetica", 18))
rb_f.place(x=500, y=350)


ventana_principal.mainloop()