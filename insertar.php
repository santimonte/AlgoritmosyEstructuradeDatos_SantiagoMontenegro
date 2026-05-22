<?php

include("conexion.php");

if(isset($_POST["registerButton"])){

    $usuario = $_POST["usuario"];
    $email = $_POST["email"];
    $contraseña = $_POST["contraseña"];

    
    $hash = password_hash($contraseña, PASSWORD_BCRYPT);

    $consulta = "INSERT INTO usuarios(usuario,email,contraseña)
    VALUES('$usuario','$email','$hash')";

    $resultado = mysqli_query($conexion,$consulta);

    if($resultado){
        header("Location: login.php");
    } else {
        echo "Error al registrar usuario";
    }

}

?>