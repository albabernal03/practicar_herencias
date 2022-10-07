
import vehiculo
import motocicleta
import coche
import camioneta
import bicicleta
import os
from catalogar import catalogar
from catalogar import catalogar2

def iniciar():
    while True:
        os.system('clear')
        print('===============================')
        print(' Bienvenido al menu de vehiculos')
        print('===============================')
        print('1. Catalogar vehiculos')
        print('2. Catalogar vehiculos por ruedas')
        print('3. Salir')
        opcion = input('Elige una opcion: ')
        if opcion == '1':
            catalogar()
        elif opcion == '2':
            catalogar2()
        elif opcion == '3':
            break
        else:
            print('Opcion no valida')
            

        