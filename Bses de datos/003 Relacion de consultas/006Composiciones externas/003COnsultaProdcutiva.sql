
SELECT * FROM matriculas;

------------------------

SELECT
*
FROM matriculas
Left join asignaturas
ON matriculas.id_asignatura = asignaturas.Identificador;

-------------------------

SELECT
*
FROM matriculas
Left join asignaturas
ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos
ON matriculas.id_alumno = alumnos.Identificador;

---------------------------

SELECT
*
FROM matriculas
Left join asignaturas
ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos
ON matriculas.id_alumno = alumnos.Identificador;