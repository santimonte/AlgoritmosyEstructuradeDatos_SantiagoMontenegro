<?php
include("conexion.php");

session_start();

if(isset($_POST["loginButton"])){

    $email = $_POST["email"];
    $contraseña = $_POST["contraseña"];

    $consulta = "SELECT * FROM usuarios WHERE email = '$email'";
    $resultado = mysqli_query($conexion, $consulta);

    $user = mysqli_fetch_assoc($resultado);

    if($user){

        if(password_verify($contraseña, $user["contraseña"])){

            $_SESSION["usuario"] = $user["usuario"];

            header("Location: paginaPrincipal.html");
            exit();

        } else {
            echo "Contraseña incorrecta";
        }

    } else {
        echo "Usuario no encontrado";
    }

}

?>