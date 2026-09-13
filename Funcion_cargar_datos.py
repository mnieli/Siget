import re
import archivoPacientes
import datetime


def buscar_cuit(Pacientes):
        """
Objetivo: Buscar un paciente por su CUIT
Parametros: Pacientes (lista de diccionarios)
Retorno: Lista de pacientes encontrados
"""

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
        """
Objetivo: Cargar un nuevo paciente
Parametros: Pacientes (lista de diccionarios)
Retorno: Lista de pacientes actualizada
"""
    
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
        """
Objetivo: Cargar un nuevo paciente en la lista
Parametros: Pacientes (lista de diccionarios), CUIT (str)
Retorno: Lista de pacientes actualizada
"""

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
        """
Objetivo: Cargar un nuevo médico
Parametros: Medicos (lista de diccionarios)
Retorno: Lista de médicos actualizada
"""

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
        """
Objetivo: Mostrar la lista de pacientes en orden alfabético
Parametros: Pacientes (lista de diccionarios)
Retorno: None
"""

    Pacientes.sort(
        key=lambda paciente: paciente["Apellido"]
    )

    for paciente in Pacientes:
        print(paciente)

def actualizar_paciente(Pacientes):
        """
Objetivo: Actualizar los datos de un paciente existente
Parametros: Pacientes (lista de diccionarios)
Retorno: Lista de pacientes actualizada
"""
    CUIT = input("Ingresar CUIT del paciente a actualizar: ")
    
    for paciente in Pacientes:
        if CUIT == paciente["CUIT"]:
            print("Paciente encontrado.")
            paciente["Apellido"] = input("Ingresar nuevo apellido: ").capitalize()
            paciente["Nombre"] = input("Ingresar nuevo nombre: ").capitalize()
            paciente["Edad"] = int(input("Ingresar nueva edad: "))
            print("Paciente actualizado exitosamente.")
            return Pacientes
    
    print("Paciente no encontrado.")
    return Pacientes

def eliminar_paciente(Pacientes):
        """
Objetivo: Eliminar un paciente de la lista
Parametros: Pacientes (lista de diccionarios)
Retorno: Lista de pacientes actualizada
"""
    CUIT = input("Ingresar CUIT del paciente a eliminar: ")

    for i, paciente in enumerate(Pacientes):
        if CUIT == paciente["CUIT"]:
            print("Paciente encontrado.")
            del Pacientes[i]
            print("Paciente eliminado exitosamente.")
            return Pacientes

    print("Paciente no encontrado.")
    return Pacientes


def main():
        """
Objetivo: Mostrar el menú principal y permitir la interacción con el usuario
Parametros: No recibe parámetros.
Retorno: No retorna ningún valor"""

    Pacientes = []
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

            print(" Opcion 1: Buscar Pacientes por CUIT.")
            print(" Opcion 2: Cargar Paciente.")
            print(" Opcion 3: Dar Turno Paciente.")
            print(" Opcion 4: Mostrar Lista de Pacientes en Orden Alfabetico.")
            print(" Opcion 5: Actualizar Paciente.")
            print(" Opcion 6: Eliminar Paciente.")
            print()

            opcion_paciente = int(input("Ingresar opcion de PACIENTES: "))

            if opcion_paciente == 1:
                buscar_cuit(Pacientes)

            elif opcion_paciente == 2:
                cargar_paciente(Pacientes)

            elif opcion_paciente == 4:
                mostrar_Pacientes(Pacientes)

            elif opcion_paciente == 5:
                actualizar_paciente(Pacientes)

            elif opcion_paciente == 6:
                eliminar_paciente(Pacientes)

        elif opcion == -1:

            print("Fin del programa...")

        else:

            print("Opcion incorrecta")


main()