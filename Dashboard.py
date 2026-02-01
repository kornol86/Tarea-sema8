import os
import subprocess

# ===== COLORES ANSI =====
AZUL = "\033[94m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
CIAN = "\033[96m"
RESET = "\033[0m"
NEGRITA = "\033[1m"

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n{CIAN}{NEGRITA}--- Código de {ruta_script} ---{RESET}\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(f"{ROJO}El archivo no se encontró.{RESET}")
        return None
    except Exception as e:
        print(f"{ROJO}Error al leer el archivo: {e}{RESET}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Linux / macOS
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"{ROJO}Error al ejecutar el código: {e}{RESET}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print(f"\n{AZUL}{NEGRITA}===== MENÚ PRINCIPAL - DASHBOARD ====={RESET}")
        for key, valor in unidades.items():
            print(f"{VERDE}{key} - {valor}{RESET}")
        print(f"{ROJO}0 - Salir{RESET}")

        eleccion_unidad = input(f"{AMARILLO}Elige una opción: {RESET}")

        if eleccion_unidad == '0':
            print(f"{ROJO}Saliendo del programa...{RESET}")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print(f"{ROJO}Opción no válida.{RESET}")

def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print(f"\n{AZUL}{NEGRITA}--- SUBMENÚ: Subcarpetas ---{RESET}")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{VERDE}{i} - {carpeta}{RESET}")
        print(f"{ROJO}0 - Regresar al menú principal{RESET}")

        eleccion = input(f"{AMARILLO}Elige una opción: {RESET}")

        if eleccion == '0':
            break
        try:
            indice = int(eleccion) - 1
            if 0 <= indice < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
            else:
                print(f"{ROJO}Opción no válida.{RESET}")
        except ValueError:
            print(f"{ROJO}Entrada inválida.{RESET}")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta)
               if f.is_file() and f.name.endswith('.py')]

    while True:
        print(f"\n{AZUL}{NEGRITA}--- SCRIPTS DISPONIBLES ---{RESET}")
        for i, script in enumerate(scripts, start=1):
            print(f"{CIAN}{i} - {script}{RESET}")

        print(f"{VERDE}0 - Regresar al submenú{RESET}")
        print(f"{ROJO}9 - Menú principal{RESET}")

        eleccion = input(f"{AMARILLO}Selecciona un script: {RESET}")

        if eleccion == '0':
            break
        elif eleccion == '9':
            return
        try:
            indice = int(eleccion) - 1
            if 0 <= indice < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                codigo = mostrar_codigo(ruta_script)

                if codigo:
                    ejecutar = input(f"{AMARILLO}¿Ejecutar script? (1=Sí / 0=No): {RESET}")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
                    else:
                        print(f"{ROJO}Script no ejecutado.{RESET}")

                input(f"\n{CIAN}Presiona Enter para continuar...{RESET}")
            else:
                print(f"{ROJO}Opción no válida.{RESET}")
        except ValueError:
            print(f"{ROJO}Entrada inválida.{RESET}")

# ===== EJECUCIÓN =====
if __name__ == "__main__":
    mostrar_menu()
