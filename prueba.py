import ipywidgets as widgets
from IPython.display import display
import time

# Datos de usuario y contraseña
data_user = "betak9999@gmail.com"
data_pass = "1234"
Mensaje1 = "Ingreso exitoso"
Mensaje2 = "Acceso denegado"
bloqueo_mensaje = "Debes esperar dado que se bloqueó tu ingreso."
reintento_mensaje = "Puedes intentar nuevamente."
user = "Demian"

# Variables de control de intentos
intentos = 3

# Crear campos de entrada y botón
input_user = widgets.Text(placeholder='Introduce tu Email:')
input_pass = widgets.Password(placeholder='Introduce tu contraseña:')
button = widgets.Button(description="Siguiente")

# Mostrar los widgets
display(input_user)
display(input_pass)
display(button)

# Función de validación
def validar_credenciales(b):
    global intentos
    usuario = input_user.value
    contrasena = input_pass.value

    if usuario == data_user and contrasena == data_pass:
        print(Mensaje1)
        print(f"Bienvenido, {user}")
        button.disabled = True  # Desactivar el botón
    else:
        intentos -= 1
        print(Mensaje2)
        if intentos > 0:
            print(f"Te quedan {intentos} intentos.")
        else:
            print(bloqueo_mensaje)
            for i in range(59, 0, -1):
                print(f"Reintentando en {i} segundos...", end="\r")
                time.sleep(1)
            print(reintento_mensaje)
            intentos = 3  # Restablecer los intentos

# Asignar la función al botón
button.on_click(validar_credenciales)



























demian_estres = 10000
if demian_estres >= 1
    print ("demian estresadito")