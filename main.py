from mis_funciones import *
#agregarEstudiantes()
#iimprimirListaBid(fListaBid)
#imprimirBisiesto()
#limpiarConsola()

print("Aqui estuvo Juan")
bandera = 0
respuesta = 0
estudiantes = []

limpiarConsola()
while bandera == 0:    
    print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
    print(f"Menú de opciones:")
    print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
    print(f"1. Agregar estudiantes al grupo\n2. Ver estudiantes del grupo\n3. Encontrar si un año es bisiesto\n4. Salir")    
    respuesta = input(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><\nDigite su opción: ")
    if respuesta == "1":  
        limpiarConsola()
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"1. Agregar estudiantes al grupo")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        estudiantes = agregarEstudiantes()  
    elif respuesta == "2":
        limpiarConsola()
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"2. Ver estudiantes del grupo")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        imprimirListaBid(estudiantes)
    elif respuesta == "3":
        limpiarConsola()
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"3. Encontrar si un año es bisiesto")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        imprimirBisiesto()
    else:
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"GitHub: kamurillUC")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        break
