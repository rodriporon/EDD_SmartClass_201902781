class NodoPunteroB:
    def __init__(self, puntero):
        self.puntero = puntero
        self.siguienteP = None
        self.anteriorP = None
    
    def getPuntero(self):
        return self.puntero

    def setPuntero(self, puntero):
        self.puntero = puntero

    def getSiguienteP(self):
        return self.siguienteP

    def setSiguienteP(self, s):
        self.siguienteP = s

    def getAnteriorP(self):
        return self.anteriorP

    def setAnteriorP(self, a):
        self.anteriorP = a