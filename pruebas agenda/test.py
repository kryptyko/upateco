import tkinter as tk
from tkinter import ttk

class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calendario Semanal")
        
        # Crear el Treeview con columnas de horas y días
        self.treeview = ttk.Treeview(self.root, columns=("Horas", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"), show="headings")
        self.treeview.heading("Horas", text="Horas")
        self.treeview.heading("Lunes", text="Lunes")
        self.treeview.heading("Martes", text="Martes")
        self.treeview.heading("Miércoles", text="Miércoles")
        self.treeview.heading("Jueves", text="Jueves")
        self.treeview.heading("Viernes", text="Viernes")
        self.treeview.heading("Sábado", text="Sábado")
        self.treeview.heading("Domingo", text="Domingo")
        self.treeview.pack()
        
        # Agregar las filas de horarios
        for hora in range(8, 21):
            self.treeview.insert("", tk.END, values=[f"{hora}:00 - {hora+1}:00"] + [""]*7)
        
        # Agregar eventos desde una lista
        lista_eventos = [("Lunes", "10:00", "Reunión con el jefe"), ("Martes", "14:00", "Presentación de proyecto"), ("Viernes", "18:00", "Cena con amigos")]
        for evento in lista_eventos:
            dia, hora, descripcion = evento
            self.agregar_evento(dia, hora, descripcion)
        
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
        boton_agregar = tk.Button(self.root, text="Agregar Evento", command=self.agregar_evento_input)
        boton_agregar.pack()
        
        self.root.mainloop()
    
    def agregar_evento(self, dia, hora, descripcion):
        # Obtener el índice de la fila correspondiente a la hora indicada
        indice = int(hora[:2]) - 8
        # Obtener el índice de la columna correspondiente al día indicado
        columna = self.treeview["columns"].index(dia)
        # Insertar la descripción del evento en la celda correspondiente
        self.treeview.set(self.treeview.get_children()[indice], column=columna, value=descripcion)
    
    def agregar_evento_input(self):
        # Obtener los datos del Entry
        dia = self.entry_dia.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()
        # Agregar el evento a la grilla
        self.agregar_evento(dia, hora, descripcion)

# Crear la aplicación y ejecutarla
app = MyApp()