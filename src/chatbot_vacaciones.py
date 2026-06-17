# Importa el módulo csv para poder leer archivos CSV
import csv


# Función que carga los empleados desde el archivo empleados.csv
def cargar_empleados():

    # Diccionario donde se almacenarán los empleados
    empleados = {}

    # Abre el archivo CSV en modo lectura
    with open(
        "empleados.csv",
        mode="r",
        encoding="utf-8"
    ) as archivo:

        # DictReader permite leer cada fila como un diccionario
        # delimiter=";" porque el CSV fue generado con punto y coma
        lector = csv.DictReader(
            archivo,
            delimiter=";"
        )

        # Recorre todas las filas del archivo
        for fila in lector:

            # Obtiene el legajo y lo convierte a entero
            legajo = int(fila["Legajo"])

            # Guarda los datos del empleado en el diccionario
            empleados[legajo] = {
                "nombre": fila["Nombre"],
                "dias_disponibles": int(
                    fila["Dias_Disponibles"]
                ),
                "email": fila["Email"]
            }

    # Devuelve el diccionario completo de empleados
    return empleados


# Carga los empleados desde el archivo CSV
empleados = cargar_empleados()

# Estado inicial de la conversación
estado = "ESPERANDO_LEGAJO"

# Encabezado del programa
print("=" * 40)
print("CHATBOT DE SOLICITUD DE VACACIONES")
print("=" * 40)

# Bucle principal del chatbot
while True:

    # Estado: esperar que el usuario ingrese su legajo
    if estado == "ESPERANDO_LEGAJO":

        try:
            # Solicita el legajo y lo convierte a entero
            legajo = int(input("Ingrese su legajo: "))

        # Si el usuario escribe texto en lugar de un número
        except ValueError:
            print("Error: debe ingresar un número.")
            continue

        # Verifica si el legajo existe en la base de datos
        if legajo not in empleados:
            print("Legajo inexistente.")
            continue

        # Obtiene los datos del empleado encontrado
        empleado = empleados[legajo]

        print()
        print("Empleado encontrado")
        print("Nombre:", empleado["nombre"])
        print("Días disponibles:", empleado["dias_disponibles"])

        # Cambia al siguiente estado
        estado = "ESPERANDO_DIAS"

    # Estado: esperar cantidad de días solicitados
    elif estado == "ESPERANDO_DIAS":

        try:
            # Solicita la cantidad de días
            dias_solicitados = int(
                input("Ingrese cantidad de días solicitados: ")
            )

        # Controla que el usuario ingrese un número
        except ValueError:
            print("Error: debe ingresar un número.")
            continue

        # Valida que la cantidad sea mayor que cero
        if dias_solicitados <= 0:
            print("La cantidad debe ser mayor que cero.")
            continue

        # Verifica si el empleado tiene saldo suficiente
        if dias_solicitados > empleado["dias_disponibles"]:

            print()
            print("SOLICITUD RECHAZADA")
            print("No posee días suficientes.")

            # Finaliza el proceso
            estado = "FIN"

        else:

            # Calcula el saldo restante de vacaciones
            saldo_restante = (
                empleado["dias_disponibles"]
                - dias_solicitados
            )

            print()
            print("SOLICITUD APROBADA")
            print("Días solicitados:", dias_solicitados)
            print("Saldo restante:", saldo_restante)

            # Finaliza el proceso
            estado = "FIN"

    # Estado final del chatbot
    elif estado == "FIN":

        print()
        print("Proceso finalizado.")

        # Sale del bucle y termina el programa
        break
