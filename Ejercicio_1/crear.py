import alumno

def crear_alumno():
    nombre = input("Nombre: ")
    nota = int(input("Nota: "))
    return alumno.AlumnoNota(nombre, nota)
