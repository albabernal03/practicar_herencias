class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return'nombre: {}'.format(self.nombre)

class Nota:
    def __init__(self, nota):
        self.nota = nota
    def __str__(self):
        return "nota {}".format(self.nota)
    
    def aprobado_supendido(self):
        if self.nota >= 5:
            return "aprobado"
        else:
            return "suspendido"

class AlumnoNota(Alumno, Nota):
    def __init__(self, nombre, nota):
        Alumno.__init__(self, nombre)
        Nota.__init__(self, nota)
    def __str__(self):
        return Alumno.__str__(self) + ", " + Nota.__str__(self) + ", " + Nota.aprobado_supendido(self)

if __name__ == "__main__":
    alumno = AlumnoNota("Juan", 7)
    print(alumno)



