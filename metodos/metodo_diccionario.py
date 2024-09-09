#KEYS
diccionario = {
    "nombre" : "Demian",
    "apellido" : "Landin",
    "años" : 25
}

claves = diccionario.keys() #nos devuelve un objeto dict_item.

print(claves)  #nos sirve para iterar.

#GET
claves = diccionario.get("nombre") #se marca un parámetro de búsqueda en un diccionario. En caso de no encontrar nada nos muestra una excepción pero no se para el programa. 

print(claves) 

#CLEAR: elimina todo del diccionario.

#diccionario.clear()

#print(diccionario) 


#POP: elimina un elemento del diccionario.

diccionario.pop("nombre")

print (diccionario)

#DICT: obteniendo un elemento iterable 

diccionario_iterable = diccionario.items()

print(diccionario_iterable)