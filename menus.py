from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import *
from cursos import Cursos

# Variables
root = Tk()
cursos = Cursos ()

class Menus:
    def __init__(self):        
        # MENU PRINCIPAL
        root.geometry(self.EditorVentana(root, 800, 500))
        root.title('INGENIERIA USAC - Práctica 1')
        root.iconbitmap('archivos/books.ico')
        root.config(background='lightblue')
        root.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        # Frame
        frame = Frame (root)
        frame.config(width='800', height='600', bg='lightblue')
        frame.pack()
        # Títulos de la ventana
        titulos = Label (frame, text='\n\nCurso: Lenguajes Formales y de Programación\n\nEstudiante: Fredy Samuel Quijada Ceballos\n\nCarné: 202004812\n\n\n')
        titulos.config(background='lightblue', font=('Arial', 12, 'bold'), justify='left')
        titulos.grid(row=0, padx=0, pady=3, columnspan=1)
        # Botones de la ventana
        botonCarga = ttk.Button (frame, text='Cargar Archivo', command=lambda: self.AbrirArchivo())
        botonCarga.grid(column=1, row=3, ipadx=100, ipady=5, padx=10, pady=10)
        botonGestionar = ttk.Button (frame, text='Gestionar Cursos', command=lambda: self.VentanaGestion())
        botonGestionar.grid(column=1, row=4, ipadx=95, ipady=5, padx=10, pady=10)
        botonCreditos = ttk.Button (frame, text='Conteo de Créditos', command=lambda: self.VentanaCreditos())
        botonCreditos.grid(column=1, row=5, ipadx=88, ipady=5, padx=10, pady=10)
        botonSalir = ttk.Button (frame, text='Salir', command=lambda: self.EliminarVentana(root))
        botonSalir.grid(column=1, row=6, ipadx=105, ipady=5, padx=10, pady=10)
        # Para que la ventana principal se inicie automáticamente
        root.mainloop()

    # Crear Ventana para la lista de cursos
    def VentanaGestion (self):
        self.OcultarVentana(root)
        # Ventana de Selección de archivo
        ventanaGestionarCursos = Toplevel ()
        ventanaGestionarCursos.geometry(self.EditorVentana(root, 800, 500))
        ventanaGestionarCursos.title('INGENIERIA USAC - Gestión de cursos')
        ventanaGestionarCursos.iconbitmap('archivos/books.ico')
        ventanaGestionarCursos.config(background='lightblue')
        #ventanaGestionarCursos.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        ventanaGestionarCursos.protocol('WM_DELETE_WINDOW', root.quit)
        # Frame
        frame = Frame (ventanaGestionarCursos)
        frame.config(width='600', height='250', bg='lightblue')
        frame.pack()
        frame2 = Frame (ventanaGestionarCursos)
        frame2.config(width='600', height='250', bg='lightblue')
        frame2.pack()
        # Tabla
        tabla = ttk.Treeview(frame, columns=('#1', '#2', '#3', '#4', '#5', '#6'), height='8')
        tabla.grid(row='10', column='0', columnspan='2', pady=100)
        tabla.column('#0', width=50)
        tabla.column('#1', width=250, anchor=CENTER)
        tabla.column('#2', width=95, anchor=CENTER)
        tabla.column('#3', width=80, anchor=CENTER)
        tabla.column('#4', width=70, anchor=CENTER)
        tabla.column('#5', width=70, anchor=CENTER)
        tabla.column('#6', width=70, anchor=CENTER)
        # Títulos de la tabla
        tabla.heading('#0', text='Código', anchor=CENTER)
        tabla.heading('#1', text='Nombre', anchor=CENTER)
        tabla.heading('#2', text='Pre-requisitos', anchor=CENTER)
        tabla.heading('#3', text='Obligatorio', anchor=CENTER)
        tabla.heading('#4', text='Semestre', anchor=CENTER)
        tabla.heading('#5', text='Créditos', anchor=CENTER)
        tabla.heading('#6', text='Estado', anchor=CENTER)
        # Carga de datos para la tabla
        self.InsertarDatos(tabla)
        # Botones
        botonAgregar = ttk.Button (frame2, text='Agregar Curso', command=lambda: self.MostrarEliminarVentana(root, ventanaGestionarCursos))
        botonAgregar.grid(column=1, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonEditar = ttk.Button (frame2, text='Editar Curso', command=lambda: self.MostrarEliminarVentana(root, ventanaGestionarCursos))
        botonEditar.grid(column=2, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonEliminar = ttk.Button (frame2, text='Eliminar Curso', command=lambda: self.MostrarEliminarVentana(root, ventanaGestionarCursos))
        botonEliminar.grid(column=3, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonRegresar = ttk.Button (frame2, text='Regresar', command=lambda: self.MostrarEliminarVentana(root, ventanaGestionarCursos))
        botonRegresar.grid(column=3, row=2, ipadx=60, ipady=5, padx=10, pady=10)
        
    # Crear Ventana para agregar nuevos cursos
    def VentanaAgregar (self):
        # Ventana de Selección de archivo
        ventanaAgregarCurso = Toplevel ()
        ventanaAgregarCurso.title('Seleccionar Archivo')
        ventanaAgregarCurso.iconbitmap('archivos/books.ico')
        ventanaAgregarCurso.geometry(self.EditorVentana(ventanaAgregarCurso, 800, 500))
        # ventanaSeleccionArchivo.geometry(posicion)
        self.OcultarVentana(ventanaAgregarCurso)
        #self.OcultarVentana(root)

    def VentanaEditar (self):
        pass

    def VentanaEliminar (self):
        pass

    def VentanaCreditos (self):
        pass

    def AbrirArchivo (self):
        ruta = filedialog.askopenfilename(title='Abrir', filetypes=(('Archivos LFP (*.lfp)','*.lfp'),))
        if (ruta != ''):
            cursos.CargaData(ruta)
            showinfo('Carga de cursos', 'Los datos se han cargado correctamente')
    
    # Función para definir el tamaño de la ventana y centrarlo en la pantalla
    def EditorVentana (self, ventana, ancho, alto):
        x = ventana.winfo_screenwidth() // 2 - ancho // 2
        y = ventana.winfo_screenheight() // 2 - alto // 2
        posicion = f'{str(ancho)}x{str(alto)}+{str(x)}+{str(y)}'
        return posicion
    
    # Muestra la ventana
    def MostrarEliminarVentana (self, ventanaMostrar, ventanaEliminar):
        ventanaEliminar.destroy()
        ventanaMostrar.deiconify()

    # Oculta la ventana
    def OcultarVentana (self, ventana):
        ventana.withdraw()

    # Eliminar la ventana
    def EliminarVentana (self, ventana):
        ventana.destroy()

    # Agregar datos en la tabla
    def InsertarDatos (self, tabla):
        for dato in cursos.listado:
            separado = dato.pre_requisitos
            pre_requisitos = '--'
            obligatorio = 'No'
            estado = 'Aprobado'
            if separado != ['']:
                pre_requisitos = separado
            if dato.obligatorio == '1':
                obligatorio = 'Si'
            if dato.estado == '1':
                estado = 'Cursando'
            elif dato.estado == '-1':
                estado = 'Pendiente'
            tabla.insert('', END, text=dato.codigo, values=(dato.nombre, pre_requisitos, obligatorio, dato.semestre, dato.creditos, estado))

    # # Crear Ventana para carga de datos
    # def VentanaCarga (self):
    #     self.OcultarVentana(root)
    #     ventanaSeleccionArchivo = Toplevel ()
    #     ventanaSeleccionArchivo.title('Seleccionar Archivo')
    #     ventanaSeleccionArchivo.iconbitmap('archivos/books.ico')
    #     ventanaSeleccionArchivo.geometry(self.EditorVentana(ventanaSeleccionArchivo, 600, 200))
    #     ventanaSeleccionArchivo.config(background='lightblue')
    #     # Frame
    #     frame = Frame (ventanaSeleccionArchivo)
    #     frame.config(width='800', height='600', bg='lightblue')
    #     frame.mainloop()
    #     # Botones
    #     ruta = ''
    #     botonSeleccionar = ttk.Button (frame, text='Abrir', command=lambda: self.AbrirArchivo(ruta))
    #     botonSeleccionar.grid(column=1, row=3, ipadx=100, ipady=5, padx=10, pady=10)
    #     botonSeleccionar.place(x='400', y='150')
    #     botonRegresar = ttk.Button (frame, text='Regresar', command=lambda: self.MostrarEliminarVentana(root, ventanaSeleccionArchivo))
    #     botonRegresar.grid(column=2, row=3, ipadx=100, ipady=5, padx=10, pady=10)
    #     botonRegresar.place(x='500', y='150')

    # def VentanaGestion (self):
    #     self.OcultarVentana(root)
    #     # Ventana de Selección de archivo
    #     VentanaGestion = Toplevel ()
    #     VentanaGestion.geometry(self.EditorVentana(root, 800, 500))
    #     VentanaGestion.title('INGENIERIA USAC - Gestión de cursos')
    #     VentanaGestion.iconbitmap('archivos/books.ico')
    #     VentanaGestion.config(background='lightblue')
    #     VentanaGestion.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
    #     VentanaGestion.protocol('WM_DELETE_WINDOW', root.quit)
    #     # Frame
    #     frame = Frame (VentanaGestion)
    #     frame.config(width='800', height='600', bg='lightblue')
    #     frame.pack(pady=100)
    #     # Botones de la ventana
    #     botonLista = ttk.Button (frame, text='Listar Cursos', command=lambda: self.VentanaLista(VentanaGestion))
    #     botonLista.grid(column=1, row=3, ipadx=100, ipady=5, padx=10, pady=10)
    #     botonAgregar = ttk.Button (frame, text='Agregar Curso', command=lambda: self.VentanaAgregar())
    #     botonAgregar.grid(column=1, row=4, ipadx=95, ipady=5, padx=10, pady=10)
    #     botonEditar = ttk.Button (frame, text='Editar Curso', command=lambda: self.VentanaEditar())
    #     botonEditar.grid(column=1, row=5, ipadx=88, ipady=5, padx=10, pady=10)
    #     botonEliminar = ttk.Button (frame, text='Eliminar curso', command=lambda: self.VentanaEliminar())
    #     botonEliminar.grid(column=1, row=6, ipadx=88, ipady=5, padx=10, pady=10)
    #     botonRegresar = ttk.Button (frame, text='Regresar', command=lambda: self.MostrarEliminarVentana(root, VentanaGestion))
    #     botonRegresar.grid(column=1, row=7, ipadx=105, ipady=5, padx=10, pady=10)