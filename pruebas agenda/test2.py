import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

from numpy import integer

class CalendarioSemana:
    def __init__(self, fecha_inicio):
        # Convertir la fecha de inicio a un objeto datetime
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("Calendario Semanal")
        
        # Crear el Treeview con columnas de horas y días
        self.treeview = ttk.Treeview(self.root, columns=("Horas", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"), show="headings")
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        self.treeview.heading("Horas", text="Horas")
        self.treeview.heading("Lunes", text=self.fecha_inicio.strftime("Lunes" + " %d/%m"))
        for i in range(1, 7):
            dia = self.fecha_inicio + timedelta(days=i)
            self.treeview.heading(i+1, text=dia.strftime(dias_semana[i]+" %d/%m"))
        self.treeview.pack()
        
        # Agregar las filas de horarios
        for hora in range(8, 21):
            #self.treeview.insert("", tk.END, values=[f"{hora}"] + [""]*7)
            self.treeview.insert("", tk.END, values=[f"{hora}"])
                 
        # Agregar botones para avanzar y retroceder semanas
        boton_anterior = tk.Button(self.root, text="Semana Anterior", command=self.semana_anterior)
        boton_anterior.pack(side=tk.LEFT)
        
        boton_siguiente = tk.Button(self.root, text="Semana Siguiente", command=self.semana_siguiente)
        boton_siguiente.pack(side=tk.LEFT)
        self.entry_fecha = tk.Entry(self.root)
        self.entry_hora = tk.Entry(self.root)
        # Agregar cuadros de texto y botón para agregar evento
        self.entry_fecha.pack(side=tk.LEFT)
        self.entry_hora.pack(side=tk.LEFT)  
        # Crear botón para agregar evento
        boton_agregar = tk.Button(self.root, text="Agregar Evento", command=self.agregar_evento)
        boton_agregar.pack(side=tk.LEFT)
        
        self.root.mainloop()
    
        
    def semana_anterior(self):
        self.fecha_inicio = self.fecha_inicio - timedelta(weeks=1)
        self.actualizar_encabezados()

    def semana_siguiente(self):
        self.fecha_inicio = self.fecha_inicio + timedelta(weeks=1)
        self.actualizar_encabezados()

    def actualizar_encabezados(self):
        # Actualizar los encabezados de los días
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.treeview.heading("Lunes", text=self.fecha_inicio.strftime("Lunes" + " %d/%m"))
        for i in range(1, 7):
            dia = self.fecha_inicio + timedelta(days=i)
            self.treeview.heading(dias_semana[i], text=dia.strftime(dias_semana[i]+" %d/%m"))

        # Crear cuadros de texto para ingresar fecha y hora del evento
        self.entry_fecha = tk.Entry(self.root)
        self.entry_hora = tk.Entry(self.root)



    def agregar_evento(self):
        # Obtener fecha y hora del evento
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        
        # Convertir fecha y hora a objetos datetime
        fecha = datetime.strptime(fecha, "%Y-%m-%d")
        hora = datetime.strptime(hora, "%H:%M")
        
        # Calcular columna y fila correspondiente a la fecha y hora del evento
        dias_semana = ["Sunday","Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        dias_semana_dict = {"Monday": "Lunes","Tuesday": "Martes","Wednesday": "Miércoles","Thursday": "Jueves","Friday": "Viernes","Saturday": "Sábado","Sunday": "Domingo"}
        columna = dias_semana.index(fecha.strftime("%A"))+1
        fila = str(hora.hour - 7)
        fila_num= "I00"+fila
        # Actualizar valor de la celda correspondiente a la fecha y hora del evento
        self.treeview.set(f"{fila_num}", f"{columna}", "Evento")
        

      
       


calendario = CalendarioSemana("2023-01-01")