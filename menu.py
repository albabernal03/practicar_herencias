import herencias
import os

def iniciar():
    os.system('clear') # Limpia la pantalla, en Windows es 'cls'
    print('-------------------------')
    print(' ---Bienvenid@ al menú---')
    print('-------------------------')
    print('[1].  Catalogar vehículos')
    print('[2].  Catalogar vehículos por número de ruedas')
    print('[3].  Salir')
    print('-------------------------')

    opcion= input('Ingrese una opción: ')
    if opcion == '1':
        os.system('clear')
        herencias.catalogar(herencias.vehiculos)
        input('Presione una tecla para continuar...')
        iniciar()
    elif opcion == '2':
        os.system('clear')
        herencias.catalogar2(herencias.vehiculos,0)
        input('Presione una tecla para continuar...')
        iniciar()
    elif opcion == '3':
        print('Gracias por utilizar el programa')
        exit()
    else:
        os.system('clear')
        print('Opción incorrecta')
        iniciar()
        