
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from tkinter import Listbox

diccionario = {
    'Aseguradora Colpatria':'Nombre: Axa Colpatria\nEdad_minima: 18\nEdad_maxima: 70\nSexo: Ambos\nTipos_seguro: [Vida]\nRelacion calidad/precio: Buena\nventajas: Asistencia en viajes nacionales e internacionales, asistencia en salud, asistencia para mascotas, aseguramiento del cónyuge con descuento en la prima de la cobertura básica.',
    'Aseguradora BBVA':'Nombre: BBVA\nEdad_minima: 18\nEdad_maxima: 70\nSexo: Ambos\nTipos_seguro: [Vida, Auto]\nRelacion Calidad/Precio:Excelente\nventajas: Conoce las ventajas que ofrece el seguro de autos, responsabilidad civil Extracontractual de $4 mil millones, beneficio en la tarifa por ser cliente BBVA, ten la opción de asegurar accesorios valiosos como radios, DVD y otros, disfruta de cobertura nacional',
    'Seguros Colombia S.A':'Nombre: Seguros Colombia S.A\nEdad_minima: 18\nEdad_maxima: 70\nSexo: Ambos\nTipos_seguro: [Salud (CANCER),Auto, Hogar]\nRelacion calidad/precio: Buena\nventajas: Beneficio por Diagnóstico de Cáncer: Se pagará la suma contratada en el caso en que el asegurado sea diagnosticado por primera vez por cáncer, beneficio por Cirugía de Cáncer: Recibirás una indemnización en caso de tener una cirugía relacionada directamente con el cáncer diagnosticado. La cirugía debe practicarse dentro de los doce meses después del diagnóstico de cáncer. Este beneficio se pagará una única vez, y no aplicará en los siguientes casos.',
    'Aseguradora BMI':'Nombre: BMI\nEdad_minima: 18\nEdad_maxima: 70\nSexo: Ambos\nTipos_seguro: [Vida]\nRelacion calidad/precio: Buena\nventajas: Busca proteger y garantizar la calidad de vida de la familia en caso de Fallecimiento o Incapacidad Total y Permanente del asegurado principal, dar continuidad a la Educación de los hijos,garantiza proteger el patrimonio de la familia o beneficiarios, cubre los costos de Fallecimiento, garantiza la calidad de vida de la familia, y continuidad de los proyectos trazados.',
    'Seguros Cardiff':'Nombre: Cardiff Colombia\nEdad_minima: 30\nEdad_maxima: 70\nSexo: Ambos\nTipos_seguro: [Salud (CANCER), Accidentes]\nRelacion Calidad/precio: Regular\nventajas: Con este producto tus beneficiarios recibirán el pago de una indemnización por el valor asegurado, en caso de accidente, muerte accidental u homicidio. Muerte: fallecimiento por cualquier causa (incluida VIH) durante la vigencia de la póliza.Muerte accidental: en los casos en que el tomador del seguro fallezca como consecuencia de un accidente, dentro de la vigencia de la póliza. Renta de libre destinación: en caso de muerte accidental.',
    'Seguros Chubb':'Nombre: Chubb seguros Colombia\nedad_minima: 18\nedad_maxima: 70\nSexo: Ambos\nTipos_seguro: [Accidentes, Hogar]\nRelacion Calidad/precio: Buena\nventajas: Amparo básico de daños materiales por incendio y peligros aliados, huelga, asonada, motín conmoción civil o popular – actos mal intencionados de terceros, terremoto, temblor, erupción volcánica, maremoto, marejada y tsunami.',
    'Seguros Coface':'Nombre: Cofase\nEdad_minima: 18\nEdad_maxima: 70\nSexo: Ambos\nTipos_seguro: [Credito]\nRelacion Calidad/Precio: Excelente\nventajas: Prevención del Riesgo de Impago, Ayuda al desarrollo comercial, Facilita el acceso a la financiación bancaria,facilita el recobro.',
    'Seguros Mundial':'Nombre: Seguros Mundial S.A\nEdad_minima: 18\nEdad_maxima: 70\nSexo: Ambos\nTipos_seguro:[Soat, Arriendo, Accidentes, Vida]\nRelacion Calidad/Precio: Buena\nventajas: Incapacidad total y permanente, indemnización adicional por muerte accidental Y beneficios por desmembración',
    'Seguros Confianza':'Nombre: Seguros Confianza\nEdad_minima: 20\nEdad_maxima: 65\nSexo: Ambos\nTipos_seguro:[Daños materiales, Empresas]\nRelacion Calidad/Precio: Buena\nventajas: Amparo básico de incendio y/o rayo. Terremoto, temblor, erupción volcánica, tsunami. Inundación, avalancha, ciclón, tempestad y cualquier fenómeno hidrometeorológico. Actos mal intencionados de terceros, sabotaje, terrorismo, huelga, motín, conmoción civil o popular. Lucro cesante como consecuencia de cualquier daño material amparado. Rotura de maquinaria. Equipos eléctricos y electrónicos. Sustracción con y sin violencia. Amparos adicionales ajustados a la actividad del cliente.',
    'Global Seguros':'Nombre: Global Seguros\nEdad_minima: 18\nEdad_maxima: 65\nSexo: Ambos\nTipos_seguro[Accidentes, pension, vida]\nRelacion Calidad/Precio: Excelente\nventajas: Es una solución económica, tiene varias opciones de valor asegurado',
    'HDI Seguros':'Nombre: HDI Seguros\nEdad_minima: 14\nEdad_Maxima: 70\nSexo: Ambos\nTipos_seguros[Empresas,Soat]\nRelacion Calidad/Precio: Buena\nventajas: Rentas de libre destinación por Muerte. Rentas de libre destinación por ITP. Renta diaria por hospitalización. Renta diaria post hospitalaria. Renta diaria UCI. Repatriación. Traslado del cuerpo. Asistencias. Auxilio canasta. Auxilio para educación. Incapacidad total temporal. Incapacidad permanente parcial',
    'Positiva Seguros':'Nombre: Positiva Seguras\nEdad_minima: 18\nEdad:maxima: 70\nSexo: Ambos\nTipos_seguros[Pension]\nRelacion Calidad/Precio: Buena\nventajas: Podrás elegir el valor asegurado que mejor se ajuste a tus necesidades, Podrás elegir pagar tus primas de forma mensual, trimestral, semestral o anualmente, Tendrás la opción de decidir si quieres que tu valor asegurado sea constante o creciente, con una valorización anual según tu elección entre el 5% y el 8%. Tenemos a tu disposición diferentes coberturas con las cuales podrás ampliar la cobertura de tu seguro',
    'Seguros Alfa':'Nombre: Seguros Alfa\nEdad_minima: 18\nEdad_maxima: 70\nSexo: Ambos\nTipos_seguros[Funeral]\nRelacion Calidad/Precio: Buena\nventajas: Fallecimiento o Muerte accidental.',
    'Seguros Skandia': 'Nombre: Seguros Skandia\nEdad_minima: 18\nEdad_maxima: 65\nSexo: Ambos\nTipos_seguros[Pension]\nRelacion Calidad/Precio: Excelente\nventajas: Jubilación Voluntaria, ITP (Incapacidad Total y Permanente entendida como la pérdida del 50% y más de la capacidad laboral del asegurado, como consecuencia de lesiones corporales causadas por accidente o enfermedad, sea o no de origen profesional).',
    'Panamerican Seguros': 'Nombre: Panamerican Seguros\nEdad_minima: 18\nEdad_maxima: 70\nSexo: Ambos\nTipos_seguros[Vida]\nRelacion Calidad/Precio: Excelente\nventajas: Anticipo del Amparo por Muerte por Enfermedad Terminal, seguro por incapacidad total y permanente por causa de enfermedad ante la ocurrencia de una incapacidad total',
    
    
}




def Abrir_Ventana():
    global diccionario
    global toplevel_Ventana
    global imagen_fondo
    toplevel_Ventana=Toplevel()
    toplevel_Ventana.title("comparar")
    toplevel_Ventana.resizable(0,0)
    toplevel_Ventana.geometry("1100x600")
    toplevel_Ventana.config(bg="white")
    
    
    imagen_fondo = PhotoImage(file="fondo2.gif")
    fondo1 = Label(toplevel_Ventana, image=imagen_fondo)
    fondo1.place(x=0, y=80)

    comparar_frame= Frame(toplevel_Ventana)
    comparar_frame.config(bg="light green",bd=5, relief="ridge",width=1100, height=80)
    comparar_frame.place(x=0, y=0)
    

    titulo_label =Label(comparar_frame, text="Comparar " )
    titulo_label.config(bg="light green", fg="green", font=("Bodoni MT Black",24))
    titulo_label.place(x=450, y=15)
    
    seguro1_label =Label(toplevel_Ventana, text="Aseguradora 1 " )
    seguro1_label.config(bg="white", fg="green", font=("Imprint MT Shadow",30))
    seguro1_label.pack()
    seguro1_label.place(x=80, y=110)

    seguro2_label =Label(toplevel_Ventana, text="Aseguradora 2" )
    seguro2_label.config(bg="white", fg="green", font=("Imprint MT Shadow",30))
    seguro2_label.pack()
    seguro2_label.place(x=720, y=110)

    
    opciones_seguro_1 = ttk.Combobox(toplevel_Ventana, values=list(diccionario.keys()), font=("Helvetica", 12))
    opciones_seguro_1.place(x=100, y=170)

    opciones_seguro_2 = ttk.Combobox(toplevel_Ventana, values=list(diccionario.keys()), font=("Helvetica", 12))
    opciones_seguro_2.place(x=745, y=170)
   

    def imprimir_resultados():
      clave1 = opciones_seguro_1.get()
      clave2 = opciones_seguro_2.get()
    
      resultado1 = diccionario.get(clave1, '')
      resultado2 = diccionario.get(clave2, '')

      texto_resultados1.delete(1.0, tk.END) 
      texto_resultados1.insert(tk.END, f' {resultado1}\n')

      texto_resultados2.delete(1.0, tk.END)  
      texto_resultados2.insert(tk.END, f' {resultado2}\n')



    

    texto_resultados1 = tk.Text(toplevel_Ventana, height=20, width=45)
    texto_resultados1.pack()
    texto_resultados1.place(x=40, y=200)


    texto_resultados2 = tk.Text(toplevel_Ventana, height=20, width=45)
    texto_resultados2.pack()
    texto_resultados2.place(x=680, y=200)
    
  


    rb_k = Button(toplevel_Ventana, text="Comparar", width=7, height=1, bg="gray80")
    rb_k.config(bg="white", fg="green", font=("Imprint MT Shadow", 20), command=imprimir_resultados)
    rb_k.place(x=485, y=300)




aseguradoras = [
    {
        'nombre': 'Axa Colpatria',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Vida'],
        'información':'Aseguramos tu futuro y el de tu familia. Con esta póliza atenderemos tus necesidades de protección con un amparo básico que te protege en caso de fallecimiento, brindándote anticipo de gastos exequiales, así como exoneración de pago de primas en caso de incapacidad total y permanente.',
        'ventajas': 'Asistencia en viajes nacionales e internacionales, asistencia en salud, asistencia para mascotas, aseguramiento del cónyuge con descuento en la prima de la cobertura básica.'
    },
    {
        'nombre': 'BBVA',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Auto'],
        'información':'Aprovecha al máximo tu vehículo con la confianza de estar asegurado con BBVA en alianza con Zurich Seguro. Protección para ti, tu vehículo y ocupantes.',
        'ventajas':'Conoce las ventajas que ofrece el seguro de autos, responsabilidad civil Extracontractual de $4 mil millones, beneficio en la tarifa por ser cliente BBVA, ten la opción de asegurar accesorios valiosos como radios, DVD y otros, disfruta de cobertura nacional'
    },
    {
        'nombre': 'Seguros Colombia S.A',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Salud (CANCER)'],
        'información':'El Seguro de Salud para Cáncer y Enfermedades Graves te respalda en aquellas situaciones inesperadas para proteger tu salud y tu tranquilidad.',
        'ventajas':'Beneficio por Diagnóstico de Cáncer: Se pagará la suma contratada en el caso en que el asegurado sea diagnosticado por primera vez por cáncer, beneficio por Cirugía de Cáncer: Recibirás una indemnización en caso de tener una cirugía relacionada directamente con el cáncer diagnosticado. La cirugía debe practicarse dentro de los doce meses después del diagnóstico de cáncer. Este beneficio se pagará una única vez, y no aplicará en los siguientes casos.'
    },
    {
        'nombre': 'BMI',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Vida'],
        'información':'Este seguro de vida temporal de 5-30 años, busca resguardar y garantizar la calidad de vida de la familia en caso de Fallecimiento o Incapacidad Total y Permanente del asegurado principal, brindando la protección activa que le permita a la familia mantener su nivel de vida y continuar con los proyectos trazados.',
        'ventajas':'Busca proteger y garantizar la calidad de vida de la familia en caso de Fallecimiento o Incapacidad Total y Permanente del asegurado principal, dar continuidad a la Educación de los hijos,garantiza proteger el patrimonio de la familia o beneficiarios, cubre los costos de Fallecimiento, garantiza la calidad de vida de la familia, y continuidad de los proyectos trazados.'
    },
    {
        'nombre': 'Cardiff Colombia',
        'edad_minima': 30,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Accidentes'],
        'información':'Sabemos que el peligro puede estar en cualquier parte; por eso estamos contigo en los momentos más difíciles. Contamos con un seguro que le brinda a tu familia la protección que necesita, en caso de muerte o lesiones personales, que se genere por una causa accidental.',
        'ventajas':'Con este producto tus beneficiarios recibirán el pago de una indemnización por el valor asegurado, en caso de accidente, muerte accidental u homicidio. Muerte: fallecimiento por cualquier causa (incluida VIH) durante la vigencia de la póliza.Muerte accidental: en los casos en que el tomador del seguro fallezca como consecuencia de un accidente, dentro de la vigencia de la póliza. Renta de libre destinación: en caso de muerte accidental.'
    },
    {
        'nombre': 'Chubb seguros Colombia',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': [ 'Hogar'],
        'información':'Para tu hogar, Chubb te provee una amplia variedad de coberturas para proteger tu patrimonio familiar representado en la vivienda y sus contenidos frente a los riesgos a los que se encuentren expuestos tales como incendios, desastres de la naturaleza (terremotos, inundaciones, vientos fuertes), y actos mal intencionados de terceros, entre otros.',
        'ventajas':'Amparo básico de daños materiales por incendio y peligros aliados, huelga, asonada, motín conmoción civil o popular – actos mal intencionados de terceros, terremoto, temblor, erupción volcánica, maremoto, marejada y tsunami.'
    },
    {
        'nombre': 'Cofase',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Credito'],
        'información':'El seguro de crédito es una herramienta eficaz para la gestión del riesgo comercial que protege a las empresas frente a los costes e inconvenientes derivados del impago de sus créditos comerciales.',
        'ventajas':'Prevención del Riesgo de Impago, Ayuda al desarrollo comercial, Facilita el acceso a la financiación bancaria,facilita el recobro.'
    },
    {
        'nombre': 'Skandia',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Pensión'],
        'información':'Te ofrece un respaldo efectivo y oportuno a partir del momento en que hayas definido recibir la renta.',
        'ventajas':'Jubilación Voluntaria, ITP (Incapacidad Total y Permanente entendida como la pérdida del 50% y más de la capacidad laboral del asegurado, como consecuencia de lesiones corporales causadas por accidente o enfermedad, sea o no de origen profesional).'
    },
    {
        'nombre': 'PAN AMERICAN LIFE COLOMBIA',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Vida'],
        'información':'Este es un producto de seguro de vida que le brindará a su familia protección económica ante la ocurrencia del fallecimiento del asegurado a causa de accidente o enfermedad.Brinda en vida la oportunidad de constituir un fondo de ahorro para la realización de proyectos tan importantes como: Saldar la hipoteca del hogar familiar , Asegurar la educación superior de los hijos ,Disfrutar de una mejor jubilación.',
        'ventajas':'Anticipo del Amparo por Muerte por Enfermedad Terminal, seguro por incapacidad total y permanente por causa de enfermedad ante la ocurrencia de una incapacidad total'
    },
    {
        'nombre': 'POSITIVA COMPAÑIA DE SEGUROS',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Pensión'],
        'información':'Este seguro te ofrece un soporte económico, con el cual podrás garantizar la tranquilidad de tu familia y la tuya , en caso de un imprevisto que afecte tu vida.',
        'ventajas':'Podrás elegir el valor asegurado que mejor se ajuste a tus necesidades, Podrás elegir pagar tus primas de forma mensual, trimestral, semestral o anualmente, Tendrás la opción de decidir si quieres que tu valor asegurado sea constante o creciente, con una valorización anual según tu elección entre el 5% y el 8%. Tenemos a tu disposición diferentes coberturas con las cuales podrás ampliar la cobertura de tu seguro.'
    },
    {
        'nombre': 'Seguros Alfa',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Funeral'],
        'información':'Cubrimos tus gastos de funeral y de entierro del titular.',
        'ventajas':'Fallecimiento o Muerte accidental.'
    },
    {
        'nombre': 'Seguros Mundial S.A',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Vida'],
        'información':'El seguro de vida respalda la familia ante un eventual apremio económico en caso de fallecimiento por cualquier causa de la persona asegurada, cuando ocurra durante la vigencia de la póliza.',
        'ventajas':'Incapacidad total y permanente, indemnización adicional por muerte accidental Y beneficios por desmembración'
    },
    {
        'nombre': 'Seguros Confianza',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Empresas'],
        'información':'Ofrecemos una cobertura integral para las empresas del país, Seguros Confianza ha desarrollado un seguro para proteger a nuestros clientes de posibles daños que puedan ocurrir en el desarrollo de sus actividades.',
        'ventajas':'Amparo básico de incendio y/o rayo. Terremoto, temblor, erupción volcánica, tsunami. Inundación, avalancha, ciclón, tempestad y cualquier fenómeno hidrometeorológico. Actos mal intencionados de terceros, sabotaje, terrorismo, huelga, motín, conmoción civil o popular. Lucro cesante como consecuencia de cualquier daño material amparado. Rotura de maquinaria. Equipos eléctricos y electrónicos. Sustracción con y sin violencia. Amparos adicionales ajustados a la actividad del cliente.'
    },
    {
        'nombre': 'Global Seguros',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Accidentes'],
        'información':'Su función es proteger la estabilidad económica de la familia ante la muerte del asegurado como consecuencia de un accidente de origen común (accidente no laboral), e incluso ante imprevistos derivados del accidente que generen incapacidad, hospitalización o gastos médicos siempre y cuando estén contratados estos amparos.',
        'ventajas':'Es una solución económica, tiene varias opciones de valor asegurado'
    },
    {
        'nombre': 'HDI Seguros',
        'edad_minima': 18,
        'edad_maxima': 70,
        'sexo': 'Ambos',
        'tipos_seguro': ['Empresas'],
        'información':'El seguro de Vida Grupo es una póliza creada por HDI Seguros para empresas, fondos de empleados, asociaciones y cooperativas que agrupen empleados de una sola entidad y deseen beneficiarlos con una póliza que en caso de fallecimiento cubra a sus familiares. En HDI SEGUROS, ayudamos a las empresas a brindar a sus empleados y a sus familias, la protección que merecen.',
        'ventajas':'Rentas de libre destinación por Muerte. Rentas de libre destinación por ITP. Renta diaria por hospitalización. Renta diaria post hospitalaria. Renta diaria UCI. Repatriación. Traslado del cuerpo. Asistencias. Auxilio canasta. Auxilio para educación. Incapacidad total temporal. Incapacidad permanente parcial.'
    }
]

def Abrir_Ventana2():
    global aseguradoras
    global imagen_fondo1
    toplevel_Ventana2=Toplevel()
    toplevel_Ventana2.title("comparar")
    toplevel_Ventana2.resizable(0,0)
    toplevel_Ventana2.geometry("1205x600")
    toplevel_Ventana2.config(bg="royalblue")

    
    imagen_fondo1 = PhotoImage(file="fondo1.gif")
    fondo12 = Label(toplevel_Ventana2, image=imagen_fondo1, width=1200, height=500)
    fondo12.place(x=0, y=70)


    frame_izquierdo2 = Frame(toplevel_Ventana2)
    frame_izquierdo2.config(bg="white", bd=5, relief="groove", width=500, height=500)
    frame_izquierdo2.place(x=0, y=80)

    frame_derecho2 = Frame(toplevel_Ventana2)
    frame_derecho2.config(bg="white", bd=5, relief="groove", width=500, height=500)
    frame_derecho2.place(x=705, y=80)

    frame_superior1 = Frame(toplevel_Ventana2)
    frame_superior1.config(bg="royalblue", bd=5, relief="ridge", width=1205, height=80)
    frame_superior1.place(x=0, y=0)

    Label_recomendacion = Label(toplevel_Ventana2, text="RECOMENDADOR")
    Label_recomendacion.config(bg="royalblue", fg="black", font=("Bodoni MT Black", 20,))
    Label_recomendacion.place(x=480, y=20)

    Label_entrad1 = Label(frame_izquierdo2, text="Nombre")
    Label_entrad1.config(bg="white", fg="black", font=("Bodoni MT Black", 10))
    Label_entrad1.place(x=80, y=30)

    entrada1 = Entry(frame_izquierdo2)
    entrada1.place(x=200, y=30)

    Label_entrad2 = Label(frame_izquierdo2, text="Edad")
    Label_entrad2.config(bg="white", fg="black", font=("Bodoni MT Black", 10))
    Label_entrad2.place(x=80, y=60)

    entrada2 = Entry(frame_izquierdo2)
    entrada2.place(x=200, y=60)

    Label_entrad3 = Label(frame_izquierdo2, text="Sexo")
    Label_entrad3.config(bg="white", fg="black", font=("Bodoni MT Black", 10))
    Label_entrad3.place(x=80, y=90)

    def reiniciar():
      entrada1.delete(0, tk.END)
      entrada2.delete(0, tk.END)
      seleccion_sexo.set(opciones_sexo[0])
      checklist_seguro.selection_clear(0, tk.END)
      resultado_texto.config(state=tk.NORMAL)
      resultado_texto.delete("1.0", tk.END)
      resultado_texto.config(state=tk.DISABLED)

    opciones_sexo = ["Masculino", "Femenino"]
    seleccion_sexo = tk.StringVar(value=opciones_sexo)
    radiobutton_sexo1 = tk.Radiobutton(frame_izquierdo2, text=opciones_sexo[0], variable=seleccion_sexo, value=opciones_sexo[0])
    radiobutton_sexo2 = tk.Radiobutton(frame_izquierdo2, text=opciones_sexo[1], variable=seleccion_sexo, value=opciones_sexo[1])
    radiobutton_sexo1.place(x=200, y=90)
    radiobutton_sexo2.place(x=200, y=120)

    Label_entrad4 = tk.Label(frame_izquierdo2, text="Tipo de seguro")
    Label_entrad4.config(bg="white", fg="black", font=("Bodoni MT Black", 10))
    Label_entrad4.place(x=80, y=150)

    
    
   
    opciones_seguro = ["Vida", "Auto", "Salud (CANCER)", "Hogar", "Accidentes", "Credito", "Funeral", "Empresas","Pensión"]
    seleccion_seguro = tk.StringVar(value=opciones_seguro)
    checklist_seguro = tk.Listbox(frame_izquierdo2, listvariable=seleccion_seguro, height=6)
    checklist_seguro.place(x=200, y=150)
    scrollbar = tk.Scrollbar(toplevel_Ventana2)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    resultado_texto = tk.Text(frame_derecho2)
    resultado_texto.config(font=("Arial", 12), state=tk.DISABLED, wrap=tk.WORD)
    resultado_texto.place(relwidth=1, relheight=1)
    resultado_texto.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=resultado_texto.yview)

    def obtener_recomendaciones():
        nombre = entrada1.get()
        edad = int(entrada2.get())
        sexo = seleccion_sexo.get()
        tipos_seguro = checklist_seguro.curselection()

    # Convertir los índices seleccionados a los tipos de seguro correspondientes
        tipos_seguro_seleccionados = [opciones_seguro[i] for i in tipos_seguro]

        aseguradoras_filtradas = []
        for aseguradora in aseguradoras:
          if (edad >= aseguradora['edad_minima'] and
                edad <= aseguradora['edad_maxima'] and
                (aseguradora['sexo'] == 'Ambos' or aseguradora['sexo'] == sexo) and
                any(tipo in aseguradora['tipos_seguro'] for tipo in tipos_seguro_seleccionados)):
            aseguradoras_filtradas.append(aseguradora)

          resultado_texto.config(state=tk.NORMAL)
          resultado_texto.delete("1.0", tk.END)

        if len(aseguradoras_filtradas) >= 0:
            resultado_texto.insert(tk.END,"Hola " +nombre+ ", te recomendamos las siguients aseguradoras que ofrecen el tipo de seguro seleccionado: \n")
            for aseguradora in aseguradoras_filtradas:
                resultado_texto.insert(tk.END, "Nombre: " + aseguradora['nombre'] + "\n")
                resultado_texto.insert(tk.END, "Edad mínima: " + str(aseguradora['edad_minima']) + "\n")
                resultado_texto.insert(tk.END, "Edad máxima: " + str(aseguradora['edad_maxima']) + "\n")
                resultado_texto.insert(tk.END, "Sexo: " + aseguradora['sexo'] + "\n")
                resultado_texto.insert(tk.END, "Tipos de seguro: " + ", ".join(aseguradora['tipos_seguro']) + "\n")
                resultado_texto.insert(tk.END, "Información: " + "".join(aseguradora['información']) + "\n")
                resultado_texto.insert(tk.END, "Ventajas: " + "".join(aseguradora['ventajas']) + "\n")
                resultado_texto.insert(tk.END,"-------------------------------------------------------------------------------------------------\n")
        else:
           resultado_texto.insert(tk.END, "Lo sentimos" + nombre + ", No se encontraron aseguradoras que ofrezcan el tipo de seguro seleccionado.\n")

        resultado_texto.config(state=tk.DISABLED)
          
    boton_recomendar2 = Button(frame_izquierdo2, text="Recomendar", command=obtener_recomendaciones)
    boton_recomendar2.config(font=("Bodoni MT Black", 12), bg="light blue")
    boton_recomendar2.place(x=100, y=400)

    boton_reiniciar = Button(frame_izquierdo2, text="Reiniciar", command=reiniciar)
    boton_reiniciar.config(font=("Bodoni MT Black", 12), bg="light blue")
    boton_reiniciar.place(x=240, y=400)

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

imagen_xx = PhotoImage(file="recomp.png")
lb_imagen_xx=Label(frame_izquierdo, image=imagen_xx)
lb_imagen_xx.place(x=400, y=150)

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

rb_f = Button(frame_izquierdo, text="Recomendar",width=10, height=1, bg="gray80",command=Abrir_Ventana2 )
rb_f.config(bg="light blue", fg="black", font=("Imprint MT Shadow", 20))
rb_f.place(x=400, y=350)

rb_k =Button(frame_izquierdo, text="Comparar", width=10, height=1, bg="gray80",command=Abrir_Ventana)
rb_k.config(bg="light blue", fg="black", font=("Imprint MT Shadow", 20))
rb_k.place(x=120, y=350)


ventana_principal.mainloop()