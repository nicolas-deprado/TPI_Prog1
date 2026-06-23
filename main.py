# MAIN
from funciones import*

def main():

    archivo = "paises.csv"

    paises = cargar_paises(archivo)

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_pais(paises)

        elif opcion == "2":
            actualizar_pais(paises)

        elif opcion == "3":
            buscar_pais(paises)

        elif opcion == "4":
            filtrar_continente(paises)

        elif opcion == "5":
            filtrar_poblacion(paises)

        elif opcion == "6":
            filtrar_superficie(paises)

        elif opcion == "7":
            ordenar_nombre(paises)

        elif opcion == "8":
            ordenar_poblacion(paises)

        elif opcion == "9":
            ordenar_superficie(paises)

        elif opcion == "10":
            mostrar_estadisticas(paises)

        elif opcion == "11":

            guardar_paises(archivo,paises)

            print("Cambios guardados.")

        elif opcion == "12":

            guardar_paises(archivo,paises)

            print("Programa finalizado.")

            break

        else:
            print("Opción inválida.")


main()