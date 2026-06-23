# TPI_Prog1_Sistema de Gestión de Países
## Descripción del Proyecto
Trabajo Práctico Integrador - Gestión de Datos de Países en Python
Descripción del Proyecto

Este proyecto fue desarrollado en Python para la materia Programación 1 de la Tecnicatura Universitaria en Programación.
La aplicación permite gestionar información de distintos países almacenados en un archivo CSV. Mediante un menú interactivo en consola, el usuario puede realizar operaciones de alta, modificación, búsqueda, filtrado, ordenamiento y generación de estadísticas.
El objetivo principal es aplicar los conceptos de listas, diccionarios, funciones, estructuras de control, manejo de archivos CSV y validación de datos en Python.

Los datos que maneja el programa son:

* Nombre del país
* Población
* Superficie
* Continente

Toda la información se guarda en el archivo `paises.csv`, permitiendo conservar los cambios realizados entre ejecuciones del programa.


## Objetivo

El objetivo principal del sistema es aplicar los conceptos fundamentales vistos durante la cursada, tales como:

* Funciones y modularización.
* Manejo de listas y diccionarios.
* Lectura y escritura de archivos CSV.
* Estructuras de control (`if`, `for`, `while`).
* Manejo de excepciones mediante `try/except`.
* Búsquedas, filtros y ordenamientos de datos.


## Estructura del Proyecto

Proyecto/
│
├── main.py
├── funciones.py
├── paises.csv
└── README.md

### main.py

Archivo principal del sistema.

Sus responsabilidades son:

* Cargar los datos desde el archivo CSV.
* Mostrar el menú principal.
* Capturar la opción elegida por el usuario.
* Llamar a la función correspondiente.
* Guardar los cambios realizados.
* Finalizar la ejecución del programa.

### funciones.py

Contiene toda la lógica del sistema organizada en funciones independientes.

Incluye:

* Carga de datos.
* Guardado de datos.
* Altas de países.
* Actualización de información.
* Búsquedas.
* Filtros.
* Ordenamientos.
* Estadísticas.

### paises.csv

Archivo donde se almacenan permanentemente los datos de los países.

Ejemplo:

nombre,poblacion,superficie,continente
Argentina,46000000,2780400,America
Brasil,215000000,8516000,America
España,48000000,505990,Europa



## Funcionalidades Implementadas

### 1. Agregar país

Permite registrar un nuevo país ingresando:

* Nombre
* Población
* Superficie
* Continente

Validaciones:

* No se permiten campos vacíos.
* La población y la superficie deben ser numéricas.


### 2. Actualizar país

Permite modificar:

* Población
* Superficie

de un país ya existente.

Si el país no existe, se informa al usuario.


### 3. Buscar país

Permite buscar países por nombre mediante coincidencia:

* Exacta
* Parcial

Ejemplo:

Entrada:

arg

Salida:

Nombre: Argentina
Población: 46000000
Superficie: 2780400
Continente: America


### 4. Filtrar por continente

Muestra todos los países pertenecientes a un continente específico.

Ejemplo:

America

Ingrese continente: america
{'nombre': 'Argentina', 'poblacion': 47000000, 'superficie': 2780400, 'continente': 'America'}
{'nombre': 'Brasil', 'poblacion': 216000000, 'superficie': 8515767, 'continente': 'America'}
{'nombre': 'Chile', 'poblacion': 19600000, 'superficie': 756102, 'continente': 'America'}
{'nombre': 'Estados Unidos', 'poblacion': 340000000, 'superficie': 9833517, 'continente': 'America'}

### 5. Filtrar por población

Permite buscar países dentro de un rango de población definido por el usuario.

Ejemplo:

Población mínima: 10000000
Población máxima: 100000000

### 6. Filtrar por superficie

Permite mostrar países cuya superficie se encuentre dentro de un rango determinado.


### 7. Ordenar por nombre

Muestra los países ordenados alfabéticamente.

### 8. Ordenar por población

Permite ordenar:

* Ascendente
* Descendente

según la cantidad de habitantes.

### 9. Ordenar por superficie

Permite ordenar:

* Ascendente
* Descendente

según la superficie.

### 10. Estadísticas

El sistema calcula automáticamente:

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

### 11. Guardar cambios

Actualiza el archivo CSV con todas las modificaciones realizadas durante la ejecución.

### 12. Salir

Guarda los cambios pendientes y finaliza el programa.

## Manejo de Errores

El sistema utiliza bloques `try/except` para evitar que el programa finalice inesperadamente ante errores de ingreso de datos.

Ejemplos controlados:

* Archivo CSV inexistente.
* Ingreso de texto donde se esperan números.
* Campos obligatorios vacíos.


## Estructuras de Datos Utilizadas

### Lista de Países

Todos los países se almacenan en una lista.

Ejemplo:

paises = [
    {
        "nombre": "Argentina",
        "poblacion": 46000000,
        "superficie": 2780400,
        "continente": "America"
    }
]

### Diccionarios

Cada país es representado mediante un diccionario con sus atributos.


## Alcance del Proyecto

Este sistema está pensado para la administración básica de información de países en un entorno educativo.

Permite:

* Gestionar registros.
* Realizar búsquedas.
* Aplicar filtros.
* Obtener estadísticas.
* Mantener persistencia de datos mediante archivos CSV.

## Requisitos

* Python 3.10 o superior.
* Biblioteca estándar `csv` (incluida en Python).

No requiere instalación de dependencias externas.


## Instrucciones de Uso

1. Descargar o clonar el repositorio.
2. Verificar que exista el archivo `paises.csv`.
3. Ejecutar:

python main.py

4. Seleccionar una opción del menú.
5. Realizar las operaciones deseadas.
6. Guardar los cambios o salir del programa.

-------------------------------------------------------------

## Autor
Nicolás Germán de Prado - DNI:40.976.550 - Comisión 8
Trabajo Práctico Integrador – Programación I
