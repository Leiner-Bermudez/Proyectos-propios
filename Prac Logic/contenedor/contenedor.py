def max_area(arr):
    # Línea 1: Guardamos el área máxima encontrada hasta ahora.
    # Empezamos en 0 porque aún no hemos calculado ninguna.
    max_area = 0

    # Línea 2: Puntero izquierdo en el primer elemento (índice 0).
    izq = 0

    # Línea 3: Puntero derecho en el último elemento (índice final).
    der = len(arr) - 1

    # Línea 4: Mientras los punteros no se hayan cruzado...
    # Cuando izq == der ya no hay "ancho" (distancia = 0), no tendría sentido.
    while izq < der:

        # Línea 5: Calculamos el ancho = distancia entre los dos punteros.
        # Ejemplo: si izq=0 y der=8, ancho = 8.
        ancho = der - izq

        # Línea 6: La altura que importa es la MÁS BAJA de las dos paredes,
        # porque si echas agua, se derrama por la más baja.
        # min() devuelve el menor de los dos valores.
        altura = min(arr[izq], arr[der])

        # Línea 7: Área = ancho × altura.
        area = ancho * altura

        # Línea 8: Si el área actual supera a la máxima guardada, la actualizamos.
        # max() devuelve el mayor de los dos.
        max_area = max(max_area, area)

        # Línea 9-11: LA DECISIÓN CLAVE.
        # Movemos SIEMPRE el puntero de la pared MÁS BAJA hacia el centro.
        # ¿Por qué? Porque la más baja es la que limita el área.
        # Si moviéramos la alta, el ancho se reduce y el límite sigue
        # siendo la misma pared baja (o peor). No hay posibilidad de mejora.
        # En cambio, al mover la baja, tenemos la ESPERANZA de encontrar
        # una pared más alta y compensar la pérdida de ancho.
        if arr[izq] < arr[der]:
            izq = izq + 1    # La izquierda es más baja, la movemos a la derecha
        else:
            der = der - 1    # La derecha es más baja (o igual), la movemos a la izquierda

    # Línea 12: Terminamos el bucle, devolvemos la mejor área encontrada.
    return max_area


# Prueba con el ejemplo
arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Las paredes en índice 1 (altura=8) y 8 (altura=7):
#   ancho = 7, altura = min(8,7) = 7, área = 7×7 = 49
print(max_area(arr))  # Output: 49