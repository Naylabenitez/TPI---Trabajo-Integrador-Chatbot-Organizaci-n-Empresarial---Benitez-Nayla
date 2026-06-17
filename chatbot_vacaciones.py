import csv


def cargar_empleados():

    empleados = {}

    with open(
        "empleados.csv",
        mode="r",
        encoding="utf-8"
    ) as archivo:

        lector = csv.DictReader(
            archivo,
            delimiter=";"
        )

        for fila in lector:

            legajo = int(fila["Legajo"])

            empleados[legajo] = {
                "nombre": fila["Nombre"],
                "dias_disponibles": int(
                    fila["Dias_Disponibles"]
                ),
                "email": fila["Email"]
            }

    return empleados


empleados = cargar_empleados()

estado = "ESPERANDO_LEGAJO"

print("=" * 40)
print("CHATBOT DE SOLICITUD DE VACACIONES")
print("=" * 40)

while True:

    if estado == "ESPERANDO_LEGAJO":

        try:
            legajo = int(input("Ingrese su legajo: "))
        except ValueError:
            print("Error: debe ingresar un número.")
            continue

        if legajo not in empleados:
            print("Legajo inexistente.")
            continue

        empleado = empleados[legajo]

        print()
        print("Empleado encontrado")
        print("Nombre:", empleado["nombre"])
        print("Días disponibles:", empleado["dias_disponibles"])

        estado = "ESPERANDO_DIAS"

    elif estado == "ESPERANDO_DIAS":

        try:
            dias_solicitados = int(
                input("Ingrese cantidad de días solicitados: ")
            )
        except ValueError:
            print("Error: debe ingresar un número.")
            continue

        if dias_solicitados <= 0:
            print("La cantidad debe ser mayor que cero.")
            continue

        if dias_solicitados > empleado["dias_disponibles"]:

            print()
            print("SOLICITUD RECHAZADA")
            print("No posee días suficientes.")

            estado = "FIN"

        else:

            saldo_restante = (
                empleado["dias_disponibles"]
                - dias_solicitados
            )

            print()
            print("SOLICITUD APROBADA")
            print("Días solicitados:", dias_solicitados)
            print("Saldo restante:", saldo_restante)

            estado = "FIN"

    elif estado == "FIN":

        print()
        print("Proceso finalizado.")
        break
