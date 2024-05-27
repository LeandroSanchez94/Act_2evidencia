#Estructura secuencial

nota1=int(input("ingresa la primer nota")),
nota2=int(input("ingresa la segunda nota"))
nota3=int(input("ingresa la tercer nota"))
nota4=int(input("ingresa la cuarta nota"))
nota5=int(input("ingresa la quinta nota"))
promedio = int((nota1 + nota2 + nota3 + nota4 + nota5) / 5)
print( "el promedio es ", promedio)

#Estructura condicional (cual es el mayor de los tres)

numero1 = int(input("por favor, ingresa el primer  numero: "))
numero2 = int(input("por favor, ingresa el segundo numero: "))
numero3 = int(input("por favor, ingresa el tercer  numero: "))

if numero1 > numero2:
    if numero1 > numero3:
        mayor = numero1
    else:
        mayor = numero3
else:
    if numero2 > numero3:
        mayor = numero2
    else:
        mayor = numero3

print("El mayor numero es el: ", mayor);


#Estructuras repetitivas

num = int(input("Por favor, ingresa un numero: "))

for pares in range(0, num + 1):
    if pares == int(pares / 2) * 2 and pares > 0:
        print(pares)


# Estructura de datos 

def agregar_persona(agenda):
    apellido = input("Ingrese el apellido: ")
    nombre = input("Ingrese el nombre: ")
    dni = int(input("Ingrese el DNI: "))
    email = input("Ingrese el email: ")
    telefono = input("Ingrese el número de teléfono: ")

    if dni not in agenda:
        agenda[dni] = {
            "apellido": apellido,
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        print(f"Persona agregada exitosamente: {nombre} {apellido}")
    else:
        print(f"Ya existe una persona con el DNI {dni}.")


def modificar_persona(agenda):
    dni = int(input("Ingrese el DNI de la persona a modificar: "))

    if dni in agenda:
        persona = agenda[dni]
        print(f"Datos actuales de la persona:")
        for clave, valor in persona.items():
            print(f"{clave}: {valor}")

        apellido_nuevo = input("¿Desea modificar el apellido? (si/no): ")
        if apellido_nuevo.lower() == "si":
            persona["apellido"] = input("Ingrese el nuevo apellido: ")
            
        nombre_nuevo = input("¿Desea modificar el nombre? (si/no): ")
        if nombre_nuevo.lower() == "si":
            persona["nombre"] = input("Ingrese el nuevo nombre: ")

        dni_nuevo = input("¿Desea modificar el dni? (si/no): ")
        if dni_nuevo.lower() == "si":
            persona["dni"] = input("Ingrese el nuevo dni: ")

        email_nuevo = input("¿Desea modificar el email? (si/no): ")
        if email_nuevo.lower() == "si":
            persona["email"] = input("Ingrese el nuevo email: ")

        telefono_nuevo = input("¿Desea modificar el telefono? (si/no): ")
        if telefono_nuevo.lower() == "si":
            persona["telefono"] = input("Ingrese el nuevo telefono: ")

        print(f"Persona modificada exitosamente: {persona['nombre']} {persona['apellido']}")
    else:
        print(f"No se encontró ninguna persona con el DNI {dni}.")


def eliminar_persona(agenda):
    dni = int(input("Ingrese el DNI de la persona a eliminar: "))

    if dni in agenda:
        del agenda[dni]
        print(f"Persona eliminada exitosamente con DNI {dni}.")
    else:
        print(f"No se encontró ninguna persona con el DNI {dni}.")


def mostrar_agenda(agenda):
    if agenda:
        print("Agenda:")
        for dni, persona in agenda.items():
            print(f"DNI: {dni}")
            for clave, valor in persona.items():
                print(f"{clave}: {valor}")
    else:
        print("La agenda está vacía.")


def comienzo():
    agenda = {}

    while True:
        print("Menú de opciones:")
        print("1. Agregar persona")
        print("2. Modificar persona")
        print("3. Eliminar persona")
        print("4. Mostrar agenda")
        print("5. Salir")

        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            agregar_persona(agenda)
        elif opcion == 2:
            modificar_persona(agenda)
        elif opcion == 3:
            eliminar_persona(agenda)
        elif opcion == 4:
            mostrar_agenda(agenda)
        elif opcion == 5:
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if comienzo == comienzo():
    comienzo()

