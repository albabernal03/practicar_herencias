import alumno
import calificacion


class AlumnoNota(alumno.Alumno, calificacion.Nota):
    def __init__(self, nombre, nota):
        alumno.Alumno.__init__(self, nombre)
        calificacion.Nota.__init__(self, nota)
    def __str__(self):
        return alumno.Alumno.__str__(self) + ", " + calificacion.Nota.__str__(self) + ", " + calificacion.Nota.aprobado_supendido(self)

if __name__ == "__main__":
    alumno_nota = AlumnoNota("Juan", 7)
    print(alumno_nota)
    



