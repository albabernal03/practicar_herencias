

def dividir():
    try:
        dividendo = int(input("Ingrese el dividendo: "))
        divisor = int(input("Ingrese el divisor: "))
        resultado = dividendo / divisor
        print("El resultado es: ", resultado)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        dividir()
    except ValueError:
        print("Solo se permiten numeros")
        dividir()
    except:
        print("Error desconocido")
        dividir()
