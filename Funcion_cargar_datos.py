import re
import datetime
import archivoPacientes


def buscar_cuit(pacientes):
    """
Objetivo:
Parametros:
Retorno:"""


    cuit = input("Ingresar CUIT del paciente: ")

    resultado = re.findall(r"^[0-9]{2}-[0-9]{8}-[0-9]{1}$", cuit)

    if resultado:

        for paciente in pacientes:

            if cuit == paciente["CUIT"]:
                print("Paciente existente:")
                print(paciente)

                return pacientes


        cargar_paciente(pacientes, cuit)

    else:
        print("Formato de CUIT incorrecto.")

    return pacientes


def cargar_paciente(pacientes, cuit):
        """
Objetivo:
Parametros:
Retorno:"""

    paciente = {}

    paciente["CUIT"] = cuit

    paciente["Apellido"] = input("Ingresar apellido: ").capitalize()

    paciente["Nombre"] = input("Ingresar nombre del paciente: ").capitalize()

    paciente["Edad"] = int(input("Ingresar edad: "))

    edad_menor = lambda x: x < 16

    if edad_menor(paciente["Edad"]):

        print("Paciente menor de edad. Se debe atender en una institución pediátrica")

    pacientes.append(paciente)

    return pacientes


def cargar_medico(medicos):
        """
Objetivo:
Parametros:
Retorno:"""

    nombre = input("Ingresar nombre del medico: ").capitalize()
    apellido = input("Ingresar apellido del medico: ").capitalize()
    especialidad = input("Ingresar especialidad del medico: ").capitalize()
    cuit = input("Ingresar CUIT del medico: ")

    medico = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Especialidad": especialidad,
        "CUIT": cuit,
    }

    medicos.append(medico)

    return medicos


def mostrar_pacientes(pacientes):
        """
Objetivo:
Parametros:
Retorno:"""


    pacientes.sort(key=lambda paciente: paciente["Apellido"])

    for paciente in pacientes:
        print(paciente)


def main():
        """
Objetivo:
Parametros:
Retorno:"""


    pacientes = []

    medicos = []

    opcion = None

    patron_cuit = r"^[0-9]{2}-[0-9]{8}-[0-9]{1}$"

    while opcion != -1:

        print()
        print(" MENU PRINCIPAL ")
        print()
        print("Opciones:")
        print(" Opcion 1 : cargar paciente. ")
        print(" Opcion 2 : Ingresar CUIT paciente. ")
        print(" Opcion 3 : Mostrar Pacientes. ")
        print(" Opcion 4 : cargar medico. ")
        print(" Opcion -1 : salir. ")

        opcion_str = input("Ingresar opcion: ")

        if not opcion_str.lstrip("-").isdigit():
            print("Opción inválida, ingresar un número.")
            continue

        opcion = int(opcion_str)

        if opcion == 1:
  
            cuit = input("Ingresar CUIT del paciente: ")

            if re.findall(patron_cuit, cuit):
                cargar_paciente(pacientes, cuit)
            else:
                print("Formato de CUIT incorrecto.")

        elif opcion == 2:
            buscar_cuit(pacientes)

        elif opcion == 3:
            mostrar_pacientes(pacientes)

        elif opcion == 4:
            cargar_medico(medicos)

        elif opcion == -1:
            print("Fin del programa...")

        else:
            print("Opción no válida.")


main()
