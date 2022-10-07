def lista2():
    try:
        paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
        p= input('introduca pais:')
        if p in paises:
            print('el idioma es:',paises[p])
        else:
            print('no se encuentra el pais')
            lista2()
    except ValueError:
        print("solo se permiten numeros")
        lista2()
    except:
        print("error desconocido")
        lista2()
        



