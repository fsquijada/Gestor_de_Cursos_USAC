from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import *
from cursos import Cursos

# Variables
root = Tk()
cursos = Cursos ()

class Menus:
    #!::::::::::::::::::::::::::::::::VENTANAS::::::::::::::::::::::::::::::::::::::::::::::
    def __init__(self):        
        # MENU PRINCIPAL
        root.geometry(self.EditorVentana(root, 800, 500))
        root.title('INGENIERIA USAC - Práctica 1')
        root.iconbitmap('archivos/books.ico')
        root.config(background='lightblue')
        #root.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        # Frame
        frame = Frame (root)
        frame.config(width='800', height='220', bg='lightblue')
        frame.pack()
        frame2 = Frame (root)
        frame2.config(width='800', height='300', bg='lightblue')
        frame2.pack()
        # Títulos de la ventana
        titulos = Label (frame, text='\n\nCurso: Lenguajes Formales y de Programación\n\nEstudiante: Fredy Samuel Quijada Ceballos\n\nCarné: 202004812\n\n\n')
        titulos.config(background='lightblue', font=('Arial', 12, 'bold'), justify='left')
        titulos.grid(row=0, padx=0, pady=3, columnspan=1)
        titulos.place(x='100', y='20')
        # Imagen
        img = PhotoImage(file='archivos/usac.png')
        imgLabel = Label(frame, image=img)
        imgLabel.config(background='lightblue')
        imgLabel.place(x='550', y='10')
        # Botones de la ventana
        botonCarga = ttk.Button (frame2, text='Cargar Archivo', command=lambda: self.AbrirArchivo())
        botonCarga.grid(column=1, row=3, ipadx=100, ipady=5, padx=10, pady=10)
        botonGestionar = ttk.Button (frame2, text='Gestionar Cursos', command=lambda: self.VentanaGestion())
        botonGestionar.grid(column=1, row=4, ipadx=95, ipady=5, padx=10, pady=10)
        botonCreditos = ttk.Button (frame2, text='Conteo de Créditos', command=lambda: self.VentanaCreditos())
        botonCreditos.grid(column=1, row=5, ipadx=88, ipady=5, padx=10, pady=10)
        botonSalir = ttk.Button (frame2, text='Salir', command=lambda: self.EliminarVentana(root))
        botonSalir.grid(column=1, row=6, ipadx=105, ipady=5, padx=10, pady=10)
        # Para que la ventana principal se inicie automáticamente
        root.mainloop()

    # Crear Ventana para la lista de cursos
    def VentanaGestion (self):
        # Evento al hacer doble click en la tabla
        def Click (event):
            if cursos.listado != []:
                tabla.selection_set(tabla.get_children()[(len(cursos.listado)-1)])
                botonEditar['state'] = 'normal'
                botonEliminar['state'] = 'normal'
        # Ocultar ventana principal
        self.OcultarVentana(root)
        # Ventana de Selección de archivo
        ventanaGestionarCursos = Toplevel ()
        ventanaGestionarCursos.geometry(self.EditorVentana(root, 800, 500))
        ventanaGestionarCursos.title('INGENIERIA USAC - Gestión de cursos')
        ventanaGestionarCursos.iconbitmap('archivos/books.ico')
        ventanaGestionarCursos.config(background='lightblue')
        ventanaGestionarCursos.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
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
        tabla.bind('<Button-1>', Click)
        tabla.grid(row='10', column='0', columnspan='2', pady=100)
        tabla.column('#0', width=50)
        tabla.column('#1', width=240, anchor=CENTER)
        tabla.column('#2', width=105, anchor=CENTER)
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
        botonAgregar = ttk.Button (frame2, text='Agregar Curso', command=lambda: self.VentanaAgregar(ventanaGestionarCursos))
        botonAgregar.grid(column=1, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonEditar = ttk.Button (frame2, text='Editar Curso', command=lambda: self.VentanaEditar(ventanaGestionarCursos, tabla))
        botonEditar.grid(column=2, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonEditar['state'] = 'disabled'
        botonEliminar = ttk.Button (frame2, text='Eliminar Curso', command=lambda: self.EliminarCurso(ventanaGestionarCursos, tabla.item(tabla.selection())['text'], tabla.item(tabla.selection())['values'][0]))
        botonEliminar.grid(column=3, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonEliminar['state'] = 'disabled'
        botonBuscar = ttk.Button (frame2, text='Buscar Curso', command=lambda: self.VentanaCodigo(ventanaGestionarCursos))
        botonBuscar.grid(column=2, row=2, ipadx=55, ipady=5, padx=10, pady=10)
        botonRegresar = ttk.Button (frame2, text='Regresar', command=lambda: self.MostrarEliminarVentana(root, ventanaGestionarCursos))
        botonRegresar.grid(column=3, row=2, ipadx=60, ipady=5, padx=10, pady=10)
        
    # Crear Ventana para agregar nuevos cursos
    def VentanaAgregar (self, ventana):
        self.OcultarVentana(ventana)
        # Ventana Agregar Cursos
        ventanaAgregar = Toplevel ()
        ventanaAgregar.geometry(self.EditorVentana(root, 600, 500))
        ventanaAgregar.title('INGENIERIA USAC - Agregar Curso')
        ventanaAgregar.iconbitmap('archivos/books.ico')
        ventanaAgregar.config(background='lightblue')
        ventanaAgregar.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        ventanaAgregar.protocol('WM_DELETE_WINDOW', root.quit)
        # Frame Superior
        frame = Frame (ventanaAgregar)
        frame.config(width='600', height='400', bg='lightblue')
        frame.place(x='0', y='100')
        frame.pack()
        # Frame Inferior
        frame2 = Frame (ventanaAgregar)
        frame2.config(width='600', height='100', bg='lightblue')
        frame2.place(x='0', y='100')
        frame2.pack()
        # Labels
        codigo = Label (frame, text='Código')
        codigo.config(background='lightblue', font=('Arial', 12), pady=10)
        codigo.place(x='50', y='50')
        nombre = Label (frame, text='Nombre')
        nombre.config(background='lightblue', font=('Arial', 12), pady=10)
        nombre.place(x='50', y='100')
        preRequisito = Label (frame, text='Pre-Requisitos')
        preRequisito.config(background='lightblue', font=('Arial', 12), pady=10)
        preRequisito.place(x='50', y='150')
        semestre = Label (frame, text='Semestre')
        semestre.config(background='lightblue', font=('Arial', 12), pady=10)
        semestre.place(x='50', y='200')
        opcionalidad = Label (frame, text='Tipo')
        opcionalidad.config(background='lightblue', font=('Arial', 12), pady=10)
        opcionalidad.place(x='50', y='250')
        creditos = Label (frame, text='Créditos')
        creditos.config(background='lightblue', font=('Arial', 12), pady=10)
        creditos.place(x='50', y='300')
        estado = Label (frame, text='Estado')
        estado.config(background='lightblue', font=('Arial', 12), pady=10)
        estado.place(x='50', y='350')
        # Entradas
        cod = StringVar()
        name = StringVar()
        pre = StringVar()
        sem = StringVar()
        opc = StringVar()
        opc.set(value='1')
        cre = StringVar()
        est = StringVar()
        est.set(value='0')
        codigoEntrada = Entry(frame, textvariable = cod, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
        codigoEntrada.place(x='180', y='60')
        nombreEntrada = Entry(frame, textvariable = name, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
        nombreEntrada.place(x='180', y='110')
        preRequisitosEntrada = Entry(frame, textvariable = pre, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
        preRequisitosEntrada.place(x='180', y='160')
        semestreEntrada = Entry(frame, textvariable = sem, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
        semestreEntrada.place(x='180', y='210')
        opcionalidad1 = Radiobutton (frame, text='Obligatorio', value='1', variable=opc, background='lightblue', font=('Arial', 12, 'italic'))
        opcionalidad1.place(x='220', y='260')
        opcionalidad2 = Radiobutton (frame, text='Opcional', value='0', variable=opc, background='lightblue', font=('Arial', 12, 'italic'))
        opcionalidad2.place(x='380', y='260')
        creditosEntrada = Entry(frame, textvariable = cre, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
        creditosEntrada.place(x='180', y='310')
        estado1 = Radiobutton (frame, text='Aprobado', value='0', variable=est, background='lightblue', font=('Arial', 12, 'italic'))
        estado1.place(x='200', y='360')
        estado2 = Radiobutton (frame, text='Cursando', value='1', variable=est, background='lightblue', font=('Arial', 12, 'italic'))
        estado2.place(x='300', y='360')
        estado3 = Radiobutton (frame, text='Pendiente', value='-1', variable=est, background='lightblue', font=('Arial', 12, 'italic'))
        estado3.place(x='400', y='360')
        # Botones
        botonAgregar = ttk.Button (frame2, text='Agregar Curso', command=lambda: self.AgregarCurso(ventanaAgregar, codigoEntrada.get(), nombreEntrada.get(), preRequisitosEntrada.get(), semestreEntrada.get(), opc.get(), creditosEntrada.get(), est.get()))
        botonAgregar.grid(column=1, row=1, ipadx=30, ipady=5, padx=100, pady=30)
        botonCancelar = ttk.Button (frame2, text='Cancelar', command=lambda: self.MostrarEliminarVentana(ventana, ventanaAgregar))
        botonCancelar.grid(column=2, row=1, ipadx=35, ipady=5, padx=10, pady=30)
    
    # Crear ventana para editar nuevos cursos
    def VentanaEditar (self, ventana, tabla):
        codigoTabla = str(tabla.item(tabla.selection())['text'])
        nombreTabla = str(tabla.item(tabla.selection())['values'][0])
        preRequisitosTabla = str(tabla.item(tabla.selection())['values'][1])
        opcionalidadTabla = str(tabla.item(tabla.selection())['values'][2])
        semestreTabla = str(tabla.item(tabla.selection())['values'][3])
        creditosTabla = str(tabla.item(tabla.selection())['values'][4])
        estadoTabla = str(tabla.item(tabla.selection())['values'][5])   
        # Cambia el valor de los prerrequisitos para la edición
        if preRequisitosTabla == '--':
            preRequisitosTabla = ''
        # Cambia el valor de la opcionalidad para la edición
        if opcionalidadTabla == 'Si':
            opcionalidadTabla = '1'
        else:
            opcionalidadTabla = '0'
        # Cambia el valor del estado para la edición
        if estadoTabla == 'Aprobado':
            estadoTabla = '0'
        elif estadoTabla == 'Cursando':
            estadoTabla = '1'
        else:
            estadoTabla = '-1'
        # Oculta la ventana de gestión
        self.OcultarVentana(ventana)
        # Ventana Editar Curso
        ventanaEditarCurso = Toplevel ()
        ventanaEditarCurso.geometry(self.EditorVentana(root, 600, 500))
        ventanaEditarCurso.title('INGENIERIA USAC - Editar Curso')
        ventanaEditarCurso.iconbitmap('archivos/books.ico')
        ventanaEditarCurso.config(background='lightblue')
        ventanaEditarCurso.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        ventanaEditarCurso.protocol('WM_DELETE_WINDOW', root.quit)
        # Frame
        frame = Frame (ventanaEditarCurso)
        frame.config(width='600', height='400', bg='lightblue')
        frame.place(x='0', y='100')
        frame.pack()
        # Frame
        frame2 = Frame (ventanaEditarCurso)
        frame2.config(width='600', height='100', bg='lightblue')
        frame2.place(x='0', y='100')
        frame2.pack()
        # Labels
        codigo = Label (frame, text='Código')
        codigo.config(background='lightblue', font=('Arial', 12), pady=10)
        codigo.place(x='50', y='50')
        nombre = Label (frame, text='Nombre')
        nombre.config(background='lightblue', font=('Arial', 12), pady=10)
        nombre.place(x='50', y='100')
        preRequisito = Label (frame, text='Pre-Requisitos')
        preRequisito.config(background='lightblue', font=('Arial', 12), pady=10)
        preRequisito.place(x='50', y='150')
        semestre = Label (frame, text='Semestre')
        semestre.config(background='lightblue', font=('Arial', 12), pady=10)
        semestre.place(x='50', y='200')
        opcionalidad = Label (frame, text='Opcionalidad')
        opcionalidad.config(background='lightblue', font=('Arial', 12), pady=10)
        opcionalidad.place(x='50', y='250')
        creditos = Label (frame, text='Créditos')
        creditos.config(background='lightblue', font=('Arial', 12), pady=10)
        creditos.place(x='50', y='300')
        estado = Label (frame, text='Estado')
        estado.config(background='lightblue', font=('Arial', 12), pady=10)
        estado.place(x='50', y='350')
        # Entradas
        cod = StringVar()
        name = StringVar()
        pre = StringVar()
        sem = StringVar()
        opc = StringVar()
        cre = StringVar()
        esta = StringVar()
        codigoEntrada = Entry(frame, textvariable = cod, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
        codigoEntrada.insert(0, codigoTabla)
        codigoEntrada['state'] = 'disabled'
        codigoEntrada.place(x='180', y='60')
        nombreEntrada = Entry(frame, textvariable = name, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
        nombreEntrada.insert(0, nombreTabla)
        nombreEntrada.place(x='180', y='110')
        preRequisitosEntrada = Entry(frame, textvariable = pre, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
        preRequisitosEntrada.insert(0, preRequisitosTabla)
        preRequisitosEntrada.place(x='180', y='160')
        semestreEntrada = Entry(frame, textvariable = sem, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
        semestreEntrada.insert(0, semestreTabla)
        semestreEntrada.place(x='180', y='210')
        opcionalidad1 = Radiobutton (frame, text='Obligatorio', value='1', variable=opc, background='lightblue', font=('Arial', 12, 'italic'))
        opcionalidad1.place(x='220', y='260')
        opcionalidad2 = Radiobutton (frame, text='Opcional', value='0', variable=opc, background='lightblue', font=('Arial', 12, 'italic'))
        opcionalidad2.place(x='380', y='260')
        opc.set(value=opcionalidadTabla)
        creditosEntrada = Entry(frame, textvariable = cre, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
        creditosEntrada.insert(0, creditosTabla)
        creditosEntrada.place(x='180', y='310')
        estado1 = Radiobutton (frame, text='Aprobado', value='0', variable=esta, background='lightblue', font=('Arial', 12, 'italic'))
        estado1.place(x='200', y='360')
        estado2 = Radiobutton (frame, text='Cursando', value='1', variable=esta, background='lightblue', font=('Arial', 12, 'italic'))
        estado2.place(x='300', y='360')
        estado3 = Radiobutton (frame, text='Pendiente', value='-1', variable=esta, background='lightblue', font=('Arial', 12, 'italic'))
        estado3.place(x='400', y='360')
        esta.set(value=estadoTabla)
        # Botones
        botonEditar = ttk.Button (frame2, text='Editar Curso', command=lambda: self.EditarCurso(ventanaEditarCurso, codigoEntrada.get(), nombreEntrada.get(), preRequisitosEntrada.get(), semestreEntrada.get(), opc.get(), creditosEntrada.get(), esta.get()))
        botonEditar.grid(column=1, row=1, ipadx=30, ipady=5, padx=100, pady=30)
        botonCancelar = ttk.Button (frame2, text='Cancelar', command=lambda: self.MostrarEliminarVentana(ventana, ventanaEditarCurso))
        botonCancelar.grid(column=2, row=1, ipadx=35, ipady=5, padx=10, pady=30)

    # Crear ventana para el ingreso de un código de búsqueda
    def VentanaCodigo (self, ventana):
        if cursos.listado != []:
            self.OcultarVentana(ventana)
            # Ventana Código
            ventanaCodigo = Toplevel ()
            ventanaCodigo.geometry(self.EditorVentana(root, 600, 200))
            ventanaCodigo.title('INGENIERIA USAC - Buscar Curso')
            ventanaCodigo.iconbitmap('archivos/books.ico')
            ventanaCodigo.config(background='lightblue')
            ventanaCodigo.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
            ventanaCodigo.protocol('WM_DELETE_WINDOW', root.quit)
            # Frame
            frame = Frame (ventanaCodigo)
            frame.config(width='600', height='100', bg='lightblue')
            frame.place(x='0', y='100')
            frame.pack()
            # Frame Inferior
            frame2 = Frame (ventanaCodigo)
            frame2.config(width='600', height='50', bg='lightblue')
            frame2.place(x='0', y='100')
            frame2.pack()
            # Labels
            codigo = Label (frame, text='Código')
            codigo.config(background='lightblue', font=('Arial', 12), pady=10)
            codigo.place(x='50', y='50')
            # Botones
            botonBuscar = ttk.Button (frame2, text='Buscar Curso', command=lambda: self.VentanaBusqueda(cod.get(), ventanaCodigo, ventana))
            botonBuscar.grid(column=1, row=1, ipadx=30, ipady=5, padx=100, pady=30)
            botonRegresar = ttk.Button (frame2, text='Regresar', command=lambda: self.MostrarEliminarVentana(ventana, ventanaCodigo))
            botonRegresar.grid(column=2, row=1, ipadx=35, ipady=5, padx=10, pady=30)
            # Entradas
            cod = StringVar()
            codigoEntrada = Entry(frame, textvariable = cod, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
            codigoEntrada.place(x='180', y='60')
        else:
            showerror ('INGENIERIA USAC - Buscar Curso', 'No se encuentra ningún curso en el sistema.')

    # Crear ventana para el curso buscado
    def VentanaBusqueda (self, codigo, ventana, ventanaGestion):
        if codigo == '':
            showerror ('INGENIERIA USAC - Buscar Curso', 'Debe de ingresar un código')
        else:
            curso = cursos.MostrarCurso (codigo)
            if curso == None:
                showerror ('INGENIERIA USAC - Buscar Curso', 'El código ingresado no pertenece a ningún curso')
            else:
                if curso[2] == '' or curso[2] == {''} or curso[2] == ['']:
                    curso[2] = ''
                # Oculta la ventana de gestión
                self.EliminarVentana(ventana)
                # Ventana Editar Curso
                ventanaEcontrado = Toplevel ()
                ventanaEcontrado.geometry(self.EditorVentana(root, 600, 500))
                ventanaEcontrado.title('INGENIERIA USAC - Curso Encontrado')
                ventanaEcontrado.iconbitmap('archivos/books.ico')
                ventanaEcontrado.config(background='lightblue')
                ventanaEcontrado.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
                ventanaEcontrado.protocol('WM_DELETE_WINDOW', root.quit)
                # Frame
                frame = Frame (ventanaEcontrado)
                frame.config(width='600', height='400', bg='lightblue')
                frame.place(x='0', y='100')
                frame.pack()
                # Frame
                frame2 = Frame (ventanaEcontrado)
                frame2.config(width='600', height='100', bg='lightblue')
                frame2.place(x='0', y='100')
                frame2.pack()
                # Labels
                codigo = Label (frame, text='Código')
                codigo.config(background='lightblue', font=('Arial', 12), pady=10)
                codigo.place(x='50', y='50')
                nombre = Label (frame, text='Nombre')
                nombre.config(background='lightblue', font=('Arial', 12), pady=10)
                nombre.place(x='50', y='100')
                preRequisito = Label (frame, text='Pre-Requisitos')
                preRequisito.config(background='lightblue', font=('Arial', 12), pady=10)
                preRequisito.place(x='50', y='150')
                semestre = Label (frame, text='Semestre')
                semestre.config(background='lightblue', font=('Arial', 12), pady=10)
                semestre.place(x='50', y='200')
                opcionalidad = Label (frame, text='Opcionalidad')
                opcionalidad.config(background='lightblue', font=('Arial', 12), pady=10)
                opcionalidad.place(x='50', y='250')
                creditos = Label (frame, text='Créditos')
                creditos.config(background='lightblue', font=('Arial', 12), pady=10)
                creditos.place(x='50', y='300')
                estado = Label (frame, text='Estado')
                estado.config(background='lightblue', font=('Arial', 12), pady=10)
                estado.place(x='50', y='350')
                # Entradas
                cod = StringVar()
                name = StringVar()
                pre = StringVar()
                sem = StringVar()
                opc = StringVar()
                cre = StringVar()
                esta = StringVar()
                codigoEntrada = Entry(frame, textvariable = cod, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
                codigoEntrada.insert(0, curso[0])
                codigoEntrada['state'] = 'disabled'
                codigoEntrada.place(x='180', y='60')
                nombreEntrada = Entry(frame, textvariable = name, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
                nombreEntrada.insert(0, curso[1])
                nombreEntrada.place(x='180', y='110')
                preRequisitosEntrada = Entry(frame, textvariable = pre, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
                preRequisitosEntrada.insert(0, curso[2])
                preRequisitosEntrada.place(x='180', y='160')
                semestreEntrada = Entry(frame, textvariable = sem, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
                semestreEntrada.insert(0, curso[3])
                semestreEntrada.place(x='180', y='210')
                opcionalidad1 = Radiobutton (frame, text='Obligatorio', value='1', variable=opc, background='lightblue', font=('Arial', 12, 'italic'))
                opcionalidad1.place(x='220', y='260')
                opcionalidad2 = Radiobutton (frame, text='Opcional', value='0', variable=opc, background='lightblue', font=('Arial', 12, 'italic'))
                opcionalidad2.place(x='380', y='260')
                opc.set(value=curso[4])
                creditosEntrada = Entry(frame, textvariable = cre, width='40', background='white', font=('Arial', 12, 'italic'), justify=CENTER, borderwidth=2)
                creditosEntrada.insert(0, curso[5])
                creditosEntrada.place(x='180', y='310')
                estado1 = Radiobutton (frame, text='Aprobado', value='0', variable=esta, background='lightblue', font=('Arial', 12, 'italic'))
                estado1.place(x='200', y='360')
                estado2 = Radiobutton (frame, text='Cursando', value='1', variable=esta, background='lightblue', font=('Arial', 12, 'italic'))
                estado2.place(x='300', y='360')
                estado3 = Radiobutton (frame, text='Pendiente', value='-1', variable=esta, background='lightblue', font=('Arial', 12, 'italic'))
                estado3.place(x='400', y='360')
                esta.set(value=curso[6])
                # Botones
                botonEditar = ttk.Button (frame2, text='Editar Curso', command=lambda: self.EditarCurso(ventanaEcontrado, codigoEntrada.get(), nombreEntrada.get(), preRequisitosEntrada.get(), semestreEntrada.get(), opc.get(), creditosEntrada.get(), esta.get()))
                botonEditar.grid(column=1, row=1, ipadx=35, ipady=5, padx=10, pady=30)
                botonEliminar = ttk.Button (frame2, text='Eliminar Curso', command=lambda: self.EliminarCurso(ventanaEcontrado, curso[0], curso[1]))
                botonEliminar.grid(column=2, row=1, ipadx=35, ipady=5, padx=10, pady=30)
                botonCancelar = ttk.Button (frame2, text='Cancelar', command=lambda: self.MostrarEliminarVentana(ventanaGestion, ventanaEcontrado))
                botonCancelar.grid(column=3, row=1, ipadx=35, ipady=5, padx=10, pady=30)

    # Crear ventana para la gestión con los créditos
    def VentanaCreditos (self):
        self.OcultarVentana(root)
        # Ventana Créditos
        ventanaCreditos = Toplevel ()
        ventanaCreditos.geometry(self.EditorVentana(root, 600, 500))
        ventanaCreditos.title('INGENIERIA USAC - Gestión de créditos')
        ventanaCreditos.iconbitmap('archivos/books.ico')
        ventanaCreditos.config(background='lightblue')
        ventanaCreditos.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        ventanaCreditos.protocol('WM_DELETE_WINDOW', root.quit)
        # Frame Superior
        frame = Frame (ventanaCreditos)
        frame.config(width='600', height='150', bg='lightblue')
        frame.place(x='0', y='100')
        frame.pack()
        # Frame Central
        frame2 = Frame (ventanaCreditos)
        frame2.config(width='600', height='280', bg='lightblue')
        frame2.place(x='0', y='100')
        frame2.pack()
        # Frame Inferior
        frame3 = Frame (ventanaCreditos)
        frame3.config(width='400', height='100', bg='lightblue')
        frame3.place(x='0', y='100')
        frame3.pack()
        # Labels Superiores
        creditosAprobados = Label (frame, text = f'Créditos Aprobados: {cursos.CreditosAprobados()}')
        creditosAprobados.config(background='lightblue', font=('Arial', 12, 'italic'), justify='left')
        creditosAprobados.place(x='60', y='30')
        creditosCursando = Label (frame, text = f'Créditos Cursando: {cursos.CreditosCursando()}')
        creditosCursando.config(background='lightblue', font=('Arial', 12, 'italic'), justify='left')
        creditosCursando.place(x='60', y='70')
        creditosPendientes = Label (frame, text = f'Créditos Pendientes: {cursos.CreditosPendientes()}')
        creditosPendientes.config(background='lightblue', font=('Arial', 12, 'italic'), justify='left')
        creditosPendientes.place(x='60', y='110')
        # Labels centrales
        creditosObligatorios = Label (frame2, text = 'Créditos obligatorios hasta el semestre: ')
        creditosObligatorios.config(background='lightblue', font=('Arial', 12, 'italic'), justify='left')
        creditosObligatorios.place(x='60', y='20')
        comboObligatorios = ttk.Combobox(frame2)
        comboObligatorios['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        comboObligatorios.config(width='5')
        comboObligatorios.current(0)
        comboObligatorios.place(x='360', y='22')
        botonCalculo1 = ttk.Button (frame2, text='Calcular', command=lambda: self.CreditosN(calculo1, comboObligatorios.get()))
        botonCalculo1.grid(column=1, row=1, ipadx=80, ipady=5, padx=10, pady=10)
        botonCalculo1.place(x='150', y='70')
        calculo1 = StringVar()
        calculo1.set('0 Créditos Obligatorios')
        textoCalculo1 = Label (frame2, textvariable=calculo1)
        textoCalculo1.config(background='lightblue', font=('Arial', 12, 'italic'), justify='left')
        textoCalculo1.place(x='250', y='70')

        creditosSemestre = Label (frame2, text = 'Créditos del semestre:')
        creditosSemestre.config(background='lightblue', font=('Arial', 12, 'italic'), justify='left')
        creditosSemestre.place(x='60', y='130')
        comboSemestre = ttk.Combobox(frame2)
        comboSemestre['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        comboSemestre.config(width='5')
        comboSemestre.current(0)
        comboSemestre.place(x='240', y='132')
        botonCalculo2 = ttk.Button (frame2, text='Calcular', command=lambda: self.CreditosSemestre(calculo2, comboSemestre.get()))
        botonCalculo2.grid(column=1, row=1, ipadx=80, ipady=5, padx=10, pady=10)
        botonCalculo2.place(x='150', y='180')
        calculo2 = StringVar()
        calculo2.set('0 Créditos Aprobados\n0 Créditos Asignados\n0 Créditos Pendientes')
        textoCalculo2 = Label (frame2, textvariable=calculo2)
        textoCalculo2.config(background='lightblue', font=('Arial', 12, 'italic'), justify='left')
        textoCalculo2.place(x='250', y='180')
        # Botones
        botonRegresar = ttk.Button (frame3, text='Regresar', command=lambda: self.MostrarEliminarVentana(root, ventanaCreditos))
        botonRegresar.grid(column=1, row=1, ipadx=80, ipady=5, padx=10, pady=10)

    #!:::::::::::::::::::::::::::MÉTODOS DE VENTANAS::::::::::::::::::::::::::::::::::::::::
    # Función para definir el tamaño de la ventana y centrarlo en la pantalla
    def EditorVentana (self, ventana, ancho, alto):
        x = ventana.winfo_screenwidth() // 2 - ancho // 2
        y = ventana.winfo_screenheight() // 2 - alto // 2
        posicion = f'{str(ancho)}x{str(alto)}+{str(x)}+{str(y)}'
        return posicion

    # Método para eliminar la pantalla actual y mostrar en pantalla la ventana oculta
    def MostrarEliminarVentana (self, ventanaMostrar, ventanaEliminar):
        ventanaEliminar.destroy()
        ventanaMostrar.deiconify()

    # Método para ocultar la ventana actual
    def OcultarVentana (self, ventana):
        ventana.withdraw()

    # Método para eliminar la ventana actual
    def EliminarVentana (self, ventana):
        ventana.destroy()

    #!::::::::::::::::::::::::::::MÉTODOS GENERALES:::::::::::::::::::::::::::::::::::::::::
    # Método para abrir y cargar archivos
    def AbrirArchivo (self):
        ruta = filedialog.askopenfilename(title='Abrir', filetypes=(('Archivos LFP (*.lfp)','*.lfp'),))
        if (ruta != ''):
            cursos.CargaData(ruta)
            showinfo('Carga de cursos', 'Los datos se han cargado correctamente')
    
    # Método para agregar datos en una tabla
    def InsertarDatos (self, tabla):
        for dato in cursos.listado:
            separado = dato.pre_requisitos
            pre_requisitos = '--'
            obligatorio = 'No'
            estado = 'Aprobado'
            if separado != ['']:
                if separado == '':
                    pass
                else:
                    pre_requisitos = separado
            if dato.obligatorio == '1':
                obligatorio = 'Si'
            if dato.estado == '1':
                estado = 'Cursando'
            elif dato.estado == '-1':
                estado = 'Pendiente'
            tabla.insert('', END, text=dato.codigo, values=(dato.nombre, pre_requisitos, obligatorio, dato.semestre, dato.creditos, estado))

    # Método para agregar cursos a la base de datos
    def AgregarCurso (self, ventana, codigo, nombre, preRequisitos, semestre, opcionalidad, creditos, estado):
        if codigo == '' or nombre == '' or semestre == '' or creditos == '':
            showerror ('INGENIERIA USAC - Agregar Curso', 'Aún no se han ingresado todos los datos')
        else:
            if semestre == '1' or semestre == '2' or semestre == '3' or semestre == '4' or semestre == '5' or semestre == '6' or semestre == '7' or semestre == '8' or semestre == '9' or semestre == '10':
                cursos.EliminarCurso(codigo)
                cursos.AgregarCurso(codigo, nombre, preRequisitos, opcionalidad, semestre, creditos, estado)
                self.EliminarVentana(ventana)
                self.VentanaGestion()
                showinfo ('INGENIERIA USAC - Agregar Curso', f'El curso {nombre} fue agregado correctamente')
            else:
                showerror ('INGENIERIA USAC - Agregar Curso', 'El número de semestre no es válido')

    # Método para editar cursos en la base de datos
    def EditarCurso (self, ventana, codigo, nombre, preRequisitos, semestre, opcionalidad, creditos, estado):
        if nombre == '' or semestre == '' or creditos == '':
            showerror ('INGENIERIA USAC - Editar Curso', 'Aún no se han ingresado todos los datos')
        else:
            if semestre == '1' or semestre == '2' or semestre == '3' or semestre == '4' or semestre == '5' or semestre == '6' or semestre == '7' or semestre == '8' or semestre == '9' or semestre == '10':
                cursos.EditarCurso(codigo, nombre, preRequisitos, opcionalidad, semestre, creditos, estado)
                self.EliminarVentana(ventana)
                self.VentanaGestion()
                showinfo ('INGENIERIA USAC - Editar Curso', f'El curso {codigo} fue editado correctamente')
            else:
                showerror ('INGENIERIA USAC - Editar Curso', 'El número de semestre no es válido')

    # Método para eliminar cursos en la base de datos
    def EliminarCurso (self, ventana, codigo, nombre):
        respuesta = askyesno('INGENIERIA USAC - Eliminar Curso', f'¿Estás seguro de borrar el curso {codigo} - {nombre}?')
        if respuesta == True:
            cursos.EliminarCurso(codigo)
            self.EliminarVentana(ventana)
            self.VentanaGestion()
            showinfo ('INGENIERIA USAC - Eliminar Curso', f'El curso {nombre} fue eliminado exitosamente')

    # Método para contar los créditos obligatorios hasta el semestre N y trasladarlos a un label
    def CreditosN (self, texto, semestre):
        texto.set(f'{cursos.CreditosN(semestre)} Créditos Obligatorios')

    # Método para contar los créditos de determinado semestre y trasladarlos a un label
    def CreditosSemestre (self, texto, semestre):
        listado = cursos.CreditosSemestre(semestre)
        texto.set(f'{listado[0]} Créditos Aprobados\n{listado[1]} Créditos Asignados\n{listado[2]} Créditos Pendientes')
