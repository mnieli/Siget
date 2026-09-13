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
        opcion = int(input("Desea Cargarlo? Si = 1, No = 2:  "))
        
        if opcion == 1:
            cargar_paciente(Pacientes, CUIT)
    
    return Pacientes


def cargar_paciente(Pacientes, CUIT):

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


def main():

    Pacientes = []
    opcion = 0

    while opcion != -1:

        print()
        print(" MENU PRINCIPAL ")
        print()
        print("Opciones:")
        print(" Opcion 1: Ingresar CUIT paciente.")
        print(" Opcion 2: Mostrar Lista de Pacientes en Orden Alfabetico.")
        print(" Opcion -1: Salir.")

        opcion = int(input("Ingresar opcion: "))

        if opcion == 1:

            buscar_cuit(Pacientes)

        elif opcion == 2:

            mostrar_Pacientes(Pacientes)

        elif opcion == -1:

            print("Fin del programa...")

        else:

            print("Opcion incorrecta")


main()