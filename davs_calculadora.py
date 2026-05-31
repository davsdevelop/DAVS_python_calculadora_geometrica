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


# **********************************************************************************************************************************
# ****************** FIGURAS **************************
# **********************************************************************************************************************************

def mini_cuadrado():
    """Figura pequeña de 3 líneas para el menú."""
    return [
        "┌───┐",
        "│   │",
        "└───┘",
    ]

def mini_rectangulo():
    """Figura pequeña de 3 líneas para el menú."""
    return [
        "┌──────┐",
        "│      │",
        "└──────┘",
    ]

def mini_triangulo_equilatero():
    """Figura pequeña de 3 líneas que representa un triángulo."""
    return [
        "   /\  ",
        "  /  \  ",
        " /____\ "
    ]

def mini_triangulo_isosceles():
    """Figura pequeña de 3 líneas (triángulo rectángulo isósceles)."""
    return [
        " |\   ",
        " | \   ",
        " |__\  ",
    ]


def mini_triangulo_escaleno():
    """Figura pequeña de 3 líneas que representa un triángulo escaleno."""
    return [
        "  /\     ",
        " /    \   ",
        "/________\ "
    ]

def mini_triangulo_rectangulo():
    """Figura pequeña de 3 líneas que representa un triángulo rectángulo."""
    return [
        " |\        ",
        " |   \     ",
        " |______\   "
    ]

def mini_triangulo_acutangulo():
    """Figura pequeña de 3 líneas (triángulo acutángulo asimétrico)."""
    return [
        "     /\     ",
        "    /  \    ",
        "   /____\   "
    ]


def mini_triangulo_obtusangulo():
    """Figura pequeña de 3 líneas que representa un triángulo obtusángulo."""
    return [
        "      /\      ",
        "    _/  \_    ",
        " _/________\_ "
    ]

def mini_rombo():
    """Figura pequeña de 3 líneas que representa un rombo."""
    return [
        "  /\   ",
        " /  \  ",
        "  \/   "
    ]

def mini_romboide():
    """Figura pequeña de 3 líneas que representa un romboide."""
    return [
        "  /----/ ",
        " /    /  ",
        "/----/   "
    ]

def mini_trapecio():
    """Figura pequeña de 3 líneas que representa un trapecio."""
    return [
        " /----\ ",
        "/      \\",
        "--------"
    ]

def mini_deltoide():
    """Figura pequeña de 3 líneas que representa un deltoide (cometa)."""
    return [
        "  /\   ",
        " /  \  ",
        "  \/   "
    ]

def mini_poligono_regular():
    """Figura pequeña de 3 líneas que representa un hexágono."""
    return [
        " /--\  ",
        "|    | ",
        " \--/  "
    ]

def mini_circulo():
    """Figura pequeña de 3 líneas que representa un círculo."""
    return [
        "  ( )  ",
        " (   ) ",
        "  ( )  "
    ]

def mini_sector_circular():
    """Figura pequeña de 3 líneas que representa un sector circular."""
    return [
        " /^^\\  ",
        "|  /   ",
        " \\/    "
    ]

def mini_corona_circular():
    """Figura pequeña de 3 líneas que representa una corona circular."""
    return [
        " (( )) ",
        "(( o ))",
        " (( )) "
    ]

def mini_elipse():
    """Figura pequeña de 3 líneas que representa una elipse."""
    return [
        " /----\\ ",
        "|      |",
        " \\----/ "
    ]

def mini_cubo():
    """Figura pequeña de 3 líneas que representa un cubo."""
    return [
        " +--+  ",
        "/  /|  ",
        "+--+ + "
    ]

def mini_prisma_rectangular():
    """Figura pequeña de 3 líneas que representa un prisma rectangular."""
    return [
        " +---+ ",
        "/   /| ",
        "+---+ +"
    ]

def mini_prisma_regular():
    """Figura pequeña de 3 líneas que representa un prisma regular."""
    return [
        "  /\\   ",
        " /--\\  ",
        "/____\\ "
    ]

def mini_cilindro():
    """Figura pequeña de 3 líneas que representa un cilindro."""
    return [
        " /^^\\  ",
        "|    | ",
        " \\__/  "
    ]

def mini_esfera():
    """Figura pequeña de 3 líneas que representa una esfera."""
    return [
        "  ***  ",
        " *   * ",
        "  ***  "
    ]

def mini_cono():
    """Figura pequeña de 3 líneas que representa un cono."""
    return [
        "   /\\  ",
        "  /  \\ ",
        " /____\\"
    ]

def mini_piramide():
    """Figura pequeña de 3 líneas que representa una pirámide regular."""
    return [
        "   /\\  ",
        "  /  \\ ",
        " /----\\"
    ]

def mini_tronco_cono():
    """Figura pequeña de 3 líneas que representa un tronco de cono."""
    return [
        "  /--\\ ",
        " /    \\",
        "/______\\"
    ]

def mini_toroide():
    """Figura pequeña de 3 líneas que representa un toroide (dona)."""
    return [
        " (( )) ",
        "(( o ))",
        " (( )) "
    ]

def mini_tetraedro():
    """Figura pequeña de 3 líneas que representa un tetraedro regular."""
    return [
        "   /\\  ",
        "  /  \\ ",
        " /--__\\"
    ]

def mini_octaedro():
    """Figura pequeña de 3 líneas que representa un octaedro regular."""
    return [
        "  /\\   ",
        " /  \\  ",
        "  \\/   "
    ]

def mini_dodecaedro():
    """Figura pequeña de 3 líneas que representa un dodecaedro regular."""
    return [
        " /--\\  ",
        "|    | ",
        " \\--/  "
    ]

def mini_icosaedro():
    """Figura pequeña de 3 líneas que representa un icosaedro regular."""
    return [
        "  /\\   ",
        " /\\/\\  ",
        "/____\\ "
    ]



# ─────────────────────────────────────────────
#  OPCION DE MENU CON FIGURA INLINE
# ─────────────────────────────────────────────

def print_menu_option_figura(key, label, mini_art):
    """
    Imprime una opción de menú con la figura mini al lado derecho.
    mini_art: lista de 3 strings (salida de mini_FIGURA())
    """
    # La figura ocupa la parte derecha (ancho fijo 8 chars)
    FIG_W = 14
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










# **********************************************************************************************************************************
# ****************** CALCULOS **************************
# **********************************************************************************************************************************

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

def calcular_perimetro_cuadrado():
    print_header()
    box_line("  CUADRADO  ──  Perímetro", align="left")
    box_mid()
    box_line("  Fórmula:  P = 4 * lado", align="left")
    box_mid()
    lado = get_float("Lado (l)")
    perimetro = lado * 4
    print_result_block("Perímetro del Cuadrado", f"{perimetro:.6g}", "u")
    wait_enter()

def calcular_diagonal_cuadrado():
    print_header()
    box_line("  CUADRADO  ──  Diagonal", align="left")
    box_mid()
    box_line("  Fórmula:  d = lado * √2", align="left")
    box_mid()
    lado = get_float("Lado (l)")
    diagonal = lado * math.sqrt(2)
    print_result_block("Diagonal del Cuadrado", f"{diagonal:.6g}", "u")
    wait_enter()



# ─────────────────────────────────────────────
#  CALCULOS: RECTANGULO
# ─────────────────────────────────────────────
def calcular_area_rectangulo():
    print_header()
    box_line("  RECTÁNGULO  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = b * h", align="left")
    box_mid()
    lado_b = get_float("Lado (l-b)")
    lado_h = get_float("Lado (l-h)")
    area = lado_b * lado_h
    print_result_block("Área del Rectángulo", f"{area:.6g}", "u²")
    wait_enter()

def calcular_perimetro_rectangulo():
    print_header()
    box_line("  RECTÁNGULO  ──  Perímetro", align="left")
    box_mid()
    box_line("  Fórmula:  P = 2 * (b + h)", align="left")
    box_mid()
    lado_b = get_float("Lado (l-b)")
    lado_h = get_float("Lado (l-h)")
    perimetro = 2 * (lado_b + lado_h)
    print_result_block("Perímetro del Rectángulo", f"{perimetro:.6g}", "u")
    wait_enter()

def calcular_diagonal_rectangulo():
    print_header()
    box_line("  RECTÁNGULO  ──  Diagonal", align="left")
    box_mid()
    box_line("  Fórmula:  d= √l-b² + l-h²", align="left")
    box_mid()
    lado_b = get_float("Lado (l-b)")
    lado_h = get_float("Lado (l-h)")
    diagonal = math.sqrt((lado_b ** 2) + (lado_h ** 2))
    # CORRECCIÓN: título corregido de "Perímetro" a "Diagonal"
    print_result_block("Diagonal del Rectángulo", f"{diagonal:.6g}", "u")
    wait_enter()



# ─────────────────────────────────────────────
#  CALCULOS: TRIANGULO EQUILATERO
# ─────────────────────────────────────────────
def calcular_area_triangulo_equilatero():
    print_header()
    box_line("  TRIÁNGULO EQUILÁTERO  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = ((√3)/4) * l²", align="left")
    box_mid()
    lado = get_float("Lado l")
    area = (math.sqrt(3)/4) * lado ** 2
    print_result_block("Área del Triángulo Equilátero", f"{area:.6g}", "u²")
    wait_enter()

def calcular_perimetro_triangulo_equilatero():
    print_header()
    box_line("  TRIÁNGULO EQUILÁTERO  ──  Perímetro", align="left")
    box_mid()
    box_line("  Fórmula:  P = 3 * l", align="left")
    box_mid()
    lado = get_float("Lado l")
    perimetro = 3 * lado
    print_result_block("Perímetro del Triángulo Equilátero", f"{perimetro:.6g}", "u")
    wait_enter()

def calcular_altura_triangulo_equilatero():
    print_header()
    box_line("  TRIÁNGULO EQUILÁTERO  ──  Altura", align="left")
    box_mid()
    # CORRECCIÓN: fórmula corregida de "((√3)2)" a "(√3 / 2)"
    box_line("  Fórmula:  h = (√3 / 2) * l", align="left")
    box_mid()
    lado = get_float("Lado l")
    altura = (math.sqrt(3)/2) * lado
    print_result_block("Altura del Triángulo Equilátero", f"{altura:.6g}", "u")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: TRIANGULO ISÓSCELES
# ─────────────────────────────────────────────
def calcular_altura_triangulo_isosceles():
    print_header()
    box_line("  TRIÁNGULO ISÓSCELES  ──  Altura", align="left")
    box_mid()
    box_line("  Fórmula:  h = √(a² - (b²/4))", align="left")
    box_mid()
    lado_a = get_float("Lado l-a")
    lado_base = get_float("Lado l-base")
    altura = math.sqrt((lado_a ** 2) - ((lado_base ** 2) / 4))
    # CORRECCIÓN: título corregido de "Área" a "Altura"
    print_result_block("Altura del Triángulo Isósceles", f"{altura:.6g}", "u")
    wait_enter()

def calcular_perimetro_triangulo_isosceles():
    print_header()
    box_line("  TRIÁNGULO ISÓSCELES  ──  Perímetro", align="left")
    box_mid()
    box_line("  Fórmula:  P = (2*a) + b", align="left")
    box_mid()
    lado_a = get_float("Lado l-a")
    lado_base = get_float("Lado l-base")
    perimetro = (2 * lado_a) + lado_base
    print_result_block("Perímetro del Triángulo Isósceles", f"{perimetro:.6g}", "u")
    wait_enter()

def calcular_area_triangulo_isosceles():
    print_header()
    box_line("  TRIÁNGULO ISÓSCELES  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = (b * h) / 2", align="left")
    box_mid()
    lado_base = get_float("Lado l-base")
    altura = get_float("altura h")
    # CORRECCIÓN: variable renombrada a "area" para no sobreescribir "altura"
    area = (lado_base * altura) / 2
    # CORRECCIÓN: título corregido de "Altura del Triángulo Equilátero" a "Área del Triángulo Isósceles"
    print_result_block("Área del Triángulo Isósceles", f"{area:.6g}", "u²")
    wait_enter()



# ─────────────────────────────────────────────
#  CALCULOS: TRIANGULO ESCALENO
# ─────────────────────────────────────────────
def calcular_perimetro_triangulo_escaleno():
    print_header()
    box_line("  TRIÁNGULO ESCALENO  ──  Perímetro", align="left")
    box_mid()
    box_line("  Fórmula:  P = a + b + c", align="left")
    box_mid()
    lado_a = get_float("Lado l-a")
    lado_b = get_float("Lado l-b")
    lado_c = get_float("Lado l-c")
    perimetro = lado_a + lado_b + lado_c
    print_result_block("Perímetro del Triángulo Escaleno", f"{perimetro:.6g}", "u")
    wait_enter()

def calcular_area_triangulo_escaleno():
    print_header()
    box_line("  TRIÁNGULO ESCALENO  ──  Área (Herón)", align="left")
    box_mid()
    box_line("  Fórmula:  A = √(s*((s-a)*(s-b)*(s-c)))", align="left")
    box_mid()
    lado_a = get_float("Lado l-a")
    lado_b = get_float("Lado l-b")
    lado_c = get_float("Lado l-c")
    # CORRECCIÓN: semiperímetro calculado automáticamente en vez de pedirlo al usuario
    lado_s = (lado_a + lado_b + lado_c) / 2
    # CORRECCIÓN: validación para evitar error matemático con lados inválidos
    factor = lado_s * ((lado_s - lado_a) * (lado_s - lado_b) * (lado_s - lado_c))
    if factor <= 0:
        box_mid()
        box_line("  ⚠  Los lados ingresados no forman un triángulo válido.", align="left")
        box_line()
        wait_enter()
        return
    area = math.sqrt(factor)
    print_result_block("Área del Triángulo Escaleno", f"{area:.6g}", "u²")
    wait_enter()

def calcular_angulo_triangulo_escaleno():
    print_header()
    box_line("  TRIÁNGULO ESCALENO  ──  Angulo α (Ley Cosenos)", align="left")
    box_mid()
    box_line("  Fórmula:  cos(α) = (b² + c² - a² ) / 2bc", align="left")
    box_mid()
    lado_a = get_float("Lado l-a")
    lado_b = get_float("Lado l-b")
    lado_c = get_float("Lado l-c")
    angulo_a = ((lado_b ** 2) + (lado_c ** 2) - (lado_a ** 2)) / (2 * lado_b * lado_c)
    angulo_radian = math.acos(angulo_a)
    angulo = math.degrees(angulo_radian)
    print_result_block("Angulo del Triángulo Escaleno", f"{angulo:.6g}", "°")
    wait_enter()



# ─────────────────────────────────────────────
#  CALCULOS: TRIANGULO RECTÁNGULO
# ─────────────────────────────────────────────
def calcular_perimetro_triangulo_rectangulo():
    print_header()
    box_line("  TRIÁNGULO RECTÁNGULO  ──  Perímetro", align="left")
    box_mid()
    box_line("  Fórmula:  P = a + b + c", align="left")
    box_mid()
    lado_a = get_float("Lado l-a")
    lado_b = get_float("Lado l-b")
    lado_c = get_float("Lado l-c")
    perimetro = lado_a + lado_b + lado_c
    print_result_block("Perímetro del Triángulo Rectángulo", f"{perimetro:.6g}", "u")
    wait_enter()

def calcular_area_triangulo_rectangulo():
    print_header()
    box_line("  TRIÁNGULO RECTÁNGULO  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = (a * b) / 2", align="left")
    box_mid()
    lado_a = get_float("Lado l-a")
    lado_b = get_float("Lado l-b")
    area = (lado_a * lado_b) / 2
    print_result_block("Área del Triángulo Rectángulo", f"{area:.6g}", "u²")
    wait_enter()

def calcular_hipotenusa_triangulo_rectangulo():
    print_header()
    box_line("  TRIÁNGULO RECTÁNGULO  ──  Hipotenusa", align="left")
    box_mid()
    box_line("  Fórmula:  c = √(a² + b²)", align="left")
    box_mid()
    lado_a = get_float("Lado l-a")
    lado_b = get_float("Lado l-b")
    hipotenusa = math.sqrt((lado_a ** 2) + (lado_b ** 2))
    # CORRECCIÓN: unidad corregida de "°" a "u" (es una longitud, no un ángulo)
    print_result_block("Hipotenusa del Triángulo Rectángulo", f"{hipotenusa:.6g}", "u")
    wait_enter()



# ─────────────────────────────────────────────
#  CALCULOS: TRIANGULO ACUTÁNGULO
# ─────────────────────────────────────────────
def calcular_suma_angulos_internos_triangulo_acutangulo():
    print_header()
    box_line("  TRIÁNGULO ACUTÁNGULO  ──  Suma Ángulos Internos", align="left")
    box_mid()
    box_line("  Fórmula:  Σ = α + β + γ = 180°", align="left")
    box_mid()

    # 1. Función auxiliar para manejar el input híbrido (float o "x")
    def obtener_valor(mensaje):
        while True:
            # Nota: Quizás debas ajustar el 'input' para que encaje con el estilo de tu menú
            entrada = input(f"  {mensaje}: ").strip().lower()
            if entrada == "x":
                return "x"
            try:
                return float(entrada)
            except ValueError:
                print("  [!] Opción inválida. Ingresa un número válido o 'x'.")

    angulo_a = obtener_valor("Angulo α (x si es incognita)")
    angulo_b = obtener_valor("Angulo β (x si es incognita)")
    angulo_y = obtener_valor("Angulo γ (x si es incognita)")

    # 2. Validación de seguridad: Contar cuántas "x" ingresó el usuario
    cantidad_incognitas = [angulo_a, angulo_b, angulo_y].count("x")

    if cantidad_incognitas != 1:
        print("  [!] Error: Debes ingresar exactamente una 'x' para calcular el ángulo faltante.")
        wait_enter()
        return

    # 3. Lógica de cálculo
    if angulo_a == "x":
        angulo = 180 - angulo_b - angulo_y
        nombre_incognita = "α"
    elif angulo_b == "x":
        angulo = 180 - angulo_a - angulo_y
        nombre_incognita = "β"
    elif angulo_y == "x":
        angulo = 180 - angulo_a - angulo_b
        nombre_incognita = "γ"

    # 4. Mostrar el resultado (ajusté el título para que refleje que calculaste el ángulo faltante)
    print_result_block(f"Valor del Ángulo Faltante ({nombre_incognita})", f"{angulo:.6g}", "°")
    wait_enter()


def calcular_area_triangulo_acutangulo():
    print_header()
    box_line("  TRIÁNGULO ACUTÁNGULO  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = (b * h) / 2", align="left")
    box_mid()
    lado_base = get_float("Lado l-base")
    altura = get_float("altura")
    area = (lado_base * altura) / 2
    print_result_block("Área del Triángulo Acutángulo", f"{area:.6g}", "u²")
    wait_enter()




# ─────────────────────────────────────────────
#  CALCULOS: TRIANGULO OBTUSÁNGULO
# ─────────────────────────────────────────────
def calcular_angulo_obtuso_triangulo_obtusangulo():
    print_header()
    box_line("  TRIÁNGULO OBTUSÁNGULO  ──  Ángulo Faltante", align="left")
    box_mid()
    box_line("  Regla:     Un ángulo debe ser mayor a 90°", align="left")
    box_line("  Fórmula:   Σ = α + β + γ = 180°", align="left")
    box_mid()

    # Función auxiliar para manejar el input (número o "x")
    def obtener_valor(mensaje):
        while True:
            entrada = input(f"  {mensaje}: ").strip().lower()
            if entrada == "x":
                return "x"
            try:
                return float(entrada)
            except ValueError:
                print("  [!] Opción inválida. Ingresa un número válido o 'x'.")

    angulo_a = obtener_valor("Angulo α (x si es incognita)")
    angulo_b = obtener_valor("Angulo β (x si es incognita)")
    angulo_y = obtener_valor("Angulo γ (x si es incognita)")

    # Validar que solo haya una incógnita
    cantidad_incognitas = [angulo_a, angulo_b, angulo_y].count("x")

    if cantidad_incognitas != 1:
        print("  [!] Error: Debes ingresar exactamente una 'x' para calcular el ángulo faltante.")
        wait_enter()
        return

    # Calcular el ángulo faltante
    if angulo_a == "x":
        angulo = 180 - angulo_b - angulo_y
        nombre_incognita = "α"
        angulos_totales = [angulo, angulo_b, angulo_y]
    elif angulo_b == "x":
        angulo = 180 - angulo_a - angulo_y
        nombre_incognita = "β"
        angulos_totales = [angulo_a, angulo, angulo_y]
    elif angulo_y == "x":
        angulo = 180 - angulo_a - angulo_b
        nombre_incognita = "γ"
        angulos_totales = [angulo_a, angulo_b, angulo]

    # Validar si el resultado tiene sentido matemático
    if angulo <= 0:
        print("  [!] Error: Los ángulos ingresados superan o igualan los 180°. Geométricamente imposible.")
        wait_enter()
        return

    # Comprobar si realmente es un triángulo obtusángulo (al menos un ángulo > 90)
    es_obtusangulo = any(a > 90 for a in angulos_totales)

    print_result_block(f"Valor del Ángulo {nombre_incognita}", f"{angulo:.6g}", "°")
    
    if not es_obtusangulo:
        print("\n  [i] Nota: Con estos datos, ningún ángulo supera los 90°.")
        print("      Estás calculando un triángulo acutángulo, no uno obtusángulo.")
        
    wait_enter()


def calcular_area_triangulo_obtusangulo():
    print_header()
    box_line("  TRIÁNGULO OBTUSÁNGULO  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = (b * h) / 2", align="left")
    box_mid()
    lado_base = get_float("Lado l-base")
    altura = get_float("altura")
    area = (lado_base * altura) / 2
    # CORRECCIÓN: título corregido de "Acutángulo" a "Obtusángulo"
    print_result_block("Área del Triángulo Obtusángulo", f"{area:.6g}", "u²")
    wait_enter()







# ─────────────────────────────────────────────
#  CALCULOS: ROMBO
# ─────────────────────────────────────────────
def calcular_perimetro_rombo():
    print_header()
    box_line("  ROMBO  ──  Perímetro", align="left")
    box_mid()
    box_line("  Fórmula:  P = 4 * l", align="left")
    box_mid()
    lado = get_float("Lado l")
    perimetro = 4 * lado
    print_result_block("Perímetro del Rombo", f"{perimetro:.6g}", "u")
    wait_enter()

def calcular_area_rombo():
    print_header()
    box_line("  ROMBO  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = (D * d) / 2", align="left")
    box_mid()
    diag_D = get_float("Diagonal mayor D")
    diag_d = get_float("Diagonal menor d")
    area = (diag_D * diag_d) / 2
    print_result_block("Área del Rombo", f"{area:.6g}", "u²")
    wait_enter()

def calcular_angulos_rombo():
    print_header()
    box_line("  ROMBO  ──  Suma Ángulos", align="left")
    box_mid()
    box_line("  Fórmula:  2α + 2β = 360°", align="left")
    box_mid()

    def obtener_valor(mensaje):
        while True:
            entrada = input(f"  {mensaje}: ").strip().lower()
            if entrada == "x":
                return "x"
            try:
                return float(entrada)
            except ValueError:
                print("  [!] Opción inválida. Ingresa un número válido o 'x'.")

    angulo_a = obtener_valor("Ángulo α (x si es incógnita)")
    angulo_b = obtener_valor("Ángulo β (x si es incógnita)")

    cantidad_incognitas = [angulo_a, angulo_b].count("x")

    if cantidad_incognitas != 1:
        print("  [!] Error: Debes ingresar exactamente una 'x'.")
        wait_enter()
        return

    if angulo_a == "x":
        angulo = (360 - 2 * angulo_b) / 2
        nombre_incognita = "α"
    else:
        angulo = (360 - 2 * angulo_a) / 2
        nombre_incognita = "β"

    print_result_block(f"Valor del Ángulo {nombre_incognita}", f"{angulo:.6g}", "°")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: ROMBOIDE
# ─────────────────────────────────────────────
def calcular_perimetro_romboide():
    print_header()
    box_line("  ROMBOIDE  ──  Perímetro", align="left")
    box_mid()
    box_line("  Fórmula:  P = 2 * (a + b)", align="left")
    box_mid()
    lado_a = get_float("Lado a")
    lado_b = get_float("Lado b")
    perimetro = 2 * (lado_a + lado_b)
    print_result_block("Perímetro del Romboide", f"{perimetro:.6g}", "u")
    wait_enter()

def calcular_area_romboide():
    print_header()
    box_line("  ROMBOIDE  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = b * h", align="left")
    box_mid()
    lado_b = get_float("Base b")
    altura = get_float("Altura h")
    area = lado_b * altura
    print_result_block("Área del Romboide", f"{area:.6g}", "u²")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: TRAPECIO
# ─────────────────────────────────────────────
def calcular_area_trapecio():
    print_header()
    box_line("  TRAPECIO  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = ((B + b) * h) / 2", align="left")
    box_mid()
    base_B = get_float("Base mayor B")
    base_b = get_float("Base menor b")
    altura = get_float("Altura h")
    area = ((base_B + base_b) * altura) / 2
    print_result_block("Área del Trapecio", f"{area:.6g}", "u²")
    wait_enter()

def calcular_perimetro_trapecio():
    print_header()
    box_line("  TRAPECIO  ──  Perímetro", align="left")
    box_mid()
    box_line("  Fórmula:  P = B + b + c + d", align="left")
    box_mid()
    base_B = get_float("Base mayor B")
    base_b = get_float("Base menor b")
    lado_c = get_float("Lado c")
    lado_d = get_float("Lado d")
    perimetro = base_B + base_b + lado_c + lado_d
    print_result_block("Perímetro del Trapecio", f"{perimetro:.6g}", "u")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: DELTOIDE (COMETA)
# ─────────────────────────────────────────────
def calcular_area_deltoide():
    print_header()
    box_line("  DELTOIDE (COMETA)  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = (D * d) / 2", align="left")
    box_mid()
    diag_D = get_float("Diagonal mayor D")
    diag_d = get_float("Diagonal menor d")
    area = (diag_D * diag_d) / 2
    print_result_block("Área del Deltoide", f"{area:.6g}", "u²")
    wait_enter()

def calcular_perimetro_deltoide():
    print_header()
    box_line("  DELTOIDE (COMETA)  ──  Perímetro", align="left")
    box_mid()
    box_line("  Fórmula:  P = 2 * (a + b)", align="left")
    box_mid()
    lado_a = get_float("Lado a (lados iguales cortos)")
    lado_b = get_float("Lado b (lados iguales largos)")
    perimetro = 2 * (lado_a + lado_b)
    print_result_block("Perímetro del Deltoide", f"{perimetro:.6g}", "u")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: POLIGONO REGULAR (HEXAGONO)
# ─────────────────────────────────────────────
def calcular_perimetro_poligono_regular():
    print_header()
    box_line("  POLÍGONO REGULAR  ──  Perímetro", align="left")
    box_mid()
    box_line("  Fórmula:  P = n * l", align="left")
    box_mid()
    n = get_float("Número de lados n")
    lado = get_float("Longitud de lado l")
    perimetro = n * lado
    print_result_block("Perímetro del Polígono Regular", f"{perimetro:.6g}", "u")
    wait_enter()

def calcular_area_poligono_regular():
    print_header()
    box_line("  POLÍGONO REGULAR  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = (P * ap) / 2", align="left")
    box_mid()
    perimetro = get_float("Perímetro P")
    apotema = get_float("Apotema ap")
    area = (perimetro * apotema) / 2
    print_result_block("Área del Polígono Regular", f"{area:.6g}", "u²")
    wait_enter()

def calcular_angulo_interno_poligono_regular():
    print_header()
    box_line("  POLÍGONO REGULAR  ──  Ángulo Interno", align="left")
    box_mid()
    box_line("  Fórmula:  α = ((n-2) * 180) / n", align="left")
    box_mid()
    n = get_float("Número de lados n")
    angulo = ((n - 2) * 180) / n
    print_result_block("Ángulo Interno del Polígono Regular", f"{angulo:.6g}", "°")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: CIRCULO
# ─────────────────────────────────────────────
def calcular_perimetro_circulo():
    print_header()
    box_line("  CÍRCULO  ──  Perímetro (Circunferencia)", align="left")
    box_mid()
    box_line("  Fórmula:  P = 2 * π * r", align="left")
    box_mid()
    radio = get_float("Radio r")
    perimetro = 2 * math.pi * radio
    print_result_block("Circunferencia del Círculo", f"{perimetro:.6g}", "u")
    wait_enter()

def calcular_area_circulo():
    print_header()
    box_line("  CÍRCULO  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = π * r²", align="left")
    box_mid()
    radio = get_float("Radio r")
    area = math.pi * radio ** 2
    print_result_block("Área del Círculo", f"{area:.6g}", "u²")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: SECTOR CIRCULAR
# ─────────────────────────────────────────────
def calcular_area_sector_circular():
    print_header()
    box_line("  SECTOR CIRCULAR  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = (α * π * r²) / 360°", align="left")
    box_mid()
    angulo = get_float("Ángulo α (en grados)")
    radio = get_float("Radio r")
    area = (angulo * math.pi * radio ** 2) / 360
    print_result_block("Área del Sector Circular", f"{area:.6g}", "u²")
    wait_enter()

def calcular_arco_sector_circular():
    print_header()
    box_line("  SECTOR CIRCULAR  ──  Longitud de Arco", align="left")
    box_mid()
    box_line("  Fórmula:  L = (α * π * r) / 180°", align="left")
    box_mid()
    angulo = get_float("Ángulo α (en grados)")
    radio = get_float("Radio r")
    arco = (angulo * math.pi * radio) / 180
    print_result_block("Longitud de Arco", f"{arco:.6g}", "u")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: CORONA CIRCULAR
# ─────────────────────────────────────────────
def calcular_area_corona_circular():
    print_header()
    box_line("  CORONA CIRCULAR  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = π * (R² - r²)", align="left")
    box_mid()
    radio_R = get_float("Radio mayor R")
    radio_r = get_float("Radio menor r")
    area = math.pi * (radio_R ** 2 - radio_r ** 2)
    print_result_block("Área de la Corona Circular", f"{area:.6g}", "u²")
    wait_enter()

def calcular_perimetro_corona_circular():
    print_header()
    box_line("  CORONA CIRCULAR  ──  Perímetro Total", align="left")
    box_mid()
    box_line("  Fórmula:  P = 2 * π * (R + r)", align="left")
    box_mid()
    radio_R = get_float("Radio mayor R")
    radio_r = get_float("Radio menor r")
    perimetro = 2 * math.pi * (radio_R + radio_r)
    print_result_block("Perímetro Total de la Corona Circular", f"{perimetro:.6g}", "u")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: ELIPSE
# ─────────────────────────────────────────────
def calcular_area_elipse():
    print_header()
    box_line("  ELIPSE  ──  Área", align="left")
    box_mid()
    box_line("  Fórmula:  A = π * a * b", align="left")
    box_mid()
    semieje_a = get_float("Semieje mayor a")
    semieje_b = get_float("Semieje menor b")
    area = math.pi * semieje_a * semieje_b
    print_result_block("Área de la Elipse", f"{area:.6g}", "u²")
    wait_enter()

def calcular_perimetro_elipse():
    print_header()
    box_line("  ELIPSE  ──  Perímetro (Aprox.)", align="left")
    box_mid()
    box_line("  Fórmula:  P ≈ π*[3(a+b)-√((3a+b)(a+3b))]", align="left")
    box_mid()
    semieje_a = get_float("Semieje mayor a")
    semieje_b = get_float("Semieje menor b")
    perimetro = math.pi * (3 * (semieje_a + semieje_b) - math.sqrt((3 * semieje_a + semieje_b) * (semieje_a + 3 * semieje_b)))
    print_result_block("Perímetro (Aprox.) de la Elipse", f"{perimetro:.6g}", "u")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: CUBO (HEXAEDRO)
# ─────────────────────────────────────────────
def calcular_area_cubo():
    print_header()
    box_line("  CUBO (HEXAEDRO)  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = 6 * l²", align="left")
    box_mid()
    lado = get_float("Lado l")
    area = 6 * lado ** 2
    print_result_block("Área Superficial del Cubo", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_cubo():
    print_header()
    box_line("  CUBO (HEXAEDRO)  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = l³", align="left")
    box_mid()
    lado = get_float("Lado l")
    volumen = lado ** 3
    print_result_block("Volumen del Cubo", f"{volumen:.6g}", "u³")
    wait_enter()

def calcular_diagonal_cubo():
    print_header()
    box_line("  CUBO (HEXAEDRO)  ──  Diagonal Espacial", align="left")
    box_mid()
    box_line("  Fórmula:  D = l * √3", align="left")
    box_mid()
    lado = get_float("Lado l")
    diagonal = lado * math.sqrt(3)
    print_result_block("Diagonal Espacial del Cubo", f"{diagonal:.6g}", "u")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: PRISMA RECTANGULAR
# ─────────────────────────────────────────────
def calcular_area_prisma_rectangular():
    print_header()
    box_line("  PRISMA RECTANGULAR  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = 2(ab + ah + bh)", align="left")
    box_mid()
    lado_a = get_float("Lado a")
    lado_b = get_float("Lado b")
    altura = get_float("Altura h")
    area = 2 * (lado_a * lado_b + lado_a * altura + lado_b * altura)
    print_result_block("Área Superficial del Prisma Rectangular", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_prisma_rectangular():
    print_header()
    box_line("  PRISMA RECTANGULAR  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = a * b * h", align="left")
    box_mid()
    lado_a = get_float("Lado a")
    lado_b = get_float("Lado b")
    altura = get_float("Altura h")
    volumen = lado_a * lado_b * altura
    print_result_block("Volumen del Prisma Rectangular", f"{volumen:.6g}", "u³")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: PRISMA REGULAR GENERAL
# ─────────────────────────────────────────────
def calcular_area_prisma_regular():
    print_header()
    box_line("  PRISMA REGULAR GENERAL  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = 2*A_base + P_base*h", align="left")
    box_mid()
    area_base = get_float("Área de la base A_base")
    perimetro_base = get_float("Perímetro de la base P_base")
    altura = get_float("Altura h")
    area = 2 * area_base + perimetro_base * altura
    print_result_block("Área Superficial del Prisma Regular", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_prisma_regular():
    print_header()
    box_line("  PRISMA REGULAR GENERAL  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = A_base * h", align="left")
    box_mid()
    area_base = get_float("Área de la base A_base")
    altura = get_float("Altura h")
    volumen = area_base * altura
    print_result_block("Volumen del Prisma Regular", f"{volumen:.6g}", "u³")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: CILINDRO
# ─────────────────────────────────────────────
def calcular_area_cilindro():
    print_header()
    box_line("  CILINDRO  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = 2 * π * r * (r + h)", align="left")
    box_mid()
    radio = get_float("Radio r")
    altura = get_float("Altura h")
    area = 2 * math.pi * radio * (radio + altura)
    print_result_block("Área Superficial del Cilindro", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_cilindro():
    print_header()
    box_line("  CILINDRO  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = π * r² * h", align="left")
    box_mid()
    radio = get_float("Radio r")
    altura = get_float("Altura h")
    volumen = math.pi * radio ** 2 * altura
    print_result_block("Volumen del Cilindro", f"{volumen:.6g}", "u³")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: ESFERA
# ─────────────────────────────────────────────
def calcular_area_esfera():
    print_header()
    box_line("  ESFERA  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = 4 * π * r²", align="left")
    box_mid()
    radio = get_float("Radio r")
    area = 4 * math.pi * radio ** 2
    print_result_block("Área Superficial de la Esfera", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_esfera():
    print_header()
    box_line("  ESFERA  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = (4/3) * π * r³", align="left")
    box_mid()
    radio = get_float("Radio r")
    volumen = (4 / 3) * math.pi * radio ** 3
    print_result_block("Volumen de la Esfera", f"{volumen:.6g}", "u³")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: CONO
# ─────────────────────────────────────────────
def calcular_generatriz_cono():
    print_header()
    box_line("  CONO  ──  Generatriz", align="left")
    box_mid()
    box_line("  Fórmula:  g = √(r² + h²)", align="left")
    box_mid()
    radio = get_float("Radio r")
    altura = get_float("Altura h")
    generatriz = math.sqrt(radio ** 2 + altura ** 2)
    print_result_block("Generatriz del Cono", f"{generatriz:.6g}", "u")
    wait_enter()

def calcular_area_cono():
    print_header()
    box_line("  CONO  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = π * r * (r + g)", align="left")
    box_mid()
    radio = get_float("Radio r")
    altura = get_float("Altura h")
    generatriz = math.sqrt(radio ** 2 + altura ** 2)
    area = math.pi * radio * (radio + generatriz)
    print_result_block("Área Superficial del Cono", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_cono():
    print_header()
    box_line("  CONO  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = (π * r² * h) / 3", align="left")
    box_mid()
    radio = get_float("Radio r")
    altura = get_float("Altura h")
    volumen = (math.pi * radio ** 2 * altura) / 3
    print_result_block("Volumen del Cono", f"{volumen:.6g}", "u³")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: PIRAMIDE REGULAR
# ─────────────────────────────────────────────
def calcular_area_piramide():
    print_header()
    box_line("  PIRÁMIDE REGULAR  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = A_base + (P_base * Ap) / 2", align="left")
    box_mid()
    area_base = get_float("Área de la base A_base")
    perimetro_base = get_float("Perímetro de la base P_base")
    apotema = get_float("Apotema lateral Ap")
    area = area_base + (perimetro_base * apotema) / 2
    print_result_block("Área Superficial de la Pirámide Regular", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_piramide():
    print_header()
    box_line("  PIRÁMIDE REGULAR  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = (A_base * h) / 3", align="left")
    box_mid()
    area_base = get_float("Área de la base A_base")
    altura = get_float("Altura h")
    volumen = (area_base * altura) / 3
    print_result_block("Volumen de la Pirámide Regular", f"{volumen:.6g}", "u³")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: TRONCO DE CONO
# ─────────────────────────────────────────────
def calcular_area_tronco_cono():
    print_header()
    box_line("  TRONCO DE CONO  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = π*[R²+r²+g(R+r)]", align="left")
    box_mid()
    radio_R = get_float("Radio mayor R")
    radio_r = get_float("Radio menor r")
    altura = get_float("Altura h")
    generatriz = math.sqrt((radio_R - radio_r) ** 2 + altura ** 2)
    area = math.pi * (radio_R ** 2 + radio_r ** 2 + generatriz * (radio_R + radio_r))
    print_result_block("Área Superficial del Tronco de Cono", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_tronco_cono():
    print_header()
    box_line("  TRONCO DE CONO  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = (π*h/3)*[R²+r²+(R*r)]", align="left")
    box_mid()
    radio_R = get_float("Radio mayor R")
    radio_r = get_float("Radio menor r")
    altura = get_float("Altura h")
    volumen = (math.pi * altura / 3) * (radio_R ** 2 + radio_r ** 2 + radio_R * radio_r)
    print_result_block("Volumen del Tronco de Cono", f"{volumen:.6g}", "u³")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: TOROIDE (DONA)
# ─────────────────────────────────────────────
def calcular_area_toroide():
    print_header()
    box_line("  TOROIDE (DONA)  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = 4 * π² * R * r", align="left")
    box_mid()
    radio_R = get_float("Radio mayor R (centro al tubo)")
    radio_r = get_float("Radio menor r (del tubo)")
    area = 4 * math.pi ** 2 * radio_R * radio_r
    print_result_block("Área Superficial del Toroide", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_toroide():
    print_header()
    box_line("  TOROIDE (DONA)  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = 2 * π² * R * r²", align="left")
    box_mid()
    radio_R = get_float("Radio mayor R (centro al tubo)")
    radio_r = get_float("Radio menor r (del tubo)")
    volumen = 2 * math.pi ** 2 * radio_R * radio_r ** 2
    print_result_block("Volumen del Toroide", f"{volumen:.6g}", "u³")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: TETRAEDRO REGULAR
# ─────────────────────────────────────────────
def calcular_area_tetraedro():
    print_header()
    box_line("  TETRAEDRO REGULAR  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = √3 * a²", align="left")
    box_mid()
    arista = get_float("Arista a")
    area = math.sqrt(3) * arista ** 2
    print_result_block("Área Superficial del Tetraedro Regular", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_tetraedro():
    print_header()
    box_line("  TETRAEDRO REGULAR  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = (√2 / 12) * a³", align="left")
    box_mid()
    arista = get_float("Arista a")
    volumen = (math.sqrt(2) / 12) * arista ** 3
    print_result_block("Volumen del Tetraedro Regular", f"{volumen:.6g}", "u³")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: OCTAEDRO REGULAR
# ─────────────────────────────────────────────
def calcular_area_octaedro():
    print_header()
    box_line("  OCTAEDRO REGULAR  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = 2 * √3 * a²", align="left")
    box_mid()
    arista = get_float("Arista a")
    area = 2 * math.sqrt(3) * arista ** 2
    print_result_block("Área Superficial del Octaedro Regular", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_octaedro():
    print_header()
    box_line("  OCTAEDRO REGULAR  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = (√2 / 3) * a³", align="left")
    box_mid()
    arista = get_float("Arista a")
    volumen = (math.sqrt(2) / 3) * arista ** 3
    print_result_block("Volumen del Octaedro Regular", f"{volumen:.6g}", "u³")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: DODECAEDRO REGULAR
# ─────────────────────────────────────────────
def calcular_area_dodecaedro():
    print_header()
    box_line("  DODECAEDRO REGULAR  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = 3*√(25+10√5) * a²", align="left")
    box_mid()
    arista = get_float("Arista a")
    area = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * arista ** 2
    print_result_block("Área Superficial del Dodecaedro Regular", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_dodecaedro():
    print_header()
    box_line("  DODECAEDRO REGULAR  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = ((15+7√5)/4) * a³", align="left")
    box_mid()
    arista = get_float("Arista a")
    volumen = ((15 + 7 * math.sqrt(5)) / 4) * arista ** 3
    print_result_block("Volumen del Dodecaedro Regular", f"{volumen:.6g}", "u³")
    wait_enter()


# ─────────────────────────────────────────────
#  CALCULOS: ICOSAEDRO REGULAR
# ─────────────────────────────────────────────
def calcular_area_icosaedro():
    print_header()
    box_line("  ICOSAEDRO REGULAR  ──  Área Superficial", align="left")
    box_mid()
    box_line("  Fórmula:  A = 5 * √3 * a²", align="left")
    box_mid()
    arista = get_float("Arista a")
    area = 5 * math.sqrt(3) * arista ** 2
    print_result_block("Área Superficial del Icosaedro Regular", f"{area:.6g}", "u²")
    wait_enter()

def calcular_volumen_icosaedro():
    print_header()
    box_line("  ICOSAEDRO REGULAR  ──  Volumen", align="left")
    box_mid()
    box_line("  Fórmula:  V = (5*(3+√5)/12) * a³", align="left")
    box_mid()
    arista = get_float("Arista a")
    volumen = (5 * (3 + math.sqrt(5)) / 12) * arista ** 3
    print_result_block("Volumen del Icosaedro Regular", f"{volumen:.6g}", "u³")
    wait_enter()


# **********************************************************************************************************************************
# ****************** MOSTRAR CALCULOS EN MENU **************************
# **********************************************************************************************************************************

# === CUADRADO ====
def menu_calculos_cuadrado():

    opciones = {
        # CORRECCIÓN: fórmula del área corregida de "(√3/4) * l²" a "l²"
        "1": ("Área",      "A = l²",  calcular_area_cuadrado),
        "2": ("Perímetro", "P = 4·l", calcular_perimetro_cuadrado),
        "3": ("Diagonal",  "d = l√2", calcular_diagonal_cuadrado),
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


# === RECTANGULO ====
def menu_calculos_rectangulo():

    opciones = {
        # CORRECCIÓN: fórmula del área corregida de "A = l²" a "A = b * h"
        "1": ("Área",      "A = b * h",  calcular_area_rectangulo),
        "2": ("Perímetro", "P = 2·(l-b + l-h)", calcular_perimetro_rectangulo),
        "3": ("Diagonal",  "d = √l-b² + l-h²", calcular_diagonal_rectangulo),
    }

    while True:
        print_header()
        box_line("  RECTÁNGULO  ──  Selecciona cálculo", align="left")
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



# === TRIANGULO EQUILATERO ====
def menu_calculos_triangulo_equilatero():

    opciones = {
        "1": ("Área",      "A = ((√3)/4) * l²",  calcular_area_triangulo_equilatero),
        "2": ("Perímetro", "P = 3 * l", calcular_perimetro_triangulo_equilatero),
        "3": ("Altura",  "h = (√3/2) * l", calcular_altura_triangulo_equilatero),
    }


    while True:
        print_header()
        box_line("  TRIÁNGULO EQUILÁTERO  ──  Selecciona cálculo", align="left")
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



# === TRIANGULO ISÓSCELES ====
def menu_calculos_triangulo_isosceles():

    opciones = {
        "1": ("Área",      "A = (b * h) / 2",  calcular_area_triangulo_isosceles),
        "2": ("Perímetro", "P = (2*a) + b", calcular_perimetro_triangulo_isosceles),
        "3": ("Altura",  "h = √(a² - (b²/4))", calcular_altura_triangulo_isosceles),
    }

    while True:
        print_header()
        box_line("  TRIÁNGULO ISÓSCELES  ──  Selecciona cálculo", align="left")
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


# === TRIANGULO ESCALENO ====
def menu_calculos_triangulo_escaleno():

    opciones = {
        "1": ("Perímetro", "P = a + b + c",  calcular_perimetro_triangulo_escaleno),
        "2": ("Área", "A = √(s*((s-a)*(s-b)*(s-c)))", calcular_area_triangulo_escaleno),
        "3": ("Ángulo",  "cos(α) = (b² + c² - a² ) / 2bc", calcular_angulo_triangulo_escaleno),
    }

    while True:
        print_header()
        box_line("  TRIÁNGULO ESCALENO  ──  Selecciona cálculo", align="left")
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
            


# === TRIANGULO RECTANGULO ====
def menu_calculos_triangulo_rectangulo():

    opciones = {
        "1": ("Perímetro", "P = a + b + c",  calcular_perimetro_triangulo_rectangulo),
        "2": ("Área", "A = (a * b) / 2", calcular_area_triangulo_rectangulo),
        "3": ("Hipotenusa",  "c = √(a² + b²)", calcular_hipotenusa_triangulo_rectangulo),
    }

    while True:
        print_header()
        box_line("  TRIÁNGULO RECTÁNGULO  ──  Selecciona cálculo", align="left")
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



# === TRIANGULO ACUTÁNGULO ====
def menu_calculos_triangulo_acutangulo():

    opciones = {
        "1": ("Suma Ángulos Internos", "Σ = α + β + γ = 180°",  calcular_suma_angulos_internos_triangulo_acutangulo),
        "2": ("Área", "A = (b * h) / 2", calcular_area_triangulo_acutangulo),
    }

    while True:
        print_header()
        box_line("  TRIÁNGULO ACUTÁNGULO  ──  Selecciona cálculo", align="left")
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


# === TRIANGULO OBTUSÁNGULO ====
def menu_calculos_triangulo_obtusangulo():

    opciones = {
        "1": ("Ángulos Obtuso", "Σ = α + β + γ = 180°| β > 90°",  calcular_angulo_obtuso_triangulo_obtusangulo),
        "2": ("Área", "A = (b * h) / 2", calcular_area_triangulo_obtusangulo),
    }

    while True:
        print_header()
        box_line("  TRIÁNGULO OBTUSÁNGULO  ──  Selecciona cálculo", align="left")
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











# === ROMBO ====
def menu_calculos_rombo():

    opciones = {
        "1": ("Perímetro", "P = 4 * l",        calcular_perimetro_rombo),
        "2": ("Área",      "A = (D * d) / 2",  calcular_area_rombo),
        "3": ("Suma Ángulos", "2α + 2β = 360°", calcular_angulos_rombo),
    }

    while True:
        print_header()
        box_line("  ROMBO  ──  Selecciona cálculo", align="left")
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


# === ROMBOIDE ====
def menu_calculos_romboide():

    opciones = {
        "1": ("Perímetro", "P = 2 * (a + b)", calcular_perimetro_romboide),
        "2": ("Área",      "A = b * h",        calcular_area_romboide),
    }

    while True:
        print_header()
        box_line("  ROMBOIDE  ──  Selecciona cálculo", align="left")
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


# === TRAPECIO ====
def menu_calculos_trapecio():

    opciones = {
        "1": ("Área",      "A = ((B + b) * h) / 2", calcular_area_trapecio),
        "2": ("Perímetro", "P = B + b + c + d",      calcular_perimetro_trapecio),
    }

    while True:
        print_header()
        box_line("  TRAPECIO  ──  Selecciona cálculo", align="left")
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


# === DELTOIDE (COMETA) ====
def menu_calculos_deltoide():

    opciones = {
        "1": ("Área",      "A = (D * d) / 2",  calcular_area_deltoide),
        "2": ("Perímetro", "P = 2 * (a + b)",  calcular_perimetro_deltoide),
    }

    while True:
        print_header()
        box_line("  DELTOIDE (COMETA)  ──  Selecciona cálculo", align="left")
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


# === POLIGONO REGULAR (HEXÁGONO) ====
def menu_calculos_poligono_regular():

    opciones = {
        "1": ("Perímetro",      "P = n * l",           calcular_perimetro_poligono_regular),
        "2": ("Área",           "A = (P * ap) / 2",    calcular_area_poligono_regular),
        "3": ("Ángulo Interno", "α = ((n-2)*180) / n", calcular_angulo_interno_poligono_regular),
    }

    while True:
        print_header()
        box_line("  POLÍGONO REGULAR  ──  Selecciona cálculo", align="left")
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


# === CIRCULO ====
def menu_calculos_circulo():

    opciones = {
        "1": ("Perímetro (Circunferencia)", "P = 2 * π * r", calcular_perimetro_circulo),
        "2": ("Área",                       "A = π * r²",    calcular_area_circulo),
    }

    while True:
        print_header()
        box_line("  CÍRCULO  ──  Selecciona cálculo", align="left")
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


# === SECTOR CIRCULAR ====
def menu_calculos_sector_circular():

    opciones = {
        "1": ("Área",             "A = (α * π * r²) / 360°", calcular_area_sector_circular),
        "2": ("Longitud de Arco", "L = (α * π * r) / 180°",  calcular_arco_sector_circular),
    }

    while True:
        print_header()
        box_line("  SECTOR CIRCULAR  ──  Selecciona cálculo", align="left")
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


# === CORONA CIRCULAR ====
def menu_calculos_corona_circular():

    opciones = {
        "1": ("Área",            "A = π * (R² - r²)",   calcular_area_corona_circular),
        "2": ("Perímetro Total", "P = 2 * π * (R + r)", calcular_perimetro_corona_circular),
    }

    while True:
        print_header()
        box_line("  CORONA CIRCULAR  ──  Selecciona cálculo", align="left")
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


# === ELIPSE ====
def menu_calculos_elipse():

    opciones = {
        "1": ("Área",              "A = π * a * b",                    calcular_area_elipse),
        "2": ("Perímetro (Aprox.)", "P ≈ π*[3(a+b)-√((3a+b)(a+3b))]", calcular_perimetro_elipse),
    }

    while True:
        print_header()
        box_line("  ELIPSE  ──  Selecciona cálculo", align="left")
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


# === CUBO (HEXAEDRO) ====
def menu_calculos_cubo():

    opciones = {
        "1": ("Área Superficial",  "A = 6 * l²",  calcular_area_cubo),
        "2": ("Volumen",           "V = l³",       calcular_volumen_cubo),
        "3": ("Diagonal Espacial", "D = l * √3",   calcular_diagonal_cubo),
    }

    while True:
        print_header()
        box_line("  CUBO (HEXAEDRO)  ──  Selecciona cálculo", align="left")
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


# === PRISMA RECTANGULAR ====
def menu_calculos_prisma_rectangular():

    opciones = {
        "1": ("Área Superficial", "A = 2(ab + ah + bh)", calcular_area_prisma_rectangular),
        "2": ("Volumen",          "V = a * b * h",        calcular_volumen_prisma_rectangular),
    }

    while True:
        print_header()
        box_line("  PRISMA RECTANGULAR  ──  Selecciona cálculo", align="left")
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


# === PRISMA REGULAR GENERAL ====
def menu_calculos_prisma_regular():

    opciones = {
        "1": ("Área Superficial", "A = 2*A_base + P_base*h", calcular_area_prisma_regular),
        "2": ("Volumen",          "V = A_base * h",           calcular_volumen_prisma_regular),
    }

    while True:
        print_header()
        box_line("  PRISMA REGULAR GENERAL  ──  Selecciona cálculo", align="left")
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


# === CILINDRO ====
def menu_calculos_cilindro():

    opciones = {
        "1": ("Área Superficial", "A = 2*π*r*(r + h)", calcular_area_cilindro),
        "2": ("Volumen",          "V = π * r² * h",    calcular_volumen_cilindro),
    }

    while True:
        print_header()
        box_line("  CILINDRO  ──  Selecciona cálculo", align="left")
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


# === ESFERA ====
def menu_calculos_esfera():

    opciones = {
        "1": ("Área Superficial", "A = 4 * π * r²",    calcular_area_esfera),
        "2": ("Volumen",          "V = (4/3) * π * r³", calcular_volumen_esfera),
    }

    while True:
        print_header()
        box_line("  ESFERA  ──  Selecciona cálculo", align="left")
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


# === CONO ====
def menu_calculos_cono():

    opciones = {
        "1": ("Generatriz",       "g = √(r² + h²)",     calcular_generatriz_cono),
        "2": ("Área Superficial", "A = π * r * (r + g)", calcular_area_cono),
        "3": ("Volumen",          "V = (π * r² * h) / 3",calcular_volumen_cono),
    }

    while True:
        print_header()
        box_line("  CONO  ──  Selecciona cálculo", align="left")
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


# === PIRAMIDE REGULAR ====
def menu_calculos_piramide():

    opciones = {
        "1": ("Área Superficial", "A = A_base + (P_base*Ap)/2", calcular_area_piramide),
        "2": ("Volumen",          "V = (A_base * h) / 3",       calcular_volumen_piramide),
    }

    while True:
        print_header()
        box_line("  PIRÁMIDE REGULAR  ──  Selecciona cálculo", align="left")
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


# === TRONCO DE CONO ====
def menu_calculos_tronco_cono():

    opciones = {
        "1": ("Área Superficial", "A = π*[R²+r²+g(R+r)]",    calcular_area_tronco_cono),
        "2": ("Volumen",          "V = (π*h/3)*[R²+r²+(R*r)]",calcular_volumen_tronco_cono),
    }

    while True:
        print_header()
        box_line("  TRONCO DE CONO  ──  Selecciona cálculo", align="left")
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


# === TOROIDE (DONA) ====
def menu_calculos_toroide():

    opciones = {
        "1": ("Área Superficial", "A = 4 * π² * R * r",   calcular_area_toroide),
        "2": ("Volumen",          "V = 2 * π² * R * r²",  calcular_volumen_toroide),
    }

    while True:
        print_header()
        box_line("  TOROIDE (DONA)  ──  Selecciona cálculo", align="left")
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


# === TETRAEDRO REGULAR ====
def menu_calculos_tetraedro():

    opciones = {
        "1": ("Área Superficial", "A = √3 * a²",       calcular_area_tetraedro),
        "2": ("Volumen",          "V = (√2 / 12) * a³", calcular_volumen_tetraedro),
    }

    while True:
        print_header()
        box_line("  TETRAEDRO REGULAR  ──  Selecciona cálculo", align="left")
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


# === OCTAEDRO REGULAR ====
def menu_calculos_octaedro():

    opciones = {
        "1": ("Área Superficial", "A = 2 * √3 * a²",  calcular_area_octaedro),
        "2": ("Volumen",          "V = (√2 / 3) * a³", calcular_volumen_octaedro),
    }

    while True:
        print_header()
        box_line("  OCTAEDRO REGULAR  ──  Selecciona cálculo", align="left")
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


# === DODECAEDRO REGULAR ====
def menu_calculos_dodecaedro():

    opciones = {
        "1": ("Área Superficial", "A = 3*√(25+10√5) * a²",  calcular_area_dodecaedro),
        "2": ("Volumen",          "V = ((15+7√5)/4) * a³",   calcular_volumen_dodecaedro),
    }

    while True:
        print_header()
        box_line("  DODECAEDRO REGULAR  ──  Selecciona cálculo", align="left")
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


# === ICOSAEDRO REGULAR ====
def menu_calculos_icosaedro():

    opciones = {
        "1": ("Área Superficial", "A = 5 * √3 * a²",          calcular_area_icosaedro),
        "2": ("Volumen",          "V = (5*(3+√5)/12) * a³",    calcular_volumen_icosaedro),
    }

    while True:
        print_header()
        box_line("  ICOSAEDRO REGULAR  ──  Selecciona cálculo", align="left")
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




def menu_principal():

    figuras_2d = {
        "1":  ("Cuadrado",               menu_calculos_cuadrado,            mini_cuadrado),
        "2":  ("Rectángulo",             menu_calculos_rectangulo,          mini_rectangulo),
        "3":  ("Triángulo Equilátero",   menu_calculos_triangulo_equilatero,  mini_triangulo_equilatero),
        # CORRECCIÓN: clave duplicada "4" resuelta — Isósceles="4", Escaleno="5", Rectángulo="6", Acutángulo="7", Obtusángulo="8"
        "4":  ("Triángulo Isósceles",    menu_calculos_triangulo_isosceles,   mini_triangulo_isosceles),
        "5":  ("Triángulo Escaleno",     menu_calculos_triangulo_escaleno,    mini_triangulo_escaleno),
        "6":  ("Triángulo Rectángulo",   menu_calculos_triangulo_rectangulo,  mini_triangulo_rectangulo),
        "7":  ("Triángulo Acutángulo",   menu_calculos_triangulo_acutangulo,  mini_triangulo_acutangulo),
        "8":  ("Triángulo Obtusángulo",  menu_calculos_triangulo_obtusangulo, mini_triangulo_obtusangulo),
        "9":  ("Rombo",                  menu_calculos_rombo,               mini_rombo),
        "10": ("Romboide",               menu_calculos_romboide,            mini_romboide),
        "11": ("Trapecio",               menu_calculos_trapecio,            mini_trapecio),
        "12": ("Deltoide (Cometa)",      menu_calculos_deltoide,            mini_deltoide),
        "13": ("Polígono Regular",       menu_calculos_poligono_regular,    mini_poligono_regular),
        "14": ("Círculo",                menu_calculos_circulo,             mini_circulo),
        "15": ("Sector Circular",        menu_calculos_sector_circular,     mini_sector_circular),
        "16": ("Corona Circular",        menu_calculos_corona_circular,     mini_corona_circular),
        "17": ("Elipse",                 menu_calculos_elipse,              mini_elipse),
    }

    figuras_3d = {
        "18": ("Cubo (Hexaedro)",        menu_calculos_cubo,               mini_cubo),
        "19": ("Prisma Rectangular",     menu_calculos_prisma_rectangular,  mini_prisma_rectangular),
        "20": ("Prisma Regular General", menu_calculos_prisma_regular,      mini_prisma_regular),
        "21": ("Cilindro",               menu_calculos_cilindro,            mini_cilindro),
        "22": ("Esfera",                 menu_calculos_esfera,              mini_esfera),
        "23": ("Cono",                   menu_calculos_cono,                mini_cono),
        "24": ("Pirámide Regular",       menu_calculos_piramide,            mini_piramide),
        "25": ("Tronco de Cono",         menu_calculos_tronco_cono,         mini_tronco_cono),
        "26": ("Toroide (Dona)",         menu_calculos_toroide,             mini_toroide),
        "27": ("Tetraedro Regular",      menu_calculos_tetraedro,           mini_tetraedro),
        "28": ("Octaedro Regular",       menu_calculos_octaedro,            mini_octaedro),
        "29": ("Dodecaedro Regular",     menu_calculos_dodecaedro,          mini_dodecaedro),
        "30": ("Icosaedro Regular",      menu_calculos_icosaedro,           mini_icosaedro),
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