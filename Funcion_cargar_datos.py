import re
import archivoPacientes
import datetime


def buscar_cuit(Pacientes):
    
    CUIT = input("Ingresar CUIT del paciente: ")
    
    encontrado = False
    
    for paciente in Pacientes:
        
        if CUIT == paciente["CUIT"]:
            encontrado = True
    
    if encontrado == True:
        print("Paciente encontrado.")
    else:
        print("Paciente Inexistente.")

    return Pacientes


def cargar_paciente(Pacientes):
    
    CUIT = input("Ingresar CUIT del paciente: ")
    
    encontrado = False
    
    for paciente in Pacientes:
        
        if CUIT == paciente["CUIT"]:
            encontrado = True
    
    if encontrado == True:
        print("Paciente encontrado.")
    else:
        print("Paciente Inexistente.")
        opcion = int(input("Desea Cargarlo? Si = 1, No = 2:  "))
        
        if opcion == 1:
            cargar_diccionario_paciente(Pacientes, CUIT)
    
    return Pacientes

def cargar_diccionario_paciente(Pacientes, CUIT):

    paciente = {}

    paciente["CUIT"] = CUIT

    paciente["Apellido"] = input(
        "Ingresar apellido: "
    ).capitalize()

    paciente["Nombre"] = input(
        "Ingresar nombre del paciente: "
    ).capitalize()

    paciente["Edad"] = int(
        input("Ingresar edad: ")
    )

    edad_menor = lambda x: x < 16

    if edad_menor(paciente["Edad"]):
        print(
            "Paciente menor de edad. "
            "Se debe atender en una institución pediátrica"
        )
    print()
    print("PACIENTE CARGADO EXITOSAMENTE")
    print()
    Pacientes.append(paciente)

    return Pacientes


def cargar_medico(Medicos):

    nombre = input(
        "Ingresar nombre del medico: "
    ).capitalize()

    apellido = input(
        "Ingresar apellido del medico: "
    ).capitalize()

    especialidad = input(
        "Ingresar especialidad del medico: "
    ).capitalize()

    cuit = input(
        "Ingresar CUIT del medico: "
    )

    medico = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Especialidad": especialidad,
        "CUIT": cuit
    }

    Medicos.append(medico)

    return Medicos


def mostrar_Pacientes(Pacientes):

    Pacientes.sort(
        key=lambda paciente: paciente["Apellido"]
    )

    for paciente in Pacientes:
        print(paciente)


def cargar_turno(Lista_turnos, Medicos, Pacientes):

    print()
    print("CARGAR TURNO")
    print()

    medico = input("Ingresar CUIT del medico: ")
    paciente = input("Ingresar CUIT del paciente: ")

    fecha = input("Ingresar fecha DD/MM/AAAA: ")
    hora = input("Ingresar hora HH:MM: ")

    fecha_hora = datetime.datetime.strptime(
        fecha + " " + hora,
        "%d/%m/%Y %H:%M"
    )

    disponible = verificar_disponibilidad(
        Lista_turnos,
        medico,
        fecha_hora
    )

    if disponible == True:

        turno = {
            "CUIT_medico": medico,
            "CUIT_paciente": paciente,
            "Fecha_hora": fecha_hora
        }

        Lista_turnos.append(turno)

        print()
        print("TURNO CARGADO EXITOSAMENTE")
        print()

    else:

        print()
        print("EL MEDICO NO ESTA DISPONIBLE EN ESE HORARIO")
        print()

    return Lista_turnos





def main():

    Pacientes = []
    Medicos = []
    Lista_turnos = []
    opcion = 0

    while opcion != -1:

        print()
        print(" MENU PRINCIPAL ")
        print()
        print("Opciones:")
        print("Opcion 1: PACIENTES ")
        print("Opcion 2: MEDICOS ")
        print("Opcion 3: TURNOS ")
        print("Opcion -1: Salir.")
        print()

        opcion = int(input("Ingresar opcion: "))

        if opcion == 1:

            print(" Opcion 1: Buscar Paciente por CUIT.")
            print(" Opcion 2: Cargar Paciente.")
            print(" Opcion 3: Mostrar Lista de Pacientes en Orden Alfabetico.")
            print(" Opcion 4: Actualizar Paciente.")
            print(" Opcion 5: Eliminar Paciente.")
            print()

            opcion_paciente = int(input("Ingresar opcion de PACIENTES: "))

            if opcion_paciente == 1:
                buscar_cuit(Pacientes)

            elif opcion_paciente == 2:
                cargar_paciente(Pacientes)

            elif opcion_paciente == 3:
                mostrar_Pacientes(Pacientes)

            elif opcion_paciente == 4:
                pass

            elif opcion_paciente == 5:
                pass

        elif opcion == 2:

            print(" Opcion 1: Buscar Médico por CUIT.")
            print(" Opcion 2: Cargar Médico.")
            print(" Opcion 3: Mostrar Lista de Médicos en Orden Alfabetico.")
            print(" Opcion 4: Actualizar Médico.")
            print(" Opcion 5: Eliminar Médico.")
            print()

            opcion_medico = int(input("Ingresar opcion de MEDICO: "))

            if opcion_medico == 1:
                buscar_cuit(Medicos)

            elif opcion_medico == 2:
                cargar_medico(Medicos)

            elif opcion_medico == 3:
                mostrar_medico(Medicos)

            elif opcion_medico == 4:
                pass

            elif opcion_medico == 5:
                pass

        elif opcion == 3:

            print(" Opcion 1: Buscar Turnos de Paciente por CUIT.")
            print(" Opcion 2: Buscar Turnos de Médico por CUIT.")
            print(" Opcion 3: Cargar Turno.")
            print(" Opcion 4: Actualizar Turno.")
            print(" Opcion 5: Eliminar Turno.")
            print()

            opcion_turno = int(input("Ingresar opcion de TURNO: "))

            if opcion_turno == 1:
                pass

            elif opcion_turno == 2:
                pass

            elif opcion_turno == 3:
                cargar_turno(Lista_turnos, Medicos, Pacientes)

            elif opcion_turno == 4:
                pass

            elif opcion_turno == 5:
                pass

        elif opcion == -1:

            print("Fin del programa...")

        else:

            print("Opcion incorrecta")


main()