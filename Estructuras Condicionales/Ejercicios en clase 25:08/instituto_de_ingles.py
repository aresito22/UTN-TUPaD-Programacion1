print("Ingrese la fecha con formato [Día, DD/MM]")
fecha = str(input())

dia_semana, resto = fecha.split(", ")

dd, mm = resto.split("/")
dia_semana = dia_semana.lower()
dias_permitidos = ["lunes", "martes", "miercoles", "miércoles", "jueves", "viernes"]

mm_permitidos = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
mm_30 = ["04", "06", "09", "11"]
mm_31 = ["01", "03", "05", "07", "08", "10", "12"]
dd = int(dd)

dias_de_cursado = ["lunes", "martes", "miercoles", "miércoles"]

if dia_semana not in dias_permitidos:
    print("Día de la semana inválido")
elif mm not in mm_permitidos:
    print("Mes inválido")
elif mm in mm_30 and (dd < 1 or dd > 30):
    print("Día inválido")
elif mm in mm_31 and (dd < 1 or dd > 31):
    print("Día inválido")
elif mm == "02" and (dd < 1 or dd > 28):
    print("Día inválido")
else:
    # Main logic for valid date
    if dia_semana in dias_de_cursado:
        print("Hoy fue día de éxamen? S/N")
        examen = str(input()).lower()
        if examen == "s":
            aprobados = float(input("Cuántos alumnos aprobaron? "))
            desaprobados = float(input("Cuántos desaprobaron? "))
            total = aprobados + desaprobados
            porcentaje = (aprobados / total) * 100
            print(f"El porcentaje de alumnos aprobados es {porcentaje}")
        elif examen == "n":
            print("No es día de exámen; terminando programa.")
    elif dia_semana == "jueves":
        porcentaje_asistencia = float(input("Qué porcentaje de alumnos asistió? "))
        if porcentaje_asistencia >= 50:
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")
    elif dia_semana == "viernes":
        if (dd == 1 and mm == "01") or (dd == 1 and mm == "07"):
            print("Comienzo de nuevo ciclo.")
            alumnos = int(input("Ingrese la cantidad de alumnos: "))
            arancel = int(input("Ingrese el precio del arancel por alumno: "))
            print(f"Ingreso total: {alumnos * arancel}.")
        else:
            print("Día de inglés para viajeros")
    else:
        print("Día de la semana inválido")