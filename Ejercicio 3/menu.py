import producto

def iniciar():
    print('''
    1. Aplicar rebaja a un producto
    2. Nada
    ''')
    opcion= input('Elige una opcion: ')

    if opcion == '1':
        print('Aplicar rebaja')
        from producto import rebajar_producto
        rebajar_producto()
    elif opcion == '2':
        print('Nada')
    else:
        print('Opcion no valida')
        

