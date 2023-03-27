### prueba de Marcelo
class EventosSemanalesFrame(ttk.Frame):
    def __init__(self, parent, fechas_ordenadas):
        super().__init__(parent)
        self.fechas_ordenadas = fechas_ordenadas
        self.selector_fecha = DateEntry(self, width=12, background='darkblue',
                                        foreground='white', borderwidth=2, locale='es_ES')
        self.selector_fecha.pack(padx=10, pady=10)
        self.treeview_semanal = ttk.Treeview(self)
        
        # Crear la lista de nombres de columnas con los días de la semana y las fechas correspondientes
        dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        fecha_actual = datetime.now().date() # o cualquier otra fecha que quieras
        fechas = [fecha_actual + timedelta(days=i) for i in range(7)]
        nombres_columnas = [dia.capitalize() + "\n" + fecha.strftime("%d/%m/%Y") for dia, fecha in zip(dias_semana, fechas)]
        
        # Configurar la cabecera de las columnas del Treeview con los nombres de la lista creada
        self.treeview_semanal["columns"] = tuple(dias_semana)
        for i, nombre in enumerate(nombres_columnas):
            self.treeview_semanal.heading(dias_semana[i], text=nombre)

        self.treeview_semanal.column("#0", anchor="w", width=80)
        for dia in self.treeview_semanal["columns"]:
            self.treeview_semanal.column(dia, anchor="center", width=100)
        
        self.treeview_semanal.pack(fill="both", expand=True)
        self.selector_fecha.bind("<<DateEntrySelected>>", lambda _: self.mostrar_eventos_en_tabla())
        self.mostrar_eventos_en_tabla()

### fin prueba marcelo
