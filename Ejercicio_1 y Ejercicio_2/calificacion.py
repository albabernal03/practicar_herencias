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
            