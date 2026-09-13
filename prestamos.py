from datetime import date

from archivos import cargar, guardar, pedir_texto, RUTA_PRESTAMOS
from equipos import buscar_equipo, cambiar_estado_equipo
from estudiantes import buscar_estudiante


def siguiente_id(prestamos):
   
    if len(prestamos) == 0:
        return 1
    return max(prestamo["id"] for prestamo in prestamos) + 1


def buscar_prestamo_activo(prestamos, codigo_equipo):
    
    for prestamo in prestamos:
        if prestamo["codigo_equipo"] == codigo_equipo and prestamo["estado"] == "activo":
            return prestamo
    return None


def nombre_estudiante(documento):
   
    estudiante = buscar_estudiante(documento)
    if estudiante is None:
        return "(no encontrado)"
    return estudiante["nombre"]



def registrar_prestamo():
    print("\n--- Registrar prestamo ---")

    
    documento = pedir_texto("Documento del estudiante: ")
    estudiante = buscar_estudiante(documento)
    if estudiante is None:
        print(f"Error: no existe un estudiante con el documento {documento}.")
        return

    
    codigo = pedir_texto("Codigo del equipo: ").upper()
    equipo = buscar_equipo(codigo)
    if equipo is None:
        print(f"Error: no existe un equipo con el codigo {codigo}.")
        return

    
    if equipo["estado"] != "disponible":
        print(f"Error: el equipo {codigo} no esta disponible (estado actual: {equipo['estado']}).")
        return

    prestamos = cargar(RUTA_PRESTAMOS)
    nuevo_prestamo = {
        "id": siguiente_id(prestamos),
        "documento": documento,
        "codigo_equipo": codigo,
        "fecha_prestamo": date.today().isoformat(),
        "fecha_devolucion": None,
        "estado": "activo",
    }
    prestamos.append(nuevo_prestamo)

    
    guardar(RUTA_PRESTAMOS, prestamos)
    cambiar_estado_equipo(codigo, "prestado")

    print(f"Prestamo #{nuevo_prestamo['id']} registrado para {estudiante['nombre']}.")
    print(f"El equipo {codigo} paso a estado 'prestado'.")


def registrar_devolucion():
    print("\n--- Registrar devolucion ---")
    codigo = pedir_texto("Codigo del equipo a devolver: ").upper()

    if buscar_equipo(codigo) is None:
        print(f"Error: no existe un equipo con el codigo {codigo}.")
        return

    prestamos = cargar(RUTA_PRESTAMOS)
    prestamo = buscar_prestamo_activo(prestamos, codigo)
    if prestamo is None:
        print(f"Error: el equipo {codigo} no tiene un prestamo activo.")
        return

    prestamo["fecha_devolucion"] = date.today().isoformat()
    prestamo["estado"] = "cerrado"

    guardar(RUTA_PRESTAMOS, prestamos)
    cambiar_estado_equipo(codigo, "disponible")

    print(f"Devolucion registrada. Prestamo #{prestamo['id']} cerrado.")
    print(f"El equipo {codigo} paso a estado 'disponible'.")