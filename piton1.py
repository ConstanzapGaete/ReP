import os
cine=[
    ['A1' , 'A2' , 'A3'],
    ['B1' , 'B2' , 'B3'],
    ['C1' , 'C2' , 'C3']
]

asiento_comprados=[]
persona_registrada=[]
asientos_disponibles=[]


def menu_principal():
    print("**********CINEPOLIS**********")
    print("1- Ver Asientos disponibles ")
    print("2- Comprar asiento")
    print("3- Ver todas las reservas")
    print("4- Ver informacion de una reserva")
    print("5- salir del sistema ")
    opcion=int(input("Ingresa una opcion >  "))
    try:
        if opcion>0 and opcion<6:
            return opcion
        else:
            input("Opcion no disponible , vuelve a intentarlo >  ")
    except:
        input("Error , presiona enter para continuar")


def mostrar_cine():
    os.system("cls")
    dibujo="-----------PANTALLA-----------\n"
    for fila in cine:
        for asiento in fila:
            asientos_disponibles.append(asiento)

            if asiento in asiento_comprados:
                dibujo +=f"[ X ]"
            else:
                dibujo +=f"[ {asiento} ]"
        dibujo+="\n"
    dibujo+="--------------------------------\n"
    print(dibujo)


def compra():
    asiento=input("Ingresa el asiento que quieres reservar > ")
    if asiento in asientos_disponibles:
        if not asiento in asiento_comprados:
            asiento_comprados.append(asiento)
            print("Indica tus datos para la reserva > ")
            nombre=validar_nombre()
            rut=validar_rut()
            num=validar_num()
            persona_registrada.append([asiento,nombre,rut,num])
            os.system("cls")
            input(f"Reserva de asiento {asiento} registrada ")
        else:
            input("El asiento ingresado ya esta reservado > ")
    else:
        input("El asiento no existe presiona enter para continuar > ")

def validar_nombre():
    validar=True
    while validar:
        try:

            nombre=input("Nombre > ")
            if len(nombre) >0 and len(nombre)<30:
                validar=False
            else:
                input("Nombre no valido,presiona cualquier tecla para continuar > ")
        except:
            input("No valido")
    return nombre

def validar_rut():
    validar=True
    while validar:
        try:
            rut=input("Rut > ")
            if len(rut) >0 and len(rut)<13:
                validar=False
            else:
                input("Rut no valido, vuelve a ingresar")
        except:
            input("no valido")
    return rut

def validar_num():
    validar=True
    while validar:
        try:
            num=input("Numero de telefono > ")
            if len(num) >0 and len(num)<10:
                validar=False
            else:
                input("Cantidad de numeros no valida , intenalo denuevo")
        except:
            input("no valido")
    return num

def ver_todo():
    os.system("cls")
    for asiento in persona_registrada:
        print("------------------------")
        print(f"Nombre : {asiento[1]}")
        print(f"Rut    : {asiento[2]}")
        print(f"Telefono : {asiento[3]}")
    input("----------------------------")

def mostrar_un():
    asiento=input("Ingresa el asiento que quieres revisar")
    if asiento in asientos_disponibles:
        if asiento in asiento_comprados:
            for reserva in persona_registrada:
                if reserva[0]==asiento:
                    print("------------------------")
                    print(f"Asiento :  {reserva[0]}")
                    print(f"Nombre  :  {reserva[1]}")
                    print(f"rut     :  {reserva[2]}")
                    print("------------------------")
        else:
            input("Asiento no disponible")
    else:
        input("Asiento disponible")

def salir():
    os.system("cls")
    print("*********Vuelva pronto*********")


menu_g=True
while menu_g:
    opcion=menu_principal()
    if opcion==1:
       mostrar_cine() 
    if opcion==2:
        mostrar_cine()
        compra()
    if opcion==3:
        ver_todo()
    if opcion==4:
        mostrar_cine()
        mostrar_un()
    if opcion==5:
        salir()
        menu_g=False