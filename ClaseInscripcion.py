class Inscripcion:
    __fechaInscripcion = ""
    __pago = False

    __persona: object
    __taller: object

    def __init__(self, persona, taller, fechaInscripcion, pago=False):
        self.__persona = persona
        self.__taller = taller
        self.__fechaInscripcion = fechaInscripcion
        self.__pago = pago

    def __str__(self):
        return f"Fecha de inscripcion: {self.__fechaInscripcion}"

    def getFecha(self):
        return self.__fechaInscripcion

    def getPago(self):
        return self.__pago

    def getPersona(self):
        return self.__persona

    def getTaller(self):
        return self.__taller

    def actualizarPago(self):
        self.__pago = True