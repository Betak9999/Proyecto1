# EJEMPLO 1
dinero = 5000

if dinero > 10000:
    print("Bien económicamente")

if dinero > 10000:
    print("Buen sueldo a nivel mundial")
    
else: 
    print("Debajo de la línea de pobreza")


# EJEMPLO 2
dinero = 10500
gasto_mensual = 3000

if dinero > 10000:
    if gasto_mensual < 7000:
        print("Buena situación financiera")
    elif gasto_mensual > 7000:
        print("Mala situación financiera")
    else:
        print("Situación financiera neutral")  # Si es exactamente 7000

elif dinero > 1000:  #significaría "caso contrario", es un operador "else if", y se escribe como elif.
    print("Buen sueldo en latinoamérica")
    
elif dinero > 500:  
    print("Buen sueldo en Argentina")

elif dinero > 200:  
    print("Buen sueldo en Venezuela")
    
else: 
    print("Debajo de la línea de pobreza")  
    

# EJEMPLO 3
dinero = 5000
gasto_mensual = 4500

if dinero > 4999:
    if dinero - gasto_mensual < 0:
        print("Déficit")
    elif gasto_mensual > 3000:
        print("Mala situación financiera")
    else:
        print("Situación financiera neutral")  # Si es exactamente 7000