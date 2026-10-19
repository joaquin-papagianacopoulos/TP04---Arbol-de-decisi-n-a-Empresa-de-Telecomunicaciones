# Ejercicio a) Árbol de decisión a mano (entropía y ganancia de información)
from math import log2

# Datos: (id, edad, uso de datos, tiene línea fija, aceptó oferta)
datos = [
    (1, 24, 2.5, "No", "No"),
    (2, 38, 6.0, "Si", "Si"),
    (3, 29, 3.0, "No", "No"),
    (4, 45, 8.0, "Si", "Si"),
    (5, 52, 7.5, "Si", "Si"),
    (6, 33, 4.0, "No", "No"),
    (7, 41, 5.5, "Si", "Si"),
    (8, 27, 2.0, "No", "No"),
    (9, 36, 6.5, "Si", "Si"),
    (10, 31, 3.5, "No", "No"),
]


# ---------- Funciones auxiliares ----------
def entropia(clases):
    """Entropía de una lista de clases, ej: ["Si", "No", "Si"]"""
    total = len(clases)
    if total == 0:
        return 0
    resultado = 0
    for c in set(clases):
        p = clases.count(c) / total
        resultado = resultado - p * log2(p)
    return resultado


def grupo_edad(edad):
    if edad <= 30:
        return "Joven"
    elif edad <= 50:
        return "Adulto"
    else:
        return "Mayor"


def grupo_uso(uso):
    if uso <= 3:
        return "Bajo"
    elif uso <= 6:
        return "Medio"
    else:
        return "Alto"


def ganancia(grupos, clases):
    """grupos: lista con el grupo de cada cliente. clases: lista con 'Si'/'No'."""
    entropia_total = entropia(clases)
    entropia_ponderada = 0
    print("  Grupos:")
    for g in sorted(set(grupos)):
        # clases de los clientes que pertenecen al grupo g
        clases_g = [clases[i] for i in range(len(clases)) if grupos[i] == g]
        e = entropia(clases_g)
        peso = len(clases_g) / len(clases)
        print(f"    {g}: {len(clases_g)} clientes, "
              f"Si={clases_g.count('Si')}, No={clases_g.count('No')}, entropía={e:.3f}")
        entropia_ponderada = entropia_ponderada + peso * e
    print(f"  Entropía ponderada = {entropia_ponderada:.3f}")
    return entropia_total - entropia_ponderada


# ---------- 1. Entropía del conjunto original ----------
clases = [fila[4] for fila in datos]
print("1) Entropía del conjunto original")
print(f"   Si = {clases.count('Si')}, No = {clases.count('No')}")
print(f"   Entropía = {entropia(clases):.3f}\n")

# ---------- 2. Ganancia de información de cada atributo ----------
edades = [grupo_edad(fila[1]) for fila in datos]
usos = [grupo_uso(fila[2]) for fila in datos]
lineas = [fila[3] for fila in datos]

print("2) Ganancia de información")
print("Edad:")
g_edad = ganancia(edades, clases)
print(f"  Ganancia = {g_edad:.3f}\n")

print("Tiene línea fija:")
g_linea = ganancia(lineas, clases)
print(f"  Ganancia = {g_linea:.3f}\n")

print("Uso de datos:")
g_uso = ganancia(usos, clases)
print(f"  Ganancia = {g_uso:.3f}\n")

# ---------- 3. Árbol ----------
print("3) Árbol de decisión")
print("   El mejor atributo es 'Tiene línea fija' (ganancia 1.0).")
print("   Cada rama queda pura, así que no hace falta seguir dividiendo:")
print("   Tiene línea fija?")
print("     ├── Si -> Acepta la oferta (ids 2, 4, 5, 7, 9)")
print("     └── No -> No acepta la oferta (ids 1, 3, 6, 8, 10)")

# ---------- 4. Conclusión ----------
print("\n4) Conclusión")
mejores = {"Edad": g_edad, "Tiene línea fija": g_linea, "Uso de datos": g_uso}
mejor = max(mejores, key=mejores.get)
print(f"   El mejor atributo para empezar el árbol es: {mejor}")
print("   Para predecir: si el cliente tiene línea fija, se predice que acepta;")
print("   si no tiene, se predice que no acepta.")
