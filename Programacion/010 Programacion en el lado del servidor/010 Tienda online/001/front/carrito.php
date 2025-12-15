<?php include "inc/cabecera.php"; ?>

Hola que tal yo soy el carrito<br>
Vamos a ver si atrapamos correctamente el producto<br>
<?php
	echo "El producto es: ".$_POST['id']."<br>";
    echo "Las unidades son: ".$_POST['unidades']."<br>";
?>

<form action="finalizacion.php" method="POST">

    <!--Datos del producto-->
    <input type="hidden" name="idproducto" value="<?= $_POST['id'] ?>">
    <input type="hidden" name="unidades" value="<?= $_POST['unidades'] ?>">

    <!--Datos del cliente-->
    <input type="text" name="nombre_cliente">
    <input type="text" name="apellido_cliente">
    <input type="text" name="email">
    <input type="text" name="direccion">
    <input type="text" name="telefono">


    <input type="submit" value="Finalizar compra">
</form>

<?php include "inc/piedepagina.php"; ?>



