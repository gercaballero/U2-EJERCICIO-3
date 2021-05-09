from claseCosecha import Cosecha
from manejadorCamiones import ManejadorCamiones
from menu import Menu
import os

if __name__=='__main__':
    cose=Cosecha()                  #OBJETO COSECHA CON LISTA
    cose.testLista()                #SE CARGA LA LISTA CON EL ARCHIVO COSECHAS.CSV
    camiones=ManejadorCamiones()    #OBJETO DE MANEJADOR
    camiones.testCamiones()         #SE CARGA LA LISTA CON LOS OBJETOS  DE LA CLASE CAMION
    menu= Menu()                    #OBJETO MENU
    salir= True
    while salir:
                print("\n-------------------Menu-------------------")
                print(' 1- Consultar Kilos descargados')
                print(' 2- Listado descargas por dia')
                print(' 3- Salir')
                op= input('\n INGRESE UNA OPCION: ')
                if op in ('1','2','3'):
                        menu.opcion(int(op),cose,camiones)
                        if op=='3':
                            salir=False
                else:
                    os.system('cls')
                    print ("    ---OPCION NO VALIDA---")