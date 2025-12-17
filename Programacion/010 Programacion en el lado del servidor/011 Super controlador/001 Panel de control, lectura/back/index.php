<html>
<head>
    <title>Panel de control</title>
    <link rel="stylesheet" href="css/estilo.css">
</head>
<body>

    <?php include "inc/conexion_BD.php" ?>
    <nav>
        <?php include "controladores/poblar_menu.php" ?>
    </nav>
    <main>
        <?php include "controladores/leer.php" ?>
    </main>
</body>
</html>