numero = input("Por favor, ingrese su numero de teléfono: ")

resultado = numero*2

print(resultado)  #input devuelve un resultado str, por lo que si indico el número 4 y doy print al resultado *2, lo que me devolverá no será 8, sino "44", dado que input interpreta que mi número 4 es un texto.


#INPUT de números enteros:
resultado_numerico = int(numero)*2

print(resultado_numerico)  #al yo indicar mediante el int(), el input interpreta que me refiero a un número.


#INPUT de números flotantes:
resultado_numerico2 = float(numero)*2

print(resultado_numerico2) #al yo indicar mediante el float(), me devuelve un número con coma.


