import tkinter as tk
from tkcalendar import Calendar, DateEntry

class CalendarioEventos(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Crear el widget Calendar y agregarlo al frame
        self.calendario = Calendar(self)
        self.calendario.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Crear botones para crear y borrar eventos
        self.boton_crear = tk.Button(self, text="Crear evento", command=self.crear_evento)
        self.boton_crear.grid(row=1, column=0, sticky="w")
        self.boton_borrar = tk.Button(self, text="Borrar evento", command=self.borrar_evento)
        self.boton_borrar.grid(row=1, column=1, sticky="e")

        # Crear diccionario para almacenar los eventos
        self.eventos = {}

    def crear_evento(self):
        # Crear ventana para ingresar los datos del evento
        ventana = tk.Toplevel(self)
        ventana.title("Crear evento")
        etiqueta_fecha = tk.Label(ventana, text="Fecha:")
        etiqueta_fecha.grid(row=0, column=0)
        fecha = DateEntry(ventana, width=12, background="darkblue", foreground="white", borderwidth=2)
        fecha.grid(row=0, column=1)
        etiqueta_titulo = tk.Label(ventana, text="Título:")
        etiqueta_titulo.grid(row=1, column=0)
        titulo = tk.Entry(ventana)
        titulo.grid(row=1, column=1)
        etiqueta_descripcion = tk.Label(ventana, text="Descripción:")
        etiqueta_descripcion.grid(row=2, column=0)
        descripcion = tk.Entry(ventana)
        descripcion.grid(row=2, column=1)
        boton_guardar = tk.Button(ventana, text="Guardar", command=lambda: self.guardar_evento(fecha.get_date(), titulo.get(), descripcion.get(), ventana))
        boton_guardar.grid(row=3, column=1)

    def guardar_evento(self, fecha, titulo, descripcion, ventana):
        # Almacenar el evento en el diccionario de eventos
        if fecha in self.eventos:
            self.eventos[fecha].append((titulo, descripcion))
        else:
            self.eventos[fecha] = [(titulo, descripcion)]
        # Actualizar el calendario con el evento creado
        self.calendario.calevent_create(fecha, f"{titulo}: {descripcion}")
        # Cerrar la ventana de creación de eventos
        ventana.destroy()

    def borrar_evento(self):
        # Obtener la fecha seleccionada en el calendario
        fecha = self.calendario.selection_get()
        # Verificar si hay eventos en la fecha seleccionada
        if fecha in self.eventos:
            # Crear ventana para seleccionar el evento a borrar
            ventana = tk.Toplevel(self)
            ventana.title("Borrar evento")
            etiqueta_evento = tk.Label(ventana, text="Selecciona el evento a borrar:")
            etiqueta_evento.grid(row=0, column=0, sticky="w")
            lista_eventos = tk.Listbox(ventana)
            lista_eventos.grid(row=1, column=0, columnspan=2)
            for evento in self.eventos[fecha]:
                lista_eventos.insert("end", evento[0])
            boton_borrar = tk.Button(ventana, text="Borrar", command=lambda: self.remover_evento(fecha, lista_eventos.curselection(), ventana))
            boton_borrar.grid(row=2, column=1, sticky="e")
        else:
            pass
            # Si no hay eventos en la fecha seleccionada, mostrar un mensaje de error
            #tk.messagebox.showerror("Error", "No hay eventos en la fecha seleccionada")

    def remover_evento(self, fecha, seleccion, ventana):
        # Remover el evento seleccionado del diccionario de eventos
        self.eventos[fecha].pop(seleccion[0])
        # Actualizar el calendario eliminando el evento borrado
        self.calendario.calevent_remove(fecha, seleccion[0])
        # Cerrar la ventana de eliminación de eventos
        ventana.destroy()

# Crear la ventana principal y agregar el frame con el calendario
root = tk.Tk()
root.title("Calendario de eventos")
calendario_eventos = CalendarioEventos(root)
calendario_eventos.grid(row=0, column=0)
root.mainloop()