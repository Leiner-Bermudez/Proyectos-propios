numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
palabras = ["hola", "mundo", "python", "es", "genial"]

def pares(nums):
    return [n for n in nums if n % 2 == 0]
print(pares(numeros))

def potencia(pont):
    return [p ** 2 for p in pont]
print(potencia(numeros))

def letra(disnt):
    return[d for d in disnt if len(d) > 3]
print(letra(palabras))

def longitudes(palabras):
    return {p:len(p) for p in palabras}
print(longitudes(palabras))