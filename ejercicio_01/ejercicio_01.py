"""
Ejercicio 1. Potencia recursiva

Implementa una función que calcule una potencia mediante multiplicaciones y
llamadas recursivas. Recibe una base numérica y un exponente entero no
negativo.

    def potencia(base, exponente):
        pass

En este ejercicio, cualquier base elevada a cero devuelve 1, incluido
potencia(0, 0).

Ejemplos

    potencia(2, 4)    # 16
    potencia(5, 0)    # 1
    potencia(-2, 3)   # -8
    potencia(0, 5)    # 0

Restricciones

- No utilices ciclos.
- No utilices  ni pow().
- La solución debe ser recursiva.
"""


def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuál es el caso base? RESPUESTA = el caso base es que cualquier numero elevado a 0 es igual a 1
#
#
# 2. ¿Qué argumento cambia en cada llamada? RESPUESTA = exponente va disminuyendo
#
#
# 3. ¿Qué operación queda pendiente mientras se resuelve la llamada recursiva? RESPUESTA =
# Respuesta = base * potencia, no se resuelve porque necesita el valor de la llamada recursiva.
#
#
# 4. Escribe las llamadas y los retornos de potencia(3, 3).
#
#

if __name__ == "__main__":
    print(potencia(2, 4))    # 16
    print(potencia(5, 0))    # 1
    print(potencia(-2, 3))   # -8
    print(potencia(0, 5))    # 0

    #VAMOS A EMPEZAR Alumno: Clisman
    #empezare haciendo mi funcion

print(potencia(2,4))
print(potencia(3,3))



