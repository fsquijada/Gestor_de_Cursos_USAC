# Clase del listado principal de cursos
class Listado:
    def __init__(self, codigo, nombre, pre_requisitos, obligatorio, semestre, creditos, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.pre_requisitos = pre_requisitos
        self.obligatorio = obligatorio
        self.semestre = semestre
        self.creditos = creditos
        self.estado = estado

# Clase para separar los pre-requisitos en un listado
class Pre_Cursos:
    def __init__(self, cursos):
        self.cursos = cursos

class Cursos:
    def __init__(self):
        # Esto simula la base de datos del listado de clases
        self.listado = []

    # Carga del listado de cursos
    def CargaData (self, ruta):
        # archivo = open(ruta, "r", "", "utf-8")
        archivo = open(ruta, "r", 1, "utf-8")
        listaClases = archivo.read()
        archivo.close()
        x = listaClases.replace("\n", ",") # Reemplaza los saltos de línea por comas
        y = x.split(",") # Separa todo el string por cada coma
        # Iteración para ir agregando cada curso
        contador = 0
        codigo = ""
        nombre = ""
        pre_requisitos = ""
        obligatorio = ""
        semestre = ""
        creditos = ""
        estado = ""
        for dato in y:
            if contador == 0:
                codigo = dato
                contador += 1
            elif contador == 1:
                nombre = dato
                contador += 1
            elif contador == 2:
                clases = dato.split(";")
                pre_requisitos = clases
                contador += 1
            elif contador == 3:
                obligatorio = dato
                contador += 1
            elif contador == 4:
                semestre = dato
                contador += 1
            elif contador == 5:
                creditos = dato
                contador += 1
            else:
                estado = dato
                contador = 0
                self.EliminarCurso(codigo)
                nuevo = Listado (codigo, nombre, pre_requisitos, obligatorio, semestre, creditos, estado)
                self.listado.append (nuevo)

    # Ver listado actual
    def ListadoCompleto (self):
        for curso in self.listado:
            print(f"Codigo: {curso.codigo}, Nombre: {curso.nombre}, Pre: {curso.pre_requisitos}, Obligatorio: {curso.obligatorio}, Semestre: {curso.semestre}, Creditos: {curso.creditos}, Estado: {curso.estado}")

    # Mostrar un Curso
    def MostrarCurso (self, codigo):
        for curso in self.listado:
            if codigo == curso.codigo:
                print(f"Codigo: {curso.codigo}, Nombre: {curso.nombre}, Pre: {curso.pre_requisitos}, Obligatorio: {curso.obligatorio}, Semestre: {curso.semestre}, Creditos: {curso.creditos}, Estado: {curso.estado}")
                return
        return None

    # Agregar Curso
    def AgregarCurso (self, codigo, nombre, pre_requisitos, obligatorio, semestre, creditos, estado):
        nuevo = Listado(codigo, nombre, pre_requisitos, obligatorio, semestre, creditos, estado)
        self.listado.append (nuevo)

    # Editar Curso
    def EditarCurso (self, codigo, nombre, pre_requisitos, obligatorio, semestre, creditos, estado):
        for curso in self.listado:
            if codigo == curso.codigo:
                curso.nombre = nombre
                curso.pre_requisitos = pre_requisitos
                curso.obligatorio = obligatorio
                curso.semestre = semestre
                curso.creditos = creditos
                curso.estado = estado
                return
        return None

    # Eliminar Curso
    def EliminarCurso (self, codigo):
        for curso in self.listado:
            if codigo == curso.codigo:
                self.listado.remove (curso)
                print("Curso eliminado")
                return
        print("No existe ese curso")
        return None

    # Cantidad de créditos aprobados
    def CreditosAprobados (self):
        creditos = 0
        for curso in self.listado:
            if curso.estado == "0":
                creditos += int(curso.creditos)
        print(f"Créditos Aprobados: {creditos}")
        #!return creditos

    # Cantidad de créditos cursando
    def CreditosCursando (self):
        creditos = 0
        for curso in self.listado:
            if curso.estado == "1":
                creditos += int(curso.creditos)
        print(f"Créditos Cursando: {creditos}")
        #!return creditos

    # Cantidad de créditos pendientes
    def CreditosPendientes (self):
        creditos = 0
        for curso in self.listado:
            if curso.estado == "-1":
                creditos += int(curso.creditos)
        print(f"Créditos Pendientes: {creditos}")
        return creditos

    # Cantidad de créditos hasta semestre N
    def CreditosN (self, semestre):
        creditos = 0
        for curso in self.listado:
            if  int(curso.semestre) <= int(semestre):
                if curso.obligatorio == "1":
                    creditos += int(curso.creditos)
        print(f"Creditos obligatorios hasta el semestre {semestre}: {creditos}")
        return creditos

    # Cantidad de créditos del semestre
    def CreditosSemestre (self, semestre):
        creditosAprobados = 0
        creditosAsignados = 0
        creditosPendientes = 0
        for curso in self.listado:
            if int(semestre) == int(curso.semestre):
                if curso.estado == "0":
                    creditosAprobados += int(curso.creditos)
                elif curso.estado == "1":
                    creditosAsignados += int(curso.creditos)
                else:
                    creditosPendientes += int(curso.creditos)
        print (f"Aprobados: {creditosAprobados}\nAsignados: {creditosAsignados}\nPendientes: {creditosPendientes}")