def lack(array):
    n = len(array)
    sum_esperada = n * (n + 1) // 2
    sum_real = sum(array)
    faltante = sum_esperada - sum_real
    return faltante
Entrada = [3, 0, 1]
# n = 3 (el arreglo tiene 3 elementos, el rango es 0..3)
# Salida: 2
print(lack(Entrada))