#existen 3 tipos de operadores lógicos: AND, OR y NOT.

#AND, devuelve un resultado True siempre y cuando las dos condiciones se cumplan, es decir, True & True.

resultado = True & True #Resultado True
resultado1 = False & True #Resultado False
resultado2 = True & False #Resultado False
resultado3 = False & False #Resultado False


#OR, devuelve un resultado False siempre y cuando ninguna de las dos condiciones se cumplan, False | False.

resultado4 = True | True #Resultado True
resultado5 = False | True #Resultado True
resultado6 = True | False #Resultado True
resultado7 = False | False #Resultado False 


#NOT, devuelve el valor inverso al indicado, True = False y viceversa. 

resultado8 = not True #Resultado False
resultado9 = not False #Resultado True

#EJEMPLO NOT:
resultado10 = not 2 == 2 #Resultado False, dado que 2 sí es igual a 2.
resultado11 = not 2 > 50 #Resultado True, dado que 2 es cierto que no es verdadero que sea mayor que 50.

#EJEMPLO AND:
resultado12 = 2 & 2 #Resultado True, en este caso dará el número igual: 2.
resultado13 = 2 & 4 #Resultado False, en este caso dará número 0.
resultado14 = 4 & 2 #Resultado False

#EJEMPLO OR:
resultado15 = 2 | 2 
resultado16 = -3 | 2 
resultado17 = 2 | -3 
resultado18 = -3 | -3 

print(resultado18)
