from archivos import cargar, guardar, pedir_texto, RUTA_ESTUDIANTES


def buscar_estudiante(documento):
    
    for estudiante in cargar(RUTA_ESTUDIANTES):
        if estudiante["documento"] == documento:
            return estudiante
    return None


def pedir_documento(mensaje):
   
    while True:
        documento = pedir_texto(mensaje)
        if documento.isdigit():
            return documento
        print("Error: el documento debe contener solo numeros.")


def pedir_correo():
    
    while True:
        correo = pedir_texto("Correo: ").lower()
        if "@" in correo and "." in correo and " " not in correo:
            return correo
        print("Error: correo invalido. Ejemplo: ana@mail.com")



def registrar_estudiante():
    print("\n--- Registrar estudiante ---")
    documento = pedir_documento("Documento: ")

    if buscar_estudiante(documento) is not None:
        print(f"Error: ya existe un estudiante con el documento {documento}.")
        return

    nombre = pedir_texto("Nombre completo: ")
    correo = pedir_correo()
    programa = pedir_texto("Programa academico: ")

    nuevo_estudiante = {
        "documento": documento,
        "nombre": nombre,
        "correo": correo,
        "programa": programa,
    }

    estudiantes = cargar(RUTA_ESTUDIANTES)
    estudiantes.append(nuevo_estudiante)
    guardar(RUTA_ESTUDIANTES, estudiantes)
    print(f"Estudiante {nombre} registrado correctamente.")


def listar_estudiantes():
    
    print("\n--- Listado de estudiantes ---")
    estudiantes = cargar(RUTA_ESTUDIANTES)

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    print(f"{'DOCUMENTO':<12}{'NOMBRE':<22}{'CORREO':<24}{'PROGRAMA':<20}")
    print("-" * 78)
    for estudiante in estudiantes:
        print(f"{estudiante['documento']:<12}{estudiante['nombre']:<22}"
              f"{estudiante['correo']:<24}{estudiante['programa']:<20}")
    print("-" * 78)
    print(f"Total: {len(estudiantes)} estudiante(s)")
