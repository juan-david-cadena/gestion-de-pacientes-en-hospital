pacientes = [input("ingrese el nombre de su paciente"),input("ingrese el nombre de su paciente"),input("ingrese el nombre de su paciente"),input("ingrese el nombre de su paciente"),input("ingrese el nombre de su paciente")]
if "Migel" in pacientes :
    pacientes.append("Valentina")
    print(pacientes)
else :
    print(pacientes)

#consultorios (2)

consultorios = [int(input("ingrese el numero de consultorio ocupado ")),int(input("ingrese el numero de consultorio ocupado ")),int(input("ingrese el numero de consultorio ocupado ")),int(input("ingrese el numero de consultorio ocupado ")),int(input("ingrese el numero de consultorio ocupado "))]
if 103 in consultorios :
    consultorios.append(104)
    print(consultorios)
else :
    print(consultorios)

# eliminar Andres (3)

if "Andres" in pacientes :
    pacientes.remove("Andres")
else :
    print(pacientes)

#eliminar consultorios (4)
numero = len(consultorios) 
if numero > 3 :
    nu = consultorios[0]
    consultorios.remove(nu)
    print(consultorios)
else :
    print(consultorios)

#laura (5)
if "Laura" in pacientes :
    pacientes.remove("Laura")
    pacientes.append("Camila")
else :
    print(pacientes)

#turno mañana (6)

turno_mañana = [pacientes[0],pacientes[-1]]

#consultas (7)

consultas_activas = [consultorios[0],consultorios[-1]]

#consulta108 (8)

if 104 in consultas_activas:
    emergencia = ("camila",104)
    print(emergencia)
else :
    print(consultas_activas)

#atencion (9)

if "Camila" in turno_mañana :
    turno_mañana.append("Atancion Prioritaria")
else :
    print(turno_mañana)

#prioritaria (10)

if "Atencion Prioritaria" in turno_mañana:
    registro_pacientes = {
        "nombre" : "camila",
        "consultorio" : 102,
        "estado" : "en observacion"
    }
else :
    print(turno_mañana)

#hora (11)

if "registro_pacientes" in globals() :
    registro_pacientes.append("Hora de ingreso")
    registro_pacientes["Hora de ingreso"] = "10:45 AM"
else :
    print(pacientes)

#105 (12)

esta = 105 in consultorios
if esta in globals() :
    print(consultorios)
else :
    consultorios.append(105)

#andres (13)

if "Andres" in pacientes :
    print(pacientes)
else :
    pacientes.append("Andres")
    print(pacientes)

#mostrar (14)

if "registro_pacientes" in globals() and "emergencia" in globals() and "registro_pacientes" in globals() :
    print(pacientes,consultorios,turno_mañana,consultas_activas,registro_pacientes,emergencia,registro_pacientes)
elif "registro_pacientes" in globals() and "emergencia" in globals() :
    print(pacientes,consultorios,turno_mañana,consultas_activas,registro_pacientes,emergencia)
elif "registro_pacientes" in globals():
    print(pacientes,consultorios,turno_mañana,consultas_activas,registro_pacientes)
else:
    print(pacientes,consultorios,turno_mañana,consultas_activas)