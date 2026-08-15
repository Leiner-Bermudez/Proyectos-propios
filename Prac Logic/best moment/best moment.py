def moment(best):
    precio_minimo = best[0]
    max_ganancia = 0
    for i in range(1, len(best)):                          # ← :
        if best[i] - precio_minimo > max_ganancia:          # ← if y :
            max_ganancia = best[i] - precio_minimo          # ← actualizar
        if best[i] < precio_minimo:                         # ← if y :
            precio_minimo = best[i]                         # ← actualizar
    return max_ganancia                                     # ← devolver

#solicion mas concisa
#def moment(prices):
    precio_min = prices[0]
    max_ganancia = 0
    for p in prices:
        precio_min = min(precio_min, p)
        max_ganancia = max(max_ganancia, p - precio_min)
    return max_ganancia

Entrada = [7, 1, 5, 3, 6, 4]
Salida = 5
print(moment(Entrada))