<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .container {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            width: 300px;
        }
        .message {
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <div id="message" class="message"></div>
        <label for="email">Email:</label>
        <input type="text" id="email" placeholder="Introduce tu Email" /><br/><br/>
        <label for="password">Contraseña:</label>
        <input type="password" id="password" placeholder="Introduce tu contraseña" /><br/><br/>
        <button onclick="validarCredenciales()">Siguiente</button>
    </div>

    <script>
        // Datos de usuario y contraseña
        const dataUser = "betak9999@gmail.com";
        const dataPass = "1234";
        let intentos = 3;
        const mensaje1 = "Ingreso exitoso";
        const mensaje2 = "Acceso denegado";
        const bloqueoMensaje = "Debes esperar dado que se bloqueó tu ingreso.";
        const reintentoMensaje = "Puedes intentar nuevamente.";
        const user = "Demian";

        function validarCredenciales() {
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const messageDiv = document.getElementById('message');

            if (email === dataUser && password === dataPass) {
                messageDiv.textContent = `${mensaje1} Bienvenido, ${user}`;
                messageDiv.style.color = 'green';
                document.querySelector('button').disabled = true; // Desactivar el botón
            } else {
                intentos--;
                if (intentos > 0) {
                    messageDiv.textContent = `${mensaje2} Te quedan ${intentos} intentos.`;
                    messageDiv.style.color = 'red';
                } else {
                    messageDiv.textContent = bloqueoMensaje;
                    messageDiv.style.color = 'red';
                    setTimeout(() => {
                        messageDiv.textContent = reintentoMensaje;
                        messageDiv.style.color = 'blue';
                        intentos = 3; // Restablecer intentos
                    }, 60000); // Esperar 60 segundos
                }
            }
        }
    </script>
</body>
</html>




























demian_estres = 10000
if demian_estres >= 1
    print ("demian estresadito")