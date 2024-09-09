lunes = [5,4,6,7]
martes = [0,5,6,7]
miercoles = [3,3,1,9]
jueves = [10,4,6,7] 
viernes = [3,1,9,7]
semana1 = [lunes [0],martes [0],miercoles [0],jueves [0],viernes [0]]
semana2 = [lunes [1],martes [1],miercoles [1],jueves [1],viernes [1]]
semana3 = [lunes [2],martes [2],miercoles [2],jueves [2],viernes [2]]
semana4 = [lunes [3],martes [3],miercoles [3],jueves [3],viernes [3]]

ingreso_semanal = 15
salida_semanal1 = lunes [0] + martes [0] + miercoles [0] + jueves [0] + viernes [0]
salida_semanal2 = lunes [1] + martes [1] + miercoles [1] + jueves [1] + viernes [1]
salida_semanal3 = lunes [2] + martes [2] + miercoles [2] + jueves [2] + viernes [2]
salida_semanal4 = lunes [3] + martes [3] + miercoles [3] + jueves [3] + viernes [3]

ingreso_mensual = (ingreso_semanal * 4)
salida_mensual = (salida_semanal1 + salida_semanal2 + salida_semanal3 + salida_semanal4)

if salida_semanal1 > ingreso_semanal:
    print("Es mayor la salida que el ingreso")
else:
    print("No se logra vender mensualmente el ingreso,",ingreso_mensual - salida_mensual, "es la diferencia de productos remanentes")
    
if ingreso_mensual - salida_mensual > 0:
    print(ingreso_mensual - salida_mensual)
    
    
print(salida_mensual)





























demian_estres = 10000
if demian_estres >= 1
    print ("demian estresadito")