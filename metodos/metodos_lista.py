#creando una lista con list
lista = list(["hola","demian","landin",25])

#devuelve la cantidad de elementos que hay en una lista.
resultado = len(lista)  

#agregar elementos a la lista
lista.append("Empleado administrativo")  #se agrega un elemento nuevo al printear "lista", sin necesidad de printear "agregar_elementos".

#agregar elementos a la lista con un índice específico
lista.insert(6,"Activo")

#agregar varios elementos a la lista
lista.extend([True, 41584490])  #se agregan corchetes porque es en formato de lista dado que agrega información en cantidad. La ordena al final de la lista.

#eliminar elementos de la lista por su índice
lista.pop("0")  #si usara el valor -1 se eliminaría el último elemento de la lista.

#remover un elemento de la lista por su valor
lista.remove("landin")

#eliminda todos los elementos de la lista
lista.clear()

print(lista)

#ordenar valores que no sean string
lista2 = [2,3,66,21,55,22,False,True]
lista2.sort()

print(lista2)

lista3 = [2,3,66,21,55,22,False,True]
lista3.sort(reverse=True)  #al utilizar el parámetro reverse, se ordenan de mayor a menor

print(lista3)  

#invertir los elementos de una lista
lista3.reverse()

print (lista3)

#Cosas que pueden hacerse con una lista:
print(dir(lista))

#Cosas que pueden hacerse con una tupla:
print(dir(("tupla")))
print(dir(("tupla",5))) 