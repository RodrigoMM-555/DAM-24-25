<?php
// En linux los permisos son muy restrictivos, tenlo en cuenta
// Recordar el tema de los permisos

mkdir('uploads');

move_uploaded_file(
    $_FILES['archivo']['tmp_name'],
    'uploads/' . $_FILES['archivo']['name']
);

echo 'OK';
?>