from ClasePersona import Persona
from ClaseManejadorTalleres import ManejadorTalleres
from ClaseManejadorPersonas import ManejadorPersonas
from ClaseManejadorInscripciones import ManejadorInscripciones

if __name__ == '__main__':

    ListaTalleres = ManejadorTalleres()
    ListaPersonas = ManejadorPersonas()
    ListaInscripciones = ManejadorInscripciones(10,5)

    archivo = "Talleres.csv"
    ListaTalleres.cargaTalleres(archivo)
    ban = True
    while ban:
        print("Menu")
        print("1 - Talleres")
        print("2 - Inscribir una persona en un taller")
        print("3 - Consultar inscripción")
        print("4 - Consultar inscriptos")
        print("5 - Registrar pago")
        print("6 - Guardar inscripciones")
        print("0 - Salir")

        op = input("Ingrese una opcion: ")

        if op == "0":
            ban = False

        elif op == "1":
            ListaTalleres.mostrarTalleres()

        elif op == "2":
            idTaller = input("Ingrese ID del taller: ")
            taller = ListaTalleres.getTaller(idTaller)

            if taller == None:
                print("Taller no encontrado")
            else:
                vacantes = taller.actualizarVacantes()
                if not vacantes:
                    print("El taller no tiene vacantes")
                else:
                    nombre = input("Ingrese nombre: ")
                    direccion = input("Ingrese direccion: ")
                    dni = input("Ingrese DNI: ")
                    persona = Persona(nombre, direccion, dni)
                    ListaPersonas.agregarPersona(persona)
                    taller.agregarPersona(persona)

                    fecha = input("Ingrese fecha de inscripcion: ")
                    ListaInscripciones.registrarInscripcion(taller, persona, fecha)

        elif op == "3":
            dni = input("Ingrese DNI: ")
            inscripcion = ListaInscripciones.getInscripcionporDNI(dni)
            if inscripcion == None:
                print("Persona no encontrada")
            else:
                ListaInscripciones.consultarInscripcion(inscripcion)

        elif op == "4":
            idTaller = input("Ingrese ID del taller: ")
            taller = ListaTalleres.getTaller(idTaller)
            if taller == None:
                print("Taller no encontrado")
            else:
                taller.consultarInscriptos()

        elif op == "5":
            dni = input("Ingrese DNI: ")
            inscripcion = ListaInscripciones.getInscripcionporDNI(dni)
            if inscripcion == None:
                print("Persona no encontrada")
            else:
                ListaInscripciones.registrarPago(inscripcion)

        elif op == "6":
            nuevo = "Inscripciones.csv"
            ListaInscripciones.generarArchivo(nuevo)

        else:
            print("Opcion no valida")

        print("")