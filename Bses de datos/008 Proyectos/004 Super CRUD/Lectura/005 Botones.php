<nav>
    <a href="?tabla=cliente"><button>Cliente</button></a>
    <a href="?tabla=producto"><button>Producto</button></a>
    <a href="?tabla=pedido"><button>Pedido</button></a>
    <a href="?tabla=lineaspedido"><button>Lineas pedido</button></a>
</nav>
<main></main>
    <table>
    <?php
        $host = "localhost";
        $user = "tiendaonlinedamdaw";
        $pass = "Tiendaonlinedamdaw123$";
        $db   = "tiendaonlinedamdaw";

        $conexion = new mysqli($host, $user, $pass, $db);
        // Usamos el parámetro 'tabla' pasado por la URL, si ponemos tabla=cliente o producto,etc saldran diferentes tablas        
        $resultado = $conexion->query("    
            SELECT * FROM ".$_GET['tabla'].";
        ");
        while ($fila = $resultado->fetch_assoc()) {
            echo "<tr>";
            foreach($fila as $clave=>$valor){
                echo "<td>".$valor."</td>";
            }
            echo "</tr>";
        }
    ?>
    </table>
</main>