from archivos import cargar, guardar, pedir_texto, RUTA_EQUIPOS

ESTADOS_REGISTRO = ["disponible", "mantenimiento"]


def buscar_equipo(codigo):
   
    for equipo in cargar(RUTA_EQUIPOS):
        if equipo["codigo"] == codigo:
            return equipo
    return None


def cambiar_estado_equipo(codigo, nuevo_estado):
    
    equipos = cargar(RUTA_EQUIPOS)
    for equipo in equipos:
        if equipo["codigo"] == codigo:
            equipo["estado"] = nuevo_estado
            guardar(RUTA_EQUIPOS, equipos)
            return True
    return False


def pedir_estado():
    
    while True:
        estado = input("Estado (disponible/mantenimiento) [disponible]: ").strip().lower()
        if estado == "":
            return "disponible"
        if estado in ESTADOS_REGISTRO:
            return estado
        print("Error: estado invalido. Escriba 'disponible' o 'mantenimiento'.")


# ---------------- HU01 ----------------
def registrar_equipo():
    print("\n--- Registrar equipo ---")
    codigo = pedir_texto("Codigo del equipo: ").upper()

    if buscar_equipo(codigo) is not None:
        print(f"Error: ya existe un equipo con el codigo {codigo}.")
        return

    tipo = pedir_texto("Tipo (ej. Portatil, Tablet): ")
    marca = pedir_texto("Marca: ")
    modelo = pedir_texto("Modelo: ")
    estado = pedir_estado()

    nuevo_equipo = {
        "codigo": codigo,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": estado,
    }

    equipos = cargar(RUTA_EQUIPOS)
    equipos.append(nuevo_equipo)
    guardar(RUTA_EQUIPOS, equipos)
    print(f"Equipo {codigo} registrado correctamente.")