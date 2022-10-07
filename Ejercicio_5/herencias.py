#TODO: cambiar


class Vehiculo():

    def __init__(self,color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas) #el super() llama al constructor de la clase madre
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada,carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return super().__str__() + ", {} kg".format(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


vehiculos=[Coche("rojo", 4, 150, 1200),Camioneta("blanco", 4, 100, 2000, 500),Bicicleta("azul", 2, "urbana"), Motocicleta('negra', 2, 'deportiva', 200, 600)]

def catalogar(vehiculos):
    for v in vehiculos:
        print('{} {}'.format(type(v).__name__, v))
catalogar(vehiculos)

def catalogar2(vehículos,ruedas=None):
    if ruedas != None:
        contador=0
        for v in vehículos:
            if v.ruedas == ruedas:
                contador+=1
        print("Hay {} vehículos con {} ruedas".format(contador,ruedas))
        print('--------------------------------------------------------')
    else:
        if v.ruedas == ruedas:
            print('{} {}'.format(type(v).__name__, v))
catalogar2(vehiculos,0)