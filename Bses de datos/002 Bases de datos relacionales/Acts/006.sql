import sqlite3
import os
import time

# Colores ANSI
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
UNDERLINE = "\033[4m"

# Limpiar pantalla
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Texto centrado en consola (80 caracteres ancho típico)
def center(text, width=80):
    return text.center(width)

# Línea separadora colorida
def separator(char='-', length=80):
    return f"{MAGENTA}{char*length}{RESET}"

# Caja con borde
def box(text_lines, width=80):
    top = f"{MAGENTA}╔{'═'*(width-2)}╗{RESET}"
    bottom = f"{MAGENTA}╚{'═'*(width-2)}╝{RESET}"
    boxed = [top]
    for line in text_lines:
        line_str = line[:width-4]  # recortar si es muy largo
        padded = line_str.ljust(width-4)
        boxed.append(f"{MAGENTA}║{RESET} {padded} {MAGENTA}║{RESET}")
    boxed.append(bottom)
    return "\n".join(boxed)

# Simular animación sencilla de carga
def loading(message="Cargando", duration=1.5, steps=3):
    for i in range(steps):
        print(f"{CYAN}{message}{'.' * (i+1)}{' ' * (steps - i -1)}{RESET}", end='\r')
        time.sleep(duration/steps)
    print(' ' * (len(message)+steps), end='\r')  # limpiar línea

# Conexión a la base de datos
conexion = sqlite3.connect("1empresa.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        identificador INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        email TEXT NOT NULL
    );
""")
conexion.commit()

def menu():
    clear()
    title = center(f"{BOLD}{CYAN}📋 GESTIÓN DE CLIENTES - MENU PRINCIPAL 📋{RESET}")
    opciones = [
        f"{YELLOW}1.{RESET} ➤ Crear cliente 🆕",
        f"{YELLOW}2.{RESET} ➤ Listar clientes 📜",
        f"{YELLOW}3.{RESET} ➤ Actualizar cliente ✏️",
        f"{YELLOW}4.{RESET} ➤ Eliminar cliente ❌",
        f"{YELLOW}5.{RESET} ➤ Salir del programa 🚪"
    ]
    print(box([title, ""] + opciones))
    print(separator())

def imprimir_clientes(clientes):
    clear()
    header = f"{BOLD}{UNDERLINE}Lista de Clientes{RESET}"
    print(center(header))
    if not clientes:
        print(f"\n{YELLOW}⚠ No hay clientes registrados.{RESET}\n")
        return

    print(separator())
    # Cabecera tabla
    print(f"{BOLD}{'ID':<5} {'Nombre':<20} {'Apellidos':<25} {'Email':<30}{RESET}")
    print(separator())

    for c in clientes:
        print(f"{c[0]:<5} {c[1]:<20} {c[2]:<25} {c[3]:<30}")

    print(separator())

def main():
    while True:
        menu()
        try:
            opcion = int(input(f"{BOLD}Selecciona una opción (1-5): {RESET}"))
        except ValueError:
            print(f"{RED}❌ Por favor, introduce un número válido.{RESET}")
            input("Pulsa Enter para continuar...")
            continue

        if opcion == 1:
            clear()
            print(center(f"{BOLD}{GREEN}🆕 Crear nuevo cliente 🆕{RESET}"))
            nombre = input("Introduce el nombre del nuevo cliente: ").strip()
            apellidos = input("Introduce los apellidos del nuevo cliente: ").strip()
            email = input("Introduce el email del nuevo cliente: ").strip()

            if nombre and apellidos and email:
                loading("Guardando cliente")
                cursor.execute("""
                    INSERT INTO clientes (nombre, apellido, email) VALUES (?, ?, ?);
                """, (nombre, apellidos, email))
                conexion.commit()
                print(f"{GREEN}✔ Cliente creado correctamente.{RESET}")
            else:
                print(f"{RED}❌ Todos los campos son obligatorios.{RESET}")

        elif opcion == 2:
            cursor.execute("SELECT * FROM clientes;")
            clientes = cursor.fetchall()
            imprimir_clientes(clientes)

        elif opcion == 3:
            clear()
            print(center(f"{BOLD}{CYAN}✏️ Actualizar cliente ✏️{RESET}"))
            identificador = input("Introduce el ID del cliente a actualizar: ").strip()
            cursor.execute("SELECT * FROM clientes WHERE identificador = ?;", (identificador,))
            cliente = cursor.fetchone()

            if cliente:
                print(f"{YELLOW}Deja en blanco para mantener el valor actual.{RESET}")
                nombre = input(f"Nuevo nombre ({cliente[1]}): ").strip() or cliente[1]
                apellidos = input(f"Nuevos apellidos ({cliente[2]}): ").strip() or cliente[2]
                email = input(f"Nuevo email ({cliente[3]}): ").strip() or cliente[3]

                loading("Actualizando cliente")
                cursor.execute("""
                    UPDATE clientes SET nombre = ?, apellido = ?, email = ? WHERE identificador = ?;
                """, (nombre, apellidos, email, identificador))
                conexion.commit()
                print(f"{GREEN}✔ Cliente actualizado correctamente.{RESET}")
            else:
                print(f"{RED}❌ Cliente no encontrado.{RESET}")

        elif opcion == 4:
            clear()
            print(center(f"{BOLD}{RED}❌ Eliminar cliente ❌{RESET}"))
            identificador = input("Introduce el ID del cliente a eliminar: ").strip()
            cursor.execute("SELECT * FROM clientes WHERE identificador = ?;", (identificador,))
            cliente = cursor.fetchone()

            if cliente:
                confirmacion = input(f"{YELLOW}¿Seguro que quieres eliminar a {cliente[1]} {cliente[2]}? (s/n): {RESET}").lower()
                if confirmacion == 's':
                    loading("Eliminando cliente")
                    cursor.execute("DELETE FROM clientes WHERE identificador = ?;", (identificador,))
                    conexion.commit()
                    print(f"{GREEN}✔ Cliente eliminado correctamente.{RESET}")
                else:
                    print(f"{YELLOW}❗ Eliminación cancelada.{RESET}")
            else:
                print(f"{RED}❌ Cliente no encontrado.{RESET}")

        elif opcion == 5:
            clear()
            print(center(f"{CYAN}Gracias por usar el sistema. ¡Hasta luego! 👋{RESET}"))
            break
        else:
            print(f"{RED}❌ Opción inválida. Selecciona entre 1 y 5.{RESET}")

        input("\nPulsa Enter para continuar...")

    cursor.close()
    conexion.close()

if __name__ == "__main__":
    main()

