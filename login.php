<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Login</title>

    <link rel="stylesheet" href="styleLogin.css">
</head>
<body>

    <div class="formContainer">

        <h1>Iniciar Sesión</h1>

        <form action="validarLogin.php" method="POST">

            <label>Email</label>

            <input 
                type="email"
                name="email"
                required
            >

            <label>Contraseña</label>

            <input 
                type="password"
                name="contraseña"
                required
            >

            <button type="submit" name="loginButton">
                Ingresar
            </button>

        </form>

    </div>

</body>
</html>