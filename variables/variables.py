a = "demian"
b = "landin"

print(a,b)



numero = 15
numero += 5 #el símbolo + deltante del signo =, indica que se sume el valor indicado a la variable indicada previamente.
print(numero)


numero = 15
numero *= 5 #básicamente, cualquier simbolo que indique una operación matemática, antes de un signo =, indica la operación matemática indicada posteriormente, sobre la variable que se indica al comienzo de la línea.
print(numero)

# CONCATENAR CON +
#para referirse al término "unir" un dato o variable, en este caso un string, no se dice propiamente "unir", sino "concatenar".
nombre = "Demian"
bienvenida = "Hola! " + nombre + ", ¿cómo estás?"
print(bienvenida)

# CONCATENAR CON F-STRINGS
nombre = "Demian"
bienvenida = f"Hola! {nombre} , ¿cómo estás?"  #se trata de un "f string", es otra manera de utilizar un dato concatenado, indicado la f antes de la variable, y usando llaves para reemplazar otros símbolos que indiquen sumatoria de variables. Ademas vuelve un dato booleano o numérico a texto.
print(bienvenida)

#ejemplo 1
nombre = True
bienvenida = f"Hola! {nombre} , ¿cómo estás?" 
print(bienvenida)

#ejemplo 2
nombre = 40
bienvenida = f"Hola! {nombre} , ¿cómo estás?"   
print(bienvenida)


#operador del (delete), se usa luego de lo que se quiere eliminar, si otra línea dispone de una variable previamente al código del, se utilizará la variable de todas formas, porque en orden de prioridades, se borra después.
nombre = "Demian"
bienvenida = f"Hola! {nombre} , ¿cómo estás?"  
del nombre  #en este caso aunque se corra el print, dirá el nombre.
print(bienvenida)

nombre = "Demian"
del nombre  #lanza un error al correr "bienvenida", dado que la variable nombre ya se borró.
bienvenida = f"Hola! {nombre} , ¿cómo estás?"  
print(bienvenida)

# OPERADORES DE PERTENENCIA
#operadores de pertenencia: not in / in,  indican que un string se encuentra o no se encuentra en la variable que se citará:
nombre = True
bienvenida = f"Hola! {nombre} , ¿cómo estás?" 
print("Hola" not in bienvenida)  #en este caso el resultado será False, dado que no es cierto que la palabra Hola no se encuentra en el mensaje de bienvenida, dado la palabra que busca es hola con minúscula, y en mi mensaje de bienvenida lleva mayúscula.

nombre = True
bienvenida = f"Hola! {nombre} , ¿cómo estás?" 
print("Hola" in bienvenida)  #in indica que un string se encuentra en el mensaje de bienvenida.


#Definir una variable con CamelCase, se refiere a separar las palabras por la primer letra mayúscula, dado que no se puede usar el espacio.
nombreCompleto = Demian Landin #Bien
nombre completo = Demian Landin #Mal

#Definir una variable con Snake_case, se refiere a separar las palabras por guiones bajos.
nombre_completo = Demian Landin #Bien















