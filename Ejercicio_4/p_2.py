

def lista():
    try:
        lista=[1,2,3,4,5,6,7,8,9,10]
        numero=int(input("ingrese un numero: "))
        if numero in lista:
            print("el numero esta en la lista")
        else:
            print("el numero no esta en la lista")
            lista()
    except ValueError:
        print("solo se permiten numeros")
        lista()
    except:
        print("error desconocido")
        lista()