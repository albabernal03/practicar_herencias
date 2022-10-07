class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return "nombre {}, nota {}".format(self.nombre, self.nota)

        