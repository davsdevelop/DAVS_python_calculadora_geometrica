"""
╔══════════════════════════════════════════════════════════════╗
║           DAVS CALCULADORA GEOMETRICA  v1.0                  ║
║                  Python Pure · Terminal UI                    ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import math


# ─────────────────────────────────────────────
#  UTILIDADES DE INTERFAZ
# ─────────────────────────────────────────────

WIDTH = 64

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def box_top():
    print("╔" + "═" * (WIDTH - 2) + "╗")

def box_bottom():
    print("╚" + "═" * (WIDTH - 2) + "╝")

def box_mid():
    print("╠" + "═" * (WIDTH - 2) + "╣")

def box_line(text="", align="center"):
    if align == "center":
        inner = text.center(WIDTH - 4)
    elif align == "left":
        inner = " " + text.ljust(WIDTH - 5)
    else:
        inner = text.rjust(WIDTH - 5) + " "
    print("║ " + inner + " ║")

def box_raw(left, right):
    """Imprime una línea del box con contenido izquierdo y derecho ya formateados."""
    inner = left + right
    # pad hasta WIDTH-4
    inner = inner.ljust(WIDTH - 4)
    print("║ " + inner + " ║")

def print_header():
    clear()
    box_top()
    box_line()
    box_line("DAVS  CALCULADORA  GEOMETRICA", align="center")
    box_line("v1.0  ·  Python Pure  ·  ASCII Mode", align="center")
    box_line()
    box_mid()

def print_footer():
    box_bottom()
    print()

def print_section(titulo):
    """Imprime un separador de sección dentro del box."""
    box_line(f"  ▸ {titulo}", align="left")
    box_mid()

def input_prompt(label):
    print("║" + " " * (WIDTH - 2) + "║")
    prompt = f"  ▶  {label}: "
    print("║ " + prompt, end="")
    value = input()
    return value

def print_result_block(titulo, resultado, unidad=""):
    box_mid()
    box_line(f"  RESULTADO  ──  {titulo}", align="left")
    box_mid()
    box_line()
    result_str = f"  ► {resultado} {unidad}".strip()
    box_line(result_str, align="left")
    box_line()

def get_float(label):
    """Solicita un número flotante positivo al usuario."""
    while True:
        raw = input_prompt(label)
        try:
            val = float(raw)
            if val <= 0:
                box_line("  ⚠  El valor debe ser mayor que 0.", align="left")
            else:
                return val
        except ValueError:
            box_line("  ⚠  Ingresa un número válido.", align="left")

def wait_enter():
    print("║" + " " * (WIDTH - 2) + "║")
    box_line("  Presiona ENTER para continuar...", align="left")
    box_bottom()
    input()


# ─────────────────────────────────────────────
#  ASCII ART DE FIGURAS  (mini = para menu,
#                         full = para resultado)
# ─────────────────────────────────────────────

def mini_cuadrado():
    """Figura pequeña de 3 líneas para el menú."""
    return [
        "┌───┐",
        "│   │",
        "└───┘",
    ]

# Para agregar nueva figura: crea mini_FIGURA() que retorne lista de 3 strings


# ─────────────────────────────────────────────
#  OPCION DE MENU CON FIGURA INLINE
# ─────────────────────────────────────────────

def print_menu_option_figura(key, label, mini_art):
    """
    Imprime una opción de menú con la figura mini al lado derecho.
    mini_art: lista de 3 strings (salida de mini_FIGURA())
    """
    # La figura ocupa la parte derecha (ancho fijo 8 chars)
    FIG_W = 8
    label_w = WIDTH - 4 - FIG_W - 1   # espacio para el label

    label_lines = [
        f"  [{key}]  {label}",
        "",
        "",
    ]

    for i, fig_row in enumerate(mini_art):
        left  = label_lines[i].ljust(label_w)
        right = fig_row.ljust(FIG_W)
        print("║ " + left + " " + right + " ║")

def print_menu_option(key, label, description=""):
    if description:
        text = f"  [{key}]  {label:<20}  {description}"
    else:
        text = f"  [{key}]  {label}"
    box_line(text, align="left")


# ─────────────────────────────────────────────
#  CALCULOS: CUADRADO
# ─────────────────────────────────────────────

def calcular_area_cuadrado():
    print_header()
    box_line("  CUADRADO  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = lado²", align="left")
    box_mid()

    lado = get_float("Lado (l)")
    area = lado ** 2

    print_result_block("Área del Cuadrado", f"{area:.6g}", "u²")

    wait_enter()


# ─────────────────────────────────────────────
#  MENUS DE CALCULOS POR FIGURA
# ─────────────────────────────────────────────

def menu_calculos_cuadrado():
    """
    Para agregar un nuevo cálculo al cuadrado:
    1. Crea la función   calcular_X_cuadrado()  arriba
    2. Agrega una entrada en el dict  opciones  abajo
    """
    opciones = {
        "1": ("Área",      "A = l²",  calcular_area_cuadrado),
        # "2": ("Perímetro", "P = 4·l", calcular_perimetro_cuadrado),
        # "3": ("Diagonal",  "d = l√2", calcular_diagonal_cuadrado),
    }

    while True:
        print_header()
        box_line("  CUADRADO  ──  Selecciona cálculo", align="left")
        box_mid()
        for key, (nombre, formula, _) in opciones.items():
            print_menu_option(key, nombre, formula)
        print_menu_option("0", "Volver al menú principal")
        print_footer()

        seleccion = input("  Opción: ").strip()

        if seleccion == "0":
            break
        elif seleccion in opciones:
            opciones[seleccion][2]()
        else:
            print("  ⚠  Opción no válida.")


# ─────────────────────────────────────────────
#  MENU PRINCIPAL DE FIGURAS
# ─────────────────────────────────────────────

def menu_principal():
    """
    Para agregar una nueva figura:
    1. Crea mini_FIGURA() con 3 líneas de ASCII
    2. Crea calcular_X_FIGURA() y menu_calculos_FIGURA()
    3. Agrégala al dict  figuras_2d  o  figuras_3d  abajo
    """
    # (nombre, menu_fn, mini_art_fn)
    figuras_2d = {
        "1": ("Cuadrado",   menu_calculos_cuadrado, mini_cuadrado),
        # "2": ("Rectángulo", menu_calculos_rectangulo, mini_rectangulo),
        # "3": ("Triángulo",  menu_calculos_triangulo,  mini_triangulo),
        # "4": ("Círculo",    menu_calculos_circulo,    mini_circulo),
    }

    figuras_3d = {
        # "5": ("Cubo",       menu_calculos_cubo,    mini_cubo),
        # "6": ("Esfera",     menu_calculos_esfera,  mini_esfera),
    }

    # Mapa unificado para buscar selección
    todas = {**figuras_2d, **figuras_3d}

    while True:
        print_header()

        # ── Sección 2D ──
        print_section("Figuras Geométricas 2D  (Planas)")
        if figuras_2d:
            for key, (nombre, _, mini_fn) in figuras_2d.items():
                print_menu_option_figura(key, nombre, mini_fn())
        else:
            box_line("  (próximamente)", align="left")
        box_mid()

        # ── Sección 3D ──
        print_section("Figuras Geométricas 3D  (Sólidos)")
        if figuras_3d:
            for key, (nombre, _, mini_fn) in figuras_3d.items():
                print_menu_option_figura(key, nombre, mini_fn())
        else:
            box_line("  (próximamente)", align="left")
        box_mid()

        print_menu_option("0", "Salir")
        print_footer()

        seleccion = input("  Opción: ").strip()

        if seleccion == "0":
            clear()
            box_top()
            box_line()
            box_line("Gracias por usar DAVS Calculadora Geométrica", align="center")
            box_line()
            box_bottom()
            print()
            break
        elif seleccion in todas:
            todas[seleccion][1]()
        else:
            print("  ⚠  Opción no válida. Intenta de nuevo.")


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    menu_principal()