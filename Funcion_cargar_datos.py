import datetime 

def buscar_cuit(pacientes):

    cuit = input("Ingresar CUIT del paciente: ")

    for paciente in pacientes:
        if cuit == paciente["CUIT"]:
            print("Paciente existente:")
            print(paciente)
            return pacientes

    print("Paciente no encontrado. Se procede a cargarlo.")
    cargar_paciente(pacientes, cuit)

    return pacientes

def cargar_paciente(pacientes, cuit):

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

    pacientes.sort(key=lambda paciente: paciente["Apellido"])

    for paciente in pacientes:
        print(paciente)


def main():

    
    pacientes = [
        {"CUIT": "20-11601169-1", "Apellido": "Perez", "Nombre": "Julian", "Edad": 28},
        {"CUIT": "20-22202279-2", "Apellido": "Gomez", "Nombre": "Maria", "Edad": 34},
        {"CUIT": "27-33303339-3", "Apellido": "Lopez", "Nombre": "Ernestina", "Edad": 82},
        {"CUIT": "20-44404449-4", "Apellido": "Martinez", "Nombre": "Ana Clara", "Edad": 28},
        {"CUIT": "20-55015559-5", "Apellido": "van Rossum", "Nombre": "Guido", "Edad": 70},
        {"CUIT": "20-62066666-6", "Apellido": "Fernandez", "Nombre": "Laura", "Edad": 67},
        {"CUIT": "20-77707739-7", "Apellido": "Sanchez", "Nombre": "Lucas", "Edad": 38},
        {"CUIT": "21-88938068-8", "Apellido": "Romero", "Nombre": "Sofia", "Edad": 31},
        {"CUIT": "20-99999039-9", "Apellido": "Torres", "Nombre": "Martin", "Edad": 52},
        {"CUIT": "20-12345678-9", "Apellido": "Ruiz", "Nombre": "Julieta", "Edad": 64},
        {"CUIT": "20-11811317-1", "Apellido": "Perez", "Nombre": "Hipolito", "Edad": 55},
        {"CUIT": "27-22022337-2", "Apellido": "Messi", "Nombre": "Maria", "Edad": 34},
        {"CUIT": "20-32733317-3", "Apellido": "Lopez", "Nombre": "Pedro", "Edad": 52},
        {"CUIT": "27-44044397-4", "Apellido": "De La Colina", "Nombre": "Ana Julia", "Edad": 58},
        {"CUIT": "20-52855527-5", "Apellido": "Rodriguez", "Nombre": "Carlos", "Edad": 85},
    ]

    medicos = []

    opcion = None

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
            cargar_paciente(pacientes)

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
