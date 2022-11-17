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
print("---------------------------------------------------------------------------------------")

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




