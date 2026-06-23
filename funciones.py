import csv

def cargar_paises(nombre_archivo):

    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:

                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }

                paises.append(pais)

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")

    except Exception as error:
        print("Error al leer archivo:", error)

    return paises


# ==========================
# GUARDAR CSV
# ==========================

def guardar_paises(nombre_archivo, paises):

    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:

        campos = ["nombre", "poblacion", "superficie", "continente"]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)


# ==========================
# AGREGAR PAIS
# ==========================

def agregar_pais(paises):

    try:

        nombre = input("Nombre: ").strip()
        continente = input("Continente: ").strip()

        if nombre == "" or continente == "":
            raise ValueError("No se permiten campos vacíos.")

        poblacion = int(input("Población: "))
        superficie = int(input("Superficie: "))

        nuevo_pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }

        paises.append(nuevo_pais)

        print("País agregado correctamente.")

    except ValueError as error:
        print("Error:", error)


# ==========================
# ACTUALIZAR PAIS
# ==========================

def actualizar_pais(paises):

    nombre = input("Ingrese país a actualizar: ").lower()

    for pais in paises:

        if pais["nombre"].lower() == nombre:

            try:

                pais["poblacion"] = int(
                    input("Nueva población: ")
                )

                pais["superficie"] = int(
                    input("Nueva superficie: ")
                )

                print("Datos actualizados.")

            except ValueError:
                print("Debe ingresar números.")

            return

    print("País no encontrado.")


# ==========================
# BUSCAR PAIS
# ==========================

def buscar_pais(paises):

    texto = input(
        "Ingrese nombre del país: "
    ).lower()

    encontrado = False

    for pais in paises:

        if texto in pais["nombre"].lower():

            print("\nNombre:", pais["nombre"])
            print("Población:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])

            encontrado = True

    if not encontrado:
        print("No se encontraron resultados.")


# ==========================
# FILTRAR CONTINENTE
# ==========================

def filtrar_continente(paises):

    continente = input(
        "Ingrese continente: "
    ).lower()

    encontrado = False

    for pais in paises:

        if pais["continente"].lower() == continente:

            print(pais)

            encontrado = True

    if not encontrado:
        print("No hay resultados.")


# ==========================
# FILTRAR POBLACION
# ==========================

def filtrar_poblacion(paises):

    try:

        minimo = int(
            input("Población mínima: ")
        )

        maximo = int(
            input("Población máxima: ")
        )

        encontrado = False

        for pais in paises:

            if minimo <= pais["poblacion"] <= maximo:

                print(pais)

                encontrado = True

        if not encontrado:
            print("No hay resultados.")

    except ValueError:
        print("Ingrese números válidos.")


# ==========================
# FILTRAR SUPERFICIE
# ==========================

def filtrar_superficie(paises):

    try:

        minimo = int(
            input("Superficie mínima: ")
        )

        maximo = int(
            input("Superficie máxima: ")
        )

        encontrado = False

        for pais in paises:

            if minimo <= pais["superficie"] <= maximo:

                print(pais)

                encontrado = True

        if not encontrado:
            print("No hay resultados.")

    except ValueError:
        print("Ingrese números válidos.")


# ==========================
# ORDENAR NOMBRE
# ==========================

def ordenar_nombre(paises):

    ordenados = sorted(
        paises,
        key=lambda pais: pais["nombre"]
    )

    for pais in ordenados:
        print(pais)


# ==========================
# ORDENAR POBLACION
# ==========================

def ordenar_poblacion(paises):

    opcion = input(
        "A-Ascendente / D-Descendente: "
    ).upper()

    if opcion == "A":

        ordenados = sorted(
            paises,
            key=lambda pais: pais["poblacion"]
        )

    elif opcion == "D":

        ordenados = sorted(
            paises,
            key=lambda pais: pais["poblacion"],
            reverse=True
        )

    else:
        print("Opción inválida.")
        return

    for pais in ordenados:
        print(pais)


# ==========================
# ORDENAR SUPERFICIE
# ==========================

def ordenar_superficie(paises):

    opcion = input(
        "A-Ascendente / D-Descendente: "
    ).upper()

    if opcion == "A":

        ordenados = sorted(
            paises,
            key=lambda pais: pais["superficie"]
        )

    elif opcion == "D":

        ordenados = sorted(
            paises,
            key=lambda pais: pais["superficie"],
            reverse=True
        )

    else:
        print("Opción inválida.")
        return

    for pais in ordenados:
        print(pais)


# ==========================
# ESTADISTICAS
# ==========================

def mostrar_estadisticas(paises):

    if len(paises) == 0:
        print("No hay datos.")
        return

    mayor = max(
        paises,
        key=lambda pais: pais["poblacion"]
    )

    menor = min(
        paises,
        key=lambda pais: pais["poblacion"]
    )

    promedio_poblacion = (
        sum(
            pais["poblacion"]
            for pais in paises
        ) / len(paises)
    )

    promedio_superficie = (
        sum(
            pais["superficie"]
            for pais in paises
        ) / len(paises)
    )

    continentes = {}

    for pais in paises:

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n===== ESTADÍSTICAS =====")

    print(
        "Mayor población:",
        mayor["nombre"]
    )

    print(
        "Menor población:",
        menor["nombre"]
    )

    print(
        "Promedio población:",
        round(promedio_poblacion, 2)
    )

    print(
        "Promedio superficie:",
        round(promedio_superficie, 2)
    )

    print("\nPaíses por continente:")

    for continente, cantidad in continentes.items():

        print(
            continente,
            ":",
            cantidad
        )


# ==========================
# MENU
# ==========================

def mostrar_menu():

    print("\n========== MENU ==========")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar por continente")
    print("5. Filtrar por población")
    print("6. Filtrar por superficie")
    print("7. Ordenar por nombre")
    print("8. Ordenar por población")
    print("9. Ordenar por superficie")
    print("10. Mostrar estadísticas")
    print("11. Guardar cambios")
    print("12. Salir")
