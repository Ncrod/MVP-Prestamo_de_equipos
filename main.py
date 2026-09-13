
from equipos import registrar_equipo, listar_equipos, eliminar_equipo
from estudiantes import registrar_estudiante, listar_estudiantes
from prestamos import (registrar_prestamo, registrar_devolucion,
                       listar_equipos_prestados, listar_historial)


def mostrar_menu():
    print("\n===== SISTEMA DE PRESTAMO DE EQUIPOS =====")
    print("1. Registrar equipo")
    print("2. Listar equipos")
    print("3. Registrar estudiante")
    print("4. Registrar prestamo")
    print("5. Registrar devolucion")
    print("6. Equipos prestados")
    print("7. Historial de prestamos")
    print("8. Eliminar equipo")
    print("9. Listar estudiantes")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            registrar_estudiante()
        elif opcion == "4":
            registrar_prestamo()
        elif opcion == "5":
            registrar_devolucion()
        elif opcion == "6":
            listar_equipos_prestados()
        elif opcion == "7":
            listar_historial()
        elif opcion == "8":
            eliminar_equipo()
        elif opcion == "9":
            listar_estudiantes()
        elif opcion == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opcion invalida. Ingrese un numero del 0 al 9.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")
