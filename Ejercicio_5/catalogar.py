import vehiculo
import coche 
import bicicleta
import camioneta
import motocicleta

vehiculos= [coche.Coche('rojo', 4, 120, 1000), bicicleta.Bicicleta('azul', 2, 'urbana'), camioneta.Camioneta('verde', 4, 100, 1500, 500), motocicleta.Motocicleta('negra', 2, 'deportiva', 200, 600)]

def catalogar(vehiculos):
    for v in vehiculos:
        print('{} {}'.format(type(v).__name__, v))

def catalogar2(vehiculos, ruedas=None):
    if ruedas != None:
        contador=0
        for v in vehiculos:
            if v.ruedas == ruedas:
                contador+=1
        print("Hay {} vehículos con {} ruedas".format(contador,ruedas))
        print('--------------------------------------------------------')
    else:
        for v in vehiculos:
            if v.ruedas == ruedas:
                print('{} {}'.format(type(v).__name__, v))

                