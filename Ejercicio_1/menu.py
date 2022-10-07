import crear

def iniciar():
    print("Bienvenido al menu")
    print('[1]. Crear alumno y nota')
    print('[2]. Salir')

    opcion = input("Seleccione una opcion: ")
    if opcion == '1':
        crear.AlumnoNota()
    elif opcion == '2':
        print("Saliendo...")
        exit()
    else:
        print("Opcion invalida")
        iniciar()
        



    
