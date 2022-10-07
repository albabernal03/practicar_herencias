import alumno
import nota


class AlumnoNota(alumno.Alumno, nota.Nota):
    def __init__(self, nombre, nota):
        alumno.Alumno.__init__(self, nombre)
        nota.Nota.__init__(self, nota)
    def __str__(self):
        return alumno.Alumno.__str__(self) + ", " + Nota.__str__(self) + ", " + Nota.aprobado_supendido(self)



