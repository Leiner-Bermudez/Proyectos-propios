frase = "python es un lenguaje genial"
# Resultado final: "Python Es Un Lenguaje Genial"

def procesar_frase(frase):
    palabras = frase.split()           # dividir
    cantidad = len(palabras)              # contar
    capitalizadas = [p.capitalize() for p in palabras]   # capitalizar cada una
    resultado = " ".join(capitalizadas)        # unir
    return resultado, cantidad

print(procesar_frase(frase))