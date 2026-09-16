# Sistema de Préstamo de Equipos Tecnológicos

MVP por consola desarrollado en Python para gestionar el préstamo y la devolución de equipos tecnológicos (portátiles, tablets, etc.) de una institución educativa. Permite registrar equipos y estudiantes, prestar un equipo, consultar su estado y devolverlo, guardando todo en archivos JSON.

Proyecto construido en un Sprint aplicando Scrum.

## Requisitos
- Python 3.10 o superior
- Sin librerías externas: solo se usa la librería estándar (`json`, `os`, `datetime`)

## Instalación y ejecución
```bash
git clone https://github.com/<usuario>/<repo>.git
cd <repo>
python main.py
```
En Windows también funciona `py main.py`.

Los datos se guardan en la carpeta `datos/`. Si los archivos no existen, se crean solos al registrar el primer dato.
Para empezar con el sistema vacío, deje cada archivo `.json` con el contenido `[]`.

## Funcionalidades

| ID | Historia de usuario | Opción del menú |
|---|---|---|
| HU01 | Registrar equipo (código, tipo, marca, modelo, estado) | 1 |
| HU02 | Listar equipos y su disponibilidad | 2 |
| HU03 | Registrar estudiante (documento, nombre, correo, programa) | 3 |
| HU04 | Registrar préstamo (valida estudiante, equipo y disponibilidad) | 4 |
| HU05 | Registrar devolución (cierra el préstamo y libera el equipo) | 5 |
| HU06 | Consultar equipos actualmente prestados | 6 |
| HU07 | Consultar historial de préstamos | 7 |
| HU08 | Eliminar equipo del inventario (no se permite si está prestado) | 8 |
| — | Listar estudiantes (apoyo para pruebas y demo) | 9 |

## Reglas de negocio y validaciones
- Ningún campo puede quedar vacío: el sistema vuelve a pedir el dato.
- El código del equipo es único y se guarda en mayúsculas (`eq001` → `EQ001`).
- Un equipo se registra como `disponible` o `mantenimiento`. El estado `prestado` solo lo pone el sistema al registrar un préstamo.
- El documento del estudiante es único y solo acepta números. El correo debe tener `@` y `.`.
- Un préstamo solo se crea si el estudiante existe, el equipo existe y está `disponible`.
- Al prestar, el equipo pasa a `prestado`; al devolver, el préstamo pasa a `cerrado` y el equipo vuelve a `disponible`.
- No se puede eliminar un equipo prestado. Antes de eliminar se pide confirmación (`s/n`).
- Si se escribe una opción inválida en el menú (por ejemplo `abc`) el programa muestra un mensaje y no se cae.
- Si un archivo JSON está dañado, el programa avisa y continúa con una lista vacía.

## Estructura del proyecto
```
Proyecto_MVP/
├── main.py           menú principal: solo muestra opciones y llama funciones
├── equipos.py        HU01, HU02, HU08 (inventario de equipos)
├── estudiantes.py    HU03 (registro de estudiantes)
├── prestamos.py      HU04, HU05, HU06, HU07 (préstamos y consultas)
├── archivos.py       cargar/guardar JSON y pedir datos obligatorios
├── README.md
└── datos/
    ├── equipos.json
    ├── estudiantes.json
    └── prestamos.json
```

### Dependencias entre módulos
```
main.py ──> equipos.py ─────┐
        ──> estudiantes.py ─┼──> archivos.py ──> datos/*.json
        ──> prestamos.py ───┘
             (usa equipos.py y estudiantes.py)
```

## Formato de los datos (JSON)
```json
// datos/equipos.json
[{"codigo": "EQ001", "tipo": "Portatil", "marca": "HP", "modelo": "240", "estado": "disponible"}]

// datos/estudiantes.json
[{"documento": "1001", "nombre": "Ana Perez", "correo": "ana@mail.com", "programa": "Ing. Sistemas"}]

// datos/prestamos.json
[{"id": 1, "documento": "1001", "codigo_equipo": "EQ001",
  "fecha_prestamo": "2026-09-12", "fecha_devolucion": null, "estado": "activo"}]
```

## Ejemplo de uso
```
===== SISTEMA DE PRESTAMO DE EQUIPOS =====
1. Registrar equipo
2. Listar equipos
3. Registrar estudiante
4. Registrar prestamo
5. Registrar devolucion
6. Equipos prestados
7. Historial de prestamos
8. Eliminar equipo
9. Listar estudiantes
0. Salir
Seleccione una opcion: 4

--- Registrar prestamo ---
Documento del estudiante: 1001
Codigo del equipo: EQ001
Prestamo #1 registrado para Ana Perez.
El equipo EQ001 paso a estado 'prestado'.
```

```
Seleccione una opcion: 6

--- Equipos actualmente prestados ---
EQUIPO    DOCUMENTO   ESTUDIANTE            FECHA PRESTAMO
------------------------------------------------------------
EQ001     1001        Ana Perez             2026-09-13
------------------------------------------------------------
Total: 1 equipo(s) prestado(s)
```

## Pruebas
Los 18 casos de prueba (CP01–CP18) están en `07_Pruebas/Plan_y_Casos_de_Prueba.docx`. El resultado esperado de cada caso coincide con los mensajes exactos que muestra el programa.



