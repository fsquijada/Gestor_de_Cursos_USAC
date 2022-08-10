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
        root.iconbitmap("archivos/books.ico")
        root.config(background="lightblue")
        root.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        # Frame
        frame = Frame ()
        frame.config(width="800", height="600", bg="lightblue")
        frame.pack()
        # Títulos de la ventana
        titulos = Label (frame, text="\n\nCurso: Lenguajes Formales y de Programación\n\nEstudiante: Fredy Samuel Quijada Ceballos\n\nCarné: 202004812\n\n\n")
        titulos.config(background="lightblue", font=("Arial", 12, "bold"), justify="left")
        titulos.grid(row=0, padx=0, pady=3, columnspan=1)
        # Botones de la ventana
        botonCarga = ttk.Button (frame, text="Cargar Archivo", command=lambda: self.AbrirArchivo())
        botonCarga.grid(column=1, row=3, ipadx=100, ipady=5, padx=10, pady=10)
        botonGestionar = ttk.Button (frame, text="Gestionar Cursos", command=lambda: self.VentanaGestion())
        botonGestionar.grid(column=1, row=4, ipadx=95, ipady=5, padx=10, pady=10)
        botonCreditos = ttk.Button (frame, text="Conteo de Créditos", command=lambda: self.VentanaCreditos())
        botonCreditos.grid(column=1, row=5, ipadx=88, ipady=5, padx=10, pady=10)
        botonSalir = ttk.Button (frame, text="Salir", command=lambda: self.EliminarVentana(root))
        botonSalir.grid(column=1, row=6, ipadx=105, ipady=5, padx=10, pady=10)

        root.mainloop()

    # Crear Ventana para carga de datos
    def VentanaCarga (self):
        self.OcultarVentana(root)
        ventanaSeleccionArchivo = Toplevel ()
        ventanaSeleccionArchivo.title("Seleccionar Archivo")
        ventanaSeleccionArchivo.iconbitmap("archivos/books.ico")
        ventanaSeleccionArchivo.geometry(self.EditorVentana(ventanaSeleccionArchivo, 600, 200))
        ventanaSeleccionArchivo.config(background="lightblue")
        # Botones
        ruta = ""
        botonSeleccionar = ttk.Button (ventanaSeleccionArchivo, text="Abrir", command=lambda: self.AbrirArchivo(ruta))
        botonSeleccionar.grid(column=1, row=3, ipadx=100, ipady=5, padx=10, pady=10)
        botonSeleccionar.place(x="400", y="150")
        botonRegresar = ttk.Button (ventanaSeleccionArchivo, text="Regresar", command=lambda: self.MostrarEliminarVentana(root, ventanaSeleccionArchivo))
        botonRegresar.grid(column=2, row=3, ipadx=100, ipady=5, padx=10, pady=10)
        botonRegresar.place(x="500", y="150")

    # Crear Ventana para la gestión de cursos
    def VentanaGestion (self):
        self.OcultarVentana(root)
        # Ventana de Selección de archivo
        ventanaGestionarCursos = Toplevel ()
        ventanaGestionarCursos.title("Gestionar Cursos")
        ventanaGestionarCursos.iconbitmap("archivos/books.ico")
        ventanaGestionarCursos.geometry(self.EditorVentana(ventanaGestionarCursos, 800, 500))
        # Botones
        botonListar = ttk.Button (ventanaGestionarCursos, text="Listar Cursos", command=lambda: self.VentanaLista())
        botonListar.grid(ipadx=100, ipady=5, padx=1000, pady=10)
        botonListar.place(x="400", y="150")
        botonRegresar = ttk.Button (ventanaGestionarCursos, text="Regresar", command=lambda: self.MostrarEliminarVentana(root, ventanaGestionarCursos))
        botonRegresar.grid(ipadx=100, ipady=5, padx=100, pady=10)
        botonRegresar.place(x="400", y="250")

    # Crear Ventana para la lista de cursos
    def VentanaLista (self):
        # Ventana de Selección de archivo
        ventanaGestionarCursos = Toplevel ()
        ventanaGestionarCursos.title("Gestionar Cursos")
        ventanaGestionarCursos.iconbitmap("archivos/books.ico")
        ventanaGestionarCursos.geometry(self.EditorVentana(ventanaGestionarCursos, 800, 500))
        # ventanaSeleccionArchivo.geometry(posicion)
        # self.OcultarVentana(ventanaGestionarCursos)
        #self.OcultarVentana(root)

    # Crear Ventana para agregar nuevos cursos
    def VentanaAgregar (self):
        # Ventana de Selección de archivo
        ventanaAgregarCurso = Toplevel ()
        ventanaAgregarCurso.title("Seleccionar Archivo")
        ventanaAgregarCurso.iconbitmap("archivos/books.ico")
        ventanaAgregarCurso.geometry(self.EditorVentana(ventanaAgregarCurso, 800, 500))
        # ventanaSeleccionArchivo.geometry(posicion)
        Menus.OcultarVentana(ventanaAgregarCurso)
        #self.OcultarVentana(root)

    def VentanaEditar (self):
        pass

    def VentanaEliminar (self):
        pass

    def VentanaCreditos (self):
        pass

    def AbrirArchivo (self):
        ruta = filedialog.askopenfilename(title="Abrir", filetypes=(("Archivos LFP (*.lfp)","*.lfp"),))
        if (ruta != ""):
            cursos.CargaData(ruta)
            cursos.ListadoCompleto()
            showinfo("Carga de cursos", "Los datos se han cargado correctamente")

    
    # Función para definir el tamaño de la ventana y centrarlo en la pantalla
    def EditorVentana (self, ventana, ancho, alto):
        x = ventana.winfo_screenwidth() // 2 - ancho // 2
        y = ventana.winfo_screenheight() // 2 - alto // 2
        posicion = f"{str(ancho)}x{str(alto)}+{str(x)}+{str(y)}"
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

