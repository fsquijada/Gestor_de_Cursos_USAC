from archivos.cursos import Cursos

cursos = Cursos ()

# cursos.ListadoCursos()
# print("--------------------------")
# cursos.AgregarCurso("017", "Social Humanistica 1", "", "1", "1", "4", "0")
# cursos.AgregarCurso("101", "Matematica basica 1", "", "1", "1", "7", "0")
# cursos.AgregarCurso("069", "Tecnica Complementaria 1", "", "1", "1", "3", "0")
# cursos.AgregarCurso("039", "Deportes 1", "", "0", "1", "1", "-1")
# cursos.AgregarCurso("348", "Quimica General 1", "", "1", "1", "3", "0")
# cursos.AgregarCurso("006", "Idioma Tecnico 1", "", "0", "1", "2", "0")
# cursos.AgregarCurso("150", "Fisica 1", "103, 147", "1", "3", "6", "1")
# cursos.ListadoCursos()

cursos.CargaData("archivos/contenido.lfp")
# cursos.ListadoCompleto()
# cursos.MostrarCurso("960")
# cursos.MostrarCurso("152")
# cursos.AgregarCurso("152", "Física 2222", "107;150", "100", "400", "600", "0")
# cursos.MostrarCurso("152")
# cursos.ListadoCompleto()
# cursos.EditarCurso("152", "Física 2", "107;150", "1", "4", "6", "-1")
# cursos.EliminarCurso("152")
# cursos.ListadoCompleto()
# cursos.CreditosAprobados()
# cursos.CreditosCursando()
# cursos.CreditosPendientes()
# cursos.CreditosN ("3")
# cursos.CreditosSemestre("2")
