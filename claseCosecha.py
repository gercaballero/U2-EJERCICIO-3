import csv

class Cosecha:
    def __init__(self):
        self.__lista=[]
    
    def testLista(self):
        archivo=open('cosechas.csv')
        reader=csv.reader(archivo,delimiter=',')
        bandera =True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                self.__lista.append(fila)
        archivo.close()

    def mostrar(self):
        for i in range(len(self.__lista)):
            print('{}'.format(self.__lista[i]))
    
    def cantKilos(self, ide, tara, dia):
        return float(self.__lista[ide][dia-1])-tara

    def cantidadTotal(self, ide, tara):
        total=0
        for i in range(len(self.__lista[ide])):
            total=total+(self.cantKilos(ide,tara,i))
        return total
    
    def cosechaDia(self, dia):
        for i in range(len(self.__lista)):
            return float(self.__lista[i][dia-1])