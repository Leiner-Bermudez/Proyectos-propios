def solitario(result):
    resultado = 0
    for i in range(len(result)):
        resultado = resultado ^ result[i]
    return resultado
Entrada = [4, 1, 2, 1, 2]
# Salida: 4
print(solitario(Entrada))