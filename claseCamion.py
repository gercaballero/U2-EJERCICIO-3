
class Camion:
    __identificador=0
    __conductor=''
    __patente=''
    __marca=''
    __tara=0.0
    
    def __init__(self,identificador,conductor,patente,marca,tara):
        if isinstance(identificador, int) and isinstance(conductor, str) and isinstance(patente, str) and isinstance(marca, str) and isinstance(tara, float):
            self.__identificador=identificador
            self.__conductor=conductor
            self.__patente=patente
            self.__marca=marca
            self.__tara=tara
    
    def __str__(self):
        return ('ID:{}, CONDUCTOR:{}, PATENTE:{}, MARCA:{}, TARA:{}'.format(self.__identificador,self.__conductor,self.__patente,self.__marca,self.__tara))
    
    def tara(self):
        return float(self.__tara)
    
    def getPatente(self):
        return str(self.__patente)
    def getConductor(self):
        return str(self.__conductor)