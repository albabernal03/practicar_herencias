

def suma():
    try:
        numero1=int(input("ingrese un numero: "))
        numero2=int(input("ingrese otro numero: "))
        resultado=numero1+numero2
        print("el resultado es: ",resultado)
    except ValueError:
        print("solo se permiten numeros")
        suma()
    except:
        print("error desconocido")
        suma()  

