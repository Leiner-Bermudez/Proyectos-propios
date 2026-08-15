palabras = ["hola", "mundo", "hola", "python", "mundo", "hola"]
# Resultado: {"hola": 3, "mundo": 2, "python": 1}

def contar(palabras):
    conteo = {}
    for p in palabras:
        conteo[p] = conteo.get(p, 0) + 1    # ← qué va en el ?
    return conteo

print(contar(palabras))