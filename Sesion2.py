from data.countries import countries
from data.countries_data import countries_data

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

# EJERCICIO 7 (Recorrer los países)

# Recorra los países y extraiga todos los países que contengan la palabra land.


for pais in countries:
    pais.lower()
    if pais.find('land', 0, len(pais)) >= 0:
        print(pais)

print("")
print("=====================================================================================================")

# EJERCICIO 8 (Recorrer listas)

# Dada una lista de frutas: ['plátano', 'naranja', 'mango', 'limón'] invierta el orden usando bucle.

lista_Frutas = ['platano', 'naranja', 'mango', 'limon']

for n in reversed(lista_Frutas):
    print(n)
print()
for n in lista_Frutas[::-1]:
    print(n)

print()
print("=====================================================================================================")

# PENDIENTE
# Vaya a la carpeta de datos y use el archivo countries_data.py.
# 1. ¿Cuál es el número total de idiomas en los datos?
# 2. Encuentra los diez idiomas más hablados a partir de los datos
# 3. Encuentra los 10 países más poblados del mundo

# 1
lenguajes = list()
for country in countries_data:
    for language in country['languages']:
        lenguajes.append(language)
#dict(zip(lenguajes, map(lambda x: lenguajes.count(x), lenguajes)))
#print(lenguajes)
set_languages = set(lenguajes)
print(len(set_languages))

# 2
