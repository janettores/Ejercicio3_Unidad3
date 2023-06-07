from ClaseInscripcion import Inscripcion
import numpy as np
import csv


class ManejadorInscripciones:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    __inscripciones = None

    def __init__(self, dimension, incremento=5):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        self.__inscripciones = np.empty(dimension, dtype=Inscripcion)

    def mostrarInscripciones(self):
        for i in range(self.__cantidad):
            print(self.__inscripciones[i])

    def agregarInscripcion(self, inscripcion):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__inscripciones.resize(self.__dimension)
        self.__inscripciones[self.__cantidad] = inscripcion
        self.__cantidad += 1

    def registrarInscripcion(self, taller, persona, fecha):
        inscripcion = Inscripcion(persona, taller, fecha)
        self.agregarInscripcion(inscripcion)

    def getInscripcionporDNI(self, dni):
        inscripcion = None
        i = 0
        while inscripcion == None and i < self.__cantidad:
            if dni == self.__inscripciones[i].getPersona().getDNI():
                inscripcion = self.__inscripciones[i]
            else:
                i += 1

        return inscripcion

    def consultarInscripcion(self, inscripcion):
        print(f"Taller de {inscripcion.getTaller().getNombre()}, Monto: {inscripcion.getTaller().getMonto()}")

    def registrarPago(self, inscripcion):
        inscripcion.actualizarPago()

    def generarArchivo(self, newfile):

        archivo = open(newfile, "w", newline="")
        writer = csv.writer(archivo)

        for i in range(self.__cantidad):
            line = [self.__inscripciones[i].getPersona().getDNI(), self.__inscripciones[i].getTaller().getIdTaller(),
                    self.__inscripciones[i].getFecha(), self.__inscripciones[i].getPago()]
            writer.writerow(line)

        archivo.close()