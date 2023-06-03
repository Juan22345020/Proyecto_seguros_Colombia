

from tkinter import * 
from tkinter import messagebox
import random

# Fun
ventana_principal=Tk()
ventana_principal.geometry("1250x650")
ventana_principal.title("Comparador y Recomendador de Aseguradoras en Colombia", )
ventana_principal.resizable(0,0)
ventana_principal.config(bg="white")

# Frames e imagenes

frame_superior=Frame(ventana_principal)
frame_superior.config(bg="blue", width=1250, height=80)
frame_superior.place(x=0, y=0)

frame_izquierdo=Frame(ventana_principal)
frame_izquierdo.config(bg="white", width=725, height=620)
frame_izquierdo.place(x=0, y=110)

imagen_d = PhotoImage(file="comp.png")
lb_imagen_d= Label(frame_izquierdo, image=imagen_d)
lb_imagen_d.place(x=90, y=90)

imagen_i = PhotoImage(file="recomp.png")
lb_imagen_i= Label(frame_izquierdo, image=imagen_i)
lb_imagen_i.place(x=460, y=130)

frame_derecho=Frame(ventana_principal)
frame_derecho.config(bg="white", width=625, height=630)
frame_derecho.place(x=725, y=110)

imagen_d = PhotoImage(file="imagen.png")
lb_imagen_i= Label(frame_derecho, image=imagen_d)
lb_imagen_i.place(x=-80, y=-50)

# Label de bienvenida

Label_bienv = Label(ventana_principal, text="Bienvenido a CRS ")
Label_bienv.config(bg = "blue",fg="white", font=( "Arial Black", 20,))
Label_bienv.place(x=520,y=30)

# Label de entrada

Label_entrad = Label(frame_izquierdo, text="Escoge el servicio que deseas utilizar ")
Label_entrad.config(bg = "white",fg="black", font=( "Arial Black", 20,))
Label_entrad.place(x=100,y=30)


rb_k = Button(frame_izquierdo, text="Comparar", width=10, height=1, bg="gray80" )
rb_k.config(bg="white", fg="black", font=("Italic", 18))
rb_k.place(x=105, y=300)

# Boton 
rb_f = Button(frame_izquierdo, text="Recomendar",width=10, height=1, bg="gray80" )
rb_f.config(bg="white", fg="black", font=("Italic", 18))
rb_f.place(x=465, y=300)


ventana_principal.mainloop()