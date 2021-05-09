from claseCamion import Camion
from claseCosecha import Cosecha
import csv
from os import system

class ManejadorCamiones:
    def __init__(self):
        self.__listaCam=[]

    def testCamiones(self):
        archivo=open('camiones.csv')
        reader=csv.reader(archivo,delimiter=',')
        bandera =True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                camion=Camion(int(fila[0]),str(fila[1]),str(fila[2]),str(fila[3]),float(fila[4]))
                self.__listaCam.append(camion)
        archivo.close()
    
    def mostrar(self):
        for i in range(len(self.__listaCam)):
            print(self.__listaCam[i])
    
    def kilos(self, identi, cosecha):
        ki=cosecha.cantidadTotal(identi-1,self.__listaCam[identi-1].tara())
        system("cls")
        print('LA CANTIDAD DE KILOS DESCARGADOS POR EL CAMION CON IDENTIFICADOR {} ES DE {} KILOS EN 45 DIAS'.format(identi,ki))
    
    def listaDia(self, dia,cosecha):
        system("cls")
        print('     ---------- LISTADO DIA {} -----------\n'.format(dia))
        print('PATENTE\t          CONDUCTOR\t     CANTIDAD DE KILOS')
        for i in range(len(self.__listaCam)):
            print('{:>6}{:>25}{:>15}'.format(self.__listaCam[i].getPatente(),self.__listaCam[i].getConductor(), cosecha.cantKilos(i,self.__listaCam[i].tara(),dia)))
        