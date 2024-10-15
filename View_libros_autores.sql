-- VIEW 
CREATE VIEW v_pais_autores AS
SELECT autor, pais_autor 
FROM libros
WHERE pais_autor lIKE "A%";

SELECT * FROM v_pais_autores