# CREANDO UNA LISTA, TUPLA O CONJUNTO.
lista = ["Demian landin", "Empleado administrativo", True, 1.75]  #Tipo de operador list, el código de corchetes es Alt+91 o Shift + llave.
print(lista[0])  #Es importante entender que las órdenes numéricas empiezan desde el 0, siendo el dato 1 empleado administrativo, y 0 demian landin. Se diría que dentro de la lista hay 4 elementos, siendo Demian Landin el elemento 1, pero alojado en el índice 0.

#aparte del operador list, puede usarse el operador tupla, que funciona igual y se utiliza sin corchetes.
tupla = ("Demian landin", "Empleado administrativo", True, 1.75)
print(tupla[1]) #a diferencia del operador list, tupla no puede modificar sus variantes. Es muy útil para datos que NUNCA se van a modificar.

lista [2] = "En búsqueda laboral"  #en este caso gracias al operador list, se pudo modificar un elemento de la lista.
print(lista [2])

conjunto = {"Demian landin", "Empleado administrativo", True, 1.75,"Demian landin"} #el conjunto omite las duplicaciones de variables que se asignen. No se puede llamar a los elementos por índice tampoco, y no da un resultado ordenado.
print(conjunto)

#print(conjunto [3]). Esto no podría hacerse dado que no realiza llamado a elementos.

# OPERADOR DICT (Diccionario). La estructura del diccionario está conformada por Key : Value, siendo Key "nombre", y value "Demian Landin", la linea se separa por comas.
diccionario = {
    "nombre" : "Demian Landin",
    "estado" : "En oficio de empleado",
    "búsqueda laboral" : False,
    "medida" : 1.75,
    "dato duplicado" : "Demian Landin"
}

print(diccionario["búsqueda laboral"])
print(diccionario["medida"]+ 0.2) 