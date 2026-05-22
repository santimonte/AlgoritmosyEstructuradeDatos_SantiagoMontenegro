<?php

$host = "localhost";
$user = "root";
$pass = "";
$db = "torneodetruco";

$conexion = mysqli_connect($host, $user,$pass,$db,3307);

if(!$conexion){
    die("Error de conexión");
}

?>