#Trabajo en clase - Condicionales (valentina albizu y sofia blangetti)

fecha=input("ingrese la fecha actual DIA, DD/MM: ")
fecha=fecha.split(",")

dia_semana:str=fecha[0].lower()
aux=fecha[1].strip().split("/")

dia=int(aux[0])
mes=int(aux[1])

if dia > 31 or mes > 12:
    print("Fecha inexistente")
else:
    if dia_semana in ["lunes", "martes", "miercoles"]:
      hubo_examen=input("¿Hubo examen ese dia? (si/no): ").lower()

      if hubo_examen == "si":
         aprobados=int(input("Alumnos aprobados: "))
         desaprobados=int(input("Alumnos desaprobados: "))
         cantidad_de_alumnos= aprobados + desaprobados

         if cantidad_de_alumnos > 0:
             porc_aprobados = (aprobados/ cantidad_de_alumnos ) * 100
             print(f"Procentaje de aprobados en el examan: {porc_aprobados}")
         else:
            print("No se ingresaron alumnos")
      else:
       print("Ese dia no hubo examenes")

    elif dia_semana == "jueves":
      asistieron=int(input("Alumnos que asistieron a clases: "))
      no_asistieron=int(input("Alumnos que no asistieron a clases: "))
      alumnos_en_total = asistieron + no_asistieron
      
      if alumnos_en_total > 0:
         porc_asistencia =(asistieron/ alumnos_en_total ) * 100
        
         if porc_asistencia > 50:
             print("Asistio la mayoria")
         else:
              print("No asistio la mayoria")  
      else:
         print ("No se ingresaron alumnos")
      
    elif dia_semana == "viernes":
      
      if (dia == 1 and (mes == 1 or mes == 7)):
         print("Comienza un nuevo ciclo")
         cant_alumnos=int(input("Cantidad de alumnos: "))
         arancel=float(input("Arancel por alumno en $: "))
         total_ingreso= cant_alumnos* arancel
         print(f"Ingreso total $ {total_ingreso}")
      else:
         print("No hay nuevo ciclo")
