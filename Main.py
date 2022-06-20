import random as rd
import numpy as np
import funciones1 as fc1
import funciones2 as fc2

datos = ''
clientes = {} #diccionario que tendrá todos los datos de los ciudadanos que hayan ingresado al programa
opcion = ""
sub_opcion = ''

while opcion != 4:
    opcion=fc2.menu
        
    # OPCIÓN 1 DEL MENÚ PRINCIPAL
    if opcion == 1: #Si el usuario ingresa la opción 1, se presentará un sub-menú

        while sub_opcion != 'c':
            print()
            sub_opcion = fc2.adminCiudadanos

                # SUBOPCIÓN A del submenú 'Administrar Ciudadanos'
            if sub_opcion == 'a': #Si la subopción es 'a' deberá ejecutarse el ingreso de datos para cada ciudadano
                datos = ''
                fc1.AgregarCliente(clientes)
                print()

                #SUBOPCIÓN B del submenú 'Administrar Ciudadanos'
            elif sub_opcion == "b":            #esta subopción eliminará los datos almacenados
                if len(clientes)>0:
                    print('DATOS ELIMINADOS CON ÉXITO')
                    clientes.clear()
                    print()
                else:
                    print('NO EXISTEN DATOS POR ELIMINAR')

                #SUBOPCIÓN C del submenú 'Administrar Ciudadanos'
            elif sub_opcion =='c': #se volverá al menú principal
                print('Volviendo al Menú principal...')

        #OPCIÓN 2 DEL MENÚ PRINCIPAL
    elif opcion == 2:#si el usuario ingresa la opción 2 del menú principal, se volverá a presentar un sub-menú "Informe"
        fc1.Informes(clientes,opcion)

        #OPCIÓN 3 DEL MENÚ PRINCIPAL
    elif opcion == 3:#En esta opción se debe solicitar un código de acceso
        fc1.Informes(clientes, opcion)

        # OPCIÓN 4 DEL MENÚ PRINCIPAL
    elif opcion == 4:
        print('FIN DEL PROGRAMA'.center(50,'*'))
        opcion=4


#3214567890,ronny garcia,3-7-2001,0912345678,claro,m
#0943823633,natalia romero,3-10-1999,0962871251,movistar,f
