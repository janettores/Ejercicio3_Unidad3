from ClasePersona import Persona


class ManejadorPersonas:
    __personas = []

    def __init__(self):
        self.__personas = []

    def agregarPersona(self, persona):
        self.__personas.append(persona)

    def getPersona(self, dni):
        persona = None
        i = 0
        while persona == None and i < len(self.__personas):
            if dni == self.__personas[i].getDNI():
                persona = self.__personas[i]
            else:
                i += 1

        return persona

    def mostrarPersonas(self):
        for persona in self.__personas:
            print(persona)