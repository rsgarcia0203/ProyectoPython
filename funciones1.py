import random as rd
import numpy as np


# Función que permite agregar clientes a la base de datos
def AgregarCliente (dic):
    datos=""

    # Se solicita los datos de un cliente hasta que el usuario ingrese "salir" 
    while datos != 'SALIR'.lower():
        print()
        datos = input('Ingrese cédula, nombre completo, fecha de nacimiento(dd-mm-YYYY), número de celular, operadora y género.\n'
            'Todos los datos que ingrese debe de estar separados por una coma ",".\n''Para terminar escribir "SALIR": ').lower()
        if datos != 'SALIR'.lower():
            lista_datos = datos.split(",")  # con el método split crearemos una lista con todos los datos que el usuario ingrese
            # al separar por coma (',')cada dato.
            if len(lista_datos) == 6:  # si el usuario ingresa los 6 datos que pide el programa, el programa seguirá corriendo
                cedula = lista_datos[0]
                nombre_completo = lista_datos[1].title()
                fecha_nacimiento = lista_datos[2]
                celular = lista_datos[3]
                operadora = lista_datos[4].title()
                genero = lista_datos[5].title()
                lista_ciudadanos = []  # se crea una lista para que guarde cada información del ciudadano: cédula, nombre, fecha de nacimiento...
                # VALIDACIONES
                # validar cedula
                validar_cedula = False  # Es importante al iniciar una validación que el resultado de la validación sea False
                if len(cedula) == 10 and cedula.isdigit():
                    validar_cedula = True  # Una vez que se hayan cumplido todas las condiciones para que una cedula sea válida cambiamos el estado a True
                else:
                    print('Cédula no válida, ingrese nuevamente')

                # validar nombre
                validar_nombre = False
                validar_nombre1 = nombre_completo.replace(' ','').isalpha()  # condición de que el nombre debe ser ingresado solo con caracteres alfabéticos
                if validar_nombre1 == True:  # True si el nombre que ingrese el usuario solo tiene caracteres alfabéticos y si es TRUE...
                    nombre_completo = nombre_completo.split(' ')
                    if len(nombre_completo) == 2 or len(nombre_completo) == 4:  # el nombre debe tener 2 o 4 palabras
                        validar_nombre = True
                    else:
                        print('Error. Debe ingresar un nombre y un apellido o todo su nombre completo, intente nuevamente')
                else:
                    print('Error. El nombre debe de tener solo caracteres alfabéticos')

                    # validar fecha de nacimiento y edad
                    validar_fecha = False
                    validar_edad = False
                    edad=0
                    validar_fecha1 = fecha_nacimiento.replace('-','').isdigit()  # validar de que la fecha sea ingresada con numeros
                    if validar_fecha1 == True:
                        if '-' in fecha_nacimiento:  # validar de que el usuario haya ingresado en el formato correcto con el guion
                            fecha_nacimiento = fecha_nacimiento.split('-')
                            if len(fecha_nacimiento) == 3:
                                dia = fecha_nacimiento[0]
                                mes = fecha_nacimiento[1]
                                anio = fecha_nacimiento[2]
                                if int(dia) <= 31 and int(mes) <= 12 and len(anio) == 4:
                                    edad = 2019 - int(anio)
                                    if edad >= 18:
                                        validar_fecha = True
                                        validar_edad = True
                                    else:
                                        print('Es menor de edad, intente nuevamente')
                        else:
                            print('No ha ingresado la fecha en el formato pedido, usted debe ingresar la fecha separada por un guión')
                    else:
                        print('Error. La fecha debe ser ingresada sólo con dígitos')

                    # validar celular
                    validar_celular = False
                    if len(celular) == 10 and celular[:2] == '09' and celular.isdigit():
                        validar_celular = True
                    else:
                        print('Número de celular no valido. Aségurese de que tenga 10 digitos y empezar con 09, intente nuevamente')

                    # Validar operadora.La operadora puede ser: claro, movistar o tuenti
                    validar_operadora = False
                    if operadora in ['Claro', 'Movistar', 'Tuenti']:
                        validar_operadora = True
                    else:
                        print('La operadora que ha ingresado no se encuentra en nuestro sistema. Intente de nuevo')

                    # Validar el género. Debe ser Masculino o Femenino(también permitir 'M' o 'F')
                    validar_genero = False
                    if genero in ['Masculino', 'Femenino', 'M', 'F']:
                        validar_genero = True
                        if genero in ['Masculino', 'M']:
                            genero="M"
                        elif genero in ['Femenino', 'F']:
                            genero="F"
                    else:
                        print('Género no válido. Debe ser: Masculino - Femenino o M/F ')

                    # Se debe crear un vector (y almacenar sus datos junto al ciudadano) con 10 numeros telefónicos
                    arr_telefonos=[]
                    l_telefonos = []  # se crea lista para guardar posteriormente cada número telefónico aleatorio
                    for j in range(10):  # utilzamos un for para generar números en la longitud que se requiera, en este caso serán 10 números telefónicos(0-9)
                        aleatorio = rd.randint(900000000,999999999)  # un número teléfonico tendrá 9 dígitos que serán al azar
                        numero_telefonico = '593' + str(aleatorio)  # que cumpla con la condición de que empiece con 593 y los 9 digítos restantes sean los que salgan de la variable anterior 'aleatorio'
                        l_telefonos.append(int(numero_telefonico))  # convertimos el numero_telefonico a entero y lo agregamos a la lista de teléfonos
                        arr_telefonos = np.array(l_telefonos)  # convertimos la lista teléfono en arreglo

                    # Si todas las validaciones se cumplen, entonces se agregan los datos a la lista de ciudadanos
                    if validar_cedula == True and validar_nombre == True and validar_fecha == True and validar_celular == True \
                            and validar_operadora == True and validar_genero == True and validar_edad == True:
                        dic[cedula] = {"Nombre": nombre_completo, "Género": genero, "Celular": celular,
                                       "Operadora": operadora, "Fecha de nacimiento": fecha_nacimiento,
                                       "Edad":edad, "Teléfonos": arr_telefonos}

            else:
                print("Faltan datos, por favor intente de nuevo\n")

    return ""


# Función para mostrar los datos de los ciudadanos ingresados
def Informes(dic,op):
    sub_opcion=""
    if op==2:
        if len(dic) == 0:
            print('No se han ingresado ciudadanos')
            print()
        else:
            print("\n")
            print('Informe'.center(50, '='))
            print("\t a. Mostrar Ciudadanos")
            print("\t b. Volver")
            print()
            while sub_opcion != 'b':
                print()
                sub_opcion = input('Ingrese la subopción que desea realizar: ').lower()
                if sub_opcion == 'a':  # Si el usuario ingresa la sub-opción a se presentará la información de los ciudadanos
                    if len(dic) != 0:  # Si se han ingresado ciudadanos, mostrará la cantidad
                        print()
                        print('En total se ingresaron', len(dic), 'ciudadanos y son los siguientes: ')
                        print()
                        for cedula in dic:
                            print("\tEl numero de cedula del cliente es: ", cedula)
                            print("\tEl nombre del cliente es: ", dic[cedula]["Nombre"])
                            print("\tEl Genero del cliente es: ", dic[cedula]["Género"])
                            print("\tEl número de celular del cliente es: ", dic[cedula]["Celular"])
                            print("\tLa operadora del client es: ", dic[cedula]["Operadora"])
                            print("\tLa fecha de nacimiento del cliente es: ", dic[cedula]["Fecha de nacimiento"],
                                  "Tiene ", dic[cedula]["Edad"], "años")
                            print("\tLos teléfonos del cliente son: ", dic[cedula]["Teléfonos"])
                    print()

                elif sub_opcion == 'b':
                    print('Volviendo al Menú principal...')
                else:
                    print('Opcion no válida.Ingrese nuevamente ')
        print("El numero de clientes que se han ingresado son: ", len(dic))
        print()

    elif op==3:
        print("\n")
        print("Integrantes".center(50, '-'))
        print()
        validar_codigo = False
        # validar que el código de acceso sea el correcto
        while validar_codigo != True:
            codigo = input('Debe ingresar un código de acceso: ')
            # valida que el código de accesso tenga 5 digítos
            validar_digitos = len(codigo) == 5 and codigo.isdigit()
            # validar que se cumpla la validación anterior y que sea par
            if validar_digitos == True and int(codigo) % 2 == 0:
                validar_codigo = True  # una vez que se haya cumplido todas las validaciones, el estado de la variable cambia a True
            else:
                print('El código de acceso no es válido.Intente de nuevo')
        print("Integrantes:\n \t-Ronny Steven Garcìa Zambrano\n \t-Natalia Jamile Romero Medina")
        print("Paralelo: 19")

    else:
        print("Ingrese una opcion valida")

    return ""

