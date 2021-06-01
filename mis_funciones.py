#Funciones del Diagrama1
def agregarEstudiantes():

    CUPO = 3
    estudiantes = []    
    nombre = ""
    email = ""
    x = 0
    y = 0   
    respuesta = ""
    
    for x in range(CUPO):
        nombre = input('Por favor digite su nombre: ')
        correo = input('Por favor digite su correo: ')                
        estudiantes.append([nombre, correo])
        if(x != CUPO-1):         
            respuesta = input("Agregar otro estudiante? (Si/No)")
            if respuesta.lower() == "no":
                break
        else:
            print("El cupo esta lleno")
            break
    return estudiantes


def imprimirListaBid(fListaBid):
    lenLista = len(fListaBid)
    print("-----------------------------------------------------------") 
    print(">< >< >< >< >< >< ><Lista de estudiantes>< >< >< >< >< >< >")
    print("-----------------------------------------------------------")
    if lenLista > 0:    
        for x in range(lenLista):
            print(f"Estudiante #{x+1}\nNombre:{fListaBid[x][0]}\nCorreo: {fListaBid[x][1]}\n")
        
    else:
        print("No hay estudiantes agregados")
    print("-----------------------------------------------------------")    


#Funcion del Diagrama2

def identifBisiesto(n):    
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 == 0:
            return True        
    else:
        return False


def identifInt(var):
    if var[0] == ('-', '+'):
        return var[1:].isdigit()
    else:
        return var.isdigit()

def imprimirBisiesto():
    bandera = 0
    while bandera == 0:
        respuesta = input("Ingresar año: ")
        if identifInt(respuesta) == False:
            print(">< >< >< >< >< Por favor ingresar un número >< >< >< >< ><")                   
        else:
            respuesta = int(respuesta)
            if identifBisiesto(respuesta):
                print("El año es bisiesto")
                break
            else:
                print("El año no es bisiesto")
                break


#Funcion para limpiar consola segun OS
def limpiarConsola():
    import os
    if os.name == "posix" or os.name == "mac":
        os.system("clear")
    elif os.name == "ce" or os.name == "dos" or os.name == "nt":
        os.system("cls")

        
   

    

