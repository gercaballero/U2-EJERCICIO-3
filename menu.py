import os
import sys
from manejadorCamiones import ManejadorCamiones
from claseCosecha import Cosecha
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.salir
                          }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op, cosecha,camiones):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(cosecha,camiones)

    def salir(self, maneja,indice):
        print('Salida del programa')
        sys.exit(0)

    def opcion1(self, cosecha,camiones):
             identificador=int(input('Ingrese el identificador del camion: '))
             if identificador in range(1,20):
                camiones.kilos(identificador,cosecha)
             else:
                os.system('cls')
                print('~~~~~ERROR: INGRESE UN IDENTIFICADOR ENTRE 1 Y 20~~~~~\n')
    def opcion2(self, cosecha,camiones):
             dia= int(input("INGRESE DIA PARA MOSTRAR LISTADO: "))
             if dia in range(1,45):
                camiones.listaDia(dia,cosecha)
             else:
                os.system('cls')
                print('~~~~~ERROR: INGRESE UN DIA ENTRE 1 Y 45~~~~~\n')
             