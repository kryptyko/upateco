
import csv
import tkinter as tk
from tkinter import messagebox


class Recetario:
    def __init__(self):
        self.recetas = []
        self.cargar_recetas()

    def cargar_recetas(self):
        try:
            with open('recetas.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # Creamos un diccionario con los datos de la receta
                    receta = {'nombre': row['nombre'], 'ingredientes': row['ingredientes']}
                    self.recetas.append(receta)
        except FileNotFoundError:
            # Si el archivo no existe, lo creamos vacío
            open('recetas.csv', 'w').close()

    def guardar_recetas(self):
        with open('recetas.csv', 'w', newline='') as csvfile:
            fieldnames = ['nombre', 'ingredientes']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for receta in self.recetas:
                writer.writerow(receta)

    def agregar_receta(self, nombre, ingredientes):
        receta = {'nombre': nombre, 'ingredientes': ingredientes}
        self.recetas.append(receta)
        self.guardar_recetas()

    def editar_receta(self, index, nombre, ingredientes):
        self.recetas[index]['nombre'] = nombre
        self.recetas[index]['ingredientes'] = ingredientes
        self.guardar_recetas()

    def eliminar_receta(self, index):
        del self.recetas[index]
        self.guardar_recetas()


class RecetarioGUI:
    def __init__(self, recetario):
        self.recetario = recetario

        # Creamos la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title('Recetario')

        # Creamos los widgets de la ventana
        self.lbl_nombre = tk.Label(self.ventana, text='Nombre:')
        self.entry_nombre = tk.Entry(self.ventana)
        self.lbl_ingredientes = tk.Label(self.ventana, text='Ingredientes:')
        self.entry_ingredientes = tk.Text(self.ventana, height=10, width=40)
        self.btn_agregar = tk.Button(self.ventana, text='Agregar', command=self.agregar_receta)
        self.btn_editar = tk.Button(self.ventana, text='Editar', command=self.editar_receta)
        self.btn_eliminar = tk.Button(self.ventana, text='Eliminar', command=self.eliminar_receta)
        self.lista_recetas = tk.Listbox(self.ventana, height=10, width=40)
        self.lista_recetas.bind('<<ListboxSelect>>', self.mostrar_receta)

        # Añadimos los widgets a la ventana
        self.lbl_nombre.grid(row=0, column=0)
        self.entry_nombre.grid(row=0, column=1)
        self.lbl_ingredientes.grid(row=1, column=0)
        self.entry_ingredientes.grid(row=1, column=1)
        self.btn_agregar.grid(row=2, column=0)
        self.btn_editar.grid(row=2, column=1)
        self.btn_eliminar.grid(row=2, column=2)
        self.lista_recetas.grid(row=3, column=0, columnspan=3)

        # Cargamos las recetas en la lista
        for receta in self.recetario.recetas:
            self.lista_recetas.insert(tk.END, receta['nombre'])

        # Mostramos la ventana
        self.ventana.mainloop()

    def mostrar_receta(self, event):
        # Obtenemos el índice de la receta seleccionada en la lista
        try:
            index = self.lista_recetas.curselection()[0]
            receta = self.recetario.recetas[index]
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, receta['nombre'])
            self.entry_ingredientes.delete('1.0', tk.END)
            self.entry_ingredientes.insert('1.0', receta['ingredientes'])
        except IndexError:
            pass

    def agregar_receta(self):
        nombre = self.entry_nombre.get()
        ingredientes = self.entry_ingredientes.get('1.0', tk.END)
        if nombre and ingredientes:
            self.recetario.agregar_receta(nombre, ingredientes)
            self.lista_recetas.insert(tk.END, nombre)
            self.limpiar_campos()
        else:
            messagebox.showerror('Error', 'Debe ingresar un nombre y al menos un ingrediente.')

    def editar_receta(self):
        try:
            index = self.lista_recetas.curselection()[0]
            nombre = self.entry_nombre.get()
            ingredientes = self.entry_ingredientes.get('1.0', tk.END)
            self.recetario.editar_receta(index, nombre, ingredientes)
            self.lista_recetas.delete(index)
            self.lista_recetas.insert(index, nombre)
            self.limpiar_campos()
        except IndexError:
            pass

    def eliminar_receta(self):
        try:
            index = self.lista_recetas.curselection()[0]
            self.recetario.eliminar_receta(index)
            self.lista_recetas.delete(index)
            self.limpiar_campos()
        except IndexError:
            pass

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_ingredientes.delete('1.0', tk.END)


if __name__ == '__main__':
    recetario = Recetario()
    gui = RecetarioGUI(recetario)
    gui.mainloop()