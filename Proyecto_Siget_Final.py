"""
Módulo de turnos, agenda médica y persistencia.
Encargado: [nombre del integrante]

Entrega 40%: solo estructura (queda todo con pass).
Entrega 100%: ABM de turnos, agenda del médico y guardado en JSON.
"""

import re
import archivoPacientes
import datetime


def buscar_cuit_paciente(Pacientes):
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

def buscar_medico_cuit(Medicos):
    """
    Objetivo: Buscar un medico por su CUIT
    Parametros: Medicos (lista de diccionarios)
    Retorno: Lista de medicos encontrados
    """
    CUIT = input("Ingresar CUIT del Medico: ")

    encontrado = False

    for medico in Medicos:

        if CUIT == medico["CUIT"]:
            encontrado = True

    if encontrado == True:
        print("Medico encontrado.")
    else:
        print("Medico Inexistente.")

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

def cargar_medico(Medicos):
    """
    Objetivo: Cargar un nuevo medico
    Parametros: Medicos (lista de diccionarios)
    Retorno: Lista de medicos actualizada
    """

    CUIT = input("Ingresar CUIT del medico: ")

    encontrado = False

    for medico in Medicos:

        if CUIT == medico["CUIT"]:
            encontrado = True

    if encontrado == True:
        print("Medico encontrado.")
    else:
        print("Medico Inexistente.")
        opcion = int(input("Desea Cargarlo? Si = 1, No = 2:  "))

        if opcion == 1:
            cargar_diccionario_medico(Medicos, CUIT)

    return Medicos

def cargar_diccionario_medico(Medicos, CUIT):
    """
    Objetivo: Cargar un nuevo médico
    Parametros: Medicos (lista de diccionarios)
    Retorno: Lista de médicos actualizada
    """
    medico = {}
    medico["CUIT"] = CUIT

    medico["Apellido"] = input(
        "Ingresar apellido del medico: "
    ).capitalize()

    medico["Nombre"] = input(
        "Ingresar nombre del medico: "
    ).capitalize()
    medico["especialidad"] = input(
        "Ingresar especialidad del medico: "
    ).capitalize()

    print()
    print("MEDICO CARGADO EXITOSAMENTE")
    print()

    Medicos.append(medico)

    return Medicos

def eliminar_medico(Medicos):
    """
    Objetivo: Eliminar un medico de la lista
    Parametros: Medicos (lista de diccionarios)
    Retorno: Lista de medicos actualizada
    """
    CUIT = input("Ingresar CUIT del medico a eliminar: ")

    for i, medico in enumerate(Medicos):
        if CUIT == medico["CUIT"]:
            print("Medico encontrado.")
            del Medicos[i]
            print("Medico eliminado exitosamente.")
            return Medicos

    print("Medico no encontrado.")
    return Medicos

def actualizar_medico(Medicos):
    """
    Objetivo: Actualizar los datos de un medico existente
    Parametros: Medicos (lista de diccionarios)
    Retorno: Lista de medicos actualizada
    """
    CUIT = input("Ingresar CUIT del medico a actualizar: ")

    for medico in Medicos:
        if CUIT == medico["CUIT"]:
            print("Medico encontrado.")
            medico["Apellido"] = input("Ingresar nuevo apellido: ").capitalize()
            medico["Nombre"] = input("Ingresar nuevo nombre: ").capitalize()
            medico["especialidad"] = input("Ingresar nueva especialidad: ").capitalize()
            print("Medico actualizado exitosamente.")
            return Medicos

    print("Medico no encontrado.")
    return Medicos

def mostrar_medico(Medicos):
    """
    Objetivo: Mostrar la lista de medicos en orden alfabético
    Parametros: Medicos (lista de diccionarios)
    Retorno: None
    """
    Medicos.sort(
        key=lambda medico: medico["Apellido"]
    )

    for medico in Medicos:
        print(medico)

    return Medicos

def cargar_turno(Lista_turnos, Medicos, Pacientes):
    """
    Objetivo: Cargar un nuevo turno
    Parametros: Lista_turnos (lista de diccionarios), Medicos (lista de diccionarios), Pacientes (lista de diccionarios)
    Retorno: Lista de turnos actualizada
    """
    print()
    print("CARGAR TURNO")
    print()


    paciente = input("Ingresar CUIT del paciente: ")
    medico = input("Ingresar CUIT del medico: ")

    fecha = input("Ingresar fecha DD/MM/AAAA  ")
    hora = input("Ingresar hora HH:MM   ")

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


def verificar_disponibilidad(Lista_turnos, medico, fecha_hora):
    """
    Objetivo: Verificar si un médico está disponible
    en una determinada fecha y hora.
    Parametros: Lista_turnos, medico, fecha_hora
    Retorno: True si está disponible, False si no.
    """

    disponible = True

    for turno in Lista_turnos:

        if turno["CUIT_medico"] == medico and turno["Fecha_hora"] == fecha_hora:
            disponible = False

    return disponible


def modificar_turno(lista_turnos):
    """
    Objetivo: Modificar la fecha y hora de un turno existente
    Parametros: lista_turnos (lista de diccionarios)
    Retorno: Lista de turnos actualizada
    """
    print()
    print("MODIFICAR TURNO")
    print()

    medico = input("Ingresar CUIT del medico del turno: ")
    paciente = input("Ingresar CUIT del paciente del turno: ")
    fecha = input("Ingresar fecha actual del turno DD/MM/AAAA  ")
    hora = input("Ingresar hora actual del turno HH:MM   ")

    fecha_hora = datetime.datetime.strptime(
        fecha + " " + hora,
        "%d/%m/%Y %H:%M"
    )

    turno_encontrado = None

    for turno in lista_turnos:
        if (turno["CUIT_medico"] == medico
                and turno["CUIT_paciente"] == paciente
                and turno["Fecha_hora"] == fecha_hora):
            turno_encontrado = turno

    if turno_encontrado is None:
        print()
        print("TURNO NO ENCONTRADO")
        print()
        return lista_turnos

    nueva_fecha = input("Ingresar nueva fecha DD/MM/AAAA  ")
    nueva_hora = input("Ingresar nueva hora HH:MM   ")

    nueva_fecha_hora = datetime.datetime.strptime(
        nueva_fecha + " " + nueva_hora,
        "%d/%m/%Y %H:%M"
    )

    disponible = verificar_disponibilidad(lista_turnos, medico, nueva_fecha_hora)

    if disponible == True or nueva_fecha_hora == fecha_hora:
        turno_encontrado["Fecha_hora"] = nueva_fecha_hora
        print()
        print("TURNO MODIFICADO EXITOSAMENTE")
        print()
    else:
        print()
        print("EL MEDICO NO ESTA DISPONIBLE EN ESE HORARIO")
        print()

    return lista_turnos


def eliminar_turno(lista_turnos):
    """
    Objetivo: Eliminar un turno existente
    Parametros: lista_turnos (lista de diccionarios)
    Retorno: Lista de turnos actualizada
    """
    print()
    print("ELIMINAR TURNO")
    print()

    medico = input("Ingresar CUIT del medico del turno: ")
    paciente = input("Ingresar CUIT del paciente del turno: ")
    fecha = input("Ingresar fecha del turno DD/MM/AAAA  ")
    hora = input("Ingresar hora del turno HH:MM   ")

    fecha_hora = datetime.datetime.strptime(
        fecha + " " + hora,
        "%d/%m/%Y %H:%M"
    )

    for i, turno in enumerate(lista_turnos):
        if (turno["CUIT_medico"] == medico
                and turno["CUIT_paciente"] == paciente
                and turno["Fecha_hora"] == fecha_hora):
            del lista_turnos[i]
            print()
            print("TURNO ELIMINADO EXITOSAMENTE")
            print()
            return lista_turnos

    print()
    print("TURNO NO ENCONTRADO")
    print()
    return lista_turnos


def listar_turnos(lista_turnos):
    """
    Objetivo: Mostrar todos los turnos cargados, ordenados por fecha y hora
    Parametros: lista_turnos (lista de diccionarios)
    Retorno: lista_turnos
    """
    if not lista_turnos:
        print()
        print("NO HAY TURNOS CARGADOS")
        print()
        return lista_turnos

    turnos_ordenados = sorted(
        lista_turnos,
        key=lambda turno: turno["Fecha_hora"]
    )

    for turno in turnos_ordenados:
        print(turno)

    return lista_turnos


def consultar_agenda_medico(id_medico, lista_turnos):
    """
    Objetivo: Devolver y mostrar solo los turnos de un médico puntual
    Parametros: id_medico (CUIT del medico), lista_turnos (lista de diccionarios)
    Retorno: Lista de turnos del medico, ordenada por fecha y hora
    """
    turnos_medico = []

    for turno in lista_turnos:
        if turno["CUIT_medico"] == id_medico:
            turnos_medico.append(turno)

    turnos_medico.sort(key=lambda turno: turno["Fecha_hora"])

    if not turnos_medico:
        print()
        print("EL MEDICO NO TIENE TURNOS CARGADOS")
        print()
    else:
        for turno in turnos_medico:
            print(turno)

    return turnos_medico


def buscar_turnos_paciente(lista_turnos):
    """
    Objetivo: Buscar y mostrar los turnos de un paciente por su CUIT
    Parametros: lista_turnos (lista de diccionarios)
    Retorno: Lista de turnos del paciente, ordenada por fecha y hora
    """
    CUIT = input("Ingresar CUIT del paciente: ")

    turnos_paciente = []

    for turno in lista_turnos:
        if turno["CUIT_paciente"] == CUIT:
            turnos_paciente.append(turno)

    turnos_paciente.sort(key=lambda turno: turno["Fecha_hora"])

    if not turnos_paciente:
        print()
        print("EL PACIENTE NO TIENE TURNOS CARGADOS")
        print()
    else:
        for turno in turnos_paciente:
            print(turno)

    return turnos_paciente


def buscar_turnos_medico(lista_turnos):
    """
    Objetivo: Buscar y mostrar los turnos de un médico por su CUIT
    Parametros: lista_turnos (lista de diccionarios)
    Retorno: Lista de turnos del medico, ordenada por fecha y hora
    """
    CUIT = input("Ingresar CUIT del medico: ")
    return consultar_agenda_medico(CUIT, lista_turnos)


""" ESTAS FUNCIONES QUEDAN PENDIENTES PARA LA ENTREGA DEL 100% """

def guardar_json(datos, nombre_archivo):
    """Guarda los datos en un archivo JSON. (Se implementa en el 100%)."""
    pass


def cargar_json(nombre_archivo):
    """Carga los datos desde un archivo JSON. (Se implementa en el 100%)."""
    pass



def main():
    """
    Objetivo: Mostrar el menú principal y permitir la interacción con el usuario
    Parametros: No recibe parámetros.
    Retorno: No retorna ningún valor"""
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
        print("Opcion 4: AGENDA DEL MEDICO ")
        print("Opcion 5: GUARDAR Y CARGAR DATOS ")
        print("Opcion 6: CONSULTAR AGENDA DEL MEDICO ")
        print("Opcion 7: CONSULTAR TURNOS DE PACIENTE ")
        print("Opcion 8: CONSULTAR TURNOS DE MEDICO ")
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
                buscar_cuit_paciente(Pacientes)

            elif opcion_paciente == 2:
                cargar_paciente(Pacientes)

            elif opcion_paciente == 3:
                mostrar_Pacientes(Pacientes)

            elif opcion_paciente == 4:
                actualizar_paciente(Pacientes)

            elif opcion_paciente == 5:
                eliminar_paciente(Pacientes)

        elif opcion == 2:

            print(" Opcion 1: Buscar Médico por CUIT.")
            print(" Opcion 2: Cargar Médico.")
            print(" Opcion 3: Mostrar Lista de Médicos en Orden Alfabetico.")
            print(" Opcion 4: Actualizar Médico.")
            print(" Opcion 5: Eliminar Médico.")
            print()

            opcion_medico = int(input("Ingresar opcion de MEDICO: "))

            if opcion_medico == 1:
                buscar_medico_cuit(Medicos)

            elif opcion_medico == 2:
                cargar_medico(Medicos)

            elif opcion_medico == 3:
                mostrar_medico(Medicos)

            elif opcion_medico == 4:
                actualizar_medico(Medicos)

            elif opcion_medico == 5:
                eliminar_medico(Medicos)

        elif opcion == 3:

            print(" Opcion 1: Buscar Turnos de Paciente por CUIT.")
            print(" Opcion 2: Buscar Turnos de Médico por CUIT.")
            print(" Opcion 3: Cargar Turno.")
            print(" Opcion 4: Actualizar Turno.")
            print(" Opcion 5: Eliminar Turno.")
            print(" Opcion 6: Listar todos los Turnos.")
            print()

            opcion_turno = int(input("Ingresar opcion de TURNO: "))

            if opcion_turno == 1:
                buscar_turnos_paciente(Lista_turnos)

            elif opcion_turno == 2:
                buscar_turnos_medico(Lista_turnos)

            elif opcion_turno == 3:
                cargar_turno(Lista_turnos, Medicos, Pacientes)

            elif opcion_turno == 4:
                modificar_turno(Lista_turnos)

            elif opcion_turno == 5:
                eliminar_turno(Lista_turnos)

            elif opcion_turno == 6:
                listar_turnos(Lista_turnos)

        elif opcion == 4:
            id_medico = input("Ingresar CUIT del medico: ")
            consultar_agenda_medico(id_medico, Lista_turnos)

        elif opcion == 5:
            # Pendiente: guardar_json/cargar_json quedan con pass hasta
            # la entrega del 100%. Cuando se implementen, acá va el
            # submenú para elegir Guardar o Cargar.
            pass

        elif opcion == 6:
    
            id_medico = input("Ingresar CUIT del medico: ")
            consultar_agenda_medico(id_medico, Lista_turnos)

        elif opcion == 7:

            buscar_turnos_paciente(Lista_turnos)

        elif opcion == 8:
   
            buscar_turnos_medico(Lista_turnos)

        elif opcion == -1:

            print("Fin del programa...")

        else:

            print("Opcion incorrecta")


main()