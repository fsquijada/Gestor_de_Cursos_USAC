from tkinter import *
from tkinter import ttk
# Ventana principal como variable global
root = Tk()

class Menus:
    def __init__(self):        
        # MENU PRINCIPAL
        root.geometry(self.EditorVentana(root, 800, 600))
        root.title('INGENIERIA USAC - Práctica 1')
        root.iconbitmap("archivos/books.ico")
        root.config(background="lightblue")
        root.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        # Frame Principal
        framePrincipal = Frame ()
        framePrincipal.config(width="800", height="600", bg="lightblue")
        framePrincipal.pack()
        # Títulos de la ventana
        titulosPrincipales = Label (framePrincipal, text="\n\nCurso: Lenguajes Formales y de Programación\n\nEstudiante: Fredy Samuel Quijada Ceballos\n\nCarné: 202004812\n\n\n")
        titulosPrincipales.config(background="lightblue", font=("Arial", 12, "bold"), justify="left")
        titulosPrincipales.grid(row=0, ipadx=100, padx=0, pady=3, columnspan=2)
        # Botones de la ventana
        botonCarga = ttk.Button (framePrincipal, text="Cargar Archivo", command=lambda: self.VentanaCarga())
        botonCarga.grid(column=1, row=3, ipadx=100, ipady=5, padx=10, pady=10)
        botonGestionar = ttk.Button (framePrincipal, text="Gestionar Cursos", command=lambda: self.VentanaGestion()))
        botonGestionar.grid(column=1, row=4, ipadx=95, ipady=5, padx=10, pady=10)
        botonCreditos = ttk.Button (framePrincipal, text="Conteo de Créditos", command=lambda: self.VentanaCreditos())
        botonCreditos.grid(column=1, row=5, ipadx=88, ipady=5, padx=10, pady=10)
        botonSalir = ttk.Button (framePrincipal, text="Salir") #! Falta agregar la acción de salir
        botonSalir.grid(column=1, row=6, ipadx=105, ipady=5, padx=10, pady=10)

        root.mainloop()

    # Crear Ventana para carga de datos
    def VentanaCarga ():
        ventanaSeleccionArchivo = Toplevel ()
        ventanaSeleccionArchivo.title("Seleccionar Archivo")
        ventanaSeleccionArchivo.iconbitmap("archivos/books.ico")
        ventanaSeleccionArchivo.geometry(Menus.EditorVentana(ventanaSeleccionArchivo, 800, 200))
        # ventanaSeleccionArchivo.geometry(posicion)
        # Menus.OcultarVentana(ventanaSeleccionArchivo)
        #self.OcultarVentana(root)

    # Crear Ventana para la gestión de cursos
    def VentanaGestion ():
        # Ventana de Selección de archivo
        ventanaGestionarCursos = Toplevel ()
        ventanaGestionarCursos.title("Gestionar Cursos")
        ventanaGestionarCursos.iconbitmap("archivos/books.ico")
        ventanaGestionarCursos.geometry(Menus.EditorVentana(ventanaGestionarCursos, 800, 200))
        # ventanaSeleccionArchivo.geometry(posicion)
        Menus.OcultarVentana(ventanaGestionarCursos)
        #self.OcultarVentana(root)

    # Crear Ventana para agregar nuevos cursos
    def VentanaAgregar ():
        # Ventana de Selección de archivo
        ventanaAgregarCurso = Toplevel ()
        ventanaAgregarCurso.title("Seleccionar Archivo")
        ventanaAgregarCurso.iconbitmap("archivos/books.ico")
        ventanaAgregarCurso.geometry(Menus.EditorVentana(ventanaAgregarCurso, 800, 200))
        # ventanaSeleccionArchivo.geometry(posicion)
        Menus.OcultarVentana(ventanaAgregarCurso)
        #self.OcultarVentana(root)

    def VentanaCreditos ():
        pass

    
    # Función para definir el tamaño de la ventana y centrarlo en la pantalla
    def EditorVentana (self, ventana, ancho, alto):
        x = ventana.winfo_screenwidth() // 2 - ancho // 2
        y = ventana.winfo_screenheight() // 2 - alto // 2
        posicion = f"{str(ancho)}x{str(alto)}+{str(x)}+{str(y)}"
        return posicion
    
    # Muestra la ventana
    def MostrarOcultarVentana (self, ventanaMostrar, ventanaOcultar):
        ventanaOcultar.withdraw()
        ventanaMostrar.deiconify()

    # Oculta la ventana
    def OcultarVentana (self, ventana):
        ventana.withdraw()

