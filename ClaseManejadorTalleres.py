from ClaseTallerCapacitacion import TallerCapacitacion
import numpy as np
import csv


class ManejadorTalleres:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    __talleres = []

    def __init__(self, dimension=0, incremento=5):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        self.__talleres = np.empty(dimension, dtype=TallerCapacitacion)

    def agregarTaller(self, taller):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__talleres.resize(self.__dimension)

        self.__talleres[self.__cantidad] = taller
        self.__cantidad += 1

    def cambiarDimension(self, dimension):
        self.__dimension = dimension
        self.__talleres.resize(self.__dimension)

    def cargaTalleres(self, file):
        archivo = open(file, "r")
        reader = csv.reader(archivo, delimiter=",")

        """dim = next(reader)
        self.cambiarDimension(int(dim))"""
        next(reader)

        for line in reader:
            taller = TallerCapacitacion(line[0], line[1], line[2], line[3])
            self.agregarTaller(taller)

        archivo.close()

    def getTaller(self, idTaller):
        taller = None
        i = 0
        while taller == None and i < self.__cantidad:
            if idTaller == self.__talleres[i].getIdTaller():
                taller = self.__talleres[i]
            else:
                i += 1

        return taller

    def mostrarTalleres(self):
        for i in range(self.__cantidad):
            print(self.__talleres[i])