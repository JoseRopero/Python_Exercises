# Dados los nombres y calificaciones de cada estudiante de una clase, guárdelos en una lista anidada e imprima
# los nombres de cualquier estudiante que tenga la segunda calificación más baja.
# Nota: Si hay varios estudiantes con la segunda calificación más baja, ordene sus nombres alfabéticamente
# y escriba cada nombre en una nueva línea.

records = []
lista_scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    lista = [name, score]  # Creamos lista con el nombre y la nota y las añadimos a la lista records
    records.append(lista)  # Quedaría: records = [[], [], [],...]
    lista_scores.append(score)  # Creamos otra lista con las notas para poder comparar y sacar el segundo minimo
set_score = set(lista_scores)  # Al pasar a set eliminamos los repetidos y podemos obtener el segundo minimo
lista_scores_ordenado = sorted(list(set_score))  # La volvemos a pasar a lista para trabajar

segundo_minimo = lista_scores_ordenado[1]  # Aqui metemos en una variable el segundo para comparar con el listado

lista_name = []
for name, nota in records:
    if nota == segundo_minimo:  # Comparamos y si es igual guardamos el nombre en un listado
        lista_name.append(name)
lista_name_ordenada = sorted(lista_name)  # Con el listado de nombres lo ordenamos e imprimimos
for name in lista_name_ordenada:
    print(name)
