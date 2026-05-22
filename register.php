<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Registro</title>

    <link rel="stylesheet" href="styleRegister.css">
</head>
<body>

    <div class="formContainer">

        <h1>Crear Cuenta</h1>

        <form action="insertar.php" method="POST">
            <label>Usuario</label>

            <input 
                type="text"
                name="usuario"
                required
            >

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

            <button type="submit" name="registerButton">
                Registrarse
            </button>

        </form>

    </div>

</body>
</html>