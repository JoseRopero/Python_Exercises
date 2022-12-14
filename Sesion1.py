# EJERCICIO 1 (If-Else)

# Dado un número entero, realice las siguientes acciones condicionales:
"""
 * Si es impar, imprimir 'Weird'
 * Si es par y en el rango inclusivo de 2 a 5, imprimir 'Not Weird'
 * Si es par y en el rango inclusivo de 6 a 20, imprimir 'Weird'
 * Si es par y mayor que 20, imprimir 'Not Weird'

Restricciones 1 <= n <= 100
"""
n = int(input().strip())
if 1 <= n <= 100:
    if n % 2 != 0 or (n % 2 == 0 and 6 <= n <= 20):
        print("Weird")
    elif (n % 2 == 0 and 2 <= n <= 5) or (n % 2 == 0 and n > 20):
        print("Not Weird")

print("==================================================================================================")

# EJERCICIO 2 (Loops)

# El código lee un número entero de teclado para todos los enteros no negativos, imprime el cuadrado.
# Ejemplo
"""
La lista de enteros no negativos que son menores que 3 son 0, 1, 2.
Imprime el cuadrado de cada número en una línea separada.
0
1
4

Restricciones 1 <= n <= 20
"""

n = int(input())
lista = list(range(n))
for integer in lista:
    print(pow(integer, 2))

print("==================================================================================================")


# EJERCICIO 3 (Write a function)

# Dado un año, determine si es un año bisiesto.
# Si es un año bisiesto, devuelve el valor booleano True, de lo contrario, devuelve False.

def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = True
    return leap


year = int(input())
print(is_leap(year))

print("==================================================================================================")

# EJERCICIO 4 (Print a function)

# El código leerá un número entero n.
# Sin utilizar ningún método de cadena, intente imprimir lo siguiente: 1234...n
# Restricciones 1 < n < 150
# Imprime la lista de enteros como una cadena, sin espacios.

n = int(input())
if 1 <= n <= 150:
    lista = list(range(1, n + 1))
    cadena = ""
    for num in lista:
        cadena += str(num)
    print(cadena)

print("==================================================================================================")

# EJERCICIO 5 (List comprehensions)

# Nos dan tres enteros (x, y, z) representando las dimensiones de un paralelepípedo, junto con un número entero n.
# Imprima una lista de todas las coordenadas posibles dadas por [i, j, k] en una cuadrícula 3D, donde la suma de
# i + j + k no sea igual a n.

x = int(input())
y = int(input())
z = int(input())
n = int(input())
lista_nueva = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(lista_nueva)
