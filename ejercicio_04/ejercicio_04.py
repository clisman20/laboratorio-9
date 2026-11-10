"""
Ejercicio 4. Buscar un código en un catálogo ordenado

Un catálogo contiene códigos numéricos ordenados de menor a mayor. Implementa
una búsqueda binaria recursiva para localizar un código.

    def buscar_codigo(codigos, objetivo, izquierda, derecha):
        pass

La función devuelve el índice del código si se encuentra, o -1 si no se
encuentra. Si hay códigos repetidos, puedes devolver el índice de cualquiera de
sus apariciones.

Ejemplos

    codigos = [101, 205, 310, 415, 520, 630, 740]

    buscar_codigo(codigos, 520, 0, len(codigos) - 1)   # 4
    buscar_codigo(codigos, 300, 0, len(codigos) - 1)   # -1
    buscar_codigo([], 300, 0, -1)                      # -1
    buscar_codigo([205], 205, 0, 0)                    # 0

Restricciones

- La solución debe ser recursiva.
- No utilices ciclos ni cortes.
- No busques con objetivo in codigos ni con .index().
- No ordenes la lista dentro de la función: se recibe ordenada.
- En cada llamada, continúa únicamente en la región que todavía pueda contener
  el objetivo.
"""


def buscar_codigo(codigos, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1

    medio = (izquierda + derecha) // 2

    if codigos[medio] == objetivo:
        return medio
    elif codigos[medio] < objetivo:
        return buscar_codigo(codigos, objetivo, medio + 1, derecha)
    else:
        return buscar_codigo(codigos, objetivo, izquierda, medio - 1)
     


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuáles son las dos situaciones en las que termina la búsqueda?
#
#
# 2. ¿Por qué no debes incluir nuevamente la posición central en el
#    siguiente intervalo?
#
#
# 3. Completa la traza buscando 300 en codigos. Si una llamada no llega a
#    calcular el medio, escribe "—".
#
#    Llamada | Izquierda | Derecha | Medio | Decisión
#    --------|-----------|---------|-------|---------
#       1    |           |         |       |
#       2    |           |         |       |
#       3    |           |         |       |
#       4    |           |         |       |
#
# 4. ¿Qué diferencia hay entre el progreso de esta función y el de
#    contar_desde_limite()?
#
#


if __name__ == "__main__":
    codigos = [101, 205, 310, 415, 520, 630, 740]

    print(buscar_codigo(codigos, 520, 0, len(codigos) - 1))   # 4
    print(buscar_codigo(codigos, 300, 0, len(codigos) - 1))   # -1
    print(buscar_codigo([], 300, 0, -1))                      # -1
    print(buscar_codigo([205], 205, 0, 0))                    # 0

    #las respuestas a las preguntas de analisis son:
    #1. cuando se encuentra el objetivo o cuando izquierda es mayor que derecha
    #2 . porque ya se comparo el valor del medio y no es necesario volver a compararlo
    #3. Llamada | Izquierda | Derecha | Medio | Decisión
    #   1    |     0     |    6    |   3    |  310  |  izquierda = medio + 1
    #   2    |     4     |    6    |   5    |  520  |  derecha = medio - 1
    #   3    |     4     |    4    |   4    |  520  |  izquierda = medio + 1
    #   4    |     5     |    4    |   —    |  -1   |  izquierda > derecha
    #4. la diferencia es que en contar_desde_limite() se recorre toda la lista mientras que en buscar_codigo() se va descartando la mitad de la lista en cada llamada recursiva.

