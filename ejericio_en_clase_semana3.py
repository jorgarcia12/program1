fecha = input("ingrese la fecha en formato dia, DD/MM: ")
dia = fecha[0:fecha.find(",")]
DD = fecha[fecha.find(" ")+1: fecha.find("/")]
MM = fecha[fecha.find("/")+1:]
dia = dia.lower()
#print(fecha,dia,DD,MM)
DD = int(DD)
MM = int(MM)



if (dia != "lunes" and dia != "martes" and dia != "miercoles" and dia != "jueves" and dia != "viernes" or DD < 1 or DD > 31 or MM < 1 or MM > 12):
    print("Datos invalidos, Ingrese nuevamente los datos")

if(dia == "lunes"):
    print("Examen de nivel Inicial")
elif(dia == "martes"):
    print("Examen nivel Intermedio")
elif(dia == "miercoles"):
    print("Examen nivel Avanzado")
elif(dia == "jueves"):
    print("Practica hablada")
else:
    print("Ingles para viajeros")

if(dia == "lunes" or dia == "martes" or dia =="miercoles"):
    examen = input("¿Rindieron examnen? (INGRESE S(si) O N(no)): ")
    if (examen=="s"):
        total=int(input("Cuantos alumnos rindieron? "))
        aprob=int(input("Cuantos aprobaron? "))
        porcentaje_aprobados = (aprob*100)/total
        print("Aprobo el ",porcentaje_aprobados,"%")
    else:
        print("terminando programa")
elif(dia == "jueves"):
    porcentaje_asistencia = int(input("Ingrese el porcentaje de asistencia clase: "))
    if porcentaje_asistencia>50:
        print("Asistio la mayoria")
    else:
        print("No asistio la mayoria")
else:
    if (DD==1 and MM==1) or (DD==1 and MM==7):
        print("Comienzo nuevo Ciclo")
        cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))
        arancel = int(input("Ingrese el arancel por alumno: $"))
        ingreso_total = (cant_alumnos*arancel) * 6
        print("El ingreso esperado para este ciclo sera de: $",ingreso_total)
    else:
        print("Disfrute su clase")






