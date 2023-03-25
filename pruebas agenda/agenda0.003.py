#----------------------------------------
#    MI PRIMER PROGRAMA EN PYTHON
#   INTEGRANTES DEL GRUPO
#   JUAN MANUEL BARRIONUEVO DNI 25753378
#   MARCELO ARGAÑARAZ DNI 16722218
#   NICOLAS LUTRI DNI 32630619
#----------------------------------------
import csv
from tkinter import *
import tkinter as tk
from tkinter import ttk

from tkcalendar import Calendar, DateEntry
import datetime
from datetime import *
import os
# Obtener la ruta absoluta del archivo actual (el script de Python).
abs_path = os.path.abspath(__file__)
# Obtener el directorio de la ruta del archivo.
dir_path = os.path.dirname(abs_path)
# Cambiar la carpeta de trabajo actual a la ubicación del archivo.
os.chdir(dir_path)
var_datos_lst=[]
class frametopmenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frametopm=tk.Frame(master, width=900, height=100,bg="black")
        #self.frametopm.place(x=0,y=0)
        self.frametopm.grid(row=0,column=0,columnspan=2)

class frametopleft(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frametopl=tk.Frame(master, width=0, height=0,bg="blue")
        self.frametopl.grid(row=1,column=0)
        

class frametoprigth(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frametopr=tk.Frame(master, width=600, height=400,bg="black")
        self.frametopr.grid(column=1,row=1)
         # Crear el Treeview con columnas de horas y días
        self.treeview = ttk.Treeview(self.frametopr, columns=("Horas", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"), show="headings")
        self.treeview.heading("Horas", text="Horas")
        self.treeview.heading("Lunes", text="Lunes")
        self.treeview.heading("Martes", text="Martes")
        self.treeview.heading("Miércoles", text="Miércoles")
        self.treeview.heading("Jueves", text="Jueves")
        self.treeview.heading("Viernes", text="Viernes")
        self.treeview.heading("Sábado", text="Sábado")
        self.treeview.heading("Domingo", text="Domingo")
        self.treeview.column("Horas",width=60)
        self.treeview.column("Lunes",width=80)
        self.treeview.column("Martes",width=80)
        self.treeview.column("Miércoles",width=80)
        self.treeview.column("Jueves",width=80)
        self.treeview.column("Viernes",width=80)
        self.treeview.column("Sábado",width=80)
        self.treeview.column("Domingo",width=80)
        self.lbl_semanal=tk.Label(self.frametopr)
        self.lbl_semanal.config(text="Calendario Semanal")
        self.lbl_semanal.grid(column=1,row=0,sticky="NSEW")
        self.treeview.grid(column=1, row=2,sticky="NSEW")
        


class Framebottom(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame1=tk.Frame(root, width=600, height=600,bg="red")
        self.frame1.place(x=10, y=450,relwidth=0.9)
        self.listratree1=ttk.Treeview(self.frame1, columns=("col0","col1", "col2", "col3"), show="headings")
        self.listratree1.column('col0',width=30)
        self.listratree1.column('col1',width=100)
        self.listratree1.column('col2',width=100)
        self.listratree1.column('col3',width=300) #esta columna tiene ancho automatico stretch=tk.YES 
        
        self.listratree1.grid(row=0, column=0,sticky="nswe")
        
        #self.frame1.rowconfigure(0,weight=1)
        #self.listratree1.pack(side="top", fill="both", expand=False)
        self.listratree1.heading("col0", text="Nº")
        self.listratree1.heading("col1", text="Fecha")
        self.listratree1.heading("col2", text="Hora")
        self.listratree1.heading("col3", text="Titulo")
        self.btn_crear_evento = tk.Button(self.frame1,text="Crear Evento",command=self.crearevento_tk)
        #self.btn_crear_evento.pack(side="left")
        self.btn_borrar_evento=tk.Button(self.frame1,text="Eliminar Evento")
        #self.btn_borrar_evento.pack(side="right")
        self.btn_crear_evento.grid(row=1, column=0,sticky="w")
        #self.btn_crear_evento = tk.Button(self.frame1,text="Eliminar Evento")
        self.btn_borrar_evento.grid(row=1, column=0,sticky="e")

    def crearevento_tk(self):
        self.ventana = tk.Toplevel(self)
        self.ventana.geometry("350x200")
        self.ventana.title("Crear evento")
        self.variable_checkbox = tk.BooleanVar()
        self.etiqueta_fecha = tk.Label(self.ventana, text="Fecha:")
        self.etiqueta_fecha.grid(row=0, column=0)
        self.fecha = DateEntry(self.ventana, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.fecha.grid(row=0, column=1)
        
        self.etiqueta_hora = tk.Label(self.ventana, text="Hora HH:mm:ss")
        self.etiqueta_hora.grid(row=1, column=0)
        self.hora = tk.Entry(self.ventana)
        self.hora.grid(row=1, column=1)

        self.etiqueta_titulo = tk.Label(self.ventana, text="Título:")
        self.etiqueta_titulo.grid(row=2, column=0)
        self.titulo = tk.Entry(self.ventana)
        self.titulo.grid(row=2, column=1)
        
        self.etiqueta_descripcion = tk.Label(self.ventana, text="Descripción:")
        self.etiqueta_descripcion.grid(row=3, column=0)
        self.descripcion = tk.Entry(self.ventana)
        self.descripcion.grid(row=3, column=1)
        
        self.etiqueta_detalle = tk.Label(self.ventana, text="Detalle:")
        self.etiqueta_detalle.grid(row=4, column=0)
        self.detalle = tk.Entry(self.ventana)
        self.detalle.grid(row=4, column=1)
                
        self.checkbox = tk.Checkbutton(self.ventana, text="Es importante?", variable=self.variable_checkbox)
        self.checkbox.grid(row=5,column=1)    
        
        boton_guardar = tk.Button(self.ventana, text="Guardar", command=lambda: agenda.agregar_evento(self.fecha.get_date(),self.hora.get(), self.titulo.get(),self.descripcion.get(),self.detalle.get(),self.variable_checkbox.get(),self.ventana))
        boton_guardar.grid(row=10, column=1)

class TreeViewFrame(tk.Frame):
    """clase para crear el frame y un par de botones"""
    def __init__(self, master):
        super().__init__(master)
        

        


class Agenda:
    """ clase agenda que permite crear modificar y eliminar eventos, tambien busca eventos que se repitan """
    def __init__(self):
        self.eventos = []  #creo la variable que almacena los eventos
        self.id_counter = 0 #inicializo el contador de id de eventos
        self.var_datos_lst = []
        global vardatos
        
    def agregar_evento(self, fecha, hora, duracion, titul, importancia, criterios, detalle):
        """ metodo para agregar un evento"""
        fecha_hora = datetime.strptime(fecha + " " + hora, "%d/%m/%Y %H:%M")
        fin_evento = fecha_hora + timedelta(hours=int(duracion.split()[0]))
        if self.verificar_superposicion(fecha_hora, fin_evento):
            print("El nuevo evento se superpone con otro evento existente en la agenda.")
            return
        nuevo_evento = {"id": self.id_counter, "fecha": fecha, "hora": hora, "titulo": titul, "duracion": duracion, "importancia": importancia, "criterios": criterios, "detalle": detalle}
        self.eventos.append(nuevo_evento) #agrego el evento
        self.id_counter += 1  #sumo 1 al contador de eventos

    def verificar_superposicion(self, fecha_hora, fin_evento):
        """metodo para verificar si ya existe un evento con misma fecha y hora o se superpone con otro, devuelve un booleano true o false"""
        
        for evento in self.eventos:
            inicio_evento = datetime.strptime(evento["fecha"] + " " + evento["hora"], "%d/%m/%Y %H:%M")
            fin_evento_existente = inicio_evento + timedelta(hours=int(evento["duracion"].split()[0]))
            if inicio_evento <= fecha_hora < fin_evento_existente or inicio_evento < fin_evento <= fin_evento_existente:
                return True
        
        return False

    def agregar_eventos_mensual(self):
        """ metodo para agregar eventos en el calendario """
        for evento in self.eventos:
            evento_parseado= datetime.strptime(evento["fecha"] + " " + evento["hora"], "%d/%m/%Y %H:%M")
            cal.calevent_create(evento_parseado, evento["titulo"], 'mensaje')
            
    
    def mostrar_eventos_tk(self):
        """metodo para mostrar eventos en el calendario mensual y marcarlos con color distinto"""
        for evento in self.eventos:
            evento_parseado= datetime.strptime(evento["fecha"] + " " + evento["hora"], "%d/%m/%Y %H:%M")
            cal.calevent_create(evento_parseado, evento["hora"]+evento["titulo"], 'mensaje')
            
    
    

    def mostrar_eventos(self):
        """ metodo para mostrar los eventos en consola"""
        eventos_ordenados = sorted(self.eventos, key=lambda evento: evento["id"]) #ordeno los eventos por numero de id
        for evento in eventos_ordenados: #recorro la lista de eventos evento por evento
            print("ID: ", evento["id"])
            print("Fecha: ", evento["fecha"])
            print("Hora: ", evento["hora"])
            print("Duración: ", evento["duracion"])
            print("Importancia: ", evento["importancia"])
            print("Criterios de búsqueda: ", evento["criterios"])
            print("Detalle: ", evento["detalle"])
            print()
        
    def modificar_evento(self, id, fecha=None, hora=None, duracion=None, tit=None, importancia=None, criterios=None, detalle=None):
        """metodo para modificar un evento por numero de id, le tengo q pasar como parametro el id y alguno de los atributos a modificar"""
        evento_encontrado = False
        for evento in self.eventos: #recorro los paramtros ingresados en busqueda de algo para modificar, si el valor es none no modifico nada
            if evento["id"] == id: #recorro la lista de eventos por id si la encuentro hago lo que sigue
                if fecha is not None: #si el atributo tiene un valos distinto a none lo modifico
                    evento["fecha"] = fecha
                if hora is not None:
                    evento["hora"] = hora
                if duracion is not None:
                    evento["duracion"] = duracion
                if tit is not None:
                    evento["titulo"] = tit
                if importancia is not None:
                    evento["importancia"] = importancia
                if criterios is not None:
                    evento["criterios"] = criterios
                if detalle is not None:
                    evento["detalle"] = detalle
                evento_encontrado = True
                break
        if not evento_encontrado:
            print("No se encontró un evento con el ID especificado.")
    
    def eliminar_evento(self, id):
        """metodo para eliminar un evento"""
        evento_encontrado = False
        for evento in self.eventos:
            if evento["id"] == id:
                self.eventos.remove(evento)
                evento_encontrado = True
                break
        if not evento_encontrado:
            print("No se encontró un evento con el ID especificado.")

    def buscar_por_fecha(self, fecha):
        """busco eventos por fecha"""
        eventos_encontrados = []
        for evento in self.eventos:
            if evento["fecha"] == fecha:
                eventos_encontrados.append(evento)
        if eventos_encontrados:
            print("Eventos encontrados:")
            for evento in eventos_encontrados:
                print("ID: ", evento["id"])
                print("Fecha: ", evento["fecha"])
                print("Hora: ", evento["hora"])
                print("Duración: ", evento["duracion"])
                print("Importancia: ", evento["importancia"])
                print("Criterios de búsqueda: ", evento["criterios"])
                print("Detalle: ", evento["detalle"])
                print()
        else:
            print("No se encontraron eventos en la fecha especificada.")
    
    def buscar_por_importancia(self, importancia):
        """metodo para buscar eventos por importancia (falta pasar a tk)"""
        eventos_encontrados = []
        for evento in self.eventos:
            if evento["importancia"] == importancia:
                eventos_encontrados.append(evento)
        if eventos_encontrados:
            print("Eventos encontrados:")
            for evento in eventos_encontrados:
                print("ID: ", evento["id"])
                print("Fecha: ", evento["fecha"])
                print("Hora: ", evento["hora"])
                print("Duración: ", evento["duracion"])
                print("Importancia: ", evento["importancia"])
                print("Criterios de búsqueda: ", evento["criterios"])
                print("Detalle: ", evento["detalle"])
                print()
        else:
            print("No se encontraron eventos con la importancia especificada.")

    def exportar_a_csv(self, nombre_archivo):
        with open(nombre_archivo, mode='w', newline='') as archivo_csv:
            campos = ["id", "fecha", "hora", "duracion", "titulo", "importancia", "criterios", "detalle"]
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
            escritor.writeheader()
            for evento in self.eventos:
                escritor.writerow(evento)
    
    def importar_desde_csv(self, nombre_archivo):
        global var_datos_lst
        with open(nombre_archivo, 'r') as archivo:
            lector_csv = csv.DictReader(archivo)
            var_datos_lst = []
            self.vardatos =[]
            for fila in lector_csv:
                var_datos_lst.append(fila)
                self.agregar_evento(fila["fecha"], fila["hora"], fila["duracion"], fila["titulo"], fila["importancia"], fila["criterios"], fila["detalle"])
                self.vardatos=var_datos_lst
                       
            return  self.vardatos #devuelvo al programa principal la variable vardatos con todas las citas de la agenda en forma de lista
    
    def volcar_datos_listbox(self):
        """metodo para escribir datos en la listbox"""
        datos_columnas_seleccionadas = [[fila["id"],fila["fecha"], fila["hora"], fila["titulo"]] for fila in agenda.vardatos] #extraer datos especificos de vardatos
        for fila in datos_columnas_seleccionadas:
           #listbox.insert(tk.END, fila) #inserto en la listbox los eventos
           #listratree.insert("",tk.END,values=fila) #inserto en el treeview los eventos
           framebot.listratree1.insert("",tk.END,values=fila)

    
   # def seleccionar_fila(self,event):
    #    seleccion = listbox.curselection()
     #   if len(seleccion) > 0:
      #      fila_seleccionada = seleccion[0]
       #     contenido = listbox.get(fila_seleccionada)
        #    lbl_evento.config(text=contenido)
    def mostrar_descripcion_tree(self, event):
        item = framebot.listratree1.selection()[0]# Obtener el elemento seleccionado
        descripcion = framebot.listratree1.item(item, "values")[0]# Obtener la tercera columna del elemento seleccionado
        lbl_evento.config(text=descripcion)# Mostrar la descripción en el Label

class utiles:
    def __init__(self):
       pass
    def convertir_fecha_hora(self,fecha_str, hora_str):
        fecha_hora_str = fecha_str + ' ' + hora_str
        return datetime.strptime(fecha_hora_str, '%d/%m/%Y %H:%M')
        # Ordenamos la lista de eventos por fecha
    
    def ordenareventos(self,eventos_ordenados_f_h):

        self.eventos_ordenados_f_h= sorted(var_datos_lst, key=lambda x: (Utiles.convertir_fecha_hora(x['fecha'], x['hora']))) #ordeno
        return eventos_ordenados_f_h
    
    

root = tk.Tk() 
framebot=Framebottom(root) #frame inferior, ocupa toda la parte de abajo
frametopll=frametopleft(root)
frametoprr=frametoprigth(root)
frametopmm=frametopmenu(root)
treeview_frame = TreeViewFrame(root)
treeview_frame.place(x=10, y=200,relwidth=0.5) #coloco el frame en la posicion 10, 200 y hago que tenga un tamaño de la mitad del form
root.geometry("1280x800")# Establecer el tamaño del Form
root.title("MI PRIMER AGENDA ")
#table = ttk.Treeview(root)
framecalendario=tk.Frame(root,width=300, height=400,bg="blue") #instancio el frame que contiene el calendario
framecalendario.grid(row=1, column=0) #lo ubico en la fila0,columna0
# Añadir un calendario tooltipdelay es el tiempo que demora en mostrar el tooltip, el tooltip muestra la lista de eventos del dia con la hora al acercar el mouse
cal = Calendar(framecalendario, tooltipdelay=10 ,selectmode = 'day',
               year = 2023, month = 2,
               day = 22, locale='es_AR',date_pattern="dd-mm-yyyy")
cal.grid(row=2,column=0)
date = cal.datetime.today()
fecha_parseada=date.strftime("%d/%m/%Y") #convierto la variable date en un str conel formato que yo quiera

#print(fecha_parseada)
#cal.calevent_create(date, 'aca va un evento', 'mensaje') #asi creo un evento calevent, comentario para uso interno


agenda = Agenda() #instancio la agenda
lbl_evento=tk.Label(root) #label para mostrar los detalles del evento, todavia no se usa, falta terminar
lbl_evento.grid(row=7,column=1,sticky="nsew")
#root.columnconfigure(0, minsize=100)

framebot.listratree1.bind("<ButtonRelease-1>", agenda.mostrar_descripcion_tree)#capturo el evento soltarboton para saber que fila del treeview esta seleccionada
   
agenda.importar_desde_csv("./events2.csv")#leo el csv
agenda.volcar_datos_listbox() #cargo datos en la listbox
agenda.agregar_evento("12/03/2023", "10:00", "1 hora", "evento1", "Alta", "Reunión de trabajo", "Presentación del proyecto") #carga manual de eventos para pruebas, si el evento esta repetido o se pisa con algun otro avisa con un print
agenda.agregar_evento("15/03/2023", "14:00", "2 horas", "evento2", "Alta","Entrevista de trabajo", "Conocer al equipo")
agenda.agregar_evento("18/03/2023", "16:00", "3 horas", "evento3","Alta", "Cita médica", "Chequeo anual")
#agenda.mostrar_eventos()
#agenda.modificar_evento(1, importancia="Alta", detalle="Presentación del proyecto actualizada") #modifico un evento
#agenda.mostrar_eventos()
#agenda.eliminar_evento(1) #elimino un evento con el id
agenda.mostrar_eventos()
#agenda.agregar_eventos_mensual()
agenda.mostrar_eventos_tk()
agenda.exportar_a_csv("./events2.csv") #guardo eventos al csv
Utiles=utiles() #instancio la clase utiles
Utiles.ordenareventos(var_datos_lst)
#crearevento=framebot.crearevento_tk()
#eventos_ordenados_f_h= sorted(var_datos_lst, key=lambda x: (Utiles.convertir_fecha_hora(x['fecha'], x['hora']))) #ordeno
print(Utiles.eventos_ordenados_f_h)
print(var_datos_lst)
root.mainloop()
