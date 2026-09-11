import re
import datetime
import archivoPacientes


def buscar_cuit(pacientes):
    """
Objetivo:
Parametros:
Retorno:"""

    # Esta función busca un paciente por CUIT. Si existe, lo muestra.
    # Si no existe pero el CUIT tiene el formato correcto, lo manda a cargar.

    cuit = input("Ingresar CUIT del paciente: ")

    # Chequeamos que el CUIT tenga el formato XX-XXXXXXXX-X (números separados por guiones)
    resultado = re.findall(r"^[0-9]{2}-[0-9]{8}-[0-9]{1}$", cuit)

    if resultado:

        # Recorremos la lista de pacientes a ver si ya está cargado
        for paciente in pacientes:

            if cuit == paciente["CUIT"]:
                print("Paciente existente:")
                print(paciente)

                return pacientes

        # Si llegamos hasta acá es porque no lo encontramos, entonces lo cargamos
        cargar_paciente(pacientes, cuit)

    else:
        print("Formato de CUIT incorrecto.")

    return pacientes


def cargar_paciente(pacientes, cuit):
    # Esta función arma el diccionario de un paciente nuevo y lo agrega a la lista.
    # OJO: recibe el cuit ya validado por quien la llama, acá no se vuelve a chequear el formato.

    paciente = {}

    paciente["CUIT"] = cuit

    paciente["Apellido"] = input("Ingresar apellido: ").capitalize()

    paciente["Nombre"] = input("Ingresar nombre del paciente: ").capitalize()

    paciente["Edad"] = int(input("Ingresar edad: "))

    # Lambda cortita para chequear si es menor de 16 (institución pediátrica)
    edad_menor = lambda x: x < 16

    if edad_menor(paciente["Edad"]):

        print("Paciente menor de edad. Se debe atender en una institución pediátrica")

    pacientes.append(paciente)

    return pacientes


def cargar_medico(medicos):
    # Carga un médico nuevo pidiendo sus datos por teclado y lo agrega a la lista de médicos
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
    # Ordena la lista de pacientes por apellido (de la A a la Z) y los imprime uno por uno
    pacientes.sort(key=lambda paciente: paciente["Apellido"])

    for paciente in pacientes:
        print(paciente)


def main():

    # Lista de pacientes "hardcodeada" para tener datos de prueba desde el arranque
    pacientes = []

    medicos = []

    opcion = None

    # Regex de CUIT la sacamos afuera del loop para no repetirla, la reusamos en la opción 1
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

        # Si lo que ingresó no es un número (ej: "hola"), no dejamos que rompa el programa
        if not opcion_str.lstrip("-").isdigit():
            print("Opción inválida, ingresar un número.")
            continue

        opcion = int(opcion_str)

        if opcion == 1:
            # ACÁ ESTABA EL BUG: usaban una variable "cuit" que no existía en este scope
            # y encima sobraba un paréntesis de cierre. Ahora pedimos el CUIT acá mismo
            # y lo validamos antes de mandarlo a cargar_paciente.
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
