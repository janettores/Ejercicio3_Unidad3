class TallerCapacitacion:
    __idTaller = ""
    __nombre = ""
    __vacantes = 0
    __montoInscripcion = 0
    __personas = []

    def __init__(self, idTaller, nom, vacantes, monto):
        self.__idTaller = idTaller
        self.__nombre = nom
        self.__vacantes = int(vacantes)
        self.__montoInscripcion = int(monto)
        self.__personas = []

    def __str__(self):
        return f"{self.__idTaller}, {self.__nombre}, {self.__vacantes}, {self.__montoInscripcion}"

    def getIdTaller(self):
        return self.__idTaller

    def getNombre(self):
        return self.__nombre

    def getVacantes(self):
        return self.__vacantes

    def getMonto(self):
        return self.__montoInscripcion

    def getPersonas(self):
        return self.__personas

    def actualizarVacantes(self):
        ban = False
        if self.__vacantes > 0:
            self.__vacantes -= 1
            ban = True

        return ban

    def agregarPersona(self, persona):
        self.__personas.append(persona)

    def consultarInscriptos(self):
        for persona in self.__personas:
            print(persona)