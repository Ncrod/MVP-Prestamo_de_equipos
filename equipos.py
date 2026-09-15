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


def listar_equipos():
    print("\n--- Listado de equipos ---")
    equipos = cargar(RUTA_EQUIPOS)

    if len(equipos) == 0:
        print("No hay equipos registrados.")
        return

    print(f"{'CODIGO':<10}{'TIPO':<14}{'MARCA':<12}{'MODELO':<12}{'ESTADO':<14}")
    print("-" * 62)
    disponibles = 0
    for equipo in equipos:
        print(f"{equipo['codigo']:<10}{equipo['tipo']:<14}{equipo['marca']:<12}"
              f"{equipo['modelo']:<12}{equipo['estado']:<14}")
        if equipo["estado"] == "disponible":
            disponibles += 1
    print("-" * 62)
    print(f"Total: {len(equipos)} equipo(s) | Disponibles: {disponibles}")


def eliminar_equipo():
    print("\n--- Eliminar equipo ---")
    codigo = pedir_texto("Codigo del equipo a eliminar: ").upper()
    equipo = buscar_equipo(codigo)

    if equipo is None:
        print(f"Error: no existe un equipo con el codigo {codigo}.")
        return

    if equipo["estado"] == "prestado":
        print(f"Error: el equipo {codigo} esta prestado y no se puede eliminar.")
        return

    confirmacion = input(f"Seguro que desea eliminar el equipo {codigo}? (s/n): ").strip().lower()
    if confirmacion != "s":
        print("Operacion cancelada. El equipo no fue eliminado.")
        return

    equipos = cargar(RUTA_EQUIPOS)
    equipos_restantes = [e for e in equipos if e["codigo"] != codigo]
    guardar(RUTA_EQUIPOS, equipos_restantes)
    print(f"Equipo {codigo} eliminado del inventario.")