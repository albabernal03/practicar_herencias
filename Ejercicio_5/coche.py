from Ejercicio_5 import coche

class Coche:
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return "color {}, {} ruedas, {} km/h, {} cc".format(self.color, self.ruedas, self.velocidad, self.cilindrada)


