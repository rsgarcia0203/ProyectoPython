# Función MENU PRINCIPAL
def menu():
    print('ARCOTEL'.center(100))
    print('PROYECTO DE PYTHON'.center(100))
    print()
    print('MENÚ PRINCIPAL'.center(50, '='))
    print("\t1.- Administrar Ciudadanos")
    print("\t2.- Informe")
    print("\t3.- Integrantes")
    print("\t4.- Salir")
    print()
    opciones=[1,2,3,4]
    op= input("Ingrese una opcion: ")
    while op not in opciones:
        if op.isdigit() == True:#validar que el usuario ingrese un número de opción
            op= int(op)
        else:
            op=input("Opcion incorrecta, ingrese nuevamente: ") #caso contario, que el usuario ingrese una letra en el menú principal. El programa le mostrará que la opción no es válida
    return op


# Función para administrar los ciudadnos ingresados
def adminCiudadanos():
    print("\n")
    print('Administrar Ciudadanos'.center(50, '-'))
    print("\t a. Ingresar Ciudadanos")
    print("\t b. Borrar todo")
    print("\t c. Volver")
    print()
    subopciones=["a","b,""c"]
    sub_opcion = input('Ingrese la subopción que desea realizar: ').lower()
    while sub_opcion not in subopciones:
        if not sub_opcion.isalpha() == True:#validar que el usuario ingrese un número de opción
            sub_opcion=input("Opcion incorrecta, ingrese nuevamente: ")

    return sub_opcion


# Función para buscar un ciudadano
def buscarCliente(dic):
    print("======BUSCAR CLIENTES======\n")
    print("1.- Buscar por numero de cedula")
    print("2.- Buscar por nombres\t\n")

    opcion=input("Ingrese la opcion que desea: ")
    if opcion.isdigit()== True and int(opcion)==1:
        cedula=input("\nIngrese el numero de cedula del cliente que busca: ")
        if cedula.isdigit()==True and len(cedula) == 10:
            verificar_cedula = ""
            for codigo in dic:
                if codigo==int(cedula):
                    print("Los datos del cliente con numero de cedula {} son: ".format(codigo))
                    print()
                    print("\tNombre: ", dic[codigo]["Nombre"])
                    print("\tGenero: ", dic[codigo]["Género"])
                    print("\tNúmero de celular: ", dic[codigo]["Celular"])
                    print("\tOperadora : ", dic[codigo]["Operadora"])
                    print("\tFecha de nacimiento: ", dic[codigo]["Fecha de nacimiento"])
                    print("\tTeléfonos: ", dic[codigo]["Teléfonos"])
                    verificar_cedula =True
                else:
                    verificar_cedula=False

            if verificar_cedula == False:
                print("El numero de cedula no consta en la base de datos. Intentelo de nuevo")

        else:
            print("Numero de cedula incorrecta, intnetelo de nuevo")
    elif opcion.isdigit()== True and int(opcion)==2:
        nombre=input("\nIngrese el nombre del cliente que busca: ")
        if nombre.isalpha()==True:
            for ced in dic:
                if dic[ced]["Nombre"]== nombre:
                    print("Los datos del cliente son: ")
                    print()
                    print("\tCedula: ", dic[ced])
                    print("\tNombre Completo: ", dic[ced]["Nombre"])
                    print("\tGenero: ", dic[ced]["Género"])
                    print("\tNúmero de celular: ", dic[ced]["Celular"])
                    print("\tOperadora : ", dic[ced]["Operadora"])
                    print("\tFecha de nacimiento: ", dic[ced]["Fecha de nacimiento"])
                    print("\tTeléfonos: ", dic[ced]["Teléfonos"])

    else:
        print("Opcion incorrecta, intentelo de nuevo")