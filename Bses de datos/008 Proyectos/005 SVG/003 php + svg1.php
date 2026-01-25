<?php
declare(strict_types=1);

// ----------------------------
// Datos del programa
// ----------------------------
$valores = [12, 28, 27, 25, 22, 30, 26]; // cualquier valor de tu programa
$colores = ['#ff0000','#00ff00','#00ffff','#ff00ff','#ffff00','#ff8800','#8888ff']; // opcional

// ----------------------------
// Configuración de la gráfica
// ----------------------------
$viewBoxWidth  = 52.9;
$viewBoxHeight = 52.9;

$paddingLeft   = 3.5;
$paddingRight  = 2.0;
$paddingTop    = 2.0;
$paddingBottom = 2.2;

$plotLeft   = $paddingLeft;
$plotRight  = $viewBoxWidth - $paddingRight;
$plotTop    = $paddingTop;
$plotBottom = $viewBoxHeight - $paddingBottom;

$plotWidth  = $plotRight - $plotLeft;
$plotHeight = $plotBottom - $plotTop;

$n = count($valores);
$maxVal = max($valores) ?: 1;

// Anchura de barra y separación
$slots = $n * 1.6;
$barWidth = $plotWidth / max(1, $slots);
$gap = ($n > 1) ? (($plotWidth - ($n * $barWidth)) / ($n - 1)) : 0;

// ----------------------------
// Calculamos geometría de cada barra
// ----------------------------
$computed = [];
for ($i = 0; $i < $n; $i++) {
    $h = ($valores[$i] / $maxVal) * $plotHeight;
    $y = $plotBottom - $h;
    $x = $plotLeft + $i * ($barWidth + $gap);

    $computed[] = [
        'x' => $x,
        'y' => $y,
        'width' => $barWidth,
        'height' => $h,
        'color' => $colores[$i] ?? '#000000',
    ];
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Gráfica de barras</title>
</head>
<body>
    <h1>Gráfica de barras</h1>
<svg viewBox="0 0 <?= $viewBoxWidth ?> <?= $viewBoxHeight ?>" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bar chart">
  <!-- Ejes -->
  <line x1="<?= $plotLeft ?>" y1="<?= $plotTop ?>" x2="<?= $plotLeft ?>" y2="<?= $plotBottom ?>" stroke="#000" stroke-width="1.2"/>
  <line x1="<?= $plotLeft ?>" y1="<?= $plotBottom ?>" x2="<?= $plotRight ?>" y2="<?= $plotBottom ?>" stroke="#000" stroke-width="1.2"/>

  <!-- Barras -->
  <?php foreach ($computed as $b): ?>
    <rect
      x="<?= $b['x'] ?>"
      y="<?= $b['y'] ?>"
      width="<?= $b['width'] ?>"
      height="<?= $b['height'] ?>"
      fill="<?= $b['color'] ?>"
    />
  <?php endforeach; ?>
</svg>
</body>
</html>
