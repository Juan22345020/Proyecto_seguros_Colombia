

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
frame_superior.config(bg="light blue",bd=5,relief="ridge", width=1250, height=80)
frame_superior.place(x=0, y=0)

frame_izquierdo=Frame(ventana_principal)
frame_izquierdo.config(bg="white",bd=5,relief="groove", width=725, height=580)
frame_izquierdo.place(x=0, y=80)



imagen_i = PhotoImage(file="recomp.png")
lb_imagen_i= Label(frame_izquierdo, image=imagen_i)
lb_imagen_i.place(x=400, y=150)

imagen_b = PhotoImage(file="avion.png")
lb_imagen_b= Label(frame_izquierdo, image=imagen_b)
lb_imagen_b.place(x=400, y=430)

imagen_u = PhotoImage(file="moto.png")
lb_imagen_u= Label(frame_izquierdo, image=imagen_u)
lb_imagen_u.place(x=110, y=420)

imagen_e = PhotoImage(file="comparar.png")
lb_imagen_e= Label(frame_izquierdo, image=imagen_e)
lb_imagen_e.place(x=90, y=150)

frame_derecho=Frame(ventana_principal)
frame_derecho.config(bg="white", bd=5,relief="groove",width=625, height=630)
frame_derecho.place(x=725, y=110)

imagen_d = PhotoImage(file="imagen.png")
lb_imagen_d= Label(frame_derecho, image=imagen_d)
lb_imagen_d.place(x=-80, y=-50)

# Label de bienvenida

Label_bienv = Label(ventana_principal, text="Bienvenido a CRS ")
Label_bienv.config(bg = "light blue",fg="black",font=( "Bodoni MT Black", 20,))
Label_bienv.place(x=520,y=20)

# Label de entrada

Label_entrad = Label(frame_izquierdo, text="Escoge el servicio que deseas utilizar ")
Label_entrad.config(bg = "white",fg="black", font=( "Bodoni MT Black", 22,))
Label_entrad.place(x=80,y=30)

def Abrir_Ventana():
    global toplevel_Ventana
    toplevel_Ventana=Toplevel()
    toplevel_Ventana.title("comparar")
    toplevel_Ventana.resizable(0,0)
    toplevel_Ventana.geometry("800x500")
    toplevel_Ventana.config(bg="pink")

rb_k = Button(frame_izquierdo, text="Comparar", width=10, height=1, bg="gray80",command=Abrir_Ventana)
rb_k.config(bg="white", fg="black", font=("Imprint MT Shadow", 20))
rb_k.place(x=120, y=350)

def Abrir_Ventana2():
    global toplevel_Ventana
    toplevel_Ventana2=Toplevel()
    toplevel_Ventana2.title("comparar")
    toplevel_Ventana2.resizable(0,0)
    toplevel_Ventana2.geometry("800x500")
    toplevel_Ventana2.config(bg="pink")

rb_f = Button(frame_izquierdo, text="Recomendar",width=10, height=1, bg="gray80",command=Abrir_Ventana2 )
rb_f.config(bg="white", fg="black", font=("Imprint MT Shadow", 20))
rb_f.place(x=400, y=350)


ventana_principal.mainloop()