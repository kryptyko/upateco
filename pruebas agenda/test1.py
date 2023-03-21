import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

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
        
        # Crear un Entry para agregar eventos
        self.entry_dia = tk.Entry(self.root)
        self.entry_hora = tk.Entry(self.root)
        self.entry_descripcion = tk.Entry(self.root)
        self.entry_dia.insert(0, "Lunes")
        self.entry_hora.insert(0, "14:00")
        self.entry_descripcion.insert(0, "Nuevo evento")
        self.entry_dia.pack()
        self.entry_hora.pack()
        self.entry_descripcion.pack()
        boton_agregar = tk.Button(self.root, text="Agregar Evento", command=self.agregar_evento)
        boton_agregar.pack()
        
        # Agregar botones para avanzar y retroceder semanas
        boton_anterior = tk.Button(self.root, text="Semana Anterior", command=self.semana_anterior)
        boton_anterior.pack(side=tk.LEFT)
        
        boton_siguiente = tk.Button(self.root, text="Semana Siguiente", command=self.semana_siguiente)
        boton_siguiente.pack(side=tk.LEFT)
        
        self.root.mainloop()
    
    def agregar_evento(self):
        # Obtener los datos del Entry
        dia = self.entry_dia.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()
        # Agregar el evento a la grilla
        self.agregar_evento_a_grilla(dia, hora, descripcion)
        # Limpiar los Entries
        self.entry_dia.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.entry_dia.insert(0, "Lunes")
        self.entry_hora.insert(0, "14:00")
        self.entry_descripcion.insert(0, "Nuevo evento")

    def agregar_evento_a_grilla(self, dia, hora, descripcion):
        # Encontrar la columna correspondiente al día
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        columna_dia = dias_semana.index(dia) + 2
        
        # Encontrar la fila correspondiente a la hora
        hora_inicio = int(hora[:2]) #extraigo los primerso 2 caracteres de la hora y lo convierto en entero
        fila_hora = hora_inicio - 8 #
        
        # Agregar la descripción del evento a la celda correspondiente
        self.treeview.set(fila_hora, columna_dia, descripcion)
        
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


calendario = CalendarioSemana("2023-01-01")