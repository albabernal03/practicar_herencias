import coche

class Camioneta(coche.Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada,carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return super().__str__() + ", {} kg".format(self.carga)
        