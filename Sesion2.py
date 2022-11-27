# EJERCICIO 6 (Find the Runner-Up Score!)

# Dada la hoja de puntaje de los participantes para el Día del Deporte Universitario,
# debe encontrar el puntaje del subcampeón.
# Te dan 'n' puntuaciones. Guárdalos en una lista y encuentra la puntuación del subcampeón.

# La primera línea contiene 'n' que es el número de puntuajes que habrá en la lista.
# La segunda línea contiene una matriz A[] de números enteros separados por un espacio.
# Imprime la puntuación del subcampeón.

n = int(input())
arr = map(int, input().split())

listado = set(arr)
listado_ordenado = sorted(listado)
print(listado_ordenado[-2])

print("")
print("=====================================================================================================")
