cadena1 = "Demian Landin"
cadena2 = "Empleado administrativo"

print(dir(cadena1))  #por si solo el operador dir, ejecuta algo, es decir, una función. Para que dir funcione deberá indicarse previamente print, y en la terminal se visualizarán las funcionalidades disponibles.
print(dir(4))  #el tipo de dato 4, es decir, int, dará otra serie de funcionalidades. Lo mismo pasará si le indico una lista o una variable.

#DIR aplicado a STRINGS (variables de texto).

print(dir(cadena1))

#EJEPLO 1: UPPER - operador que vuelte un texto a mayúscula

resultado = upper(cadena1)  #esto está mal, la forma en que funcionará el dir, será la siguiente:
resultado = cadena1.upper()  #esto está bien. Dentro de los paréntesis no irá ningún valor, a no ser que se establezcan parámetros.
resultado2 = "Hola que tal".upper()  #funciona de la misma manera el método, solo que en el anterior resultado, se indicaba previamente la variable cadena1 que era igual a "Demian Landin".

print(resultado2)
#la estructura entonces será escrita de la siguiente manera: "Dato.metodo()". Dentro del paréntesis irán los parámetros si existiera alguno.

#entonces:

#convierte a mayúsculas:
mayus = "hola que tal".upper()

#convierte a minúsculas:
minus = "hola que tal".lower()

#convierte la primera letra a mayúscula:
primera_mayus = "hola que tal".capitalize()

# busca una cadena en otra cadena:
busqueda_find = cadena1.find("a")  #encuentra la posición de lo que se está buscando, puede ser un valor numérico o texto. El resultado será 4, dado que en la palabra Demian, la A es el valor 4, considerando que D es el elemento 0. 

print(busqueda_find) #el resultado dará "-1" cuando no encuentre un valor, y se debe considerar que el metodo es sensible a las mayúsculas, por lo que si buscara la letra "d", la D de Demian, no la contaría dado que la D está escrita en mayúscula.

#busca una cadena en otra cadena:
busqueda_index = cadena1.index("8778")  #a diferencia de find, cuando index no encuentre el parámetro, no dirá "-1", sino que dará error o "excepción".

print(busqueda_index)

#si es numerico dará un valor True, sino False:
es_numerico = cadena1.isnumeric()

print(es_numerico)

#si es alfa numerico dará un valor True, sino False:
es_alfanumerico = cadena1.isalpha()

print(es_alfanumerico)  #el resultado dará falso si hay caractéres especiales, como "-+#", también si hay espacios, dado que el espacio es un elemento más.

#busca la cantidad de veces que se encuentra una coincidencia:
cant_coincidencias = cadena1.count("a")

print(cant_coincidencias)  #en la cadena 1 "Demian Landin", la palabra A se encuentra 2 veces. En el caso de la letra D, la encontrará 1 vez, aunque hayan 2 letras "d", dado que una es minús y la otra es mayús. 
#puede usarse para encontrar coincidencias dentro de un mismo valor: si buscara "an", me daría valor 2, dado que en Demian y Landin, la secuencia "an"se encuentra 2 veces.

#cuenta la cantidad de caracteres de una cadena:
contar_caracteres = len(cadena1)  #se escribe así porque len no es un método, sino una función.

print(contar_caracteres)  #el resultado cuenta también los elementos de espacio, por lo que da 13, dado que demian landin son 12, pero el espacio es contabilizado.

#verifica si una cadena empieza con otra cadena, el resultado positivo será True:
empieza_con = cadena1.startswith("D") #Lo mismo, reconoce secuencias como "an", y es key sensitive.

print(empieza_con)

#verifica si una cadena termina con una cadena:
termina_con = cadena1.endswith("in") 

print(termina_con)

#reemplaza una parte de la cadena con otra cadena indicada:
cadena_nueva = cadena1.replace("Demian","Mister")  #el primer valor se reemplaza por todo lo que le siga luego de la coma. 

print(cadena_nueva)

# EJEMPLO PRÁCTIC0:

cadenaejemplo = "Que,Onda,Loco,Como,VA"
cadena_nueva = cadenaejemplo.replace(","," ")
cadena_nueva2 = cadena_nueva.lower()
cadena_nueva3 = cadena_nueva2.capitalize()
cadena_nueva4 = cadena_nueva3.replace("onda loco","onda, loco,")
cadena_nueva5 = cadena_nueva4.replace("como va","¿Cómo va?")

print(cadena_nueva5)  
#IMPORTANTE!! Fijate como el print responde a una secuencia en formato de cadena siempre que vos modifiques las distintas cadenas: cadena_nueva2 = cadena_nueva. Sucesivamente. La última cadena que ejecutes en el print tendrá el valor de todas las anteriores modificaciones cuando tengas toda la cadena lista.


#separar cadenas con la cadena que especifiquemos:
separar_cadena = cadenaejemplo.split(",")

print(separar_cadena)  #va a separar la cadena en formato de lista, si indico la coma como parámetro, me separará todos los string uno por uno. Si no especifico nada me dará un string completo en formato de lista.
print (type(separar_cadena))  #indicará que el valor es "list", dado que el resultado es una lista. Además es importante el operador "type" para corroborar la naturaleza de un operador/función/método.

#aclaración: En el caso de cadenaejemplo, se trata de una cadena compartida, dado que cada string está separado por comas.
print(separar_cadena[0])  #por eso puedo visualizar también por elementos únicos.
