alumnos_presentes = []
alumnos_ausentes = []
def menu():
    print("Para ingresar un alumno ausente escriba 1")
    print("Para eliminar un alumno de la lista de ausentes escriba 2")
    print("Para ingresar un alumno presente escriba 3")
    print("Para eliminar un alumno de la lista de presentes escriba 4")
    print("Para ver la lista de alumnos presentes escriba 5")
    print("Para ver la lista de alumnos ausentes escriba 6")
    print("Para salir escriba 7")


while True:
    menu()
    eleccion= int(input("Escriba su eleccion: "))
    if eleccion == 1:
        alumno_presente = input("Escriba el nombre del alumno presente: ")
        alumnos_presentes.append(alumno_presente)
    elif eleccion == 2: 
        alumno_ausente = input("Escriba el nombre del alumno ausente: ")
        alumnos_ausentes.append(alumno_ausente)
    elif eleccion == 3:
        alumno_presente_remover = input("Escriba el nombre del alumno presente que desea eliminar de la lista de presentes: ")
        if alumno_presente_remover in alumnos_presentes:
            alumno_presente.remove(alumno_presente_remover)
        else:
            print("El alumno no se encuentra en la lista de presentes") 
    elif eleccion == 4:
        alumno_ausente_remover = input("Escriba el nombre del alumno que desea eliminar de la lista de ausente: ")
        if alumno_ausente_remover in alumnos_ausentes: 
            alumno_ausente.remove(alumno_ausente_remover)
        else:
            print("El alumno no se encuentra en la lista de ausentes")
    elif eleccion == 5:
        print (f"La lista de alumnos presentes es: {alumnos_presentes}")
    elif eleccion == 6:
        print (f"La lista de alumnos ausentes es: {alumnos_ausentes}")
    elif eleccion == 7:
        print ("Operación terminada")
        break
    else:
        print ("Opcion invalida")