import json
import os

# Rutas

CARPETA_PROYECTO = os.path.dirname(os.path.abspath(__file__))
CARPETA_DATOS = os.path.join(CARPETA_PROYECTO, "datos")

RUTA_EQUIPOS = os.path.join(CARPETA_DATOS, "equipos.json")
RUTA_ESTUDIANTES = os.path.join(CARPETA_DATOS, "estudiantes.json")
RUTA_PRESTAMOS = os.path.join(CARPETA_DATOS, "prestamos.json")


def cargar(ruta):
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Aviso: el archivo {os.path.basename(ruta)} esta danado. Se usara una lista vacia.")
        return []

    if not isinstance(datos, list):
        return []
    return datos


def guardar(ruta, datos):
    
    try:
        os.makedirs(CARPETA_DATOS, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except OSError:
        print(f"Error: no se pudo guardar el archivo {os.path.basename(ruta)}.")


def pedir_texto(mensaje):
    
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: este campo es obligatorio. Intente de nuevo.")
