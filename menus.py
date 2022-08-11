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
    #!::::::::::::::::::::::::::::::::VENTANAS::::::::::::::::::::::::::::::::::::::::::::::
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
        # Evento al hacer doble click en la tabla
        def Click (event):
            if cursos.listado != []:
                botonEditar['state'] = 'normal'
                botonEliminar['state'] = 'normal'
            #print (str(tabla.item(tabla.selection())['text']))
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
        botonAgregar = ttk.Button (frame2, text='Agregar Curso', command=lambda: self.VentanaAgregar(ventanaGestionarCursos))
        botonAgregar.grid(column=1, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonEditar = ttk.Button (frame2, text='Editar Curso', command=lambda: self.VentanaEditar(ventanaGestionarCursos, tabla))
        botonEditar.grid(column=2, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonEditar['state'] = 'disabled'
        botonEliminar = ttk.Button (frame2, text='Eliminar Curso', command=lambda: self.EliminarCurso(ventanaGestionarCursos, tabla.item(tabla.selection())['text'], tabla.item(tabla.selection())['values'][0]))
        botonEliminar.grid(column=3, row=1, ipadx=55, ipady=5, padx=10, pady=10)
        botonEliminar['state'] = 'disabled'
        botonRegresar = ttk.Button (frame2, text='Regresar', command=lambda: self.MostrarEliminarVentana(root, ventanaGestionarCursos))
        botonRegresar.grid(column=3, row=2, ipadx=60, ipady=5, padx=10, pady=10)
        
    # Crear Ventana para agregar nuevos cursos
    def VentanaAgregar (self, ventana):
        self.OcultarVentana(ventana)
        # Ventana Agregar Cursos
        ventanaGestionarCursos = Toplevel ()
        ventanaGestionarCursos.geometry(self.EditorVentana(root, 600, 500))
        ventanaGestionarCursos.title('INGENIERIA USAC - Agregar Curso')
        ventanaGestionarCursos.iconbitmap('archivos/books.ico')
        ventanaGestionarCursos.config(background='lightblue')
        #ventanaGestionarCursos.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        ventanaGestionarCursos.protocol('WM_DELETE_WINDOW', root.quit)
        # Frame
        frame = Frame (ventanaGestionarCursos)
        frame.config(width='600', height='400', bg='lightblue')
        frame.place(x='0', y='100')
        frame.pack()
        # Frame
        frame2 = Frame (ventanaGestionarCursos)
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
        botonAgregar = ttk.Button (frame2, text='Agregar Curso', command=lambda: self.AgregarCurso(ventanaGestionarCursos, codigoEntrada.get(), nombreEntrada.get(), preRequisitosEntrada.get(), semestreEntrada.get(), opc.get(), creditosEntrada.get(), est.get()))
        botonAgregar.grid(column=1, row=1, ipadx=30, ipady=5, padx=100, pady=30)
        botonCancelar = ttk.Button (frame2, text='Cancelar', command=lambda: self.MostrarEliminarVentana(ventana, ventanaGestionarCursos))
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
        # Ventana Agregar Cursos
        ventanaGestionarCursos = Toplevel ()
        ventanaGestionarCursos.geometry(self.EditorVentana(root, 600, 500))
        ventanaGestionarCursos.title('INGENIERIA USAC - Agregar Curso')
        ventanaGestionarCursos.iconbitmap('archivos/books.ico')
        ventanaGestionarCursos.config(background='lightblue')
        #ventanaGestionarCursos.resizable(0,0) # Para que no se pueda modificar tamaño de ventana
        ventanaGestionarCursos.protocol('WM_DELETE_WINDOW', root.quit)
        # Frame
        frame = Frame (ventanaGestionarCursos)
        frame.config(width='600', height='400', bg='lightblue')
        frame.place(x='0', y='100')
        frame.pack()
        # Frame
        frame2 = Frame (ventanaGestionarCursos)
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
        botonEditar = ttk.Button (frame2, text='Editar Curso', command=lambda: self.EditarCurso(ventanaGestionarCursos, codigoEntrada.get(), nombreEntrada.get(), preRequisitosEntrada.get(), semestreEntrada.get(), opc.get(), creditosEntrada.get(), esta.get()))
        botonEditar.grid(column=1, row=1, ipadx=30, ipady=5, padx=100, pady=30)
        botonCancelar = ttk.Button (frame2, text='Cancelar', command=lambda: self.MostrarEliminarVentana(ventana, ventanaGestionarCursos))
        botonCancelar.grid(column=2, row=1, ipadx=35, ipady=5, padx=10, pady=30)

    # Crear ventana para la gestión con los créditos
    def VentanaCreditos (self):
        pass
    
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
        if codigo == "" or nombre == "" or semestre == "" or creditos == "":
            showerror ('INGENIERIA USAC - Agregar Curso', 'Aún no se han ingresado todos los datos')
        else:
            if semestre == '1' or semestre == '2' or semestre == '3' or semestre == '4' or semestre == '5' or semestre == '6' or semestre == '7' or semestre == '8' or semestre == '9' or semestre == '10':
                cursos.AgregarCurso(codigo, nombre, preRequisitos, opcionalidad, semestre, creditos, estado)
                self.EliminarVentana(ventana)
                self.VentanaGestion()
                showinfo ('INGENIERIA USAC - Agregar Curso', f'El curso {nombre} fue agregado correctamente')
            else:
                showerror ('INGENIERIA USAC - Agregar Curso', 'El número de semestre no es válido')

    # Método para editar cursos en la base de datos
    def EditarCurso (self, ventana, codigo, nombre, preRequisitos, semestre, opcionalidad, creditos, estado):
        if nombre == "" or semestre == "" or creditos == "":
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
